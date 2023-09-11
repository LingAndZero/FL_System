import time
from utils.fix_random import fix_seed
from utils.get_config import *
from utils.options import args_parser


if __name__ == "__main__":
    start_time = time.time()
    start_time = time.time()
    start_time = time.time()

    args = args_parser()
    print("{:15} {}".format("Algorithm:", args.algorithm))
    print("{:15} {}".format("Dataset:", args.dataset))
    print("{:15} {}".format("Model:", args.model))
    print("{:15} {}".format("Seed:", args.seed))

    fix_seed(args.seed)
    global_model = get_model(args)
    dataset_train, dataset_test = get_dataset(args)


    finish_time = time.time()
    print(finish_time - start_time)
