%define		php7_extension	mysqli

Name:	 	php7-mysqlnd-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	MySQL Improved Extension for PHP with Native Driver

License:	PHP Licence
Group:		System/Servers
URL:		http://www.php.net/manual/en/ref.mysqli.php

#Source0:	standart PHP module
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7 
BuildRequires: php7-devel = %php7_version
Conflicts: php7-%php7_extension
Provides: php7-%php7_extension
Provides: php7-%php7_extension = %php7_version-%php7_release
Requires: php7-mysqlnd = %php7_version

%description
MySQLi (improved) - new MySQL interface for PHP and MySQL 4.1.3+

%prep
%setup -T -c
cp -pr -- %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	#

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

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

