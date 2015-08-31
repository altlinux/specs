%define oname tinkerer

%def_with python3

Name: python-module-%oname
Version: 1.5
Release: alt1.git20150212
Summary: Sphinx-based blogging engine
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Tinkerer
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vladris/tinkerer.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-jinja2 python-module-sphinx-devel
BuildPreReq: python-module-babel python-module-pyquery
BuildPreReq: python-module-nose python-module-tox
BuildPreReq: python-module-coverage python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jinja2 python3-module-sphinx-devel
BuildPreReq: python3-module-babel python3-module-pyquery
BuildPreReq: python3-module-nose python3-module-tox
BuildPreReq: python3-module-coverage python3-module-mock
%endif

%py_provides %oname
%py_requires jinja2 sphinx babel pyquery

%description
Tinkerer is a blogging engine/static website generator powered by
Sphinx.

It allows blogging in reStructuredText format, comes with out-of-the-box
support for post publishing dates, authors, categories, tags, post
archive, RSS feed generation, comments powered by Disqus and more.

Tinkerer is also highly customizable through Sphinx extensions.

%if_with python3
%package -n python3-module-%oname
Summary: Sphinx-based blogging engine
Group: Development/Python3
%py3_provides %oname
%py3_requires jinja2 sphinx babel pyquery

%description -n python3-module-%oname
Tinkerer is a blogging engine/static website generator powered by
Sphinx.

It allows blogging in reStructuredText format, comes with out-of-the-box
support for post publishing dates, authors, categories, tags, post
archive, RSS feed generation, comments powered by Disqus and more.

Tinkerer is also highly customizable through Sphinx extensions.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Tinkerer is a blogging engine/static website generator powered by
Sphinx.

It allows blogging in reStructuredText format, comes with out-of-the-box
support for post publishing dates, authors, categories, tags, post
archive, RSS feed generation, comments powered by Disqus and more.

Tinkerer is also highly customizable through Sphinx extensions.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Tinkerer is a blogging engine/static website generator powered by
Sphinx.

It allows blogging in reStructuredText format, comes with out-of-the-box
support for post publishing dates, authors, categories, tags, post
archive, RSS feed generation, comments powered by Disqus and more.

Tinkerer is also highly customizable through Sphinx extensions.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv blog/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
pushd blog
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd
cp -fR blog/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
export PYTHONPATH=$PWD
nosetests -vv --with-cover --cover-package=tinkerer --cover-inclusive
#if_with python3
%if 0
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=$PWD
nosetests3 -vv --with-cover --cover-package=tinkerer --cover-inclusive
popd
%endif

%files
%doc CONTRIBUTORS *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc blog/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CONTRIBUTORS *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20150212
- Initial build for Sisyphus

