from mrjob.job import MRJob
import csv

class ProductCounter(MRJob):

    def configure_args(self):
        super(ProductCounter, self).configure_args()
        self.add_passthru_arg('--skip-header', action='store_true', default=False,
                                help='Skip the CSV header')
    def mapper(self, _, line):
        if self.options.skip_header:
            self.options.skip_header = False
            return
        reader = csv.reader([line], skipinitialspace=True)
        product_id = next(reader)[4] 

        yield product_id, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    mr_job = ProductCounter()

    mr_job.run()
