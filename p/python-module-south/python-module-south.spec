%define version 0.7.6
%define release alt1
%define oname south
%setup_python_module %oname
%add_python_req_skip cx_Oracle

Name: python-module-%oname
Version:%version
Release: %release
BuildArch: noarch

Summary: Migrations for Django
License: Apache
Group: Development/Python
Url: http://south.aeracode.org

# Source: http://www.aeracode.org/releases/south/%modulename-%version.tar.gz
# https://bitbucket.org/andrewgodwin/south/overview
Source: %name-%version.tar

# Automatically added by buildreq on Mon Mar 01 2010
BuildRequires: python-devel

%description
South is an intelligent database migrations library for the Django web framework.
It is database-independent and DVCS-friendly, as well as a whole host of other features.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Thu Feb 28 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.3-alt1.1
- Rebuild with Python-2.7

* Mon Dec 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Wed Apr 21 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- 0.7

* Mon Mar 01 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- initial build
