%define oname BlazeForm
Name: python-module-%oname
Version: 0.3.7
Release: alt1
Summary: A library for generating and validating HTML forms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/BlazeForm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-FormEncode
BuildPreReq: python-module-BlazeUtils python-module-webhelpers
BuildPreReq: python-module-nose python-module-DNS

%py_provides blazeform
%py_requires formencode blazeutils webhelpers

%description
BlazeForm is a library designed to facilitate the
rendering/processing/validating of HTML forms.

Features:

* validation based on FormEncode
* attempting to have complete HTML spec coverage
* extensible rendering system() (don't have to use it)
* will work with multiple WSGI frameworks (Werkzeug currently supported)
* extensive unit tests
* few dependencies: FormEncode, BlazeUtils, WebHelpers

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus

