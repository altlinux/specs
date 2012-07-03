%define pear_name DB

Name: pear-DB
Version: 1.7.13
Release: alt3

Summary: Database Abstraction Layer

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/DB

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/DB-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
DB is a database abstraction layer providing:
* an OO-style query API
* portability features that make programs written for one DBMS work with
other DBMS's
* a DSN (data source name) format for specifying database servers
* prepare/execute (bind) emulation for databases that don't support it
natively
* a result object for each query response
* portable error codes
* sequence emulation
* sequential and non-sequential row fetching as well as bulk fetching
* formats fetched rows as associative arrays, ordered arrays or objects
* row limit support
* transactions support
* table information interface
* DocBook and phpDocumentor API documentation

DB layers itself on top of PHP's existing
database extensions.

Drivers for the following extensions pass
the complete test suite and provide
interchangeability when all of DB's
portability options are enabled:

  fbsql, ibase, informix, msql, mssql,
  mysql, mysqli, oci8, odbc, pgsql,
  sqlite and sybase.

There is also a driver for the dbase
extension, but it can't be used
interchangeably because dbase doesn't
support many standard DBMS features.

DB is compatible with both PHP 4 and PHP 5.

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
%pear_dir/DB
%pear_testdir/DB/tests
%pear_dir/DB.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.13-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.13-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.13-alt1
- initial build for ALT Linux Sisyphus

