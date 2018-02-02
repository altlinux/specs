%define oname BlazeForm

Name: python-module-%oname
Version: 0.4.1
Release: alt1.1
Summary: A library for generating and validating HTML forms
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/BlazeForm/

Source: %{oname}-%{version}.tar
BuildArch: noarch

BuildRequires: python-module-setuptools python-module-FormEncode
BuildRequires: python-module-BlazeUtils python-module-webhelpers
BuildRequires: python-module-nose python-module-DNS
BuildRequires: python2.7(webhelpers2)

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.1-alt1
- Updated to upstream version 0.4.1.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus

