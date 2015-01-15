%define oname cubicweb-jqplot
Name: python-module-%oname
Version: 0.4.1
Release: alt1
Summary: Views wrapping jqPlot graphic library
License: LGPL & MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-jqplot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-markdown

Requires: cubicweb

%description
This is the CubicWeb integration of Chris Leonello's jqPlot library,
which is included under the data subdirectory, along with it's license
(MIT).

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

