%define oname Pyro4

%def_with python3

Name:           python-module-%oname
Version:        4.14
Release:        alt1
Summary:        Python Remote Objects
Group:          Development/Python
License:        LGPLv2+
URL:            http://www.xs4all.nl/~irmen/pyro4/
Source:         http://www.xs4all.nl/~irmen/pyro4/download/Pyro4-%version.tar.gz
BuildArch:      noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-devel python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

Provides: python-module-Pyro = %version-%release
Obsoletes: python-module-Pyro < %version-%release

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
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
ln -s $PWD/docs/objects.inv %buildroot%python_sitelibdir
pushd docs
%make html
%make pickle
popd
rm -f %buildroot%python_sitelibdir/objects.inv
cp -fR build/sphinx/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc LICENSE README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/test

%files tests
%python_sitelibdir/%oname/test

%files examples
%doc examples
%doc tests

%files docs
%doc build/sphinx/html/*

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/test
%endif

%changelog
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

