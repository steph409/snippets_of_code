# Python package

### Install package with poetry

```zsh
poetry install --no-dev
```

### Install mypackage for development purposes

```zsh
poetry install
```

### Install mypackage  with extra dependencies
For example the dependencies required for building the documentation.

```zsh
poetry install -E docs
```

### Add a dependency to poetry

```zsh
poetry add aPyPIpackage
```

### Add a dev dependency to poetry

```zsh
poetry add aPyPIpackage -D
```

### Add an optional dependency to poetry

```zsh
poetry add aPyPIpackage --optional
```

# On the intricacies of python packaging

## what is pyproject.toml

[https://discuss.python.org/t/where-to-get-started-with-pyproject-toml/4906](https://discuss.python.org/t/where-to-get-started-with-pyproject-toml/4906)

[https://setuptools.pypa.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files](https://setuptools.pypa.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files)

[https://snarky.ca/what-the-heck-is-pyproject-toml/](https://snarky.ca/what-the-heck-is-pyproject-toml/) - very good

[https://stackoverflow.com/questions/62983756/what-is-pyproject-toml-file-for](https://stackoverflow.com/questions/62983756/what-is-pyproject-toml-file-for)

[https://python-poetry.org/](https://python-poetry.org/)

[https://github.com/chaostoolkit/chaostoolkit/blob/master/setup.cfg](https://github.com/chaostoolkit/chaostoolkit/blob/master/setup.cfg)

[https://github.com/pypa/setuptools/issues/1688](https://github.com/pypa/setuptools/issues/1688)

[https://stackoverflow.com/questions/64150719/how-to-write-a-minimally-working-pyproject-toml-file-that-can-install-packages](https://stackoverflow.com/questions/64150719/how-to-write-a-minimally-working-pyproject-toml-file-that-can-install-packages)

## pyproject.toml vs setup.cfg vs [setup.py](http://setup.py/)

Before PEP 518 and the introduction of pyproject.toml there was no way for a project to tell a tool like pip what build tools it required in order to build a wheel (let alone an sdist). Now setuptools has a setup_requires argument to specify what is necessary to build a project, but you can't read that setting unless you have setuptools installed, which meant you couldn't declare you needed setuptools to read the setting in setuptools. This chicken-and-egg problem is why tools like virtualenv install setuptools by default and why pip always injects setuptools and wheel when running a [setup.py](http://setup.py/) file regardless of whether you explicitly installed it.

PEP 518 and pyproject.toml changed that. Now a tool like pip can read pyproject.toml, see what build tools are specified in it, and install those in a virtual environment to build your project. That means you can rely on a specific version of setuptools and 'wheel' if you want. You can even build with a tool other than setuptools if you want (e.g. flit or Poetry, but since these other tools require pyproject.toml their users are already familiar with what's going on). The key point is assumptions no longer need to be made about what is necessary to build your project, which frees up the packaging ecosystem to experiment and grow.

### Advantage: Tools standardizing on pyproject.toml

An interesting side-effect of PEP 518 trying to introduce a standard file that all projects should (eventually) have is that non-build development tools realized they now had a file where they could put their own configuration. Now, projects like Black, [coverage.py](http://coverage.py/), towncrier, and tox allow you to specify their configurations in pyproject.toml instead of in a separate file. And so, thanks to projects consolidating around pyproject.toml, there's actually an argument to be made there are fewer configuration files than before thanks to pyproject.toml.

### Deciding on a build-system in pyproject.toml - PEP 621

There is a standard called PEP 621 that specifies how a project's metadata, including dependencies, should be laid out in the pyproject.toml file.
Over time, more and more build back-ends have added support for PEP 621 (e.g. pdm, flit, trampolim, enscons, whey, ... ).

I want to provide further detail on three build-systems specifically:

Setuptools
Flit
Poetry

With setuptools: we need setup.cfg and or [setup.py](http://setup.py/) in addition.
With flit or poetry: pyproject.toml can work as a stand-alone single source of truth

### Installing additional dependencies (extra_requires/optional_dependencies)

On top of dependencies of our package, we want to install development dependencies for testing, linting, documentation (Sphinx) ...

[https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies)

### Testing - customize pytest and tox in pyproject.toml

[https://docs.pytest.org/en/6.2.x/customize.html](https://docs.pytest.org/en/6.2.x/customize.html)

[https://tox.wiki/en/latest/example/basic.html](https://tox.wiki/en/latest/example/basic.html)

### MANIFEST.in

### LICENSE

### setuptools_scm

# Interesting YT Videos

[https://www.youtube.com/watch?v=j8iXO5VErjw](https://www.youtube.com/watch?v=j8iXO5VErjw)

[https://www.youtube.com/watch?v=qRSb299awB0](https://www.youtube.com/watch?v=qRSb299awB0)

[https://www.youtube.com/watch?v=GIF3LaRqgXo](https://www.youtube.com/watch?v=GIF3LaRqgXo)

# Good examples of setup.cfg, pyproject.toml and setup.py

[chaostoolkit/setup.cfg at master · chaostoolkit/chaostoolkit](https://github.com/chaostoolkit/chaostoolkit/blob/master/setup.cfg)