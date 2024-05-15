import qrcode

#taking input 
esewa_id =input("enter your eSewa ID or khalti ID: ")
name=input("enter your name: ").upper() 

#or phonenumber
esewa_url=f'{{"eSewa_id": "{esewa_id}","name":"{name}"}}'
khalti_url=f'{{"khalti_id": "{esewa_id}","name":"{name}"}}'

#for generating QR
esewa_qr=qrcode.make (esewa_url)
khalti_qr=qrcode.make (khalti_url)

#For displaying QR
esewa_khalti=input("Esewa or Khalti ?: ").upper()
if esewa_khalti=="ESEWA":
   esewa_qr.show()
else:
   khalti_qr.show()
