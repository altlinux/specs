%define _unpackaged_files_terminate_build 1
%define oname momoko

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.2.4
Release: alt1
Summary: Wraps (asynchronous) Psycopg2 for Tornado
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Momoko
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/FSX/momoko.git
Source0: https://pypi.python.org/packages/7e/02/0495484bdbb168c55239da25ddb30f60dd26f0fbc58e5c20464417972ac4/Momoko-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-tornado python-module-psycopg2cffi
#BuildPreReq: python-module-unittest2 python-module-psycopg2
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-tornado python3-module-psycopg2cffi
#BuildPreReq: python3-module-unittest2 python3-module-psycopg2
%endif

%py_provides %oname
%py_requires tornado psycopg2cffi psycopg2

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: libsasl2-3 python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pycares python-module-pycurl python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-pycparser python3-module-setuptools python3-module-zope.interface
BuildRequires: python-module-alabaster python-module-cffi python-module-docutils python-module-html5lib python-module-objects.inv python-module-psycopg2 python-module-pytest python-module-tornado python-module-unittest2 python3-module-cffi python3-module-psycopg2 python3-module-pycares python3-module-pytest python3-module-unittest2 python3-module-zope rpm-build-python3 time

%description
Momoko wraps Psycopg2's functionality for use in Tornado.

%if_with python3
%package -n python3-module-%oname
Summary: Wraps (asynchronous) Psycopg2 for Tornado
Group: Development/Python3
%py3_provides %oname
%py3_requires tornado psycopg2cffi psycopg2

%description -n python3-module-%oname
Momoko wraps Psycopg2's functionality for use in Tornado.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Momoko wraps Psycopg2's functionality for use in Tornado.

This package contains pickles for %oname.

%prep
%setup -q -n Momoko-%{version}

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst THANKS examples docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst THANKS examples docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt1.git20150803.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.git20150803.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20150803
- Initial build for Sisyphus

