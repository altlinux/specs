%define _unpackaged_files_terminate_build 1
%define lprev lpbzr25

Name: kde4-config-gtk
Summary: Configuration module for GTK+ appearance in KDE
Url: https://launchpad.net/kcm-gtk
License: GPLv2
Group: Graphical desktop/KDE
Version: 0.5.3
Release: alt2.%lprev
Source: http://archive.ubuntu.com/ubuntu/pool/main/k/kcm-gtk/kcm-gtk_%version.orig.tar.gz
Patch1: kcm-gtk-%version-%lprev.patch
Patch11: kcm-gtk-alt-fixes.patch
Conflicts: gtk-qt4-engine
BuildRequires: kde4libs-devel cmake gcc-c++

%description
This is a configuration module for System Settings for configuring the
widget style and fonts of GTK+ applications in KDE. It is derived from
gtk-qt-engine's configuration module.

%prep
%setup -n kcm-gtk-%version
%patch1 -p1
%patch11 -p1

%K4cmake
%K4make

%install
%K4install

%K4find_lang --with-kde kcm_gtk

%files -f kcm_gtk.lang
%_K4lib/kcm_*.so
%_K4srv/kcmgtk.desktop
%_K4iconsdir/*.png

%changelog
* Tue May  3 2011 Alexey Morozov <morozov@altlinux.org> 0.5.3-alt2.lpbzr25
- Updated Russian translations
- Updated cursor theme support ass suggested in https://bugs.launchpad.net/kcm-gtk/+bug/505988/comments/4

* Tue May  3 2011 Alexey Morozov <morozov@altlinux.org> 0.5.3-alt1.lpbzr25
- Initial build for ALT Linux (based on Ubuntu package)

