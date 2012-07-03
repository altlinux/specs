%define pear_name Stream_SHM

Name: pear-Stream_SHM
Version: 1.0.0
Release: alt4

Summary: Shared Memory Stream

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Stream_SHM

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Stream_SHM-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The Stream_SHM package provides a class that can be registered with
stream_register_wrapper() in order to have stream-based shared-memory
access.

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
%pear_dir/Stream
%pear_xmldir/%pear_name.xml

%changelog
* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt4
- fix php requires

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

