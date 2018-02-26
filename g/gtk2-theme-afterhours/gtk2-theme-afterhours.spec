%define _unpackaged_files_terminate_build 1

# Here are some customizations to make the rest of the spec file as generalized
# as possible.
%define themename Afterhours
%define _name afterhours
# This is an index of the theme at http://art.gnome.org
%define themeindex 1331
%define author Jean-Paul Bizet

Name: gtk2-theme-%_name
Summary: A theme for GTK+ applications
Version: 2007.05.06
Release: alt1
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org/themes/gtk2/%themeindex

Packager: Alexey Rusakov <ktirf@altlinux.org>
Source0: http://art.gnome.org/download/themes/gtk2/%themeindex/GTK2-%themename.tar.gz

# FIXME: Should be libgtk-engine-pixmap, but this engine is packed into
# libgtk+2, and libgtk+2 doesn't provide such a symbol.
Requires: libgtk+2

%description
This package contains %themename theme for GTK+ applications, made by %author.

%install
mkdir -p %buildroot%_datadir/themes
gzip -cd %SOURCE0 | tar -C %buildroot%_datadir/themes -xf -

%files
%dir %_datadir/themes/%themename
%dir %_datadir/themes/%themename/gtk-2.0
%_datadir/themes/%themename/gtk-2.0/gtkrc
%_datadir/themes/%themename/gtk-2.0/*.png

%changelog
* Fri Jun 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2007.05.06-alt1
- Initial Sisyphus version.

