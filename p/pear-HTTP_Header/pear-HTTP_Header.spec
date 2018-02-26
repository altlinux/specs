%define pear_name HTTP_Header

Name: pear-HTTP_Header
Version: 1.2.0
Release: alt3

Summary: OO interface to modify and handle HTTP headers and status codes

License: BSD, revised
Group: Development/Other
Url: http://pear.php.net/package/HTTP_Header

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTTP_Header-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTTP >= 1.3.1

%description
This class provides methods to set/modify HTTP headers
and status codes including an HTTP caching facility.
It also provides methods for checking Status types.

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
%pear_dir/HTTP
%pear_testdir/HTTP_Header/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Linux Sisyphus

