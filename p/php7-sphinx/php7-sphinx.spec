%define		php7_extension	sphinx
%define 	real_name	sphinx
%define		real_version	1.4.0-dev

Name:	 	php7-%{php7_extension}
Version:	%php7_version
Release:	%php7_release

Summary:	PHP7 bindings for Sphinx search client library

License:	PHP License
Group:		System/Servers
URL:		https://pecl.php.net/package/sphinx

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar
Patch0:		%real_name-%real_version.patch

Patch1:		php7-sphinx-1.4.0-memory_leak.patch
Patch2:		php7-sphinx-1.4.0-RETURN_BOOL.patch

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh


BuildRequires(pre): rpm-build-php7
BuildRequires: php7-devel = %php7_version
BuildRequires: libsphinxclient-devel

%description
php7-sphinx extension provides bindings for Sphinx search client
library. Sphinx is a standalone search engine meant to provide
fast, size-efficient and relevant fulltext search functions
to other applications. Sphinx was specially designed to integrate
well with SQL databases and scripting languages.

%prep
%setup -c
%patch0 -p1

%patch1
%patch2

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version

%configure \
	--with-%php7_extension \
	--with-libdir=%_lib \
	--enable-sphinx \
	%nil

%php7_make

%install
%php7_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%doc CREDITS LICENSE

%php7_extconf/%php7_extension
%php7_extdir/*

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

* Tue Jun 13 2017 Nikolay A. Fetisov <naf@altlinux.ru> 7.1.6-alt1.S1
- Initial build for ALT Linux Sisyphus

