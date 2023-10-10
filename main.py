import argparse

from connect_to_db import session
from models import Group, Teacher, Subject, Student, Grade

MODELS = {'group': Group,
          'teacher': Teacher,
          'subject': Subject,
          'student': Student,
          'grade': Grade}


parser = argparse.ArgumentParser()
parser.add_argument(
    '-a', '--action', help='Choose an action: create, list, update or remove',
    default=argparse.SUPPRESS)
parser.add_argument(
    '-m', '--model', help='Choose model: group, student, teacher, subject or grade',
    default=argparse.SUPPRESS)
parser.add_argument('-n', '--name', help='Enter name',
                    default=argparse.SUPPRESS)
parser.add_argument('--id', help='Enter id', default=argparse.SUPPRESS)


def create(**kwargs):
    model = kwargs.pop('model', None)
    model = model.lower() or None
    if model not in MODELS.keys():
        raise ValueError('Unknown model. Please try again.')

    new_object = MODELS[model](**kwargs)
    session.add(new_object)
    return 'The operation is successful'


def list_handler(**kwargs):
    model = kwargs.pop('model', None)
    model = model.lower() or None
    if model not in MODELS.keys():
        raise ValueError('Unknown model. Please try again.')
    return session.query(*MODELS[model].__table__.columns).select_from(MODELS[model]).all()


def update(**kwargs):
    model = kwargs.pop('model', None)
    model = model.lower() or None
    if model not in MODELS.keys():
        raise ValueError('Unknown model. Please try again.')
    to_edit = session.query(MODELS[model]).filter_by(
        id=kwargs['id']).first()
    to_edit.name = kwargs['name']
    return 'The operation is successful'


def remove(**kwargs):
    model = kwargs.pop('model', None)
    model = model.lower() or None
    if model not in MODELS.keys():
        raise ValueError('Unknown model. Please try again.')
    to_delete = session.query(MODELS[model]).filter_by(
        id=kwargs['id']).first()
    session.delete(to_delete)
    return 'The operation is successful'


if __name__ == '__main__':
    actions = {'create': create,
               'list': list_handler,
               'update': update,
               'remove': remove}

    args_dict = vars(parser.parse_args())
    action = args_dict.pop('action', None)
    if action not in actions.keys():
        raise ValueError('Unknown action. Please try again.')
    print(actions[action](**args_dict))
    session.commit()