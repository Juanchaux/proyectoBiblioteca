import smtplib

class Correo:
    
    def __init__(self) -> None:
        self.message = '\n\nSe le informa que se ha generado una multa por retraso en la devolucion de un libro'
        self.subject = 'Notificacion de multa'
    
    def sendEmail(self, usuario, multa, diasMora):    
        saludo = f"Hola {usuario.getNombre()},"
        infoMulta = f"Informacion sobre la multa:\n\nValor: ${multa.getCantidad()} COP\nDias de mora: {diasMora}\n\nLe pedimos que se acerque a la biblioteca para realizar el pago de la multa."
        self.message = saludo + self.message + "\n" + infoMulta
        message = 'Subject: {}\n\n{}'.format(self.subject, self.message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('cristyant2003@gmail.com', "rwvgpzjqqxasagzk")
        server.sendmail('cristyant2003@gmail.com', f"{usuario.getCorreo()}", message)
        server.quit()