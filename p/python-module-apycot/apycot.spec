%define oname apycot
Name: python-module-%oname
Version: 3.2.0
Release: alt1
Summary: Continuous testing / integration tool for the CubicWeb framework
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/apycot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-Pygments python-module-lxml
BuildPreReq: python-module-coverage python-module-markdown
BuildPreReq: python-module-cubicweb-vcsfile
BuildPreReq: python-module-cubicweb-file
BuildPreReq: python-module-cubicweb-narval
BuildPreReq: python-module-cubicweb-tracker
BuildPreReq: python-module-cubicweb-nosylist
BuildPreReq: python-module-cubicweb-jqplot
BuildPreReq: python-module-logilab-devtools

Requires: cubicweb python-module-cubicweb-vcsfile python-test
Requires: python-module-cubicweb-file
Requires: python-module-cubicweb-narval
Requires: python-module-cubicweb-tracker
Requires: python-module-cubicweb-nosylist
Requires: python-module-cubicweb-jqplot
%py_requires pygments lxml logilab.devtools coverage
%add_python_req_skip test

%description
Apycot is an Automated Python Code Testing platform built on narval and
cubicweb.

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
%_datadir/narval
%_datadir/cubicweb/*

%changelog
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Initial build for Sisyphus

