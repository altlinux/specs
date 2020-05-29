%define oname Pyro4

Name:           python-module-%oname
Version:        4.75
Release:        alt3
Summary:        Python Remote Objects
Group:          Development/Python
License:        LGPL-2.0-or-later
URL:            https://pypi.python.org/pypi/Pyro4/
BuildArch:      noarch

# https://github.com/irmen/Pyro4.git
Source: %oname-%version.tar
Patch1: %oname-alt-tune-docs.patch

BuildRequires: python-devel python-module-sphinx-devel
BuildRequires: python-module-setuptools python-module-serpent python2.7(selectors34) python2.7(wsgiref) python2.7(wsgiref.util)
BuildRequires: python2.7(cloudpickle) python2.7(msgpack) python2.7(dill)

%py_requires json wsgiref
%py_requires selectors34

%description
Pyro is an acronym for PYthon Remote Objects. It is an advanced and
powerful Distributed Object Technology system written entirely in
Python, that is designed to be very easy to use. It resembles Java's
Remote Method Invocation (RMI). It has less similarity to CORBA - which
is a system- and language independent Distributed Object Technology and
has much more to offer than Pyro or RMI. But Pyro is small, simple and
free!

%package tests
Summary: Tests for Pyro4
Group: Development/Python
Requires: %name = %version-%release

%description tests
Pyro is an acronym for PYthon Remote Objects. It is an advanced and
powerful Distributed Object Technology system written entirely in
Python, that is designed to be very easy to use. It resembles Java's
Remote Method Invocation (RMI). It has less similarity to CORBA - which
is a system- and language independent Distributed Object Technology and
has much more to offer than Pyro or RMI. But Pyro is small, simple and
free!

This package contains tests for Pyro4.

%package examples
Summary: Examples for Pyro4
Group: Development/Documentation
BuildArch: noarch

%description examples
Pyro is an acronym for PYthon Remote Objects. It is an advanced and
powerful Distributed Object Technology system written entirely in
Python, that is designed to be very easy to use. It resembles Java's
Remote Method Invocation (RMI). It has less similarity to CORBA - which
is a system- and language independent Distributed Object Technology and
has much more to offer than Pyro or RMI. But Pyro is small, simple and
free!

This package contains examples for Pyro4.

%prep
%setup
%patch1 -p2

%build
%python_build

%install
%python_install

%check
# remove remote tests
rm -f tests/PyroTests/test_socket.py
rm -f tests/PyroTests/test_naming.py
rm -f tests/PyroTests/test_naming2.py
python setup.py test
PYTHONPATH=%buildroot%python_sitelibdir python tests/run_testsuite.py

# remove unpackages files
rm -r %buildroot%_bindir

%files
%doc LICENSE README.md
#_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%files examples
%doc examples
%doc tests

%changelog
* Fri May 29 2020 Anton Midyukov <antohami@altlinux.org> 4.75-alt3
- unpackage %_bindir/*

* Sat May 23 2020 Anton Midyukov <antohami@altlinux.org> 4.75-alt2
- disable build docs
- disable build python3 subpackages

* Sat Apr 20 2019 Anton Midyukov <antohami@altlinux.org> 4.75-alt1
- Updated to upstream version 4.75

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.62-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.62-alt1
- Updated to upstream version 4.62.

* Sun Jun 11 2017 Anton Midyukov <antohami@altlinux.org> 4.39-alt2
- Remove obsoletes and provides python-module-Pyro 

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.39-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.39-alt1
- Version 4.39

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.34-alt1
- Version 4.34

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.30-alt1
- Version 4.30

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.29-alt1
- Version 4.29

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.26-alt1
- Version 4.26

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.22-alt1
- Version 4.22

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 4.17-alt1.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.17-alt1
- Version 4.17

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.14-alt1
- Version 4.14
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11-alt1
- Version 4.11
- Added docs and pickles subpackages

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.4-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4-alt1
- Version 4.4

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1
- Version 4.2

* Wed Aug 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt2
- Provides python-module-Pyro

* Wed Jul 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1
- Initial build for Sisyphus

