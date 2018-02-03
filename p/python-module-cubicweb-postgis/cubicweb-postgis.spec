%define _unpackaged_files_terminate_build 1
%define oname cubicweb-postgis
Name: python-module-%oname
Version: 0.5.0
Release: alt1.1
Summary: Cube for GIS data support using PostGIS
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-postgis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/7e/25/47e5cfd0af48541f0cd166361cd2417d055d81c33f51a2231ec4f912ac87/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cwtags

Requires: cubicweb
%py_requires cwtags

%description
Cube for GIS data support using PostGIS.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1
- automated PyPI update

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

