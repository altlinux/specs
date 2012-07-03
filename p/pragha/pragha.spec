Name: pragha
Version: 1.0.1
Release: alt1
Summary: Pragha is a "Fork" of consonance Music manager
License: GPLv3
Group: Sound
Url: http://pragha.wikispaces.com/
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar

BuildRequires: gst-plugins-devel libcddb-devel libcdio-devel libclastfm-devel
BuildRequires: libdbus-glib-devel libexo-devel libglyr-devel
BuildRequires: libkeybinder-devel libnotify-devel libtag-devel xfce4-dev-tools

%description
Pragha is a reproducer and administrator of music for GNU/Linux, based
on Gtk, sqlite, and completely written in C, constructed to be fast,
light, and simultaneously complete without obstructing the daily work.

%prep
%setup

%build
. autogen.sh
LDFLAGS="$LDFLAGS -ldbus-glib-1" ; export LDFLAGS
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc ChangeLog FAQ NEWS
%exclude %_datadir/%name/doc
%_bindir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/128x128/apps/pragha.png
%_man1dir/%name.1.gz
%_pixmapsdir/%name

%changelog
* Fri Apr 20 2012 Egor Glukhov <kaman@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Aug 21 2011 Egor Glukhov <kaman@altlinux.org> 0.8.9-alt1
- 0.8.9

* Tue Jun 07 2011 Egor Glukhov <kaman@altlinux.org> 0.8.6-alt2
- Fixed build

* Thu Mar 24 2011 Egor Glukhov <kaman@altlinux.org> 0.8.6-alt1
- 0.8.6

* Sun Aug 08 2010 Egor Glukhov <kaman@altlinux.org> 0.8.0.2-alt1
- Initial build for Sisyphus
