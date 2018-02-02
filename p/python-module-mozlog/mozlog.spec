%define _unpackaged_files_terminate_build 1
%define oname mozlog
Name: python-module-%oname
Version: 3.3
Release: alt1.1
Summary: Robust log handling specialized for logging in the Mozilla universe
License: MPL 1.1/GPL 2.0/LGPL 2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/mozlog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/ce/ce/85ce01843e2deea5b93d457a54f0246288256c2358fd30311eadef184bf7/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-modules-json
BuildPreReq: python-module-blessings python-module-mozfile

%py_provides %oname
%py_requires blessings mozfile

%description
Robust log handling specialized for logging in the Mozilla universe.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1
- automated PyPI update

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10-alt1
- Version 2.10

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1
- Version 2.9

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt1
- Initial build for Sisyphus

