%define oname events

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20140515.1.1
Summary: Bringing the elegance of C# EventHanlder to Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Events/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nicolaiarocci/events.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions
(event handlers) can be attached to - a process referred to as
subscribing to an event. Here is a handy package that encapsulates the
core to event subscription and event firing and feels like a "natural"
part of the language.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions
(event handlers) can be attached to - a process referred to as
subscribing to an event. Here is a handy package that encapsulates the
core to event subscription and event firing and feels like a "natural"
part of the language.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Bringing the elegance of C# EventHanlder to Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions
(event handlers) can be attached to - a process referred to as
subscribing to an event. Here is a handy package that encapsulates the
core to event subscription and event firing and feels like a "natural"
part of the language.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions
(event handlers) can be attached to - a process referred to as
subscribing to an event. Here is a handy package that encapsulates the
core to event subscription and event firing and feels like a "natural"
part of the language.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS CHANGES *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.git20140515.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20140515.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140515
- Initial build for Sisyphus

