from fedlearn.tasks import train
from fedlearn.utils import MAX_TRAINING_ROUNDS
import sys

def main(q):
    
    res = train.apply_async((), queue=q, countdown=2)
    result = res.get(timeout=4, propagate=False)
    print(result)
    print(res.failed())
    print(res.successful())
    print(res.state)

if __name__ == '__main__':
    q = sys.argv[1]
    main(q)