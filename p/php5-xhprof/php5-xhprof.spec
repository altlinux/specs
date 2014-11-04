%define		php5_extension	xhprof
%define 	real_name	xhprof
%define		real_version	0.9.4

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release

Summary:	Hierarchical Profiler for PHP

License:	%asl 2.0
Group:		System/Servers
URL:		http://pecl.php.net/package/xhprof

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh
Source3:	%real_name.conf

BuildRequires(pre): rpm-build-php5 rpm-build-licenses rpm-macros-webserver-common
# Automatically added by buildreq on Fri Jul 04 2014
# optimized out: gnu-config libcloog-isl4 php5-libs
BuildRequires: glibc-devel-static
BuildRequires: php5-devel = %php5_version

%description
XHProf is a function-level hierarchical profiler for PHP and has a
simple HTML based navigational interface. The raw data collection
component is implemented in C (as a PHP extension). The reporting/UI
layer is all in PHP. It is capable of reporting function-level
inclusive and exclusive wall times, memory usage, CPU times and
number of calls for each function. Additionally, it supports ability
to compare two runs (hierarchical DIFF reports), or aggregat
results from multiple runs.

%prep
%setup -c
cp %SOURCE3 %real_name.conf

%build
cd extension

phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version

%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	--enable-xhprof \
	%nil

%php5_make

%install
pushd extension
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params
popd

mkdir -p %buildroot%webserver_webappsdir
cp -a xhprof_html %buildroot%webserver_webappsdir
cp -a xhprof_lib  %buildroot%webserver_webappsdir

sed -e 's|DIRECTORY|%webserver_webappsdir/xhprof_html|g' -i %real_name.conf

%files
%doc README CHANGELOG CREDITS package.xml examples %real_name.conf
%php5_extconf/%php5_extension
%php5_extdir/*

%webserver_webappsdir/xhprof_html
%webserver_webappsdir/xhprof_lib

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%php5_version-%php5_release

* Tue Nov  4 2014 Nikolay A. Fetisov <naf@altlinux.ru> 5.5.17.20140916-alt1
- Initial build for ALT Linux Sisyphus

