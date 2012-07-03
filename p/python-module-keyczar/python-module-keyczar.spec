%define module_name keyczar

Name: python-module-%module_name
Version: 0.6b
Release: alt1.1

Summary: Toolkit for safe and simple cryptography

License: Apache 2.0
Group: Development/Python
Url: http://www.keyczar.org/

Source: python-%module_name-%version.tar

BuildArch: noarch
BuildRequires: python-module-setuptools

%setup_python_module %module_name

%description
Keyczar is an open source cryptographic toolkit designed to make it
easier and safer for developers to use cryptography in their
applications. Keyczar supports authentication and encryption with both
symmetric and asymmetric keys.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/keyczar
%python_sitelibdir/python_keyczar*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6b-alt1.1
- Rebuild with Python-2.7

* Fri Apr 16 2010 Denis Klimov <zver@altlinux.org> 0.6b-alt1
- Initial build for ALT Linux

