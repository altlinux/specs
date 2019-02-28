%define php7_extension rrd

Name: pecl-%php7_extension
Version: 2.0.1
Release: alt1.%php7_version.%php7_release

Summary: PHP bindings to rrd tool system
License: %bsd
Group: Development/Other

Url: http://pecl.php.net/package/rrd

# Source-url: https://pecl.php.net/get/rrd-%version.tgz
Source: %php7_extension-%version.tar

Requires: pear-core

BuildRequires(pre): rpm-build-pecl-php7
BuildRequires: php7-devel
BuildPreReq: pear-core
BuildPreReq: rpm-build-licenses
BuildPreReq: librrd-devel

%description
Procedural and simple OO wrapper for rrdtool - data logging and graphing
system for time series data.

%prep
%setup -c

%build
cd %php7_extension-%version
phpize
%pecl7_configure '--with-php-config=%_bindir/php-config'
%make_build

%install
%pecl7_install
%pecl7_install_doc CREDITS LICENSE

%check
cd %php7_extension-%version
echo s | %make test

%post
%php7_extension_postin

%preun
%php7_extension_preun

%files
%pecl7_files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%php7_version-%php7_release

* Wed May 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.1.0-alt1.5.3.25.20130509.alt1
- Initial build for ALT Linux Sisyphus
