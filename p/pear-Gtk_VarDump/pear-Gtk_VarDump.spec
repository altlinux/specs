%define pear_name Gtk_VarDump

Name: pear-Gtk_VarDump
Version: 1.0.0
Release: alt1

Summary: A simple GUI to example php data trees

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Gtk_VarDump

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Gtk_VarDump-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Just a regedit type interface to examine PHP data trees.

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
%pear_dir/Gtk
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

