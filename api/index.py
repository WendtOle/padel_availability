from flask import Flask, render_template, request
from padel_availability import *
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def home():
    size = request.args.get('size', default=3, type=int)
    offset = request.args.get('offset', default=0, type=int)
    today = datetime.now().date()

    # dummy data for testing to not hit the actual endpoint
    #raw_data = [[['Padel Berlin', 'Outdoor 2', '20:30:00', 90, '56.5 EUR']], [['Padel Berlin', 'Indoor', '20:00:00', 120, '75 EUR'], ['Padel Berlin', 'Outdoor 1', '19:30:00', 90, '56.5 EUR'], ['Padel Berlin', 'Outdoor 1', '20:30:00', 90, '56.5 EUR']], [['Padel FC', 'Court 1', '17:00:00', 90, '54 EUR'], ['Padel FC', 'Court 1', '18:00:00', 120, '72 EUR'], ['Padel FC', 'Court 1', '18:30:00', 90, '54 EUR'], ['Padel FC', 'Court 2', '18:00:00', 120, '72 EUR'], ['Padel FC', 'Court 3', '18:30:00', 90, '54 EUR'], ['Padel FC', 'Court 4', '18:30:00', 90, '54 EUR'], ['Padel FC', 'Court 5', '18:30:00', 90, '54 EUR'], ['Padel FC', 'Outdoor spree 1', '18:30:00', 90, '54 EUR'], ['Padel FC', 'Outdoor spree 2', '18:00:00', 120, '72 EUR'], ['Padel Berlin', 'Indoor', '17:00:00', 90, '56.5 EUR'], ['Padel Berlin', 'Indoor', '17:00:00', 120, '75 EUR'], ['Padel Berlin', 'Indoor', '18:00:00', 90, '56.5 EUR'], ['Padel Berlin', 'Indoor', '18:00:00', 120, '75 EUR'], ['Padel Berlin', 'Indoor', '18:30:00', 90, '56.5 EUR'], ['Padel Berlin', 'Indoor', '18:30:00', 120, '75 EUR'], ['Padel Berlin', 'Indoor', '19:00:00', 90, '56.5 EUR'], ['Padel Berlin', 'Indoor', '19:00:00', 120, '75 EUR'], ['Padel Berlin', 'Indoor', '19:30:00', 90, '56.5 EUR'], ['Padel Berlin', 'Indoor', '20:00:00', 120, '75 EUR'], ['Padel Berlin', 'Indoor', '20:30:00', 90, '56.5 EUR'], ['Padel Berlin', 'Outdoor 1', '18:00:00', 90, '56.5 EUR'], ['Padel Berlin', 'Outdoor 1', '18:00:00', 120, '75 EUR'], ['Padel Berlin', 'Outdoor 1', '19:00:00', 90, '56.5 EUR'], ['Padel Berlin', 'Outdoor 1', '19:00:00', 120, '75 EUR'], ['Padel Berlin', 'Outdoor 1', '19:30:00', 90, '56.5 EUR'], ['Padel Berlin', 'Outdoor 1', '20:00:00', 120, '75 EUR'], ['Padel Berlin', 'Outdoor 1', '20:30:00', 90, '56.5 EUR'], ['Padel Berlin', 'Outdoor 2', '18:00:00', 90, '56.5 EUR'], ['Padel Berlin', 'Outdoor 2', '18:00:00', 120, '75 EUR'], ['Padel Berlin', 'Outdoor 2', '19:00:00', 90, '56.5 EUR'], ['Padel Berlin', 'Outdoor 2', '19:00:00', 120, '75 EUR'], ['Padel Berlin', 'Outdoor 2', '19:30:00', 90, '56.5 EUR'], ['Padel Berlin', 'Outdoor 2', '20:00:00', 120, '75 EUR'], ['Padel Berlin', 'Outdoor 2', '20:30:00', 90, '56.5 EUR']]]
    #dates = ["tommorow", "day after tommorow", "day after day after tommorow"]

    raw_data = []
    dates = []

    for i in range(size):
        current_date = today + timedelta(days=i + offset)
        raw_data.append(getAvailability(current_date))
        dates.append(current_date.strftime("%A") + " (" + current_date.strftime("%Y-%m-%d") + ")")

    columnNames=["Venue", "Court", "Start Time", "Duration (minutes)", "Price (EUR)"]
    data = list(raw_data)
    return render_template('table.html', data=data, colnames=columnNames, dates=dates, offset=offset + size, size=size)

@app.route('/about')
def about():
    return 'About'