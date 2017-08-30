%define		php5_extension	jsmin
%define 	real_name	jsmin
%define		real_version	2.0.1

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release

Summary:	PHP5 jsmin - extension for minifying JavaScript

License:	PHP License
Group:		System/Servers
URL:		https://github.com/allegro/php-jsmin

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%real_name-%real_version.tar
Patch0:		%real_name-%real_version.patch
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version

%description
jsmin PHP5 extension provides an API for minifying JavaScript,
by adding Douglas Crockford's JSMin functionality to PHP.
JSMin is a filter which removes comments and unnecessary whitespace
from JavaScript files. It typically reduces filesize by half,
resulting in faster downloads. It also encourages a more expressive
programming style because it eliminates the download cost of clean,
literate self-documentation.

%prep
%setup -c
%patch0 -p1

%build
cd %real_name-%real_version
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	--enable-jsmin \
	#

%php5_make

%install
cd %real_name-%real_version
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
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release

* Fri Aug 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 5.6.31.20170607-alt1.S1
- Initial build for ALT Linux Sisyphus

