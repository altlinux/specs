%define oname logex

%def_with python3

Name: python-module-%oname
Version: 2.1.0
Release: alt1.git20141214
Summary: Easily log uncaught exceptions in D-Bus, thread and other functions
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/logex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/insecure/logex.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-dbus
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-dbus
%endif

%py_provides %oname
%py_requires dbus

%description
Logex is a python module to easily add logging for unhandled exceptions
in D-Bus, thread and other functions. It can also be quite helpful when
developing with the new asyncio module of python 3.4. Although this
module does some sort of exception logging, it can easily happen that
exceptions are accidentally swallowed. Although unhandled exceptions get
written to STDERR by default and most modules provide some mechanism to
log these, this is not always sufficient, e.g. when inside a daemon
which discards all default output. Sometimes it may also be desirable to
automatically send an email if some exception occurs or at least write
some kind of audit log.

This module comes with a decorator function which can be applied on
demand. It provides advanced debugging information which gives you the
most relevant information for each frame in the exception's traceback.

%package -n python3-module-%oname
Summary: Easily log uncaught exceptions in D-Bus, thread and other functions
Group: Development/Python3
%py3_provides %oname
%py3_requires dbus

%description -n python3-module-%oname
Logex is a python module to easily add logging for unhandled exceptions
in D-Bus, thread and other functions. It can also be quite helpful when
developing with the new asyncio module of python 3.4. Although this
module does some sort of exception logging, it can easily happen that
exceptions are accidentally swallowed. Although unhandled exceptions get
written to STDERR by default and most modules provide some mechanism to
log these, this is not always sufficient, e.g. when inside a daemon
which discards all default output. Sometimes it may also be desirable to
automatically send an email if some exception occurs or at least write
some kind of audit log.

This module comes with a decorator function which can be applied on
demand. It provides advanced debugging information which gives you the
most relevant information for each frame in the exception's traceback.

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
%doc Changelog *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc Changelog *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20141214
- Initial build for Sisyphus

