%define pear_name MDB2

Name: pear-MDB2
Version: 2.5.0b3
Release: alt1

Summary: database abstraction layer

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
PEAR MDB2 is a merge of the PEAR DB and Metabase php database abstraction
layers.

It provides a common API for all supported RDBMS. The main difference to
most
other DB abstraction packages is that MDB2 goes much further to ensure
portability. MDB2 provides most of its many features optionally that
can be used to construct portable SQL statements:
* Object-Oriented API
* A DSN (data source name) or array format for specifying database servers
* Datatype abstraction and on demand datatype conversion
* Various optional fetch modes to fix portability issues
* Portable error codes
* Sequential and non sequential row fetching as well as bulk fetching
* Ability to make buffered and unbuffered queries
* Ordered array and associative array for the fetched rows
* Prepare/execute (bind) named and unnamed placeholder emulation
* Sequence/autoincrement emulation
* Replace emulation
* Limited sub select emulation
* Row limit emulation
* Transactions/savepoint support
* Large Object support
* Index/Unique Key/Primary Key support
* Pattern matching abstraction
* Module framework to load advanced functionality on demand
* Ability to read the information schema
* RDBMS management methods (creating, dropping, altering)
* Reverse engineering schemas from an existing database
* SQL function call abstraction
* Full integration into the PEAR Framework
* PHPDoc API documentation

%prep
%setup -c -n %pear_name-%version

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
%pear_dir/MDB2
%pear_testdir/MDB2/
%pear_datadir/MDB2/LICENSE
%pear_dir/MDB2.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Thu Oct 07 2010 Vitaly Lipatov <lav@altlinux.ru> 2.5.0b3-alt1
- new version 2.5.0b3 (with rpmrb script) (ALT bug #24246)

* Thu Jun 26 2008 Vitaly Lipatov <lav@altlinux.ru> 2.5.0b1-alt1
- new version 2.5.0b1 (with rpmrb script)
- due CVE-2007-5934 (fix bug #16173)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- initial build for ALT Linux Sisyphus

