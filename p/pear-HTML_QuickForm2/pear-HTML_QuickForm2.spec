%define pear_name HTML_QuickForm2

Name: pear-HTML_QuickForm2
Version: 2.3.1
Release: alt1

Summary: PHP5 rewrite of HTML_QuickForm package

License: BSD
Group: Development/Other
URL: http://pear.php.net/package/%pear_name

Source: http://pear.php.net/get/%pear_name-%{version}.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

Requires: pear-core >= 1.4.3

%description
The package is expected to offer at least the same functionality as
HTML_QuickForm and work with PHP5 E_STRICT setting.

%prep
%setup -c
%pear_prepare_module

%install
%pear_install_module

%post
%pear_install

%preun
%pear_uninstall

%files
%doc LICENSE CHANGELOG
%pear_dir/HTML/QuickForm2/
%pear_testdir/HTML_QuickForm2/
%pear_datadir/HTML_QuickForm2/
%pear_dir/HTML/QuickForm2.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt1
- new version 2.2.2 (with rpmrb script)

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Wed Jul 27 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script)

* Thu Jun 26 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for ALT Linux Sisyphus

