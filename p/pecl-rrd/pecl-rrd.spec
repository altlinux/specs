%define php5_extension rrd

Name: pecl-%php5_extension
Version: 1.1.0
Release: alt1.%php5_version.%php5_release

Summary: PHP bindings to rrd tool system
License: %bsd
Group: Development/Other

Url: http://pecl.php.net/package/%php5_extension

Source: %php5_extension-%version.tar

Requires: pear-core

BuildRequires(pre): rpm-build-pecl
BuildRequires: php5-devel
BuildPreReq: pear-core
BuildPreReq: rpm-build-licenses
BuildPreReq: librrd-devel

%description
Procedural and simple OO wrapper for rrdtool - data logging and graphing
system for time series data.

%prep
%setup -c

%build
cd %php5_extension-%version
phpize
%pecl_configure '--with-php-config=%_bindir/php-config'
%make_build

%install
%pecl_install
%pecl_install_doc CREDITS LICENSE

%check
cd %php5_extension-%version
%make test

%post
%php5_extension_postin

%preun
%php5_extension_preun

%files
%pecl_files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%php5_version-%php5_release

* Wed May 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.1.0-alt1.5.3.25.20130509.alt1
- Initial build for ALT Linux Sisyphus
