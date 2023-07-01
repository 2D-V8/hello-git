import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import mysql.connector

# Database connection configuration
config = {
    'user': 'root',
    'password': 'Danielvalencia1+',
    'host': 'localhost',
    'database': 'clinica'
}

# Create a database connection
conn = mysql.connector.connect(**config)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the main application window
root = tk.Tk()
root.title("Clinica Database Interface")



# Function to create a patient
def create_patient():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    direccion = entry_direccion.get()
    correo = entry_correo.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()

    # Insert patient data into the 'Paciente' table
    query = "INSERT INTO Paciente (nombre, apellido, direccion, correo_electronico, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s)"
    values = (nombre, apellido, direccion, correo, fecha_nacimiento)
    cursor.execute(query, values)
    conn.commit()
    print('Patient created successfully')

# Function to create a doctor
def create_doctor():
    nombre = entry_doctor_nombre.get()
    apellido = entry_doctor_apellido.get()
    direccion = entry_doctor_direccion.get()
    correo = entry_doctor_correo.get()
    especialidad = entry_doctor_especialidad.get()

    # Insert doctor data into the 'Medico' table
    query = "INSERT INTO Medico (nombre, apellido, direccion, correo_electronico, especialidad) VALUES (%s, %s, %s, %s, %s)"
    values = (nombre, apellido, direccion, correo, especialidad)
    cursor.execute(query, values)
    conn.commit()
    print('Doctor created successfully')

# Function to create a treatment
def create_treatment():
    descripcion = entry_descripcion.get()
    fecha_inicio = entry_fecha_inicio.get()
    fecha_finalizacion = entry_fecha_finalizacion.get()
    
    selected_paciente_id = paciente_dropdown_tratamiento.get()
    # Split the selected value to extract the patient ID
    paciente_id = selected_paciente_id.split("-")[0].strip()

    # Insert treatment data into the 'Tratamiento' table
    query = "INSERT INTO Tratamiento (descripcion, fecha_inicio, fecha_finalizacion, id_paciente) VALUES (%s, %s, %s, %s)"
    values = (descripcion, fecha_inicio, fecha_finalizacion, paciente_id)
    cursor.execute(query, values)
    conn.commit()
    print('Treatment created successfully')
# Function to create an appointment
def create_appointment():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    estado = entry_estado.get()

    selected_paciente_id = paciente_dropdown.get()  # Retrieve the selected paciente ID from the dropdown menu
    selected_doctor_id = doctor_dropdown.get()  # Retrieve the selected doctor ID from the dropdown menu

    if not selected_paciente_id or selected_paciente_id == 'Please select a patient':
        print('Please select a patient')
        return

    if not selected_doctor_id or selected_doctor_id == 'Please select a doctor':
        print('Please select a doctor')
        return
    
    # Insert appointment data into the 'Cita' table
    query = "INSERT INTO Cita (fecha, hora, estado, id_paciente, id_medico) VALUES (%s, %s, %s, %s, %s)"
    values = (fecha, hora, estado, int(selected_paciente_id), int(selected_doctor_id))
    cursor.execute(query, values)
    conn.commit()
    print('Appointment created successfully')




    # Function to delete a patient record
def delete_patient():
    selected_patient = paciente_dropdown.get()
    if not selected_patient or selected_patient == 'Please select a patient':
        messagebox.showwarning("Warning", "Please select a patient to delete.")
        return

    confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to delete {selected_patient}?")
    if confirmation:
        patient_id = selected_patient.split(" - ")[0]
        query = "DELETE FROM Paciente WHERE id = %s"
        cursor.execute(query, (patient_id,))
        conn.commit()
        messagebox.showinfo("Success", "Patient record has been deleted.")

# Function to delete a doctor record
def delete_doctor():
    selected_doctor = doctor_dropdown.get()
    if not selected_doctor or selected_doctor == 'Please select a doctor':
        messagebox.showwarning("Warning", "Please select a doctor to delete.")
        return

    confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to delete {selected_doctor}?")
    if confirmation:
        doctor_id = selected_doctor.split(" - ")[0]
        query = "DELETE FROM Medico WHERE id = %s"
        cursor.execute(query, (doctor_id,))
        conn.commit()
        messagebox.showinfo("Success", "Doctor record has been deleted.")

# Function to delete a treatment record
def delete_treatment():
    selected_treatment = tratamiento_dropdown.get()
    if selected_treatment:
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the treatment: {selected_treatment}?")
        if confirm:
            # Perform the deletion operation
            # Your code to delete the treatment goes here
            messagebox.showinfo("Deletion Successful", f"The treatment {selected_treatment} has been deleted.")
    else:
        messagebox.showerror("Error", "No treatment selected.")

# Function to delete an appointment record
def delete_appointment():
    selected_appointment = cita_dropdown.get()
    if selected_appointment:
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the appointment: {selected_appointment}?")
        if confirm:
            # Perform the deletion operation
            # Your code to delete the appointment goes here
            messagebox.showinfo("Deletion Successful", f"The appointment {selected_appointment} has been deleted.")
    else:
        messagebox.showerror("Error", "No appointment selected.")

    
    

    

        

    

    

    



    


    

# ... Rest of the code ...

# Create and position the dropdown menus for selecting doctor and paciente
tk.Label(root, text="Doctor Cita:").grid(row=3, column=6)
doctor_var = tk.StringVar()
doctor_dropdown = ttk.Combobox(root, textvariable=doctor_var)
doctor_dropdown.grid(row=3, column=7)

tk.Label(root, text="Paciente Cita:").grid(row=4, column=6)
paciente_var = tk.StringVar()
paciente_dropdown = ttk.Combobox(root, textvariable=paciente_var)
paciente_dropdown.grid(row=4, column=7)

# Populate the doctor and paciente dropdown menus with data from the database
query = "SELECT id, nombre FROM Medico"
cursor.execute(query)
doctors = cursor.fetchall()
doctor_dropdown['values'] = [doctor[0] for doctor in doctors]

query = "SELECT id, nombre FROM Paciente"
cursor.execute(query)
pacientes = cursor.fetchall()
paciente_dropdown['values'] = [paciente[0] for paciente in pacientes]

# ... Rest of the code ...

# ... Rest of the code ...

# Populate the patient dropdown menu with data from the database
query = "SELECT id, nombre FROM Paciente"
cursor.execute(query)
pacientes = cursor.fetchall()
paciente_dropdown['values'] = [paciente[0] for paciente in pacientes]

# ... Rest of the code ...
# ... Rest of the code ...

# Create and position the entry fields for treatments
tk.Label(root, text="Descripción Tratamiento:").grid(row=0, column=4)
entry_descripcion = tk.Entry(root)
entry_descripcion.grid(row=0, column=5)

tk.Label(root, text="Fecha Inicio Tratamiento:").grid(row=1, column=4)
entry_fecha_inicio = tk.Entry(root)
entry_fecha_inicio.grid(row=1, column=5)

tk.Label(root, text="Fecha Finalización Tratamiento:").grid(row=2, column=4)
entry_fecha_finalizacion = tk.Entry(root)
entry_fecha_finalizacion.grid(row=2, column=5)

# Create and position the dropdown menu for selecting a treatment in cita
tk.Label(root, text="Tratamiento Cita:").grid(row=4, column=4)
tratamiento_var = tk.StringVar()
tratamiento_dropdown = ttk.Combobox(root, textvariable=tratamiento_var)
tratamiento_dropdown.grid(row=4, column=5)

# Populate the treatment dropdown menu with data from the database
query = "SELECT id, descripcion FROM Tratamiento"
cursor.execute(query)
tratamientos = cursor.fetchall()
tratamiento_dropdown['values'] = [f"{tratamiento[0]} - {tratamiento[1]}" for tratamiento in tratamientos]

# Create and position the delete buttons
delete_patient_button = tk.Button(root, text="Eliminar Paciente", command=delete_patient)
delete_patient_button.grid(row=6, column=1, pady=10)

delete_doctor_button = tk.Button(root, text="Eliminar Doctor", command=delete_doctor)
delete_doctor_button.grid(row=6, column=3, pady=10)

delete_treatment_button = tk.Button(root, text="Eliminar Tratamiento", command=delete_treatment)
delete_treatment_button.grid(row=6, column=5, pady=10)

delete_appointment_button = tk.Button(root, text="Eliminar Cita", command=delete_appointment)
delete_appointment_button.grid(row=6, column=7, pady=10)






# Create and position the entry fields for appointments
tk.Label(root, text="Fecha Cita:").grid(row=0, column=6)
entry_fecha = tk.Entry(root)
entry_fecha.grid(row=0, column=7)

tk.Label(root, text="Hora Cita:").grid(row=1, column=6)
entry_hora = tk.Entry(root)
entry_hora.grid(row=1, column=7)

tk.Label(root, text="Estado Cita:").grid(row=2, column=6)
entry_estado = tk.Entry(root)
entry_estado.grid(row=2, column=7)

# Create and position the buttons
create_patient_button = tk.Button(root, text="Crear Paciente", command=create_patient)
create_patient_button.grid(row=5, column=1, pady=10)

create_doctor_button = tk.Button(root, text="Crear Doctor", command=create_doctor)
create_doctor_button.grid(row=5, column=3, pady=10)

create_treatment_button = tk.Button(root, text="Crear Tratamiento", command=create_treatment)
create_treatment_button.grid(row=5, column=5, pady=10)

create_appointment_button = tk.Button(root, text="Crear Cita", command=create_appointment)
create_appointment_button.grid(row=5, column=7, pady=10)
# Create and position the entry fields for patients
tk.Label(root, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Apellido:").grid(row=1, column=0)
entry_apellido = tk.Entry(root)
entry_apellido.grid(row=1, column=1)

tk.Label(root, text="Dirección:").grid(row=2, column=0)
entry_direccion = tk.Entry(root)
entry_direccion.grid(row=2, column=1)

tk.Label(root, text="Correo electrónico:").grid(row=3, column=0)
entry_correo = tk.Entry(root)
entry_correo.grid(row=3, column=1)

tk.Label(root, text="Fecha de nacimiento:").grid(row=4, column=0)
entry_fecha_nacimiento = tk.Entry(root)
entry_fecha_nacimiento.grid(row=4, column=1)

# Create and position the entry fields for doctors
tk.Label(root, text="Nombre Doctor:").grid(row=0, column=2)
entry_doctor_nombre = tk.Entry(root)
entry_doctor_nombre.grid(row=0, column=3)

tk.Label(root, text="Apellido Doctor:").grid(row=1, column=2)
entry_doctor_apellido = tk.Entry(root)
entry_doctor_apellido.grid(row=1, column=3)

tk.Label(root, text="Dirección Doctor:").grid(row=2, column=2)
entry_doctor_direccion = tk.Entry(root)
entry_doctor_direccion.grid(row=2, column=3)

tk.Label(root, text="Correo electrónico Doctor:").grid(row=3, column=2)
entry_doctor_correo = tk.Entry(root)
entry_doctor_correo.grid(row=3, column=3)

tk.Label(root, text="Especialidad Doctor:").grid(row=4, column=2)
entry_doctor_especialidad = tk.Entry(root)
entry_doctor_especialidad.grid(row=4, column=3)

# Create and position the dropdown menu for selecting a patient in tratamiento
tk.Label(root, text="Paciente Tratamiento:").grid(row=3, column=4)
paciente_var_tratamiento = tk.StringVar()
paciente_dropdown_tratamiento = ttk.Combobox(root, textvariable=paciente_var_tratamiento)
paciente_dropdown_tratamiento.grid(row=3, column=5)

# Populate the patient dropdown menu with data from the database for tratamiento
query = "SELECT id, nombre FROM Paciente"
cursor.execute(query)
pacientes_tratamiento = cursor.fetchall()
paciente_dropdown_tratamiento['values'] = [f"{paciente[0]} - {paciente[1]}" for paciente in pacientes_tratamiento]

cita_options = ["Appointment 1", "Appointment 2", "Appointment 3"]  # Replace with your actual appointment options


cita_dropdown = tk.StringVar(root)
cita_dropdown.set(cita_options[0])  # Set default option


















# Start the Tkinter event loop
root.mainloop()

# Close the cursor and database connection when the window is closed
cursor.close()
conn.close()
