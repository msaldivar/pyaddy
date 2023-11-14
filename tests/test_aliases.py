import unittest
from pyaddy.API.aliases import Aliases

class TestAliases(unittest.TestCase):

    def setUp(self) -> None:
        """Test class setup"""
        self.aliases = Aliases()

    def test_get_all_aliases(self):
        """Test getting all ACTIVE aliases SORTED by CREATED_AT"""
        params = {
            'filter[active]': 'true',
            'sort': '-created_at',
        }
        resp = self.aliases.get_all_aliases(params)
        details = resp.json()
        
        assert resp.status_code == 200, f'Getting alll aliases did not return 200: {resp.status_code}'
        assert details['meta']['total'] > 0, 'API returned 0 aliases'
        assert details['data'][0]['active'], 'API returned inactive aliases should only be active aliases'

    def test_alias_interactions(self):
        """Test several alias APIs, taking the result of one and feeding the result as an input for the next call"""

        # Test creating a new alias
        payload = {
            'domain': 'addymail.com',
            'description': 'addy pytest',          
        }
        
        resp = self.aliases.create_new_alias(payload)
        details = resp.json()
        alias_id = details['data']['id']

        assert resp.status_code == 201, f'API creating a new alias did not return 201: {resp.status_code}'
        assert details['data']['domain'] == 'addymail.com', f'Alias domain not set: {details["data"]["domain"]}'
        assert details['data']['description'] == 'addy pytest', f'Alias description not set: {details["data"]["description"]}'
        assert details['data']['from_name'] == None, f'Alias from_name not None: {details["data"]["from_name"]}'
        
        # Test getting a specific alias
        resp = self.aliases.get_specific_alias(alias_id)
        assert resp.status_code == 200, f'API getting specific alias did not return 200: {resp.status_code}'
        assert len(resp.json()) == 1, 'Only 1 alias should have been returned'

        # Test updating a specific alias
        payload = {
            'description': 'pytest update',
            'from_name': 'bruce wayne'
        }
        resp = self.aliases.update_specific_alias(alias_id, payload)
        details = resp.json()
    
        assert resp.status_code == 200, f'API updating alias did not return 200: {resp.status_code}'
        assert details['data']['description'] == 'pytest update', f'Alias description did not update to - pytest update: {details["data"]["description"]}'
        assert details['data']['from_name'] == 'bruce wayne', f'Alias from_name did not update to - bruce waynce: {details["data"]["from_name"]}'

        # Test deleting a specific alias
        resp = self.aliases.delete_specific_alias(alias_id)
        assert resp.status_code == 204, f'API deleting alias did not return 204: {resp.status_code}'

        # Test restoring a specific alias
        resp = self.aliases.restore_specific_alias(alias_id)
        details = resp.json()

        assert resp.status_code == 200, f'API restoring alias did not return 200: {resp.status_code}'
        assert details['data']['id'] == alias_id, 'Alias not restored with original id'
        assert details['data']['active'], 'Restored alias is not active'


        # Test deactivating a specific alias
        resp = self.aliases.deactivate_alias(alias_id)
        assert resp.status_code == 204, f'API deactivating alias did not return 204: {resp.status_code}'

        # Test activating a specific alias
        payload = {'id': alias_id}
        resp = self.aliases.activate_alias(payload)
        details = resp.json()

        assert resp.status_code == 200, f'API activating alias did not return 200: {resp.status_code}'
        assert details['data']['id'] == alias_id, 'Alias was not activated'
        assert details['data']['active'], 'Alias not marked as active'

        # Test forgetting a specific alias
        resp = self.aliases.forget_specific_alias(alias_id)
        assert resp.status_code == 204, f'API forgetting alias did not return 204: {resp.status_code}'
