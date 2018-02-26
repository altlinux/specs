%define pear_name Pager_Sliding

Name: pear-Pager_Sliding
Version: 1.6
Release: alt3

Summary: Sliding Window Pager

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Pager_Sliding

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Pager_Sliding-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
It takes an array of data as input and page it according to various
parameters. It also builds links within a specified range, and allows
complete customization of the output (it even works with mod_rewrite). It
is compatible with PEAR::Pager's API

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
%pear_dir/Pager
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- initial build for ALT Linux Sisyphus

