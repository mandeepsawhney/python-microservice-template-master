from invoke import task


# invoke start
@task
def start(c):
    c.run('python app.py')


# invoke lint --format=html --htmldir=lint-results
@task
def lint(c, format=None, htmldir='lint-results'):
    if format == 'html':
        c.run(f'flake8 --format=html --htmldir={htmldir}')
    else:
        c.run('flake8')


# invoke test
@task
def test(c):
    c.run('pytest --cov=src --cov-fail-under=90 '
          '--html=test-results/index.html '
          '--junitxml=test-results/junit.xml')
