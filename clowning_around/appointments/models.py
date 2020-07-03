from django.db import models

# Create your models here.
class ClientAppointment(models.Model):
    name = models.CharField(_("Appointment"), max_length=50)
    event_rating = models.IntegerField()

    def __str__(self):
        return self.name


class TroupeLeaderSchedule(models.Model):
    name = models.CharField(_("Create Apoointment"), max_length=50)
    clown_id = models.ForeignKey("users.Clown", on_delete=models.CASCADE)
    troupe_id = models.ForeignKey("users.Troupe", on_delete=models.CASCADE)
    troupe_capacity = models.IntegerField()

    def __str__(self):
        return self.name

class ClownSchedule(models.Model):
    name = models.CharField(_("Create Apoointment"), max_length=50)
    client_id = models.ForeignKey("users.Client", on_delete=models.CASCADE)
    clown_id = models.ForeignKey("users.Clown", on_delete=models.CASCADE)
    report_issue = models.CharField(_("Report an issue"), max_length=50)
    client_reason = models.CharField(_("Reason for cancellation"), max_length=50)
    appointment_status = models.CharField(_(""), max_length=50)

    def __str__(self):
        return self.name
