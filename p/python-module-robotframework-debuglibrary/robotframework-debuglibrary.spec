
%define oname robotframework-debuglibrary
Name: python-module-%oname
Version: 0.3
Release: alt1.git20130806
Summary: RobotFramework debug library and an interactive shell
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-debuglibrary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/xyb/robotframework-debuglibrary.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-robotframework

%description
Robotframework-DebugLibrary is A debug library for RobotFramework, which
can be used as an interactive shell(REPL) also.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc ChangeLog *.rst
%_bindir/*
%python_sitelibdir/*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20130806
- Initial build for Sisyphus

