%define pear_name Gtk2_EntryDialog

Name: pear-Gtk2_EntryDialog
Version: 1.0.0
Release: alt1

Summary: Message box with text entry field

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Gtk2_EntryDialog

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Gtk2_EntryDialog-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Gtk2 message box with additional text entry field.

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
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

