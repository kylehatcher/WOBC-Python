import sys

print(str(int(sys.argv[1])+int(sys.argv[2])) + ' ' + str(int(sys.argv[1])*int(sys.argv[3])) + " " + str(int(sys.argv[1])%int(sys.argv[2])) + " " + str(int(sys.argv[3])/int(sys.argv[1])))
sys.argv[1] = int(sys.argv[1]) + 1
sys.argv[2] = int(sys.argv[2]) + 1
sys.argv[3] = int(sys.argv[3]) + 1
print(str(sys.argv[1]>>3) + ' ' + str(sys.argv[2]/2) + ' ' + str(sys.argv[1]|sys.argv[2]))
print(int(sys.argv[1]) + (len(sys.argv)-1))