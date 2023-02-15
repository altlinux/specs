%ifarch ppc64le armh
%def_without check
%else
%def_with check
%endif
%define		php_extension	opcache
%{?optflags_lto:%global optflags_lto %nil}

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release.2

Summary:	Zend Opcache extension for opcode caching and optimization

Group:		System/Servers
License:	PHP-3.01
URL:		http://php.net/manual/en/book.opcache.php
#		http://pecl.php.net/package/ZendOpcache

Packager:       Nikolay A. Fetisov <naf@altlinux.org>

#Source0:	standart PHP module
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

Patch0: php7-opcache-sapi-names.patch

BuildRequires(pre): rpm-build-php8.0-version
BuildRequires: gcc-c++
BuildRequires: php-devel = %php_version
BuildRequires: php%_php_suffix = %php_version


%description
php7 Opcache extension provides faster PHP execution through
opcode caching and optimization. It improves PHP performance
by storing precompiled script bytecode in the shared memory.
This eliminates the stages of reading code from the disk and
compiling it on future access. In addition, it applies a few
bytecode optimization patterns that make code execution
faster.

%prep
%setup -T -c
cp -pr -- %php_extsrcdir/%php_extension/* .

%patch0

# Fix path to pdo*.h
subst 's@php/ext@php/%_php_version/ext@g' config.m4

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
%ifarch %e2k
%add_optflags -U__AVX__ -U__SSE2__
%endif
export LDFLAGS=-lphp-%_php_version

# Fix for config.m4 in %%prep would't work for some reason
subst 's@php/ext@php/%_php_version/ext@g' configure

%configure \
	--with-libdir=%_lib \
	--enable-%php_extension \
	--enable-%php_extension-file \
	%nil

%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
# create symlink to source of the dl_test for the test gh8466
[ -d %php_extsrcdir/dl_test ] && ln -s %php_extsrcdir/dl_test ../dl_test
mkdir -p ext/opcache
ln -s ../../tests ext/opcache/tests

NO_INTERACTION=1 make test

%files
%php_extconf/%php_extension
%php_extdir/*

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %version-%release

* Thu Apr 30 2020 Vitaly Lipatov <lav@altlinux.ru> 7.3.16-alt1.3
- fix SAPI name (ALT bug 38412)

* Thu Nov 28 2019 Michael Shigorin <mike@altlinux.org> 7.3.12-alt1.2
- Fix build on %%e2k (SIMD needs proper porting)

* Fri Jun 16 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.6-alt1.S1.1
- Fix build with enabled Opcache file cache

* Tue Jun 13 2017 Nikolay A. Fetisov <naf@altlinux.org> 7.1.6-alt1.S1
- Initial build for ALT Linux Sisyphus

