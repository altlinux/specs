# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: xdg-user-dirs-gtk
Version: 0.14
Release: alt1
Summary: Gnome integration of special directories
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later
URL: https://git.gnome.org/browse/xdg-user-dirs-gtk

Requires: xdg-user-dirs

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: xdg-user-dirs

%description
Contains some integration of xdg-user-dirs with the gnome
desktop, including creating default bookmarks and detecting
locale changes.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

mv %buildroot%_sysconfdir/xdg/autostart/user-dirs-update-gtk.desktop \
   %buildroot%_sysconfdir/xdg/autostart/%name.desktop

rm -v %buildroot%_desktopdir/user-dirs-update-gtk.desktop

%find_lang %name

%files -f %name.lang
%doc NEWS AUTHORS README ChangeLog COPYING
%_sysconfdir/xdg/autostart/%name.desktop
%_bindir/xdg-user-dirs-gtk-update

%changelog
* Sat Feb 08 2025 Anton Midyukov <antohami@altlinux.org> 0.14-alt1
- New version 0.14

* Tue Aug 08 2023 Anton Midyukov <antohami@altlinux.org> 0.11-alt1
- New version 0.11
- rename user-dirs-update-gtk.desktop -> %name.desktop

* Mon Apr 13 2020 Ivan A. Melnikov <iv@altlinux.org> 0.10-alt3
- fix build with -Werror=cast-align on %%mips32

* Thu Apr 09 2020 Anton Midyukov <antohami@altlinux.org> 0.10-alt2
- Added autostart to lxqt and xfce

* Mon Mar 23 2020 Anton Midyukov <antohami@altlinux.org> 0.10-alt1
- New version 0.10 (Closes: 27155)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Aug 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt1
- initial release
