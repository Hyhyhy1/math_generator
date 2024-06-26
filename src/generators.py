from schemas import *
import numpy as np
import sympy as sp
import scipy as sc
from random import *
from math import *
from moodle_export.converter import *
from task_generator import *

# async def create_db_task(topic_schema, task):
#   topic_db = await Topic.objects.get(name = topic_schema.title)
#   await Task.objects.create(topic=topic_db.id, 
#                             complexity = topic_schema.complexity, 
#                             text = str(task["data"]), answer = str(task["answer"])) 


'''
Генерация задач Матрицы
'''
async def GenerateMatrixTask(topic: TopicForGenerator):
    if topic.complexity == 0:
      task = GenerateMatrixSizeTask(topic.title)
      return task
    elif topic.complexity == 1:
      task = GenerateMatrixElementTask(topic.title)
      return task
    elif topic.complexity == 2:
      task = GenerateMatrixSummTask(topic.title)
      return task
    elif topic.complexity == 3:
      task = GenerateMatrixNumberMultiplicationTask(topic.title)
      return task
    elif topic.complexity == 4:
      task = GenerateMatrixTransposeTask(topic.title)
      return task
    elif topic.complexity == 5:
      task = GenerateMatrixMultiplicationTask(topic.title)
      return task


'''
Генерация задач Определители
'''
async def GenerateDeterminantTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
        task = GenerateFindDeterminantTask(topic.title)
        return task
    case 1:
        task = GenerateDeterminantEquationTask(topic.title)
        return task
     

'''
Генерация задач Обратная матрица
'''
async def GenerateReverseMatrixTask(topic: TopicForGenerator):
  match topic.complexity:
     case 0:
        task = GenerateFindReverseMatrixTask(topic.title)
        return task
     case 1:
        task = GenerateFindReversedMatrixElementTask(topic.title)
        return task
     

'''
Генерация задач Ранг
'''
async def GenerateMatrixRankTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateFindMatrixRankTask(topic.title)
      return task
    

'''
Генерация задач Матричные уравнения
'''
async def GenerateMatrixEquationTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateSolveMatrixEquationTask(topic.title)
      return task
    case 1:
      task = GenerateSolveDoubleMatrixEquationTask(topic.title)
      return task


'''
Генерация задач Системы линейных уравнений
'''
async def GenerateLinearEquationTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateSolveLinearEquationTask(topic.title)
      return task


'''
Генерация задач Скалярное, векторное, смешанное произведение векторов
'''
async def GenerateVectorTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateScalarVectorMultiplicationTask(topic.title)
      return task
    case 1:
      task = GenerateVectorVectorMultiplicationTask(topic.title)
      return task
    case 2:
      task = GenerateVectorVectorMultiplicationModuleTask(topic.title)
      return task
    case 3:
      task = GenerateMixedVectorMultiplicationTask(topic.title)
      return task
    case 4:
      task = GenerateIsCollinearVectorsTask(topic.title)
      return task
    case 5:
      task = GenerateIsComplanarVectorsTask(topic.title)
      return task


'''
Генерация задач Прямая на плоскости
'''    
async def GenerateVectorOnPlaneTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateFindLineEquationByPointsTask(topic.title)
    case 1:
      task = GenerateFindParalelLineEquationByEquationTask(topic.title)
    case 2:
      task = GenerateFindParalelLineEquationByPointsTask(topic.title)
    case 3:
      task = GenerateFindCrossPointOfTwoLinesTask(topic.title)
    case 4:
      task = GenerateFindDicstanceFromLineToPointTask(topic.title)


  return task

'''
Генерация задач Прямая и плоскость в пространстве
'''
async def GenerateLineAndPlaneInSpaceTask(topic: TopicForGenerator):
  match topic.complexity:
    case 0:
      task = GenerateFindPlaneEquationByThreePointsTask(topic.title)
    case 1:
      task = GenerateFindPlaneEquationByPointAndNormalVector(topic.title)
    case 2:
      task = GenerateFindParallelPlaneEquationTask(topic.title)
    case 3:
      task = GenerateFindOrtPlaneEquationTask(topic.title)
    case 4:
      task = GeneratePointProjectionOnLineTask(topic.title)
    case 5:
      task = GeneratePointProjectionOnPlainTask(topic.title)


  return task
    