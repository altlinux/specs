%define pear_name DB_Table

Name: pear-DB_Table
Version: 1.5.5
Release: alt1

Summary: An object oriented interface to, and model of, a database. Integrates with HTML_QuickForm

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/DB_Table

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/DB_Table-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The DB_Table package provides an object oriented interface to a database.

Each instance of the core DB_Table class contains the schema for a table,
defined using abstract data types. The class provides a portable api for
insert, update, delete, and select SQL commands, and can validate data
types upon insertion and updating. It provides methods to automatically
create or verify a database table. DB_Table also provides methods (using
PEAR HTML_QuickForm) to generate input forms that match the column
definitions.

Each instance of the DB_Table_Database class contains a model of
relationships between tables in a database, in which each table is
represented by an instance of DB_Table. DB_Table_Database provides a method
for automatic construction of join conditions for inner joins involving any
number of tables, optional php validation of foreign key validity, and
optional php emulation of actions triggered on delete or update of
referenced rows, such as cascading deletes.

The DB_Table_Generator class auto-generates the php code necessary to
create an interface to an existing database.

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
%pear_testdir/DB_Table/tests
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt1
- new version 1.5.5 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- initial build for ALT Linux Sisyphus

