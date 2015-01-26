# vim: set ft=spec: -*- rpm-spec -*-
%define php5_extension geoip

Name: pecl-%php5_extension
Version: 1.0.8
Release: alt%php5_version.%php5_release

Summary: Map IP address to geographic places
License: PHP License
Group: Development/Other

Url: http://pecl.php.net/package/%php5_extension

# Source: http://pecl.php.net/get/%php5_extension-%version.tgz
Source: %name-%version.tar
Patch: %name-%version-alt-timezone-GeoIP1.4.5.patch

Requires: pear-core

BuildRequires(pre): rpm-build-pecl
BuildRequires: php5-devel
BuildPreReq: pear-core
BuildPreReq: libGeoIP-devel

%description
This PHP extension allows you to find the location of an IP address -
City, State, Country, Longitude, Latitude, and other information as all,
such as ISP and connection type.
For more info, please visit Maxmind`s website.

%prep
%setup -c
cd %php5_extension-%version
%patch0 -p1

%build
cd %php5_extension-%version
phpize
%pecl_configure '--with-php-config=%_bindir/php-config'
%make_build

%install
%pecl_install
%pecl_install_doc README ChangeLog

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
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1.0.8-alt%php5_version.%php5_release
- Rebuild with php5-%php5_version-%php5_release

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.8-alt3
- Rebuild with php5-5.3.18.20121017-alt1
- cleanup spec - removed garbage from solo@

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 1.0.8-alt2
- Rebuild with php5-devel-5.3.17.20120913-alt1

* Tue Apr 24 2012 Aleksey Avdeev <solo@altlinux.ru> 1.0.8-alt1
- Initial build for ALT Linux Sisyphus
