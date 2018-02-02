%define oname Pyro4

%def_with python3
%def_with docs

Name:           python-module-%oname
Version:        4.62
Release:        alt1.1
Summary:        Python Remote Objects
Group:          Development/Python
License:        LGPLv2+
URL:            https://pypi.python.org/pypi/Pyro4/
BuildArch:      noarch

# https://github.com/irmen/Pyro4.git
Source: %oname-%version.tar
Patch1: %oname-alt-tune-docs.patch

BuildRequires: python-devel python-module-sphinx-devel
BuildRequires: python-module-setuptools python-module-serpent python2.7(selectors34) python2.7(wsgiref) python2.7(wsgiref.util)
BuildRequires: python2.7(cloudpickle) python2.7(msgpack) python2.7(dill)
%if_with docs
BuildRequires: python3-module-sphinx-devel
%endif #docs
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-serpent python3(wsgiref) python3(wsgiref.util)
BuildRequires: python3(cloudpickle) python3(msgpack) python3(dill)
%endif

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

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 Remote Objects
Group: Development/Python3
%py3_requires json wsgiref

%description -n python3-module-%oname
Pyro is an acronym for PYthon Remote Objects. It is an advanced and
powerful Distributed Object Technology system written entirely in
Python, that is designed to be very easy to use. It resembles Java's
Remote Method Invocation (RMI). It has less similarity to CORBA - which
is a system- and language independent Distributed Object Technology and
has much more to offer than Pyro or RMI. But Pyro is small, simple and
free!

%package -n python3-module-%oname-tests
Summary: Tests for Pyro4 (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Pyro is an acronym for PYthon Remote Objects. It is an advanced and
powerful Distributed Object Technology system written entirely in
Python, that is designed to be very easy to use. It resembles Java's
Remote Method Invocation (RMI). It has less similarity to CORBA - which
is a system- and language independent Distributed Object Technology and
has much more to offer than Pyro or RMI. But Pyro is small, simple and
free!

This package contains tests for Pyro4.
%endif

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

%package docs
Summary: Documentation for for Pyro4
Group: Development/Documentation
BuildArch: noarch

%description docs
Pyro is an acronym for PYthon Remote Objects. It is an advanced and
powerful Distributed Object Technology system written entirely in
Python, that is designed to be very easy to use. It resembles Java's
Remote Method Invocation (RMI). It has less similarity to CORBA - which
is a system- and language independent Distributed Object Technology and
has much more to offer than Pyro or RMI. But Pyro is small, simple and
free!

This package contains documentation for Pyro4.

%package pickles
Summary: Pickles for for Pyro4
Group: Development/Python

%description pickles
Pyro is an acronym for PYthon Remote Objects. It is an advanced and
powerful Distributed Object Technology system written entirely in
Python, that is designed to be very easy to use. It resembles Java's
Remote Method Invocation (RMI). It has less similarity to CORBA - which
is a system- and language independent Distributed Object Technology and
has much more to offer than Pyro or RMI. But Pyro is small, simple and
free!

This package contains pickles for Pyro4.

%prep
%setup
%patch1 -p2

%if_with python3
cp -a . ../python3
%endif

%if_with docs
%prepare_sphinx docs
ln -s ../objects.inv docs/source
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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

%if_with docs
export PYTHONPATH=%buildroot%python_sitelibdir
ln -s $PWD/docs/objects.inv %buildroot%python_sitelibdir
pushd docs
%make html
%make pickle
popd
rm -f %buildroot%python_sitelibdir/objects.inv
cp -fR build/sphinx/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
# remove remote tests
rm -f tests/PyroTests/test_socket.py
rm -f tests/PyroTests/test_naming.py
rm -f tests/PyroTests/test_naming2.py
python setup.py test
PYTHONPATH=%buildroot%python_sitelibdir python tests/run_testsuite.py
%if_with python3
pushd ../python3
# remove remote tests
rm -f tests/PyroTests/test_socket.py
rm -f tests/PyroTests/test_naming.py
rm -f tests/PyroTests/test_naming2.py
python3 setup.py test
PYTHONPATH=%buildroot%python3_sitelibdir python3 tests/run_testsuite.py
popd
%endif

%files
%doc LICENSE README.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%if_with docs
%exclude %python_sitelibdir/%oname/pickle
%endif #docs
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%files examples
%doc examples
%doc tests

%if_with docs
%files docs
%doc build/sphinx/html/*

%files pickles
%python_sitelibdir/%oname/pickle
%endif #docs

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test
%endif

%changelog
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

