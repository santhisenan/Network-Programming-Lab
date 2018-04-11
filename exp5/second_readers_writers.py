import sys

lock = 0
no_of_readers = 0

def reader():
    global no_of_readers
    print("Input: Reader")
    if lock:
        print("A wirter has acquired the lock, please wait till it releases the lock")
        return
    else:   
        no_of_readers += 1
        print("The reader can read.")

def release_reader():
    global no_of_readers    
    if(no_of_readers == 0):
        print("No readers")
    else:
        no_of_readers -= 1

def writer():
    global lock
    if lock:
        print("Another writer is reading.")
    else:
        print("Writer can write")
        lock = 1
def release_writer():
    global lock
    if lock == 0:
        print("No writer is writing")
    else:
        lock = 0

while True:
    read = input()
    if read == 'read':
        reader()
    elif read == 'write':
        writer()
    elif read == 'relread': # release reader
        release_reader()
    elif read == 'relwrite': # release writer
        release_writer()
    else: 
        sys.exit()        