%define pear_name Services_DynDNS

Name: pear-Services_DynDNS
Version: 0.3.1
Release: alt1

Summary: Provides access to the DynDNS web service

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
Services_DynDNS provides object-oriented interfaces to the DynDNS REST API.

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Services/DynDNS/
%pear_dir/Services/DynDNS.php
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

