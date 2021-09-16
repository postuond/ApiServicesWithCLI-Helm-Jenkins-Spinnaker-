import requests
import requests.auth
from RestService import RequestService, HttpMethods


class HelmRest(RequestService):

    def list_helm_charts(self):
        get = self.request_action(HttpMethods.GET.value, self.url)
        status = get.status_code
        if status == requests.codes.no_content:
            raise Exception(f"Chart was not found on repository! {status}")
        elif status == requests.codes.bad_request:
            raise Exception(f"Bad request! {status}")
        elif status == requests.codes.not_found:
            raise Exception(f"Not found! {status}")
        elif status == requests.codes.unauthorized:
            raise Exception(f"Something went wrong with authorization! {status}")
        return

    def post_helm_chart(self, name):
        post = self.request_action(HttpMethods.POST.value, self.url, {'chart': name})
        status = post.status_code
        if status != requests.codes.created:
            raise Exception(f"Chart uploading has failed with {status}")
        elif status == requests.codes.bad_request:
            raise Exception(f"Bad request! {status}")
        elif status == requests.codes.unauthorized:
            raise Exception(f"Something went wrong with authorization! {status}")
        return

    def delete_helm_chart(self, name):
        delete = self.request_action(HttpMethods.DELETE.value, f"{self.url}/{name}")
        status = delete.status_code
        if status == requests.codes.no_content:
            raise Exception(f"Chart was not found on repository! {status}")
        elif status == requests.codes.bad_request:
            raise Exception(f"Bad request! {status}")
        elif status == requests.codes.not_found:
            raise Exception(f"Not found! {status}")
        elif status == requests.codes.unauthorized:
            raise Exception(f"Something went wrong with authorization! {status}")
        return

