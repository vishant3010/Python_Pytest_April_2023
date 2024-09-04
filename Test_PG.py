from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from Testdata.Test_data import.all()


options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome()
driver.implicitly_wait(6)



#Open Letzpay UAT
def test_open():
    driver.get("https://uat.letzpay.com/crm/jsp/index")
    driver.maximize_window()


#login in Letzpay UAT
def test_login():
    driver.find_element(By.ID, "loginNumber").send_keys(loginphone)
    driver.find_element(By.XPATH, "//*[@id='login-form']/div[3]/button[1]").click()
    for x in range(6):
        driver.find_element(By.XPATH, "//*[@id='login-pin']/div/div[1]/input["+str(x+1)+"]").send_keys("3")
    driver.find_element(By.ID, "captchaLogin").send_keys("0000")
    #reset all dropdown
    driver.find_element(By.XPATH, "/html/body/div[2]/div/aside/header/a").click()



#Merchant Regestration
def test_merchant_regestration():
    driver.find_element(By.XPATH, "//*[@id='navigation']/li[3]/a/span[2]").click()
     driver.find_element(By.XPATH, "//*[@id='navigation']/li[3]/ul/li[1]/a/span[2]").click()
    driver.find_element(By.ID, "businessName").send_keys(name)
    driver.find_element(By.ID, "emailId").send_keys(email_id)
    driver.find_element(By.ID, "loginNumber").send_keys(phone)
    for p in range(6):
        driver.find_element(By.XPATH, "//*[@id='formname']/div[8]/div/div/div[1]/input["+str(p+1)+"]").send_keys("1")
    for cp in range(6):
        driver.find_element(By.XPATH, "//*[@id='formname']/div[9]/div/div/div[1]/input["+str(cp+1)+"]").send_keys("1")
    driver.find_element(By.ID, "submit").click()


#merchnt mapping
def test_merchant_mapping():
    driver.find_element(By.XPATH, "//*[@id='navigation']/li[4]/a").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='Merchant Mapping']").click()
    driver.find_element(By.XPATH, "//span[@class='filter-option pull-left'][normalize-space()='Select Merchant']").click()
    driver.find_element(By.XPATH, "//div[@class='btn-group bootstrap-select open']//input[@type='text']").send_keys(name)
    driver.find_element(By.XPATH, "//li[@class='active']//a").click()
    driver.find_element(By.XPATH, "//span[@class='filter-option pull-left'][normalize-space()='Select Acquirer']").click()
    driver.find_element(By.XPATH, "//div[@class='btn-group bootstrap-select open']//input[@type='text']").send_keys("Lyra")
    driver.find_element(By.XPATH, "//div[@class='btn-group bootstrap-select open']//li[@class='active']//a").click()
    driver.find_element(By.XPATH, "//*[@id='id+checkBoxes']/label[4]").click()
    driver.find_element(By.XPATH, "//input[@id='idmerchantid+356']").send_keys(mid)
    driver.find_element(By.XPATH, "//input[@id='idpassword+356']").send_keys(key_pass)
    driver.find_element(By.XPATH, "//label[normalize-space()='Credit Card']").click()
    driver.find_element(By.XPATH, "//div[@id='Credit Card']//label[@class='mop-type checkbox-label unchecked mb-0'][normalize-space()='Visa']").click()
    driver.find_element(By.XPATH, "//div[@id='Credit Card-VI']//label[@class='txn-type checkbox-label unchecked mb-10'][normalize-space()='SALE']").click()
    driver.find_element(By.XPATH, "//label[normalize-space()='Net Banking']").click()
    driver.find_element(By.XPATH, "//div[@id='Net Banking']//label[@class='checkbox-label unchecked mb-10']").click()
    driver.find_element(By.XPATH, "//button[@id='btnsubmit']").click()
    time.sleep(8)
    Alert(driver).accept()
    driver.switch_to.default_content()


#User status for Active
def test_user_status():
    driver.find_element(By.XPATH, "//*[@id='navigation']/li[3]/a").click()
    driver.find_element(By.XPATH, "//*[@id='navigation']/li[3]/ul/li[5]/a/span[2]").click()
    driver.find_element(By.ID, "merchantList").click()
    driver.find_element(By.XPATH, "//*[@id='merchantListDatatable_filter']/label/input").send_keys(name)
    driver.implicitly_wait(6)
    driver.find_element(By.ID, "editPermission").click()
    driver.find_element(By.XPATH, "//span[@class='filter-option pull-left'][normalize-space()='SUSPENDED']").click()
    driver.find_element(By.XPATH, "//div[@class='btn-group bootstrap-select dropup open']//span[@class='text'][normalize-space()='ACTIVE']").click()
    driver.find_element(By.XPATH, "//button[@id='saveMerchant']").click()
    driver.find_element(By.XPATH, "//div[@class='lpay_popup-innerbox-success lpay-center']//button[@class='lpay_button lpay_button-md lpay_button-secondary confirmButton'][normalize-space()='Ok']").click()


    #dropdown = Select(driver.find_element(By.XPATH, "//span[@class='filter-option pull-left'][normalize-space()='INACTIVE']"))
    #dropdown.select_by_visible_text("ACTIVE")
    #driver.find_element(By.XPATH, "//*[@id='saveMerchant']/i").click()

    #for status in driver.find_elements(By.XPATH, "//*[@id='wwctrl_status']/div/div/ul/li[1]/a/span[1]"):
    #       print(status.text)

    #if status != 'ACTIVE':
     #   driver.find_element(By.ID, "newStatus").click()
      #  driver.find_element(By.XPATH, "//*[@id='wwctrl_status']/div/div/ul/li[1]/a").click()
       # driver.find_element(By.XPATH, "//*[@id='saveMerchant']/i").click()


#payment options
def test_payment_options():
    driver.find_element(By.XPATH, "//*[@id='navigation']/li[4]/a").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='Payment Options']").click()
    driver.find_element(By.XPATH, "//span[@class='filter-option pull-left'][normalize-space()='ALL']").click()
    driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys(name)
    driver.find_element(By.XPATH, "//li[@class='active']//a").click()
    driver.find_element(By.XPATH, "//label[@for='creditCard']").click()
    driver.find_element(By.XPATH, "//div[@data-append='creditCard']//label[@class='checkbox-label unchecked mb-10 mr-10'][normalize-space()='Select All']").click()
    driver.find_element(By.XPATH, "//div[@data-mop='netBanking']").click()
    driver.find_element(By.XPATH, "//div[@data-append='netBanking']//label[@class='checkbox-label unchecked mb-10 mr-10'][normalize-space()='Select All']").click()
    driver.find_element(By.XPATH, "//button[@id='btn-payment-options']").click()

#user_setting_flags
def test_user_setting():
    driver.find_element(By.XPATH, "//*[@id='navigation']/li[3]/a/span[2]").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='User Settings']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Merchant List']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='Search records']").send_keys(name)
    driver.find_element(By.XPATH, "//button[@id='editPermission']").click()
    driver.find_element(By.XPATH, "//label[@for='vendorFlag']").click()
    driver.find_element(By.XPATH, "//div[@class='col-md-12 text-center button-wrapper button_wrapper']//button[@class='lpay_button lpay_button-md lpay_button-secondary'][normalize-space()='Save']").click()

#payid_salt_for_merchant_transaction
def test_payid_salt():
    driver.find_element(By.XPATH, "//*[@id='navigation']/li[3]/a/span[2]").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='Merchant Account']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='Search records']").send_keys(name)
    driver.find_element(By.XPATH, "//button[@id='editPermission']").click()
    driver.find_element(By.XPATH, "//li[normalize-space()='Onboard Details']").click()
    payid_value = driver.find_element(By.ID, "payId")
    global payid_text
    payid_text = driver.execute_script("return arguments[0].value;", payid_value)
    print(payid_text)
    salt_value = driver.find_element(By.ID, "salt")
    global salt_text
    salt_text = driver.execute_script("return arguments[0].value;", salt_value)
    print(salt_text)

#Transction_Check_for_Above_Merchant
def test_cc_transaction():
    driver.get(r"C:\Test_Automation.HTML")
    driver.find_element(By.ID, "payId").send_keys(payid_text)
    driver.find_element(By.ID, "hashkey").send_keys(salt_text)
    driver.find_element(By.NAME, "CUST_NAME").send_keys(name)
    driver.find_element(By.NAME, "CUST_PHONE").send_keys(phone)
    driver.find_element(By.NAME, "CUST_EMAIL").send_keys(email_id)
    driver.find_element(By.ID, "button").click()
    driver.find_element(By.XPATH, "//input[@id='card-number']").send_keys(cardnumber)
    driver.find_element(By.XPATH, "//input[@id='paymentDate']").send_keys(expirydate)
    driver.find_element(By.XPATH, "//input[@id='cvvNumber']").send_keys(cvv)
    driver.find_element(By.XPATH, "//input[@id='cardName']").send_keys(name)
    driver.find_element(By.XPATH, "//span[@class='d-flex align-items-center justify-content-center']").click()
    driver.find_element(By.XPATH, "//button[@class='submit-button']").click()

#netbanking transaction
def test_nb_transaction():
    driver.get(r"C:\Test_Automation.HTML")
    driver.find_element(By.ID, "payId").send_keys(payid_text)
    driver.find_element(By.ID, "hashkey").send_keys(salt_text)
    driver.find_element(By.NAME, "CUST_NAME").send_keys(name)
    driver.find_element(By.NAME, "CUST_PHONE").send_keys(phone)
    driver.find_element(By.NAME, "CUST_EMAIL").send_keys(email_id)
    driver.find_element(By.ID, "button").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='Net Banking']").click()
    driver.find_element(By.XPATH, "//label[@for='axis']").click()
    driver.find_element(By.XPATH, "//span[@class='d-flex align-items-center justify-content-center']").click()
    driver.find_element(By.XPATH, "//button[@class='submit-button']").click()
