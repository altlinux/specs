%define pear_name MDB

Name: pear-MDB
Version: 1.3.0
Release: alt3

Summary: database abstraction layer

License: BSD style
Group: Development/Other
Url: http://pear.php.net/package/MDB

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/MDB-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-XML_Parser

%description
PEAR MDB is a merge of the PEAR DB and Metabase php database abstraction
layers.
It provides a common API for all support RDBMS. The main difference to
most
other DB abstraction packages is that MDB goes much further to ensure
portability. Among other things MDB features:
* An OO-style query API
* A DSN (data source name) or array format for specifying database servers
* Datatype abstraction and on demand datatype conversion
* Portable error codes
* Sequential and non sequential row fetching as well as bulk fetching
* Ordered array and associative array for the fetched rows
* Prepare/execute (bind) emulation
* Sequence emulation
* Replace emulation
* Limited Subselect emulation
* Row limit support
* Transactions support
* Large Object support
* Index/Unique support
* Module Framework to load advanced functionality on demand
* Table information interface
* RDBMS management methods (creating, dropping, altering)
* RDBMS independent xml based schema definition management
* Altering of a DB from a changed xml schema
* Reverse engineering of xml schemas from an existing DB (currently only
MySQL)
* Full integration into the PEAR Framework
* Wrappers for the PEAR DB and Metabase APIs
* PHPDoc API documentation
Currently supported RDBMS:
MySQL
PostGreSQL
Oracle
Frontbase
Querysim
Interbase/Firebird
MSSQL

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
%pear_dir/MDB.php
%pear_dir/MDB/
%pear_testdir/MDB/tests
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Linux Sisyphus

