%define oname BlazeWeb
Name: python-module-%oname
Version: 0.4.11
Release: alt1
Summary: A light weight WSGI framework with a pluggable architecture
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/BlazeWeb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-beaker
BuildPreReq: python-module-BlazeUtils-tests python-module-blinker
BuildPreReq: python-module-decorator python-module-FormEncode
BuildPreReq: python-module-html2text python-module-jinja2
BuildPreReq: python-module-markdown2 python-module-minimock
BuildPreReq: python-module-nose python-module-PasteScript
BuildPreReq: python-module-paste python-module-webhelpers
BuildPreReq: python-module-werkzeug python-modules-json
BuildPreReq: python-module-PasteDeploy python-module-webtest

%py_provides blazeweb
%py_requires beaker blazeutils blinker decorator formencode html2text
%py_requires jinja2 markdown2 paste paste.script webhelpers werkzeug
%py_requires json

%description
BlazeWeb (formerly pysmvt) is a WSGI web framework library designed to
be relatively "light weight", but with a powerful plug-in and override
architecture that facilitates modularized development.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires minimock blazeutils.testing webtest

%description tests
BlazeWeb (formerly pysmvt) is a WSGI web framework library designed to
be relatively "light weight", but with a powerful plug-in and override
architecture that facilitates modularized development.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst docs
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/testing.*
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/testing.*
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/tests

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.11-alt1
- Initial build for Sisyphus

