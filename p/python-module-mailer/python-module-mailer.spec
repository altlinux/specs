%define modulename mailer

Name: python-module-mailer
Version: 0.5
Release: alt1.1

Summary: A module to send email simply in Python

Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/%modulename/

Packager: Mikhail A Pokidko <pma@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar

#setup_python_module %modulename

# Automatically added by buildreq on Thu Mar 11 2010
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
A module that simplifies sending email.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename.py

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1
- Rebuild with Python-2.7

* Thu Jul 01 2010 Mikhail Pokidko <pma@altlinux.org> 0.5-alt1
- initial build

