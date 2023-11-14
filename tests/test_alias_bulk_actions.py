import unittest

from collections import Counter
from pyaddy.API.aliases import Aliases
from pyaddy.API.alias_bulk_actions import AliasBulkActions

class TestAliasBulkActions(unittest.TestCase):

    def setUp(self) -> None:
        """Test class setup"""
        self.alias_bulk = AliasBulkActions()
        self.test_alias_1 = Aliases().create_new_alias({'domain': 'addymail.com', 'description': 'pytest1'}).json()
        self.test_alias_2 = Aliases().create_new_alias({'domain': 'addymail.com', 'description': 'pytest2'}).json()
        self.test_alias_ids = [self.test_alias_1['data']['id'], self.test_alias_2['data']['id']]
        

    def test_get_aliases(self):
        """Test bulk get specific aliases"""
        resp = self.alias_bulk.get_aliases([self.test_alias_1['data']['id'],
                                             self.test_alias_2['data']['id']])
        details = resp.json()
        returned_ids = [details['data'][0]['id'], details['data'][1]['id']]

        assert resp.status_code == 200, f'Bulk getting aliases did not return 200 {resp.status_code}'
        assert len(details['data']) == 2, f'Bulk getting aliases did not return 2: {len(details["data"])}'
        assert Counter(returned_ids) == Counter(self.test_alias_ids), 'The IDs returned dont match the ones created'

    def test_bulk_deactivate_activate_aliases(self):
        """Test bulk deactivating and activating aliases"""

        # Test bulk deactivating
        resp = self.alias_bulk.bulk_deactivate_aliases(self.test_alias_ids)
        details = resp.json()
        returned_ids = details['ids']

        assert resp.status_code == 200, f'Bulk deactivate aliases did not return 200 {resp.status_code}'
        assert details['message'] == '2 aliases deactivated successfully', 'Aliases not deactivated'
        assert Counter(returned_ids) == Counter(self.test_alias_ids), 'The IDs returned dont match the ones created'
        
        # Test bulk activating
        resp = self.alias_bulk.bulk_activate_aliases(self.test_alias_ids)
        details = resp.json()
        returned_ids = details['ids']

        assert resp.status_code == 200, f'Bulk activate aliases did not return 200 {resp.status_code}'
        assert details['message'] == '2 aliases activated successfully', 'Aliases not activated'
        assert Counter(returned_ids) == Counter(self.test_alias_ids), 'The IDs returned dont match the ones created'

    def test_bulk_delete_restore_aliases(self):
        """Test bulk delete and restore aliases"""

        # Test bulk deleting
        resp = self.alias_bulk.bulk_deleted_aliases(self.test_alias_ids)
        details = resp.json()
        returned_ids = details['ids']

        assert resp.status_code == 200, f'Bulk delete aliases did not return 200 {resp.status_code}'
        assert details['message'] == '2 aliases deleted successfully', 'Aliases not deleted'
        assert Counter(returned_ids) == Counter(self.test_alias_ids), 'The IDs returned dont match the ones created'

        # Test bulk restoring
        resp = self.alias_bulk.bulk_restore_aliases(self.test_alias_ids)
        details = resp.json()
        returned_ids = details['ids']

        assert resp.status_code == 200, f'Bulk restore aliases did not return 200 {resp.status_code}'
        assert details['message'] == '2 aliases restored successfully', 'Aliases not restored'
        assert Counter(returned_ids) == Counter(self.test_alias_ids), 'The IDs returned dont match the ones created'

    def test_bulk_forget_aliases(self):
        """Test bulk forget aliases"""

        resp = self.alias_bulk.bulk_forget_aliases(self.test_alias_ids)
        details = resp.json()
        returned_ids = details['ids']

        assert resp.status_code == 200, f'Bulk forget aliases did not return 200 {resp.status_code}'
        assert details['message'] == '2 aliases forgotten successfully'
        assert Counter(returned_ids) == Counter(self.test_alias_ids), 'The IDs returned dont match the ones created'
        