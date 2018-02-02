%define _unpackaged_files_terminate_build 1
%define oname cubicweb-addressbook
Name: python-module-%oname
Version: 1.9.1
Release: alt1.1
Summary: Address book component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-addressbook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/c6/9f/1b6e0308854202cdb8100c1104491699f6c42b67d93a635596365ae9132d/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-geocoding

Requires: cubicweb python-module-cubicweb-geocoding

%description
The addressbook cube adds a phone number, postal address and instant
messenger address (supports icq, msn and jabber) to the schema.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README PKG-INFO
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1
- automated PyPI update

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

