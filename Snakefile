configfile: "snakemake-config.json"


## Python ##

rule python__sdist:
    input:
        'python/setup.py'
    output:
        expand('dist/{name}-{version}.tar.gz', name=config['python']['package_name'], version=config['python']['version'])
    shell:
        'python python/setup.py sdist'

rule python__bdist_wheel:
    input:
        'python/setup.py'
    output:
        expand('dist/{name}-{version}-py3-none-any.whl', name=config['python']['package_name'], version=config['python']['version'])
    shell:
        'python python/setup.py bdist_wheel'

rule python__conda_build:
    input:
        'python/conda-recipe/meta.yaml'
    output:
        expand('conda-build/noarch/{name}-{version}-py_0.tar.bz2', name=config['python']['package_name'], version=config['python']['version'])
    shell:
        'conda build --no-anaconda-upload --output-folder ./conda-build python/conda-recipe'
        
rule python:
    input:
        rules.python__sdist.input,
        rules.python__bdist_wheel.input,
        rules.python__conda_build.input

