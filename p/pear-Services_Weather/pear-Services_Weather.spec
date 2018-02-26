%define pear_name Services_Weather

Name: pear-Services_Weather
Version: 1.4.4
Release: alt1

Summary: This class acts as an interface to various online weather-services

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/Services_Weather

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Services_Weather-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTTP_Request >= 1.2.0, pear-core >= 1.4.0

%description
Services_Weather searches for given locations and retrieves current
weather data and, dependent on the used service, also forecasts.  Up to
now, GlobalWeather from CapeScience, Weather XML from EJSE (US only),
a XOAP service from Weather.com and METAR/TAF from NOAA are supported.
Further services will get included, if they become available, have a
usable API and are properly documented.

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Services/
%pear_datadir/%pear_name/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- new version 1.4.4 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.3-alt2
- autorebuild for correct requires(pre) (see bug #16086)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.3-alt1
- new version 1.4.3 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- initial build for ALT Linux Sisyphus

