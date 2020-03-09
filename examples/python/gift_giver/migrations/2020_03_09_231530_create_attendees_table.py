from orator.migrations import Migration


class CreateAttendeesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('attendees') as table:
            table.increments('id')
            table.string('name').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('attendees')
