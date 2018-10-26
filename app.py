import api as api
from flask import Flask, jsonify, Response, json,request
from flask_restplus import Api, Resource, model,fields
from werkzeug.exceptions import abort,BadRequest
from logging import ERROR,FileHandler,WARNING,DEBUG
import validator
from jsonschema.exceptions import ValidationError
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False



api = Api(app, version='1.0', title='unsuspended Iot.nxt Accounts',
                 description='sample API that unsuspended the accounts',
                 default='Unsuspent Accounts',
                 default_label='Cell-C')

Model = api.model('Ususpend_Account', {

                'subscriber_id': fields.String(required=True, code=200,
                                               message="successfully unsuspended",
                                               description='The  unsuspend_account details')
                })

__json_content = {
                   "subscriber_id": "1234567890"
                }

if not app.debug:
    files =FileHandler('app.log')
    files.setLevel(ERROR)
    files.setLevel(WARNING)
    files.setLevel(DEBUG)
    app.logger.addHandler(files)

 #Invoke backend
 #validate
class ObjRequstClass:
     def __validate_json_input(self, sub_id):
      try:
            self.__json_content = request.json()
            print ('json from client is validated! :)')
            return True
      except ValueError as e:
            self.__json_content = {}
            print('json from client is not validted :(')
            return False
def unsuspend(status, message):
           """
            process to update access to an account on the IoT.nxt platform
             ensuring that  the Cell C customer can again gain access.
            :return: data in a json format
           """

           return jsonify({'status': status, 'message': message})

@api.route('/api/iotnxt/account/unsuspend', methods=['PUT'])
#@api.model(fields={'name': fields.String, 'age': fields.Integer}
@api.doc(params={'subscriber_id': '1234567890'})
class Unsuspend_account(Resource):
    @api.doc(Model)
    def put(self,request):
               """
                sample API with a PUT method,There are still unknown information
               :return: Status & Message Json format unsuspended
               """
               api.payload
               validated = self.__validate_json_input(request)
               if (validated == 200):
                   if 'subscribe_id' in self.__json_content:

                       collection = unsuspend('200', 'IoT.nxt user has been successfully unsuspended')
                       return collection
                   elif (validated != True):
                       coll = unsuspend('404','json input need subscribe_id params'),404
                       DEBUG(coll)
                       return coll

                   elif (validated == 400):
                          raise BadRequest("Incorrect")

               else:
                  abort(500, ' Not Allowed')

            # ----------




if __name__ == '__main__':
 app.run(debug=True)