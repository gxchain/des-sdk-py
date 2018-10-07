import Client
import requests
import time
import Common.util as util
import json
import logging
log = logging.getLogger(__name__)

class BlacklistGatewayClient(Client.DESClient):
    """get question token
       @param requestId
       @param redirectUrl
       @param loanInfoList
       @returns {Promise<any>}
    """
    def getQuestionToken(self, requestId, redirectUrl, loanInfoList):
        getTokenParams = { "requestId": requestId,
                           "redirectUrl": redirectUrl,
                           "loadInfos": loanInfoList}
        response = requests.post("https://survey.gxb.io/blacklist/token", data=getTokenParams)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            log.error(response.status_code)


    """get question report
       @param token
       @returns {Promise<any>}
    """
    def getQuestionReport(self, token):
        getQuestionReportParmas = {'token': token,
                                   'timestamp': int(time.time()) + 60
                                   }
        getQuestionReportParmas['signature'] = util.sign(bytes(str(getQuestionReportParmas), 'utf8'), self.privateKey)
        response = requests.post('https://survey.gxb.io/blacklist/question/report', data=bytes(str(getQuestionReportParmas), "utf8"), headers={'content-type': 'application/json'})
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            log.error(response.status_code)


if __name__ == "__main__":
    client = BlacklistGatewayClient('5KFachrDu7yHqhDeqdshedh6cWasLDv8d8Rko2JuvKM12345678', 'hzy13500')
    print(client.getQuestionReport("GXC4ywUcU8h6zPqESvAMkGREmmg9r54etHTpEtBHp8Rg2WYAcmFnD"))
    # print(client.getQuestionToken())
