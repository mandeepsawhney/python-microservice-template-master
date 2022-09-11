from flask_restplus import Namespace, Resource
from src.errors import (BadRequest, Conflict, InternalServerError, NotFound, NotImplemented,
                        UnprocessableEntity)


router = Namespace(
    'template',
    description='''routes that show how routes work and should be deleted''',
    validate=False
)


@router.route('/great-success')
class GreatSuccessTest(Resource):
    @router.response(200, 'Success')
    def get(self):
        return {
            'message': 'great success!'
        }, 200


@router.route('/errors/bad-request')
class BadRequestTest(Resource):
    @router.response(400, 'Bad Request')
    def get(self):
        raise BadRequest('Sorry your request is bad :(')


@router.route('/errors/conflict')
class ConflictTest(Resource):
    @router.response(409, 'Conflict')
    def get(self):
        raise Conflict('Your request is conflicted')


@router.route('/errors/internal-server-error')
class InternalServerErrorTest(Resource):
    @router.response(500, 'Internal Server Error')
    def get(self):
        raise InternalServerError('This is real bad')


@router.route('/errors/not-found')
class NotFoundTest(Resource):
    @router.response(404, 'Not Found')
    def get(self):
        raise NotFound('Sorry we couldn\'t find that :(')


@router.route('/errors/not-implemented')
class NotImplementedTest(Resource):
    @router.response(501, 'Not Implemented')
    def get(self):
        raise NotImplemented('This route is not implemented yet')


@router.route('/errors/unprocessable-entity')
class UnprocessableEntityTest(Resource):
    @router.response(422, 'Unprocessable Entity')
    def get(self):
        ex = UnprocessableEntity('Nope can\'t do it')
        ex.errors = [
            {
                'code': 5432,
                'field': 'first_name',
                'message': 'You must provide your first name'
            }
        ]
        raise ex
