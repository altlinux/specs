%define _unpackaged_files_terminate_build 1
%define oname cubicweb-dataio
Name: python-module-%oname
Version: 0.7.0
Release: alt1.1
Summary: Cube for data input/output, import and export
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-dataio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/c7/4a/31f5b219df3c07dc89f64c240e8d5dd12a4cb1e367041ba5805fecf6135e/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-rdflib

Requires: cubicweb
%py_requires rdflib

%description
Cube for data input/output, import and export.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1
- automated PyPI update

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

