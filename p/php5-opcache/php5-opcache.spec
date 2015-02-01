%define		php5_extension	opcache

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release.1

Summary:	Zend OPcache extension for opcode caching and optimization

Group:		System/Servers
License:	PHP Licence
URL:		http://php.net/manual/en/book.opcache.php
#		http://pecl.php.net/package/ZendOpcache

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

#Source0:	standart PHP module
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

Patch0: php5-opcache-sapi-names.patch

BuildRequires(pre): rpm-build-php5
BuildRequires: gcc-c++
BuildRequires: php5-devel = %php5_version


%description
PHP5 Opcache extension provides faster PHP execution through
opcode caching and optimization. It improves PHP performance
by storing precompiled script bytecode in the shared memory.
This eliminates the stages of reading code from the disk and
compiling it on future access. In addition, it applies a few
bytecode optimization patterns that make code execution
faster.

%prep
%setup -T -c
cp -pr -- %php5_extsrcdir/%php5_extension/* .
%patch0

# Fix path to pdo*.h
subst 's@php/ext@php/%_php5_version/ext@g' config.m4

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version

# Fix for config.m4 in %%prep would't work for some reason
subst 's@php/ext@php/%_php5_version/ext@g' configure

%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	--with-pdo-mysql=%_usr \
	--enable-opcache \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc README

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Sun Feb 01 2015 Anton Farygin <rider@altlinux.ru> 5.5.21.20150121-alt1.1
- fixed work with apache2-mod_php5, apache-mod_php5 and php5-cgi sapi (closes: #30496)

* Mon Oct 27 2014 Nikolay A. Fetisov <naf@altlinux.ru> 5.5.17.20140916-alt1
- Initial build for ALT Linux Sisyphus

