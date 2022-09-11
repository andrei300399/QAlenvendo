class JsTestTask:
    JS_TEST_TASK = 'js-test-task/'

    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price

    @staticmethod
    def deserialize_array(json_obj):
        item_list = json_obj["products"]
        js_test_tasks = []
        for item in item_list:
            js_test_task = JsTestTask(**item)
            js_test_tasks.append(js_test_task)
        return js_test_tasks

    @staticmethod
    def get_phones(api_client, search='Alcatel', sort_field='name'):
        params = {
            "search": search,
            "sort_field": sort_field
        }
        return api_client.get(JsTestTask.JS_TEST_TASK, params)
