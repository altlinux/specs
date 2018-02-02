%define sname pysaml2

Name: python-module-%sname
Version: 3.0.2
Release: alt1.1
Summary: Python implementation of SAML Version 2 to be used in a WSGI environment
License: ASL 2.0

Url: https://github.com/rohe/pysaml2
Group: Development/Python

# Source-url: https://github.com/rohe/pysaml2/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-setuptools

%description
PySAML2 should be compatible with any python >= 2.6 not 3.X yet.
To be able to sign/verify, encrypt/decrypt you need xmlsec1.
The repoze stuff works best together with repoze.who .

%prep
%setup

%build
%python_build

%install
%python_install

rm -fr %buildroot%python_sitelibdir/*/tests

%files
%doc README.rst
%_bindir/*.py
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt1
- new version 3.0.2 (with rpmrb script)

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- Initial build


