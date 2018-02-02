%define _unpackaged_files_terminate_build 1
%define oname cubicweb-squareui
Name: python-module-%oname
Version: 1.0.3
Release: alt1.1
Summary: Data-centric user interface for cubicweb based on bootstrap
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-squareui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/7d/ad/ec74ed6dc02775dd35247ccf111f15142cb5f04d73e8ef1c5ea75c3d4a44/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-bootstrap

Requires: cubicweb python-module-cubicweb-bootstrap

%description
Data-centric user interface for cubicweb based on bootstrap.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1
- automated PyPI update

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus

