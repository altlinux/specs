%define _unpackaged_files_terminate_build 1
%define oname mozdevice
Name: python-module-%oname
Version: 0.48
Release: alt1.1
Summary: Mozilla-authored device management
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mozdevice/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/d5/bf/5a305d6b80f2b7e49904c366e95a6e2a67141a5a6c4d1472d4bfdfb82bff/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-mozfile python-module-mozlog
BuildPreReq: python-module-moznetwork python-module-mozprocess

%py_provides %oname

%description
Mozilla-authored device management.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.48-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.44-alt1
- Initial build for Sisyphus

