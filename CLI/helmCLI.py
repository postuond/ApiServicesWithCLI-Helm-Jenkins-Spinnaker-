import click
from ..SERVICES.helm import HelmRest


@click.command()
@click.option("--chart", type=str, help="Define helm chart file")
@click.option("--url", type=str, help="Url for helm chart repository")
@click.option("--username", type=str, help="Username for helm repository")
@click.option("--password", type=str, help="Password for helm repository")
@click.option("-s", "--show", is_flag=False, flag_value="Flag", default="Default", help="List helm charts")
@click.option("-p", "--post", is_flag=False, flag_value="Flag", default="Default", type=str, help="Post chart file")
@click.option("-d", "--delete", is_flag=False, flag_value="Flag", default="Default", type=str, help="Delete chart file")
def commands(chart, show, post, delete, url, username, password):
    const_inst = HelmRest(url, username, password)
    if chart and show:
        const_inst.list_helm_charts(chart)
    elif chart and post:
        const_inst.post_helm_chart(chart)
    elif chart and delete:
        const_inst.delete_helm_chart(chart)
    else:
        print("You didn't specified any option")


if __name__ == "__main__":
    commands()
