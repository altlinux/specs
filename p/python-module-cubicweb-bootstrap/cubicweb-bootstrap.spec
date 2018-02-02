%define _unpackaged_files_terminate_build 1
%define oname cubicweb-bootstrap
Name: python-module-%oname
Version: 1.2.4
Release: alt1.1
Summary: Base cube for bootstrap-based user interfaces
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-bootstrap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/6d/6b/79981dbad6e11b812b01552cca72a7b544b7dd2adf5e79f4e2efa2dc9aeb/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
Base cube for bootstrap-based user interfaces.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README PKG-INFO doc
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1
- automated PyPI update

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Version 1.0.2

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1
- Initial build for Sisyphus

