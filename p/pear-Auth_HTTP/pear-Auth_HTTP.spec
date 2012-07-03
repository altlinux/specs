%define pear_name Auth_HTTP

Name: pear-Auth_HTTP
Version: 2.1.6
Release: alt3

Summary: HTTP authentication

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Auth_HTTP

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Auth_HTTP-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Auth >= 1.2.0

%description
The PEAR::Auth_HTTP class provides methods for creating an HTTP
authentication system using PHP, that is similar to Apache's
realm-based .htaccess authentication.

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
%pear_testdir/Auth_HTTP/
%pear_dir/Auth
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- initial build for ALT Linux Sisyphus

