%define _unpackaged_files_terminate_build 1
%define realname vatnumber

Name:           python3-module-%realname
Version:        1.2
Release:        alt1
Summary:        Python module to validate VAT numbers

Group:          Development/Python3
License:        GPLv3+
URL:            http://code.google.com/p/vatnumber/
Source0:        https://pypi.python.org/packages/d7/7c/869b59cd9cb6ed1057372cb704a3b86688ae8c12cfc7fcaedbc1424f5e7f/vatnumber-%{version}.tar.gz

BuildArch:      noarch
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%py3_requires suds

%description
Python module to validate VAT numbers.

%prep
%setup -q -n vatnumber-%{version}

%build
%python3_build

%install
%python3_install

%files
%doc CHANGELOG COPYRIGHT README PKG-INFO
%python3_sitelibdir/%realname
%python3_sitelibdir/%{realname}*.egg-info

%changelog
* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

