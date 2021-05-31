%define oname wsgi_intercept

Name: python3-module-%oname
Version: 1.5.0
Release: alt2
Summary: wsgi_intercept installs a WSGI application in place of a real URI for testing
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/wsgi_intercept
Source: %oname-%version.tar.gz
Patch: wsgi_intercept-fix.urllib3.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx

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
Group: Development/Python3
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
Group: Development/Python3

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

%prep
%setup -n %oname-%version
%patch -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/pickle

%files tests
%python3_sitelibdir/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

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

