%define _unpackaged_files_terminate_build 1
%define oname manifestparser
Name: python-module-%oname
Version: 1.1
Release: alt1.1
Summary: Library to create and manage test manifests
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/manifestparser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/53/4e/f621c25a2e0ef6e7a38987f291a88d06996e3f8bfe3ad6302b4abc45c9f8/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-modules-json

%py_provides %oname

%description
Library to create and manage test manifests.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

