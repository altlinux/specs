%define _unpackaged_files_terminate_build 1
%define oname cubicweb-trackervcs
Name: python-module-%oname
Version: 1.4.1
Release: alt1.1
Summary: vcsfile / tracker integration
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-trackervcs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/38/28/d9361b5824022228bbcb73447069e11ecf1cd9ba23d198892654cab8ea3d/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-vcsfile
BuildPreReq: python-module-cubicweb-tracker
BuildPreReq: python-module-cubicweb-vcreview
BuildPreReq: python-module-cubicweb-forge

Requires: cubicweb python-module-cubicweb-vcsfile
Requires: python-module-cubicweb-tracker
Requires: python-module-cubicweb-vcreview
Requires: python-module-cubicweb-forge

%description
Integrate tracker and vcsfile/vcreview cubes.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1
- automated PyPI update

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

