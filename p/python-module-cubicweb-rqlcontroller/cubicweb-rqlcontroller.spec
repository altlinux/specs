%define _unpackaged_files_terminate_build 1
%define oname cubicweb-rqlcontroller
Name: python-module-%oname
Version: 0.3.1
Release: alt1.1
Summary: Restfull rql edition capabilities
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-rqlcontroller/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/69/9f/7db6707f05f5f4fb54fe4d6b7a38c08b5e333d6bcd6604ae1c061eb28985/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-signedrequest

Requires: cubicweb python-module-cubicweb-signedrequest

%description
Controller that gives users rql read/ write capabilities.

%prep
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

