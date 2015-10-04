import sendgrid
import sys

sg = sendgrid.SendGridClient('chsahit', 'sahit1998')

message = sendgrid.Mail()
message.add_to('Sahit C <chsahit@gmail.com>')
message.set_subject('Example')
message.set_html(sys.argv[1])
message.set_text(sys.argv[1])
message.set_from('Chintalapudi Sahit <chsahit@gmail.com>')
status, msg = sg.send(message)
print "email sent"
