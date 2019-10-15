
from multiprocessing import Pool, Process, cpu_count


class ProcessManager:

    __pool_size = 1
    __process_list = []
    __cpu_count = cpu_count()

    @staticmethod
    def get_cpu_count():
        return ProcessManager.__cpu_count

    @staticmethod
    def update_pool(size):
        ProcessManager.__pool_size = size

    @staticmethod
    def run_in_pool(func, input_list):
        print('ProcessManager.__pool_size: ', ProcessManager.__pool_size)
        pool = Pool(ProcessManager.__pool_size)
        pool.map(func, input_list)
        pool.close()
        pool.join()


    @staticmethod
    def run_in_pool_2_inputs(func, input_list):
        pool = Pool(ProcessManager.__pool_size)
        pool.starmap(func, input_list)
        pool.close()
        pool.join()

    @staticmethod
    def create_new_process(func, input_list):
        new_process = Process(target=func, args=tuple([input_list]))
        ProcessManager.__process_list.append(new_process)
        new_process.start()


    @staticmethod
    def join_processes():
        for proc in ProcessManager.__process_list:
            proc.join()


    @staticmethod
    def kill_process(proc):
        ProcessManager.__process_list.remove(proc)
        proc.terminate()

    @staticmethod
    def kill_all_processes():
        for proc in ProcessManager.__process_list:
            proc.terminate()
