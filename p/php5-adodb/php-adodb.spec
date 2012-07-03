%def_without pear
%define oname php-adodb
%define php5_extension adodb

Name: php5-%php5_extension
Summary: Database abstraction layer for PHP
Version: 5.13
Release: alt1

License: BSD or LGPLv2+
Url: http://adodb.sf.net
Group: System/Servers
BuildArch: noarch
Source: http://downloads.sourceforge.net/project/adodb/adodb-php5-only/adodb-513-for-php5/adodb513.zip

Packager: Alexey Shabalin <shaba@altlinux.ru>

Requires: php-base

BuildPreReq: rpm-build-php5 unzip
%{?_with_pear:BuildPreReq: rpm-build-pear}

%description
PHP's database access functions are not standardized. This creates a
need for a database class library to hide the differences between the
different databases (encapsulate the differences) so we can easily
switch databases.

It currently supports MySQL, Interbase, Oracle, Microsoft SQL Server,
Sybase, PostgreSQL, Foxpro, Access, ADO and ODBC.

%package -n pear-Auth-Container-ADOdb
Summary: ADOdb container for PEAR Auth
Group: Development/Other
Requires: %name = %version-%release
Requires: %name-pear
Requires: pear-Auth

%description -n pear-Auth-Container-ADOdb
Storage driver for fetching login data from a database using
ADOdb-PHP.

This storage driver can use all databases which are supported by the
ADOdb DB abstraction layer to fetch login data.

%package pear
Summary: PEAR DB Emulation Layer for ADOdb
Group: Development/Other
Requires: %name = %version-%release
Requires: pear-core

%description pear
PEAR DB Emulation Layer for ADODB.

%description pear -l pl.UTF-8
Warstwa emulacji PEAR DB dla ADOdb.

%package tests
Summary: Tests for ADOdb
Group: Development/Other
Requires: %name = %version-%release

%description tests
Tests for ADOdb.

%prep
%setup -q -n adodb5

%build
# undos the source
find . -type f -print0 | xargs -0 sed -i -e 's,\r$,,'
# fix dir perms
find . -type d | xargs chmod 755
# fix file perms
find . -type f | xargs chmod 644

mv pear/{readme.Auth.txt,README}
rm -rf session/old

%install
mkdir -p %buildroot%php5_moddir/adodb
mkdir -p %buildroot%_var/www/icons
cp -ar * %buildroot%php5_moddir/adodb/
cp -ar cute_icons_for_site/* %buildroot%_var/www/icons/

# cleanup
rm -rf %buildroot%php5_moddir/adodb/cute_icons_for_site
rm -rf %buildroot%php5_moddir/adodb/docs
rm -f %buildroot%php5_moddir/adodb/*.txt

%if %{with pear}
mkdir -p %buildroot%pear_dir/Auth/Container
cp -a pear/Auth/Container/ADOdb.php %buildroot%pear_dir/Auth/Container
%endif


%files
%doc *.txt docs/*
%_var/www/icons/*
%php5_moddir/adodb

%exclude %php5_moddir/adodb/contrib
%exclude %php5_moddir/adodb/pear
# tests
%exclude %php5_moddir/adodb/tests
%exclude %php5_moddir/adodb/pivottable.inc.php
%exclude %php5_moddir/adodb/rsfilter.inc.php
# pear
%exclude %php5_moddir/adodb/adodb-pear.inc.php
%exclude %php5_moddir/adodb/adodb-errorpear.inc.php

%if_with pear
%files tests
%php5_moddir/adodb/tests
%php5_moddir/adodb/pivottable.inc.php
%php5_moddir/adodb/rsfilter.inc.php

%files pear
%php5_moddir/adodb/adodb-pear.inc.php
%php5_moddir/adodb/adodb-errorpear.inc.php

%files -n php-pear-Auth_Container_ADOdb
%doc pear/README
%pear_dir/Auth/Container/ADOdb.php
%endif


%changelog
* Wed Aug 31 2011 Alexey Shabalin <shaba@altlinux.ru> 5.13-alt1
- 5.13

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 5.11-alt1
- 5.11

* Thu Mar 25 2010 Alexey Shabalin <shaba@altlinux.ru> 5.10-alt1
- initial build for ALT Linux Sisyphus
