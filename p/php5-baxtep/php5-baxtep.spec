# Package name without php prefix
%define		php5_extension	baxtep
###############################################################
Name:	 	php5-%php5_extension
Version:	2.2.6
Release:	alt2

Summary:	PHP security extension to intercept execution of system commands with PHP scripts

Group:		System/Servers
License:	GPLv2
URL:		http://code.google.com/p/baxtep/

BuildRequires(pre): rpm-build-php5

# Automatically added by buildreq on Sat Jan 21 2012
# optimized out: libstdc++-devel
BuildRequires: gcc-c++ glibc-devel php5-devel re2c

BuildRequires: php5-devel = %php5_version zlib-devel
Requires: php5-libs = %php5_version

Source0:	php5-%php5_extension-%version.tar
Source1:	php5-%php5_extension.ini
Source2:	php5-%php5_extension-params.sh

%description
PHP security extension to intercept execution of system commands
with PHP scripts. The list of currently intercepted functions:
    exec()
    system()
    shell_exec()
    passthru()

Extension is useful for web-hosting to help system administrators
to find php-shells and vulnerable php-scripts. 

%prep
%setup -q -n php5-%php5_extension-%version

%build
export CFLAGS="%optflags"
phpize
%configure --enable-memcache --with-zlib-dir=/usr
%php5_make

%install
%php5_make_install
%__install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
%__install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%doc README
%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Tue Feb 14 2012 Anton Farygin <rider@altlinux.ru> 2.2.6-alt2
- rebuild with php5-5.3.10.20120202-alt1

* Sat Jan 21 2012 Vitaly Lipatov <lav@altlinux.ru> 2.2.6-alt1
- initial build for ALT Linux Sisyphus
