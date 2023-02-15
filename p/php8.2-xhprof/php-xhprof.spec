%define		php_extension	xhprof
Name:	 	php%_php_suffix-%php_extension
Version:	2.3.9
Epoch:		1
Release:	alt3.%_php_release_version

Summary:	PHP hierarchical profiler

License:	%asl
Group:		System/Servers
URL:		https://pecl.php.net/package/xhprof

Packager:	Nikolay A. Fetisov <naf@altlinux.org>

Source0:	%php_extension-%version.tar
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh
Source3:	%php_extension.conf

BuildRequires(pre): rpm-build-php8.2-version rpm-build-licenses rpm-macros-webserver-common
BuildRequires: php-devel = %php_version

%description
XHProf is a function-level hierarchical profiler for PHP and
has a simple HTML based navigational interface.
The raw data collection component is implemented in C (as a
PHP extension). The reporting/UI layer is all in PHP.
It is capable of reporting function-level inclusive and
exclusive wall times, memory usage, CPU times and number
of calls for each function. Additionally, it supports ability
to compare two runs (hierarchical DIFF reports), or aggregate
results from
multiple runs.


%prep
%setup -n %php_extension-%version
cp %SOURCE3 %php_extension.conf

%build
pushd extension/
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version

%configure \
	--with-%php_extension \
	--with-libdir=%_lib \
	--enable-zmq \
	%nil

%php_make

%install
pushd extension/
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params
popd

mkdir -p %buildroot%webserver_webappsdir
cp -a xhprof_html %buildroot%webserver_webappsdir
cp -a xhprof_lib  %buildroot%webserver_webappsdir
sed -e 's|DIRECTORY|%webserver_webappsdir/xhprof_html|g' -i %php_extension.conf

%files
%doc CHANGELOG README.md LICENSE
%doc examples/sample.php scripts/xhprofile.php
%doc xhprof.conf

%php_extconf/%php_extension
%php_extdir/*

%webserver_webappsdir/xhprof_html
%webserver_webappsdir/xhprof_lib

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1:%version-%release
- Rebuild with php-devel = %php_version-%php_release

* Tue Feb 14 2023 Anton Farygin <rider@altlinux.ru> 1:2.3.9-alt1
- update to 2.3.9

* Wed Jul 07 2021 Anton Farygin <rider@altlinux.ru> 1:2.3.3
- update to 2.3.3
- cleanup specfile
- built source from upstream git tree

* Tue Jan 28 2020 Nikolay A. Fetisov <naf@altlinux.org> 7.3.13-alt1
- Initial build for ALT Linux Sisyphus
