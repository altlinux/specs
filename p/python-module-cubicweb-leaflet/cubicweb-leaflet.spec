%define _unpackaged_files_terminate_build 1
%define oname cubicweb-leaflet
Name: python-module-%oname
Version: 0.6.0
Release: alt1.1
Summary: Cube for creating maps using Leaflet (javascript)
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-leaflet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/66/d0/dc9cd4858d150b7434ed30accda6cb1975aaddc3857a5613216f1cee3328/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
Cube for leaflet map, see http://leafletjs.com/

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1
- automated PyPI update

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

