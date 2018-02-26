%define pear_name Gtk_Styled

Name: pear-Gtk_Styled
Version: 1.0.0
Release: alt1

Summary: PHP-GTK pseudo-widgets that mimic GtkData based objects and allow the look and feel to be controlled by the programmer

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Gtk_Styled

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Gtk_Styled-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
While it is possible to control some style elements of a GtkScrollBar,
other elements cannot be controlled so easily. Items such as the images
at the begining and end (usually arrows) and the scroll bar that is
dragged to scroll the element cannot be changed. This leads to
applications that either must conform to the windowing systems look
and feel or appear incomplete. The goal of this family of PHP-GTK
classes is to provide all the same functionality as a normal scroll
bar but allow the user to have better control over the look and feel.

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
%pear_datadir/%pear_name/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

