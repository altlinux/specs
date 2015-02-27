Name: livechart
Version: 0.0.6
Release: alt1.git20150226
Summary: A CLI utility for charting data on the fly
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/livechart/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sevko/livechart.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-matplotlib
BuildPreReq: python-module-mock python-module-nose
BuildPreReq: python-module-pytz python-module-pygobject3
BuildPreReq: python-module-pycairo python-modules-json

%py_requires matplotlib mock nose pytz gi json

%description
A command-line utility for rendering quick-and-dirty graphs of STDIN
input.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.rst
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20150226
- Initial build for Sisyphus

