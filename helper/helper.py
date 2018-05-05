import pandas as pd
import os


def allowed_file(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def read_file(filename, UPLOAD_FOLDER):
    file_format = filename.rsplit('.', 1)[1].lower()
    path = os.path.join(UPLOAD_FOLDER, filename)

    if file_format == 'csv':
        file = pd.read_csv(path, engine="python", sep=None)

    elif file_format == 'xlsx':
        file = pd.read_excel(path)

    elif file_format == 'txt':
        file = pd.read_table(path)

    return file


def format_duration(seconds):
    from dateutil.relativedelta import relativedelta as rd

    time = rd(seconds=round(seconds, 2))
    intervals = ['days', 'hours', 'minutes', 'seconds']
    strg = ' '.join('{} {}'.format(getattr(time, k), k) for k in intervals if getattr(time, k))
    return strg


def render_table(df, **kwargs):
    if not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)

    default_args = {'data-toggle': "table"}

    if kwargs is not None:
        default_args.update(kwargs)

    prop = ''
    for key, value in default_args.items():
        prop += ' {0}="{1}" '.format(key, value)
    prop = '<table' + prop[:-1] + '>'

    df_html = df.to_html(index=False).replace('<table border="1" class="dataframe">', prop)
    return df_html
