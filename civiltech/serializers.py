from rest_framework import serializers
from .models import Expense_Entry,Invoice,SalesMode,Invoice_Test, Invoice_File, Invoice_File_Category
from general.models import Material,Expense,Test,Tax
from account.models import Customer
from num2words import num2words
from bs4 import BeautifulSoup

class Invoice_File_Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice_File_Category
        fields = '__all__'

class Create_Expense_Entry_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Expense_Entry
        fields = ['id','date','expense_user','expense_category','amount','narration']

class Expense_Entry_Serializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    modified_by = serializers.StringRelatedField()
    expense_category_name = serializers.SerializerMethodField()

    class Meta:
        model = Expense_Entry
        fields = ['id','expense_user','date','amount','expense_category','narration','created_by','created_date','modified_by','modified_date','expense_category_name']

    def get_expense_category_name(self,obj):
        return str(obj.expense_category)
    
class Expense_Serializer1(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'expense_name']



class Customer_Serializer1(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','customer_name','address1','phone_no']

class Sales_mode_Serializer1(serializers.ModelSerializer):
    class Meta:
        model = SalesMode
        fields = ['id','sales_mode'] 

class Tax_Serializer1(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = ['id','tax_name','tax_percentage']

class Create_Invoice_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id','customer','sales_mode','project_name','discount','tax','advance','balance']

class Edit_Invoice_Serializer(serializers.ModelSerializer):
    #date = serializers.DateField(input_formats=['%d-%m-%Y',])

    class Meta:
        model = Invoice
        fields = ['id','customer','sales_mode','project_name','discount','tax','total_amount','advance','balance','amount_paid_date','bank','cheque_number','payment_mode','date','place_of_testing','upi']

class Invoice_Serializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    incompleted_test = serializers.SerializerMethodField()
    class Meta:
        model = Invoice
        fields = ['id','invoice_no','customer','sales_mode','project_name','discount','tax','advance','balance','place_of_testing','total_amount','incompleted_test']

    def get_incompleted_test(self,obj):
        return str(obj.incompleted_test)
    
class Material_Serializer2(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'material_name']

class Material_Test_Serializer(serializers.ModelSerializer):  
    test_material_id = serializers.SerializerMethodField()
    test_material_name = serializers.SerializerMethodField()

    class Meta:
        model = Test
        fields = ['id', 'test_name', 'test_material_id','test_material_name', 'price_per_piece']

    def get_test_material_id(self, obj):
        return str(obj.material_name.id)

    def get_test_material_name(self, obj):
        return str(obj.material_name.material_name)

class Create_Invoice_Test_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice_Test
        fields = ['invoice','test','quantity','price_per_sample','total']



class Invoice_Test_Serializer(serializers.ModelSerializer):
    test_name = serializers.SerializerMethodField()
    final_html = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()

    class Meta:
        model = Invoice_Test
        fields = ['id','invoice','test','test_name','quantity','price_per_sample','total','report_template','final_html','count','completed','signature']   

    def get_test_name(self,obj):
        return obj.test.test_name
    
    def get_count(self,obj):
        return str(obj.count)
    
    
    def get_final_html(self,obj):

   
        try:

            html_content = obj.report_template

            # Parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find the div element by class name and remove it
            div_to_remove = soup.find('tr', class_='header-img-div')
            if div_to_remove:
                div_to_remove.extract()

           
            # Print the modified HTML
            final_html  = soup.prettify()
            return str(final_html)
        except:
            return "sample"

 
    

    


class Invoice_Serializer1(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    customer_no = serializers.SerializerMethodField()

    class Meta:
        model =  Invoice
        fields = ['id','invoice_no','customer','customer_no']

    def get_customer_no(self,obj):
        return (obj.customer.phone_no)
    
class Test_serializer(serializers.ModelSerializer):
    class Meta:
        model =  Test
        fields = ['id','test_name']


class Pending_Invoice_Serializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    incompleted_test = serializers.SerializerMethodField()
    class Meta:
        model =  Invoice
        fields = ['id','customer','project_name','total_amount','advance','balance','invoice_no','fully_paid','incompleted_test']
    
    def get_incompleted_test(self,obj):
        return str(obj.incompleted_test)

class Create_Invoice_File_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Invoice_File
        fields = ['invoice','file','category','expense']


class Invoice_File_Serializer(serializers.ModelSerializer):
    file_url  = serializers.SerializerMethodField()
    invoice_no  = serializers.SerializerMethodField()
    category_name  = serializers.SerializerMethodField()
    created_by = serializers.StringRelatedField()
    modified_by  = serializers.StringRelatedField()
    expense_category = serializers.SerializerMethodField()
    expense_user = serializers.SerializerMethodField()
    
    class Meta:
        model =  Invoice_File
        fields = ['id','invoice','file_url','category','invoice_no','category_name','created_by','modified_by','modified_date','created_date','expense','expense_category','expense_user']
        
    def get_invoice_no(self,obj):
        try:
            return obj.invoice.invoice_no
        except:
            return None
    
    def get_category_name(self,obj):
        return str(obj.category)
    
    def get_expense_category(self,obj):
        try:
            return str(obj.expense.expense_category.expense_name)
        except:
            return None
    
    
    def get_expense_user(self,obj):
        try:
            return str(obj.expense.expense_user)
        except:
            return None
    
    def get_file_url(self, obj):
        return "http://files.covaiciviltechlab.com/media/"+str(obj.file)
    

class CustomDateFormatField(serializers.Field):
    def to_representation(self, value):
        # Convert the DateTimeField to a date with a specific format
        return value.strftime('%d-%m-%Y')

class Expense_Entry_Serializer1(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    expense_category = serializers.StringRelatedField()
    date = CustomDateFormatField()

    class Meta:
        model = Expense_Entry
        fields = '__all__'







class Customer_Serializer_For_Invoice(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','customer_name','address1']



class Invoice_Serializer_For_Report(serializers.ModelSerializer):
    incompleted_test = serializers.SerializerMethodField()
    export_date = serializers.SerializerMethodField()


    class Meta:
        model = Invoice
        fields = ['customer_name','customer_gst_no','project_name','invoice_no','date','export_date', 'amount','cgst_tax','sgst_tax','total_amount','cash','cheque_neft','tax_deduction','advance','balance','discount','amount_paid_date','bank','cheque_number','payment_mode','place_of_testing','tax','sales_mode','incompleted_test','upi']


    def get_incompleted_test(self,obj):
        return str(obj.incompleted_test)
    

    def get_export_date(self,obj):
        try:
            return obj.date.strftime("%d-%m-%Y")
        except:
            return ''
    
    

class Invoice_Serializer_For_Print(serializers.ModelSerializer):
    inr =  serializers.SerializerMethodField()
    qr =  serializers.SerializerMethodField()
    class Meta:
        model = Invoice
        fields = ['id','qr','date','invoice_no','project_name','invoice_image','customer_name','customer_gst_no','amount','cgst_tax','sgst_tax','total_amount','cash','cheque_neft','tax_deduction','advance','balance','discount','amount_paid_date','bank','cheque_number','payment_mode','inr','tax','place_of_testing']

    def get_inr(self,obj):
        return str(num2words(obj.total_amount)).capitalize()
    
    def get_qr(self,obj):
        return "http://files.covaiciviltechlab.com/"+obj.invoice_image

class Customer_Serializer_For_Print(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['address1','place_of_testing','gstin_no','customer_name']



class Invoice_Test_Serializer_For_Print(serializers.ModelSerializer):
    test_name = serializers.SerializerMethodField()
    material_name = serializers.SerializerMethodField()
    qty = serializers.SerializerMethodField()
    final_html = serializers.SerializerMethodField()
    
    

    class Meta:
        model = Invoice_Test
        fields = ['id','invoice','material_name','test','test_name','qty','price_per_sample','total','invoice_image','final_html']   

    def get_test_name(self,obj):
        return str(obj.test)
    

    def get_material_name(self,obj):
        return str(obj.test.material_name)
    
    def get_qty(self,obj):
        return str(int(obj.quantity))
    
    def get_final_html(self,obj):
        html_content = obj.report_template

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the div element by class name and remove it
        div_to_remove = soup.find('div', class_='header-img-div')
        if div_to_remove:
            div_to_remove.extract()

        # Print the modified HTML
        final_html  = soup.prettify()
        return str(final_html)
    




class Invoice_Serializer_For_Dashboard(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    class Meta:
        model = Invoice
        fields = ['id','invoice_no','total_amount','customer','sales_mode','project_name','discount','tax','advance','balance','place_of_testing']
