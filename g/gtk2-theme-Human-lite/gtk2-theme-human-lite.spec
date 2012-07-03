%define _unpackaged_files_terminate_build 1

# Here are some customizations to make the rest of the spec file as generalized
# as possible.
%define themename HumanLite
%define _name Human-lite
# This is an index of the theme at http://art.gnome.org
#define themeindex 1377
%define author Mykola Grechukh

Name: gtk2-theme-%_name
Summary: A theme for GTK+ applications
Version: 20100202
Release: alt2
License: %gpl2plus
Group: Graphical desktop/GNOME
#Url: http://art.gnome.org/themes/gtk2/%themeindex

Source0: GTK2-%themename.tar.bz2

BuildPreReq: rpm-build-licenses
Requires: libgtk-engine-ubuntulooks

%description
This package contains %themename theme for GTK+ applications, made by %author. Based on HumanCompact theme.

%install
mkdir -p %buildroot%_datadir/themes
bzip2 -cd %SOURCE0 | tar -C %buildroot%_datadir/themes -xf -
# Fix the directory name
mv "%buildroot%_datadir/themes/Human Lite" \
    %buildroot%_datadir/themes/%themename

%files
%dir %_datadir/themes/%themename
%dir %_datadir/themes/%themename/gtk-2.0
%_datadir/themes/%themename/gtk-2.0/gtkrc

%changelog
* Tue Feb 02 2010 Mykola Grechukh <gns@altlinux.ru> 20100202-alt2
- initial build to sisyphus
