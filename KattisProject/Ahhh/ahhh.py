# Logan Barnes
# Ahhh

def compareAs():
    # Initialize
    patient = input()
    doctor = input()

    patientAs = patient.count('a')
    doctorAs = doctor.count('a')

    # print(patientAs)
    # print(doctorAs)

    if patientAs >= doctorAs:
        print("go")
    else:
        print("no")

    return 0

compareAs()