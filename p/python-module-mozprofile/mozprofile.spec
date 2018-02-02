%define _unpackaged_files_terminate_build 1
%define oname mozprofile
Name: python-module-%oname
Version: 0.28
Release: alt1.1
Summary: Library to create and modify Mozilla application profiles
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/mozprofile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/64/8d/6812c090cf072ec3689c0c5f78d75936eebfec7108783b23230844770d51/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-modules-sqlite3
BuildPreReq: python-module-manifestparser python-module-mozfile
BuildPreReq: python-module-mozlog python-module-mozhttpd

%py_provides %oname
%py_requires mozhttpd

%description
Library to create and modify Mozilla application profiles.

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
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.28-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt1
- Initial build for Sisyphus

