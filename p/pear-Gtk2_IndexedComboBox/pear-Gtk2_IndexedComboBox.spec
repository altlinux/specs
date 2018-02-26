%define pear_name Gtk2_IndexedComboBox

Name: pear-Gtk2_IndexedComboBox
Version: 1.0.0
Release: alt1

Summary: Indexed Gtk2 combo box similar to the HTML select box

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Gtk2_IndexedComboBox

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Gtk2_IndexedComboBox-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Indexed Gtk2 combo box similar to the HTML select box.
  Lets you not only store values as the normal GtkComboBox,
  but associated key/value pairs as well.

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
%pear_dir/Gtk2
%pear_testdir/Gtk2_IndexedComboBox/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

