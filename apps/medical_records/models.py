from django.db import models
from apps.users.models import User
from apps.appointments.models import Appointment

class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='medical_records'
    )
    doctor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='doctor_records'
    )
    appointment = models.ForeignKey(
        Appointment, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    
    diagnosis = models.TextField()
    symptoms = models.TextField(blank=True)
    treatment_plan = models.TextField(blank=True)
    visit_date = models.DateField()
    
    def __str__(self):
        return f"Medical Record: {self.patient.username}"

class Prescription(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, 
        on_delete=models.CASCADE, 
        related_name='prescriptions'
    )
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.medication_name}"
