Name: livechart
Version: 0.0.8
Release: alt1.1
Summary: A CLI utility for charting data on the fly
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/livechart/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sevko/livechart.git
Source: https://pypi.python.org/packages/8d/a0/790dcf4a2762cd45c241f8049bcf429b9f88a2a6d422f5609e46c52b1221/livechart-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-matplotlib
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1
- automated PyPI update

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20150226
- Initial build for Sisyphus

