"""Disk load tester

Usage:
    disk_load_tester.py [<destination>] [--reps=<reps>] [--nprocs=<nprocs>]

Options:
    <destination>       The target directory [Default: /mnt/user_storage]
    --reps=<reps>       Number of read/write loops, per process [Default: 200]
    --nprocs=<nprocs>   Number of parallel processes to spawn [Default: 20]

"""

from docopt import docopt
import os
import hashlib
import random
import time
from datetime import datetime


NUM_FILES_TO_WRITE = 15
NUM_FILES_TO_READ = 5

def write_some(path):
    print 'pid', os.getpid(), 'writing',
    for i in range(NUM_FILES_TO_WRITE):
        filename = path + '/file' + str(random.random())
        with open(filename, 'w') as f:
            for i in range(1000):
                f.write('a' * 100)

def read_some(path):
    print 'pid', os.getpid(), 'reading',
    files_to_read = os.listdir(path)
    if len(files_to_read) >= NUM_FILES_TO_READ:
        files_to_read = random.sample(files_to_read, NUM_FILES_TO_READ)
    for filename in files_to_read:
        open(path + '/' + filename).read()


def do_work(path, reps):
    start = time.time()
    unique_per_process = hashlib.md5(str(os.getpid())).hexdigest()
    random.seed(unique_per_process)
    working_directory = path + unique_per_process + '/'
    os.makedirs(working_directory)
    print 'pid', os.getpid(), 'working on', working_directory

    for x in range(reps):
        random.choice([read_some, write_some])(working_directory)
        time.sleep((os.getpid() % 3 )* 0.2)
    print
    print 'Work for process', os.getpid(), 'took: ', time.time() - start, ' seconds'



if __name__ == '__main__':
    arguments = docopt(__doc__)
    print arguments
    target_dir = arguments['<destination>'] or '/mnt/user_storage'
    target_dir += '/' + datetime.now().isoformat() + '/'

    num_processes = int(arguments['--nprocs'])
    reps = int(arguments['--reps'])

    children = []
    start = None
    for procs in range(num_processes):
        child = os.fork()
        if child:
            children.append(child)
            if not start:
                start = time.time()
        else:
            do_work(target_dir, reps)
            break

    for child in children:
        try:
            os.waitpid(child, 0)
        except:
            pass

