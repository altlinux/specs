%define		php7_extension	tidy

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	PHP binding for the Tidy HTML clean and repair utility

Group:		System/Servers
License:	PHP Licence
Url:		https://secure.php.net/manual/en/book.tidy.php

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

#Source0:	standart PHP module
Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
# Automatically added by buildreq on Thu Jul 05 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config perl php7-libs python-base python-modules python3 python3-base ruby
BuildRequires: glibc-devel-static libtidy-devel php7-devel

BuildRequires: gcc-c++
BuildRequires: php7-devel = %php7_version

%description
Tidy is a binding for the Tidy HTML clean and repair utility
which allows you to not only clean and otherwise manipulate
HTML, XHTML, and XML documents, but also traverse the  document
tree, including ones with embedded scripting languages such as
PHP or ASP within them using object oriented constructs.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-%php7_extension=%_usr
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

* Thu Jul 5  2018 Nikolay A. Fetisov <naf@altlinux.org> 7.2.6-alt1.S1
- Initial build for ALT Linux Sisyphus
