%define		php5_extension	timezonedb
%define 	real_name	timezonedb
%define		real_version	2011.13

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release

Summary:	PHP5 Timezone Database

License:	PHP License
Group:		System/Servers
URL:		http://pecl.php.net/package/timezonedb

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version

%description
timezonedb PHP5 extension is a drop-in replacement for the builtin timezone database
that comes with PHP. You should only install this extension in case you need to get
a later version of the timezone database than the one that ships with PHP.

The data that this extension uses comes from the "Olson" database, which is
located at ftp://elsie.nci.nih.gov/pub/.

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
	--enable-timezonedb \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Tue Feb 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with 5.3.10.20120202-alt1

* Sat Oct 29 2011 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.8.20110823-alt2
- Initial build for ALT Linux Sisyphus

