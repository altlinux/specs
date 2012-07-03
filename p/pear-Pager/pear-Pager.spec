%define pear_name Pager

Name: pear-Pager
Version: 2.4.6
Release: alt1

Summary: Data paging class

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/Pager

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Pager-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
It takes an array of data as input and pages it according to various
parameters.
It also builds links within a specified range, and allows complete
customization of the output (it even works with front controllers and
mod_rewrite).
Two operating modes available: "Jumping" and "Sliding" window style.

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
%pear_dir/Pager/
%pear_dir/Pager.php
%pear_testdir/Pager/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.6-alt1
- new version 2.4.6 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- initial build for ALT Linux Sisyphus

