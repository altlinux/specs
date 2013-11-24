%define		php5_extension	dbase
%define 	real_name	dbase
%define		real_version	5.1.0

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release

Summary:	PHP5 dBase database file access functions

License:	PHP Licence
Group:		System/Servers
URL:		http://pecl.php.net/package/dbase

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version

%description
PHP5 dBase functions allows to access records stored in
dBase-format (dbf) databases.

There is no support for indexes or memo fields.
There is no support for locking, too. Two concurrent webserver
processes modifying the same dBase file will very likely ruin
database.

dBase files are simple sequential files of fixed length records.
Records are appended to the end of the file and delete records
are kept until you call dbase_pack().


%prep
%setup -c
##%setup -T -c
##tar xvf %SOURCE0

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%doc CREDITS

%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun


%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release

* Tue Nov 05 2013 Nikolay A. Fetisov <naf@altlinux.ru> 5.4.17.20130704-alt1
- Initial build for ALT Linux Sisyphus

