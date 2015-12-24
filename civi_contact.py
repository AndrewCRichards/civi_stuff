import requests
import civi_base


class CiviContact:
    entity = "Contact"

    def fetch_all(self):
        url_parameters = {}
        url_parameters['action'] = "get"
        url_parameters['entity'] = self.entity
        url_parameters['key'] = civi_base.site_key
        url_parameters['api_key'] = civi_base.api_key
        url_parameters['json'] = "1"
        return requests.get(civi_base.protocol_s + civi_base.base_URL, params=url_parameters)


def main():
    print(str(CiviContact().fetch_all().json()))


if __name__ == '__main__':
    main()
