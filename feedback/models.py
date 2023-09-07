from django.db import models

class Feedback(models.Model):
    
    titulo_feedback = models.TextField()
    # data_publi = models.DateTimeField("Data da publicação")

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.titulo_feedback

class Comentario(models.Model):
    
    texto_comentario = models.CharField(max_length=200)
    data_publi = models.DateTimeField("Data publicação")
    

