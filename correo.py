import smtplib

class Correo:
    
    def __init__(self):
        self.message = '\n\nSe le informa que se ha generado una multa por retraso en la devolucion de un libro'
        self.subject = 'Notificacion de multa'
    
    def sendEmail(self, usuario, multa, diasMora, libro):    
        saludo = f"Hola {usuario.getNombre()},"
        infoMulta = f"Informacion sobre la multa:\n\nLibro: {libro.getTitulo()}\nValor: ${multa.getCantidad()} COP\nDias de mora: {diasMora}\n\nLe pedimos que se acerque a la biblioteca para realizar el pago de la multa."
        self.message = saludo + self.message + "\n" + infoMulta
        message = 'Subject: {}\n\n{}'.format(self.subject, self.message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('cristyant2003@gmail.com', "rwvgpzjqqxasagzk")
        server.sendmail('cristyant2003@gmail.com', f"{usuario.getCorreo()}", message)
        server.quit()
        
    def sendNotification(self, libro, opcion):    
        saludo = f"Hola administrador,"
        self.subject = "Notificacion de libro agotado" if opcion == 1 else "Notificacion de libro a punto de agotarse"
        infoMulta = f"Informacion sobre el libro:\n\nTitulo: {libro.getTitulo()}\nAutor: {libro.getAutor()}\nISBN: {libro.getISBN()}\nCopias Disponibles: {libro.getNumCopias()}"
        mensaje = "Se le informa que el libro se ha agotado" if opcion == 1 else "Se le informa que el libro esta a punto de agotarse"
        self.message = saludo + "\n" + mensaje + "\n" + infoMulta
        message = 'Subject: {}\n\n{}'.format(self.subject, self.message)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('cristyant2003@gmail.com', "rwvgpzjqqxasagzk")
        server.sendmail('cristyant2003@gmail.com', "c.arango1@utp.edu.co", message)
        server.quit()