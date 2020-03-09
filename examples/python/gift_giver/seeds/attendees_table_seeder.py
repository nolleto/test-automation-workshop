from orator.seeds import Seeder


class AttendeesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('attendees').insert({
            'name': 'john'
        })

