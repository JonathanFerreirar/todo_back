from rest_framework.test import APITestCase
from .models import Todo

import json

todo_to_create = "Todo created juts for test case"

obj_todo_to_create = {
  "todo":"Todo created juts for test case"
}
obj_todo_to_update = {
  "todo":"Todo updated juts for test case"
}

todos_list_to_create = [
  "Todo created juts for test case",
  "Todo created juts for test case",
  "Todo created juts for test case",
  "Todo created juts for test case"
]
class ListTodoTest(APITestCase):
  
  
  def test_create_todo(self):    
    create_response = self.client.post("/api/todo/", data=obj_todo_to_create, format='json')
  
    self.assertEqual(create_response.status_code, 201)
    self.assertEqual(Todo.objects.count(), 1)

    
    self.assertEqual(Todo.objects.get().todo, obj_todo_to_create["todo"])
    
    
    
  def test_list_todo(self):
    for todo in todos_list_to_create:
      Todo.objects.create(
        todo=todo
      )     
    list_response = self.client.get("/api/todo/", format='json')
    todo_dic = json.loads(list_response.content)
    
    self.assertEqual(list_response.status_code, 200)
    self.assertEqual(len(todo_dic), 4)
    self.assertEqual(todo_dic[0]['todo'], todos_list_to_create[0])
    



class DetailTodoTest(APITestCase):

  def test_list_one_todo_no_exist(self):
    todo_no_exist = self.client.get("/api/todo/1/", format='json')
    
    self.assertEqual(todo_no_exist.status_code, 404)
    self.assertEqual(Todo.objects.count(), 0)
    
  
  def test_one_exiting_todo(self):
     Todo.objects.create(
        todo=todo_to_create)
     
     todo = self.client.get("/api/todo/1/", format='json')
     todo_dic = json.loads(todo.content)
     
     self.assertEqual(todo.status_code, 200)
     self.assertEqual(todo_dic['todo'], todo_to_create)
     
     
  def test_delete_one_todo(self):
    Todo.objects.create(
        todo=todo_to_create)
    
    todo = self.client.delete("/api/todo/1/", format='json')
    
    self.assertEqual(todo.status_code, 204)
    self.assertEqual(Todo.objects.count(), 0)
    
  def test_update_one_todo(self):
     Todo.objects.create(
        todo=todo_to_create)
     
     todo = self.client.put("/api/todo/1/",data=obj_todo_to_update, format='json')
     todo_dic = json.loads(todo.content)
     
     self.assertEqual(todo.status_code, 200)
     self.assertEqual(todo_dic['todo'], obj_todo_to_update["todo"])
    

