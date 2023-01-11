%define		php_extension	dba

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	DBA (gdbm, db4) module for PHP
Group:		System/Servers
License:	PHP-3.01

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires:	php-devel = %php_version

# Automatically added by buildreq on Fri Jul 01 2005
BuildRequires: libdb4-devel libgdbm-devel

%description
The %name includes a dynamic shared object (DSO) that adds 
gdbm and db4 support to PHP.

These functions build the foundation for accessing Berkeley DB style
databases. This is a general abstraction layer for several file-based
databases. As such, functionality is limited to a subset of features
modern databases such as Sleepycat Software DB4 support. The behaviour 
of various aspects depend on the implementation of the underlying 
database. Functions such as dba_optimize() and dba_sync() will do 
what they promise for one database and will do nothing for others.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir 
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-libdir=%_lib \
	--with-gdbm \
	--with-db4=%_usr \
	--enable-%php_extension
%php_make

%install
%php_make_install
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %version-%release
