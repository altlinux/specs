%define pear_name HTML_Progress

Name: pear-HTML_Progress
Version: 1.2.5
Release: alt4

Summary: How to include a loading bar in your XHTML documents quickly and easily

License: PHP License 3.0
Group: Development/Other
Url: http://pear.php.net/package/HTML_Progress

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Progress-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTML_Common >= 1.2.1

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
- Look and feel can be sets by internal API or external config file
- allows many progress meter on same page without uses of iframe solution.

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
%pear_testdir/HTML_Progress/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt4
- fix php requires

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt1
- initial build for ALT Linux Sisyphus

