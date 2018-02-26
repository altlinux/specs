%define pear_name HTML_CSS

Name: pear-HTML_CSS
Version: 1.5.1
Release: alt1

Summary: HTML_CSS is a class for generating CSS declarations

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/HTML_CSS

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_CSS-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTML_Common >= 1.2.4, pear-core >= 1.5.4

%description
HTML_CSS provides a simple interface for generating a stylesheet
declaration.
It is completely standards compliant, and has some great features:
* Simple OO interface to CSS definitions
* Can parse existing CSS (string or file)
* Output to
    - Inline stylesheet declarations
    - Document internal stylesheet declarations
    - Standalone stylesheet declarations
    - Array of definitions
    - File

In addition, it shares the following with HTML_Common based classes:
* Indent style support
* Line ending style

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
%pear_dir/HTML
%pear_testdir/HTML_CSS/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version 1.5.1 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- initial build for ALT Linux Sisyphus

