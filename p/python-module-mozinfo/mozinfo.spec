%define _unpackaged_files_terminate_build 1
%define oname mozinfo

Name: python-module-%oname
Version: 0.9
Release: alt1
Summary: Library to get system information for use in Mozilla testing
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mozinfo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/cd/18/666fe2f87bb833966a5c4834fe2397fc95cd2083fff0419f548fb04bfe7d/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-mozfile python-modules-json

%py_provides %oname

%description
Library to get system information for use in Mozilla testing.

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2
- Added necessary requirements
- Enabled testing

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

