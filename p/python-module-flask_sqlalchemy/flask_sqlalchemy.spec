%define oname flask_sqlalchemy

%def_with python3

Name: python-module-%oname
Version: 2.1
Release: alt1
Summary: Adds SQLAlchemy support to your Flask application
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-SQLAlchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/flask-sqlalchemy.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-flask python-module-SQLAlchemy
#BuildPreReq: python-module-sphinx-devel flask-sphinx-themes
#BuildPreReq: python-module-pysqlite2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-flask python3-module-SQLAlchemy
#BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-cssselect python-module-genshi python-module-itsdangerous python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-werkzeug python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-itsdangerous python3-module-jinja2 python3-module-markupsafe python3-module-pytest python3-module-setuptools python3-module-werkzeug
BuildRequires: flask-sphinx-themes python-module-alabaster python-module-docutils python-module-flask python-module-html5lib python-module-objects.inv python-module-pysqlite2 python3-module-SQLAlchemy python3-module-flask python3-module-jinja2 python3-module-setuptools python3-modules-sqlite3 rpm-build-python3 time

%description
Flask-SQLAlchemy is a Flask microframework extension which adds support
for the SQLAlchemy SQL toolkit/ORM.

%package -n python3-module-%oname
Summary: Adds SQLAlchemy support to your Flask application
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Flask-SQLAlchemy is a Flask microframework extension which adds support
for the SQLAlchemy SQL toolkit/ORM.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Flask-SQLAlchemy is a Flask microframework extension which adds support
for the SQLAlchemy SQL toolkit/ORM.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Flask-SQLAlchemy is a Flask microframework extension which adds support
for the SQLAlchemy SQL toolkit/ORM.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
cp -fR %_datadir/flask-sphinx-themes/* docs/_themes/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS CHANGES README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/_build/html

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES README
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1
- NMU: updated to 2.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt1.git20141023.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0-alt1.git20141023.1
- NMU: Use buildreq for BR.

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20141023
- Initial build for Sisyphus

