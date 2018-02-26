%define pear_name MDB_QueryTool

Name: pear-MDB_QueryTool
Version: 1.2.2
Release: alt1

Summary: An OO-interface for easily retrieving and modifying data in a DB

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/MDB_QueryTool

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/MDB_QueryTool-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Log >= 1.7, pear-core >= 1.4.0b1

%description
This package is an OO-abstraction to the SQL-Query language, it provides
methods such
as setWhere, setOrder, setGroup, setJoin, etc. to easily build queries.
It also provides an easy to learn interface that interacts nicely with
HTML-forms using
arrays that contain the column data, that shall be updated/added in a DB.
This package bases on an SQL-Builder which lets you easily build
SQL-Statements and execute them.
NB: this is a PEAR::MDB porting from the original DB_QueryTool
written by Wolfram Kriesing and Paolo Panto (vision:produktion,
wk@visionp.de).

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/MDB
%pear_testdir/MDB_QueryTool/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Linux Sisyphus

