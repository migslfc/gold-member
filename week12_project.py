#Create a list of services using Python. IE: S3, Lambda, EC2, etc

#The list should be empty initially.
services = []

#Populate the list using append or insert.
services.append('S3')
services.append('Lambda')
services.append('DynamoDB')
services.insert(2,'Cloud9')
services.insert(0, 'EC2')

#Print the list and the length of the list.
print(services)
print(len(services))

#Remove two specific services from the list by name or by index.
services.remove('Lambda')
del services[1]

#Print the new list and the new length of the list.
print(services)
print(len(services))

