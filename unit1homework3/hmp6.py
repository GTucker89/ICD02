wf = int(input("Enter the number of water fountains: "))
wfl = input("Enter the locations of the water fountains: ")
wfc = (input("Enter the condition of the water fountains: "))
cr = int(input("Enter the number of classrooms: "))
crc = (input("Enter the condition of the classrooms: "))
rr = int(input("Enter the number of restrooms: "))
rrl = input("Enter the locations of the restrooms: ")
rrc = (input("Enter the condition of the restrooms: "))
gy = int(input("Enter the number of gyms: "))
gyl = input("Enter the locations of the gyms: ")
gyc = (input("Enter the condition of the gyms: "))
ly = int(input("Enter the number of lybries: "))
lyl = input("Enter the locations of the lybaries: ")
lyc = (input("Enter the condition of the lybaries: "))



total_r = wf + rr + gy + ly
total_rd = round(total_r / cr, 2)
rrd = round(rr / cr, 2)
wfd = round(wf / cr,2)
rrd = round(rr/cr,2)
gyd = round(gy/cr,2)
lyd = round(ly/cr,2)

print(f"Their are {wf} water founations")
print(f"They are located at {wfl}")
print(f"Their conditions {wfc}")
print(f"The number of classrooms is {cr}")
print("They are dispersed around the school")
print(f"Their coundition is {crc}")
print(f"There is {rr} restrooms")
print(f"They are located at {rrl}")
print(f"Their condition is {rrc}")
print(f"There is {gy} number of gyms")
print(f"They are located at {gyl}")
print(f"Their condition is {gyc}")
print(f"There is {ly} number of lybaries")
print(f"They are located at {lyl}")
print(f"Their condition is {lyc}")
print(f"The total resource density is {total_rd}")
print(f"The resources denisty of restrooms is {rrd}")
print(f"The resources denisty of water fountians is {wfd}")
print(f"The resources denisty of lybries is {gyd}")
print(f"The resources denisty of gyms is {lyd}")
