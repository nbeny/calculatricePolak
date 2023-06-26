from io import StringIO
import csv

from flask import Blueprint, request, make_response
from app.lib.polak import RPNCalculator, isPolakInversedFormule
from app.models.calcul import Formule
from app.extensions import db

main_blueprint = Blueprint("main_blueprint", __name__)


@main_blueprint.route("/", methods=["GET"])
def index():
    return "Hello World!", 200


@main_blueprint.route("/polak", methods=["GET", "POST"])
def polak():
    formule = request.form["formule"]
    if isPolakInversedFormule(formule):
        result = RPNCalculator.calculate(formule)
        insert = Formule(formule=formule, result=result)
        db.session.add(insert)
        return result, 200
    else:
        return "Formule is not supported", 400

@main_blueprint.route("/download", methods=['get'])
def download():
    allResults = Formule.query.all()

    data = []
    data.append(["formule", "result"])
    for results in allResults:
        data.append([results.formule, results.result])

    si = StringIO.StringIO()
    cw = csv.writer(si)
    cw.writerows(data)
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output
