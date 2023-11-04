from rest_framework.test import APITestCase
from .models import Todo

import json

todo_to_create = {
  "todo":"Todo created juts for test case"
}
todos_list_to_create = [
  "Todo created juts for test case",
  "Todo created juts for test case",
  "Todo created juts for test case",
  "Todo created juts for test case"
]
class ListTodoTest(APITestCase):
  def test_create_todo(self):
    
    create_response = self.client.post("/api/todo/", data=todo_to_create, format='json')
  
    self.assertEqual(create_response.status_code, 201)
    self.assertEqual(Todo.objects.count(), 1)
    self.assertEqual(Todo.objects.get().todo, todo_to_create["todo"])
    
  def test_list_todo(self):
    for todo in todos_list_to_create:
      Todo.objects.create(
        todo=todo
      )     
    list_response = self.client.get("/api/todo/", format='json')
    data = json.loads(list_response.content)
    
    self.assertEqual(list_response.status_code, 200)
    self.assertEqual(len(data), 4)
    self.assertEqual(data[0]['todo'], todos_list_to_create[0])
    

class DetailTodoTest(APITestCase):
  def test_list_one_todo(self):

    

