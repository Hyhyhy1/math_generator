from fastapi import APIRouter, Response, HTTPException
from typing import List
from generators import *
from models.topics import *
from moodle_export.moodle_converter import *
from models.categories import TEST, category_count, cat_count
import json
import os
from models.generator_id import GENERATOR_UUID, GENERATOR_TOPIC
import uuid

router = APIRouter()

@router.post("/import_params")
async def return_query(tasks: List[TopicWithCompexity]):
    return tasks

# @router.post("/task")
# async def create_tasks(tasks: List[TopicWithCompexity]):
#     problem = []
#     for task in tasks:
#         if task.title == "Матрицы":
#             for _ in range(task.count):
#                 problem.append(await GenerateMatrixTask(
#                     TopicForGenerator(title=task.title, complexity=task.complexity)))
#                 category_count["Матрицы"]+=1
#         if task.title == "Определители":
#             for _ in range(task.count):
#                 problem.append(await GenerateDeterminantTask(
#                     TopicForGenerator(title=task.title, complexity=task.complexity)
#                 ))
#                 category_count["Определители"]+=1
#         if task.title == "Обратная матрица":
#             for _ in range(task.count):
#                 problem.append(await GenerateReverseMatrixTask(
#                     TopicForGenerator(title=task.title, complexity=task.complexity)
#                 ))
#                 category_count["Обратная матрица"]+=1
#         if task.title == "Ранг":
#             for _ in range(task.count):
#                 problem.append(await GenerateMatrixRankTask(
#                     TopicForGenerator(title=task.title, complexity=task.complexity)
#                 ))
#                 category_count["Ранг"]+=1
#         if task.title == "Матричные уравнения":
#             for _ in range(task.count):
#                 problem.append(await GenerateMatrixEquationTask(
#                     TopicForGenerator(title=task.title, complexity=task.complexity)
#                 ))
#                 category_count["Матричные уравнения"]+=1
#         if task.title == "Системы линейных уравнений":
#             for _ in range(task.count):
#                 problem.append(await GenerateLinearEquationTask(
#                     TopicForGenerator(title=task.title, complexity=task.complexity)
#                 ))
#                 category_count["Системы линейных уравнений"]+=1
#         if task.title == "Скалярное, векторное, смешанное произведение векторов":
#             for _ in range(task.count):
#                 problem.append(await GenerateVectorTask(
#                     TopicForGenerator(title=task.title, complexity=task.complexity)
#                 ))
#                 category_count["Скалярное, векторное, смешанное произведение векторов"]+=1
#         if task.title == "Прямая на плоскости":
#             for _ in range(task.count):
#                 problem.append(await GenerateVectorOnPlaneTask(
#                     TopicForGenerator(title=task.title, complexity=task.complexity)
#                 ))
#                 category_count["Прямая на плоскости"] += 1
#         if task.title == "Прямая и плоскость в пространстве":
#             for _ in range(task.count):
#                 problem.append(await GenerateLineAndPlaneInSpaceTask(
#                     TopicForGenerator(title=task.title, complexity=task.complexity)
#                 ))
#                 category_count["Прямая и плоскость в пространстве"] += 1
#     path_test=os.path.join(os.path.dirname(__file__),r'temp_files\test.json')
#     path_cats=os.path.join(os.path.dirname(__file__),r'temp_files\categories.json')
#     with open(path_test, 'w', encoding="utf-8") as file:
#         json.dump(problem, file, ensure_ascii=False)
#     with open(path_cats, 'w', encoding="UTF-8") as file:
#         json.dump(category_count, file, ensure_ascii=False)
#     return problem

# @router.get("/convert")
# async def converter():
#     path_test=os.path.join(os.path.dirname(__file__),r'temp_files\test.json')
#     path_cats=os.path.join(os.path.dirname(__file__),r'temp_files\categories.json')
#     with open(path_test, 'r', encoding="utf-8") as file:
#         json_test = json.load(file)
#     with open(path_cats,'r',  encoding="utf-8") as file:
#         json_cats = json.load(file)
#     result = convert_to_moodle(json_test, json_cats)
#     with open(path_test, 'wb'):
#         pass
#     with open(path_cats, 'wb'):
#         pass
#     return Response(content = result, media_type="application/xml")

@router.post("/get_tasks")
async def get_uuid_task(tasks: List[UUIDGenerator]):
    problem = []
    for task in tasks:
        generator_id = str(task.uuid)
        if generator_id not in GENERATOR_UUID.keys():
            raise HTTPException(
                status_code=400,
                detail="Require UUID doen't exist"
                )
        topic = next(filter(lambda key: generator_id in GENERATOR_TOPIC[key], GENERATOR_TOPIC), None)
        topics = GENERATOR_TOPIC.keys()
        # указанная тема не соотвествует теме генератора
        if (task.topic in topics) and (task.topic!=topic):
            raise HTTPException(
                    status_code=300,
                    detail=f"Provided topic doesn't match generator topic. The actual topic is {topic}"
                )
        # тема не указана - по дефолту даем тему генератора
        if task.topic == None or task.topic == "None":
            task.topic = topic
        
        # if task.topic != topic and task.topic!="None" and task.topic:
        #     raise HTTPException(
        #             status_code=300,
        #             detail="Provided topic doesn't match generator topic"
        #         )
        
        for _ in range(task.count):
            generated_task = GENERATOR_UUID[generator_id]() 
            generated_task['topic'] = task.topic        
            generated_task['uuid'] = generator_id
            problem.append(generated_task)
    return problem

@router.post("/get_convert")
async def get_xml_tasks(tasks: List[Answer], topics: dict):
    result = convert_to_moodle(tasks, topics, 2)
    return Response(content = result, media_type="application/xml")


