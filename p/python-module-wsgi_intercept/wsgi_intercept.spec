%define oname wsgi_intercept

%def_with python3

Name: python-module-%oname
Version: 0.9.1
Release: alt1.git20141206.1.1
Summary: wsgi_intercept installs a WSGI application in place of a real URI for testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/wsgi_intercept
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cdent/python3-wsgi-intercept.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-requests
#BuildPreReq: python-module-httplib2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-google python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-chardet python-module-docutils python-module-html5lib python-module-httplib2 python-module-objects.inv python-module-urllib3 python3-module-setuptools rpm-build-python3 time

%description
Installs a WSGI application in place of a real URI for testing.

Testing a WSGI application normally involves starting a server at a
local host and port, then pointing your test code to that address.
Instead, this library lets you intercept calls to any specific host/port
combination and redirect them into a WSGI application importable by your
test program. Thus, you can avoid spawning multiple processes or threads
to test your Web app.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Installs a WSGI application in place of a real URI for testing.

Testing a WSGI application normally involves starting a server at a
local host and port, then pointing your test code to that address.
Instead, this library lets you intercept calls to any specific host/port
combination and redirect them into a WSGI application importable by your
test program. Thus, you can avoid spawning multiple processes or threads
to test your Web app.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Installs a WSGI application in place of a real URI for testing.

Testing a WSGI application normally involves starting a server at a
local host and port, then pointing your test code to that address.
Instead, this library lets you intercept calls to any specific host/port
combination and redirect them into a WSGI application importable by your
test program. Thus, you can avoid spawning multiple processes or threads
to test your Web app.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Installs a WSGI application in place of a real URI for testing.

Testing a WSGI application normally involves starting a server at a
local host and port, then pointing your test code to that address.
Instead, this library lets you intercept calls to any specific host/port
combination and redirect them into a WSGI application importable by your
test program. Thus, you can avoid spawning multiple processes or threads
to test your Web app.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: wsgi_intercept installs a WSGI application in place of a real URI for testing
Group: Development/Python3

%description -n python3-module-%oname
Installs a WSGI application in place of a real URI for testing.

Testing a WSGI application normally involves starting a server at a
local host and port, then pointing your test code to that address.
Instead, this library lets you intercept calls to any specific host/port
combination and redirect them into a WSGI application importable by your
test program. Thus, you can avoid spawning multiple processes or threads
to test your Web app.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Installs a WSGI application in place of a real URI for testing.

Testing a WSGI application normally involves starting a server at a
local host and port, then pointing your test code to that address.
Instead, this library lets you intercept calls to any specific host/port
combination and redirect them into a WSGI application importable by your
test program. Thus, you can avoid spawning multiple processes or threads
to test your Web app.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
mv %buildroot%python_sitelibdir/test \
	%buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%python3_sitelibdir/test \
	%buildroot%python3_sitelibdir/%oname/
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc COPYRIGHT README.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/test

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc COPYRIGHT README.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20141206.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1.git20141206.1
- NMU: Use buildreq for BR.

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20141206
- Version 0.9.1

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20140806
- Version 0.9.0

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20140806
- Initial build for Sisyphus

