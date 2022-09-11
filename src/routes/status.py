from datetime import datetime
import subprocess
from flask import current_app
from flask_restplus import Namespace, Resource

start = datetime.now()

router = Namespace(
    'status',
    description='''routes that provide health and version related information'''
)


def uptime():
    duration = (datetime.now() - start).total_seconds()
    result = ''

    days = duration // (24 * 3600)
    duration = duration % (24 * 3600)
    if days > 0:
        result += '%d %s, ' % (days, ('day', 'days')[days == 1])

    hours = duration // 3600
    duration %= 3600
    if days > 0 or hours > 0:
        result += '%d %s, ' % (hours, ('hour', 'hours')[hours == 1])

    minutes = duration // 60
    duration %= 60
    if hours > 0 or minutes > 0:
        result += '%d %s, ' % (minutes, ('minute', 'minutes')[minutes == 1])

    result += '%d %s' % (duration, ('second', 'seconds')[duration == 1])

    return result


def parse_git():
    return {
        'branch': subprocess.check_output(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
        ).decode('ascii').strip(),
        'commit': subprocess.check_output(
            ['git', 'rev-parse', 'HEAD']
        ).decode('ascii').strip()
    }


@router.route('/health')
class Health(Resource):
    def get(self):
        return {'status': 'i\'m alive'}


@router.route('/version')
class Version(Resource):
    def get(self):
        return {
            'git': parse_git(),
            'name': current_app.config['API_NAME'],
            'uptime': uptime(),
            'version': current_app.config['API_SEMANTIC_VERSION']
        }
