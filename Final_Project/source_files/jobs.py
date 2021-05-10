''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    Script File Name: jobs.py
    
        
    Description: This module contains core functionality for working with
    jobs in Redis.'''

# Import modules:
    
import redis, uuid 
from hotqueue import HotQueue  

# Instantiate "HotQueue" object and define hostname (IP address) for the queue

q = HotQueue("queue", host="jcam989-prod-redis-service", port=6379, db=0)

# Instantiate "redis" object for database to store temperature data

rd_temp = redis.StrictRedis(host="jcam989-prod-redis-service", port=6379, db=1, decode_responses = True)

# Instantiate "redis" object for database to store job ID's, keys, and statuses:

rd_jobs = redis.StrictRedis(host="jcam989-prod-redis-service", port=6379, db=2, decode_responses = True)

# Instantiate "redis" object for database to store image image data of analysis plots:

rd_im = redis.StrictRedis(host="jcam989-prod-redis-service", port=6379, db=2)

# Define private function "_generate_jid()" to generate an ID to associate with job

def _generate_jid():
    return str(uuid.uuid4())

# Define private function "_generate_job_key()" to return key to associate with job ID

def _generate_job_key(jid):
    return 'job.{}'.format(jid)


# Define private function "_instantiate_job()" to return dictionary of job params

def _instantiate_job(jid, status, start, end):
    if type(jid) == str:
        return {'id': jid,
                'status': status,
                'start': start,
                'end': end
        }
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'start': start.decode('utf-8'),
            'end': end.decode('utf-8')
    }

def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd_jobs.hmset(job_key, job_dict)

def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)
    
def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    
    # Invoke function "_generate_jid()"
    
    jid = _generate_jid()
    
    # Invoke function "_instantiate_job()":
    
    job_dict = _instantiate_job(jid, status, start, end)
    
    # Invoke function "_save_job()":
        
    _save_job(_generate_job_key(jid), job_dict)
    
    # Invoke function "_queue_job()": 
        
    _queue_job(jid)
    
    return job_dict

def get_job_data(jid):
    jid, status, job_type, start, end = rd_jobs.hmget(_generate_job_key(jid), 'id', 'status', 'job_type', 'start', 'end')
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, job_type, start, end)
    return job_dict

def get_job_start(jid):
    jid, status, job_type, start, end = rd_jobs.hmget(_generate_job_key(jid), 'id', 'status', 'job_type', 'start', 'end')
    return (str(start)[1:]).replace("'","")

def get_job_end(jid):
    jid, status, job_type, start, end = rd_jobs.hmget(_generate_job_key(jid), 'id', 'status', 'job_type', 'start', 'end')
    return (str(end)[1:]).replace("'","")

def update_job_status(jid, status):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, start, end = rd_jobs.hmget(_generate_job_key(jid), 'id', 'status', 'start', 'end')
    job = _instantiate_job(jid, status, start, end)
    if job:
        job['status'] = status
        _save_job(_generate_job_key(jid), job)
    else:
        raise Exception()
