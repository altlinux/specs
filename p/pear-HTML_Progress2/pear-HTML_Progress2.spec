%define pear_name HTML_Progress2

Name: pear-HTML_Progress2
Version: 2.4.0
Release: alt1

Summary: How to include a loading bar in your XHTML documents quickly and easily

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/HTML_Progress2

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Progress2-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTML_Common >= 1.2.1, pear-Event_Dispatcher >= 0.9.1, pear-HTML_CSS >= 1.1.2, pear-core >= 1.4.3

%description
This package provides a way to add a loading bar fully customizable in
existing XHTML documents.
Your browser should accept DHTML feature.

Features:
- create horizontal, vertival bar and also circle, ellipse and polygons
  (square, rectangle).
- allows usage of existing external StyleSheet and/or JavaScript.
- all elements (progress, cells, labels) are customizable by their html
  properties.
- percent/labels are floating all around the progress meter.
- compliant with all CSS/XHMTL standards.
- integration with all template engines is very easy.
- implements Observer design pattern. It is possible to add Listeners.
- adds a customizable monitor pattern to display a progress bar.
  User-end can abort progress at any time.
- allows many progress meter on same page without uses of iframe solution.
- error handling system that support native PEAR_Error, but also
  PEAR_ErrorStack, and any other system you might want to plug-in.
- PHP 5 ready.

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
%pear_dir/HTML/
%pear_testdir/%pear_name/
%pear_datadir/%pear_name/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- new version 2.4.0 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- initial build for ALT Linux Sisyphus

