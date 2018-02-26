%define pear_name Text_Statistics

Name: pear-Text_Statistics
Version: 1.0
Release: alt3

Summary: Compute readability indexes for documents

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Text_Statistics

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Text_Statistics-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Text_Statistics allows for computation of readability indexes for
text documents.

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
%pear_dir/Text
%pear_testdir/Text_Statistics/tests
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus

