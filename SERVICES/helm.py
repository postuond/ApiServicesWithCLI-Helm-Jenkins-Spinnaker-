import os
import requests
import requests.auth
from RestService import RequestService,HttpMethods


class HelmRest(RequestService, HttpMethods):

    def list_helm_charts(self, chart_name):
        get = self.request_action(HttpMethods.GET.value, self.url + chart_name)
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

    def post_helm_chart(self, chart_name):
        post = self.request_action(HttpMethods.POST.value, self.url, {"charts": chart_name})
        status = post.status_code
        if status != requests.codes.created:
            raise Exception(f"Chart uploading has failed with {status}")
        elif status == requests.codes.bad_request:
            raise Exception(f"Bad request! {status}")
        elif status == requests.codes.unauthorized:
            raise Exception(f"Something went wrong with authorization! {status}")
        return

    def delete_helm_chart(self, chart_name):
        delete = self.request_action(HttpMethods.DELETE.value, self.url + chart_name)
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
