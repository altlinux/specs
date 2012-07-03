%define modulename pymysql

Name: python-module-%modulename
Version: 0.3
Release: alt1.svn35.1

%setup_python_module %modulename

Summary: This pure Python MySQL client provides a DB-API to a MySQL database.
License: MIT
Group: Development/Python

Url: http://code.google.com/p/pymysql/
Packager: Alexey Morsov <swi@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: %py_dependencies setuptools

%description
This pure Python MySQL client provides a DB-API to a MySQL database by 
talking directly to the server via the binary client/server protocol.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.svn35.1
- Rebuild with Python-2.7

* Tue Oct 12 2010 Alexey Morsov <swi@altlinux.ru> 0.3-alt1.svn35
- new version

* Tue Mar 16 2010 Alexey Morsov <swi@altlinux.ru> 0.2-alt1.svn4
- initial build

