import json

class Soldier:
    def __init__(self, age, gender, pu_reps, su_reps, run_time, run_seconds, pu_score, su_score, run_score, total_score, p_f):
        self.age = age
        self.gender = gender
        self.pu_reps = pu_reps
        self.su_reps = su_reps
        self.run_time = run_time
        self.run_seconds = run_seconds
        self.pu_score = pu_score
        self.su_score = su_score
        self.run_score = run_score
        self.total_score = total_score
        self.p_f = p_f

    def set_pu_score(s, data):
        ageRange = age_range(s.age)
        if s.pu_reps < int(list(data)[1]):
            s.pu_score = 0
        elif s.pu_reps >= int(list(data)[-1]):
            s.pu_score = 100
        else:
            s.pu_score = data[str(s.pu_reps)][0].get(ageRange)
        s.set_total_score()
    
    def set_su_score(s, data):
        ageRange = age_range(s.age)
        if s.su_reps < int(list(data)[1]):
            s.su_score = 0
        elif s.su_reps >= int(list(data)[-1]):
            s.su_score = 100
        else:
            s.su_score = data[str(s.su_reps)][0].get(ageRange)
        s.set_total_score()

    def set_run_score(s, data):
        ageRange = age_range(s.age)
        runTime = int(s.run_time.replace(':',''))
        if runTime < int(list(data)[1]):
            s.run_score = 100
        elif runTime >= int(list(data)[-1]):
            s.run_score = 0
        else:
            for i in range(0,len(list(data))+1):
                if runTime > int(list(data)[i]):
                    next
                else:
                    s.run_score = data[str(list(data)[i])][0].get(ageRange)
                    break
        s.set_total_score()

    def set_total_score(s):
        s.total_score = s.pu_score + s.su_score + s.run_score
        s.set_pass_fail()

    def set_pass_fail(s):
        if s.pu_score < 60 or s.su_score < 60 or s.run_score < 60:
            s.p_f = "FAIL"
        else:
            s.p_f = "PASS"

def age_range(age):
    if age in range(17,22):
        return("17-21")
    if age in range(22,27):
        return("22-26")
    if age in range(27,32):
        return("27-31")
    if age in range(32,37):
        return("32-36")
    if age in range(37,42):
        return("37-41")
    if age in range(42,47):
        return("42-46")
    if age in range(47,52):
        return("47-51")
    if age in range(52,57):
        return("52-56")
    if age in range(57,62):
        return("57-61")
    if age >= 62:
        return("62+")

#Get user input for scores
s = Soldier(0, 'Male', 0, 0, 0, 0, 0, 0, 0, 0, "Fail")
while True:
    try:
        s.age = int(input('Enter age: '))
    except:
        print("***Please enter a valid age greater than 16")
        continue
    else:
        if s.age < 17:
            print("***Please enter a valid age greater than 16")
            continue
        else:
            break
while True:
    s.gender = input("Enter 'M/F' or 'Male/Female': ").lower()
    if s.gender == 'male' or s.gender == 'm':
        s.gender = 'male'
        break
    if s.gender == 'female' or s.gender == 'f':
        s.gender = 'female'
        break
    else:
        print("***Please enter 'M/F' or 'Male/Female'")
        continue
while True:
    try:
        s.pu_reps = int(input('Enter PU repetitions: '))
    except:
        print("***Please enter a numerical value")
        continue
    else:
        break
while True:
    try:
        s.su_reps = int(input('Enter SU repetitions: '))
    except:
        print("***Please enter a numerical value")
        continue
    else:
        break
while True:
    try:
        s.run_time = input('Enter 2-mile run time: ')
        split = s.run_time.split(':')
        minutes = int(split[0])*60
        seconds = int(split[1])
        s.run_seconds = minutes + seconds
    except:
        print("***Please enter a valid time ##:##")
        continue
    else:
        break

#Read file for standards
json_file =  open('APFTStandards.json')
data = json.load(json_file)
json_file.close()
male_pu = data['male']['pushup']
male_su = data['male']['situp']
male_run = data['male']['run']
female_pu = data['female']['pushup']
female_su = data['female']['situp']
female_run = data['female']['run']

if s.gender == 'male':
    s.set_pu_score(male_pu)
    s.set_su_score(male_su)
    s.set_run_score(male_run)
else:
    s.set_pu_score(female_pu)
    s.set_su_score(female_su)
    s.set_run_score(female_run)

print('\n****************************************************')
print('******************** APFT SCORE ********************')
print('{} year old {}'.format(s.age, s.gender))
print('Push Ups:')
print('     Raw:   {}'.format(s.pu_reps))
print('     Score: {}'.format(s.pu_score))
print('Sit Ups:')
print('     Raw:   {}'.format(s.su_reps))
print('     Score: {}'.format(s.su_score))
print('2-mile Run:')
print('     Raw:   {}'.format(s.run_time))
print('     Score: {}'.format(s.run_score))
print('Total Score:')
print('     Score: {} points'.format(s.total_score))
print('     P/F:   {}'.format(s.p_f))
print('****************************************************\n')