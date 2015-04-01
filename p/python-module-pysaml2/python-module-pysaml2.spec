%define sname pysaml2

Name: python-module-%sname
Version: 2.4.0
Release: alt1
Summary: Python implementation of SAML Version 2 to be used in a WSGI environment
License: ASL 2.0

Url: https://github.com/rohe/pysaml2
Group: Development/Python
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-setuptools-tests

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
%doc README
%_bindir/*.py
%python_sitelibdir/*

%changelog
* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- Initial build


