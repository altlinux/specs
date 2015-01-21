%define oname UniCurses

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt1
Summary: A unified OS-independent Curses wrapper for Python
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/UniCurses/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-curses
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-modules-curses
%endif

%py_provides unicurses
%py_requires curses

%description
UniCurses is a wrapper for Python 2.x/3.x that provides a unified set of
Curses functions on all platforms (MS Windows, Linux, and Mac OS X) with
syntax close to that of the original NCurses.

%package -n python3-module-%oname
Summary: A unified OS-independent Curses wrapper for Python
Group: Development/Python3
%py3_provides unicurses
%py3_requires curses

%description -n python3-module-%oname
UniCurses is a wrapper for Python 2.x/3.x that provides a unified set of
Curses functions on all platforms (MS Windows, Linux, and Mac OS X) with
syntax close to that of the original NCurses.

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

%files
%doc demos docs
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc demos docs
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

