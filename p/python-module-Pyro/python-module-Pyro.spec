%define oname Pyro

Name: python-module-%oname
Version: 3.16
Release: alt2

Summary: Python Remote Objects
License: MIT
Group: Development/Python
URL: https://pypi.python.org/pypi/Pyro/
BuildArch: noarch

Source: Pyro-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

%py_requires json wsgiref


%description
Pyro is an acronym for PYthon Remote Objects. It is an advanced and
powerful Distributed Object Technology system written entirely in
Python, that is designed to be very easy to use. It resembles Java's
Remote Method Invocation (RMI). It has less similarity to CORBA - which
is a system- and language independent Distributed Object Technology and
has much more to offer than Pyro or RMI. But Pyro is small, simple and
free!

%package tests
Summary: Tests for Pyro
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

This package contains tests for Pyro.

%package examples
Summary: Examples for Pyro
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

This package contains examples for Pyro.

%package docs
Summary: Documentation for for Pyro
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

This package contains documentation for Pyro.

%prep
%setup

%build
%python_build

%install
%python_install

%check
%__python setup.py test

%files
%doc LICENSE *.txt
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test
%exclude %python_sitelibdir/%oname/ext/BasicNTService.py*
%exclude %python_sitelibdir/%oname/ext/ES_NtService.py*
%exclude %python_sitelibdir/%oname/ext/NS_NtService.py*
%exclude %python_sitelibdir/%oname/ext/ServiceTest.py*

%files tests
%python_sitelibdir/%oname/test

%files examples
%doc examples

%files docs
%doc docs/*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.16-alt2
- Rebuild with new setuptools
- cleanup spec.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.16-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jun 11 2017 Anton Midyukov <antohami@altlinux.org> 3.16-alt1
- Initial build for Sisyphus.
