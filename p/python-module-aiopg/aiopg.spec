%define oname aiopg

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1.git20150203.1
Summary: aiopg is a library for accessing a PostgreSQL database from the asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiopg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiopg.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-psycopg2
#BuildPreReq: python-module-SQLAlchemy
%endif
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-psycopg2
#BuildPreReq: python3-module-SQLAlchemy
%endif

%py_provides %oname
%py_requires asyncio psycopg2 sqlalchemy

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-psycopg2 python3-module-setuptools-tests rpm-build-python3 time

%description
aiopg is a library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the
Psycopg database driver.

%package -n python3-module-%oname
Summary: aiopg is a library for accessing a PostgreSQL database from the asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio psycopg2 sqlalchemy

%description -n python3-module-%oname
aiopg is a library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the
Psycopg database driver.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs html

rm -f requirements.txt

%check
%if_with python2
python setup.py test
#python runtests.py -v
%endif
%if_with python3
pushd ../python3
python3 setup.py test
#python3 runtests.py -v
popd
%endif

%if_with python2
%files
%doc *.txt *.rst examples docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1.git20150203.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150203
- Version 0.6.1

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20150102
- Initial build for Sisyphus

