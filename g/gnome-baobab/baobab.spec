%define _unpackaged_files_terminate_build 1
%define appname baobab

Name: gnome-baobab
Version: 49.1
Release: alt1
Summary: Disk Usage Analyzer
License: GPL-2.0-or-later
Group: System/Libraries
Url: https://apps.gnome.org/Baobab/
Vcs: https://gitlab.gnome.org/GNOME/baobab

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
BuildRequires: meson >= 0.50.0
BuildRequires: pkgconfig
BuildRequires: vala >= 0.38.0.11
BuildRequires: yelp-tools
BuildRequires: pkgconfig(gio-2.0) 
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gtk4) >= 4.4.0
BuildRequires: pkgconfig(libadwaita-1)

Requires: udisks2 cryptsetup
Requires: gnome-icon-theme-symbolic

%description
Disk Usage Analyzer is a graphical, menu-driven application to analyse
disk usage in any GNOME environment. Disk Usage Analyzer can easily
scan either the whole filesystem tree, or a specific user-requested
directory branch (local or remote).

It also auto-detects in real-time any changes made to your home
directory as far as any mounted/unmounted device. Disk Usage Analyzer
also provides a full graphical treemap window for each selected folder.

%prep
%setup
%autopatch -p1 

%build
export CFLAGS="%optflags"
%meson
%meson_build

%install
%meson_install
%find_lang %appname --with-gnome

%check
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/org.gnome.baobab.metainfo.xml
desktop-file-validate %buildroot%_datadir/applications/org.gnome.baobab.desktop

%files
%doc AUTHORS NEWS README.md COPYING
%doc %_datadir/help/C/%appname/
%_bindir/%appname
%_datadir/applications/org.gnome.%appname.desktop
%_datadir/dbus-1/services/org.gnome.%appname.service
%_datadir/glib-2.0/schemas/org.gnome.%appname.gschema.xml
%_datadir/icons/hicolor/scalable/apps/org.gnome.baobab*.svg
%_datadir/icons/hicolor/symbolic/apps/org.gnome.%appname-symbolic.svg
%_datadir/metainfo/org.gnome.%appname.metainfo.xml
%_man1dir/*.1*
%_datadir/locale/*/LC_MESSAGES/%appname.mo
%_datadir/help/*/%appname/

%changelog
* Tue Mar 03 2026 Pavel Shilov <zerospirit@altlinux.org> 49.1-alt1
- initial build for Sisyphus
