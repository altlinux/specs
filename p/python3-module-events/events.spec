%define oname events

Name: python3-module-%oname
Version: 0.2.1
Release: alt2

Summary: Bringing the elegance of C# EventHanlder to Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Events/
BuildArch: noarch

# https://github.com/nicolaiarocci/events.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_provides %oname


%description
The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions
(event handlers) can be attached to - a process referred to as
subscribing to an event. Here is a handy package that encapsulates the
core to event subscription and event firing and feels like a "natural"
part of the language.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions
(event handlers) can be attached to - a process referred to as
subscribing to an event. Here is a handy package that encapsulates the
core to event subscription and event firing and feels like a "natural"
part of the language.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc AUTHORS CHANGES *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.git20140515.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20140515.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140515
- Initial build for Sisyphus

