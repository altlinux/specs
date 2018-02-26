%define pear_name Gtk_ScrollingLabel

Name: pear-Gtk_ScrollingLabel
Version: 1.0.0
Release: alt1

Summary: A scrolling label for PHP-Gtk

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Gtk_ScrollingLabel

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Gtk_ScrollingLabel-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This is a class to encapsulate the functionality needed for a scrolling gtk
label. This class provides a simple, easy to understand API for setting up
and controlling the label.  It allows for the ability to scroll in either
direction, start and stop the scroll, pause and unpause the scroll, get and
set the text, and set display properites of the text.

%prep
%setup -c -n %pear_name-%version
%pear_prepare_module

%install
cd %pear_name-%version
%pear_install_module

%post
%pear_install

%preun
%pear_uninstall

%files
%doc LICENSE CHANGELOG
%pear_dir/Gtk/
%pear_testdir/%pear_name/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

