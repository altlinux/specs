%define _unpackaged_files_terminate_build 1

# Here are some customizations to make the rest of the spec file as generalized
# as possible.
%define themename ClearlooksCompact
%define _name clearlooks-compact
# This is an index of the theme at http://art.gnome.org
%define themeindex 1377
%define author Martin Ankerl

Name: gtk2-theme-%_name
Summary: A theme for GTK+ applications
Version: 2007.11.06
Release: alt1
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: http://art.gnome.org/themes/gtk2/%themeindex

Packager: Alexey Rusakov <ktirf@altlinux.org>
Source0: http://art.gnome.org/download/themes/gtk2/%themeindex/GTK2-%themename.tar.bz2

BuildPreReq: rpm-build-licenses
Requires: libgtk-engine-clearlooks

%description
This package contains %themename theme for GTK+ applications, made by %author.

%install
mkdir -p %buildroot%_datadir/themes
bzip2 -cd %SOURCE0 | tar -C %buildroot%_datadir/themes -xf -
# Fix the directory name
mv "%buildroot%_datadir/themes/Clearlooks Compact" \
    %buildroot%_datadir/themes/%themename

%files
%dir %_datadir/themes/%themename
%dir %_datadir/themes/%themename/gtk-2.0
%_datadir/themes/%themename/gtk-2.0/gtkrc

%changelog
* Tue Nov 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2007.11.06-alt1
- Initial Sisyphus version.

