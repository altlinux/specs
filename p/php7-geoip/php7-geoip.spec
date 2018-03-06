# vim: set ft=spec: -*- rpm-spec -*-
%define php7_extension geoip

# TODO: pass test

Name: php7-%php7_extension
Version: 1.1.1
Release: alt%php7_version.%php7_release

Summary: Map IP address to geographic places
License: PHP License
Group: Development/Other

Url: http://pecl.php.net/package/%php7_extension

# Source-url: http://pecl.php.net/get/%php7_extension-%version.tgz
Source: %name-%version.tar

Requires: pear-core

BuildRequires(pre): rpm-build-pecl-php7
BuildRequires: php7-devel
BuildPreReq: pear-core
BuildPreReq: libGeoIP-devel

%description
This PHP extension allows you to find the location of an IP address -
City, State, Country, Longitude, Latitude, and other information as all,
such as ISP and connection type.
For more info, please visit Maxmind`s website.

%prep
%setup
#cd %php7_extension-%version
#patch0 -p1

%build
cd %php7_extension-%version
phpize
%pecl7_configure
%php7_make

%install
%pecl7_install
%pecl7_install_doc README ChangeLog

%check
cd %php7_extension-%version
#make test

%post
%php7_extension_postin

%preun
%php7_extension_preun

%files
%pecl7_files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-alt%php7_version.%php7_release
- Rebuild with php7-%php7_version-%php7_release

* Mon Mar 05 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt0
- new version (1.1.1) with rpmgs script

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.8-alt3
- Rebuild with php7-5.3.18.20121017-alt1
- cleanup spec - removed garbage from solo@

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 1.0.8-alt2
- Rebuild with php7-devel-5.3.17.20120913-alt1

* Tue Apr 24 2012 Aleksey Avdeev <solo@altlinux.ru> 1.0.8-alt1
- Initial build for ALT Linux Sisyphus
