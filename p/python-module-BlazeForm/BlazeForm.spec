%define oname BlazeForm
Name: python-module-%oname
Version: 0.4.0
Release: alt1
Summary: A library for generating and validating HTML forms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/BlazeForm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/8a/46/36526c5c1e4adf7dd5feb6d2ae1954f7e89f2c9f2a2f3f01b18d92570a1b/%{oname}-%{version}.tar.gz
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
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus

