%define pear_name HTTP

Name: pear-HTTP
Version: 1.4.0
Release: alt3

Summary: Miscellaneous HTTP utilities

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/HTTP

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTTP-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

#Requires: php5-pcre
Requires: php5

%description
The HTTP class is a class with static methods for doing
miscellaneous HTTP related stuff like date formatting,
language negotiation or HTTP redirection.

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
%pear_dir/HTTP.php
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- initial build for ALT Linux Sisyphus

