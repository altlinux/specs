%define		php7_extension	dba

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	DBA (gdbm, db4) module for PHP
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires:	php7-devel = %php7_version

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
cp -pr %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir 
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-libdir=%_lib \
	--with-gdbm \
	--with-db4=%_usr \
	--enable-%php7_extension
%php7_make

%install
%php7_make_install
install -D -m 644 %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%php7_extconf/%php7_extension
%php7_extdir/*
%doc CREDITS

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release
