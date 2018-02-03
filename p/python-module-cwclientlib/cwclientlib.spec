%define oname cwclientlib
Name: python-module-%oname
Version: 0.2.1
Release: alt1.1
Summary: A Python library to easily build CubicWeb clients
License: LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/cwclientlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-rqlcontroller
BuildPreReq: python-module-cubicweb-signedrequest
BuildPreReq: python-module-requests python-module-urllib3
# for future:
#BuildPreReq: python-module-requests-kerberos

Requires: cubicweb python-module-cubicweb-rqlcontroller
Requires: python-module-cubicweb-signedrequest
# for future:
#py_requires requests_kerberos
%py_requires urllib3

%description
A Python library to easily build CubicWeb clients:

* execute RQL queries remotely (using rqlcontroller),
* access instances that requires authentication (using signedrequest).

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

