%define _unpackaged_files_terminate_build 1
%define oname cubicweb-registration
Name: python-module-%oname
Version: 0.6.3
Release: alt1.1
Summary: Public registration component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-registration/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/3e/cc/cf2ccb69f44d3c6b21c38d2d9cc0c3fe68f5c28f94dadd0140fef4874ec4/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-Pillow

Requires: cubicweb
%py_requires PIL

%description
This CubicWeb component provides a public registration feature (users
can register and create an account without the need for admin
intervention).

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1
- automated PyPI update

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Version 0.6.1

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus

