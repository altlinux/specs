%define pear_name HTML_QuickForm2

Name: pear-HTML_QuickForm2
Version: 0.2.0
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
%pear_dir/HTML/QuickForm2.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Thu Jun 26 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for ALT Linux Sisyphus

