Name: xdg-user-dirs-gtk
Version: 0.8
Release: alt1
Summary: Gnome integration of special directories
Group: Graphical desktop/GNOME
License: GPLv2+
URL: http://freedesktop.org/wiki/Software/xdg-user-dirs
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: xdg-user-dirs

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: intltool libgtk+2-devel xdg-user-dirs

%description
Contains some integration of xdg-user-dirs with the gnome
desktop, including creating default bookmarks and detecting
locale changes.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure
%make

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc NEWS AUTHORS README
%_sysconfdir/xdg/autostart/user-dirs-update-gtk.desktop
%_bindir/*

%changelog
* Mon Aug 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt1
- initial release

