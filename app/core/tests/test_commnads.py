"""Test custome Django management commands"""

# used to temporarily replace parts of your code with 
# mock objects during the test
from unittest.mock import patch

# Specific Postgres connection error, 
# in case Postgres isn’t ready yet.
from psycopg2 import OperationalError as Psycopg2Error

# Lets you programmatically call a Django management command
# from inside Python code
from django.core.management import call_command

# Django’s general database connection error.
from django.db.utils import OperationalError

# A lightweight Django test class that doesn’t need the database.
from django.test import SimpleTestCase


# check is a method inside BaseCommand which is the django class
# inherited by our custom class "Command"
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test Commnads"""

    # To check if the db is immediatley available
    def test_wait_for_db_ready(self, patched_check):
        """Tets waiting for db if db is ready"""
        # to somulate the db is ready and so 
        # the test must be run exactly once
        patched_check.return_value = True

        call_command('wait_for_db')  
        # to test that the command is setup correctly and callable

        patched_check.assert_called_once_with(databases=['default'])

    # To check if the db is not availble immediately and we 
    # have to recheck several times
    @patch('time.sleep')
    def test_wait_for_db_delay(self, pathced_sleep, patched_check):
        """waiting for db when getting operational error"""
        # call Psycopg2Error twice, OperationalError thrice, 
        # and then finally return true(i.e. db is finally available)
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
