from django.db.models.expressions import RawSQL

from my_awesome_project.core.models import Order


def get_users():
    spent_money_subquery = (
        "select sum(total) spent_money from core_order as co where co.customer = core_order.customer"
    )
    top_users = (
        Order.objects.annotate(spent_money=RawSQL(spent_money_subquery, []))
        .order_by("-spent_money")
        .values("customer", "spent_money")
        .distinct()[:5]
    )
    items_subquery = (
        "select count(item) item_count from"
        "(select item, customer from core_order co group by customer, item)"
        "co where co.item=core_order.item"
    )
    items = (
        Order.objects.filter(customer__in=map(lambda x: x["customer"], top_users))
        .annotate(item_count=RawSQL(items_subquery, []))
        .filter(item_count__gte=2)
        .values("customer", "item")
        .distinct()
    )
    gems = {}
    for i in items:
        print(i)
        if gems.get(i["customer"]):
            gems.get(i["customer"]).append(i["item"])
        else:
            gems[i["customer"]] = [i["item"]]
    result = [
        {"username": i["customer"], "spent_money": i["spent_money"], "gems": gems.get(i["customer"], [])}
        for i in top_users
    ]
    return result
