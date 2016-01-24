%def_disable libxfce4ui

Name: pragha
Version: 1.3.3
Release: alt2

Summary: Pragha is a "Fork" of consonance Music manager
License: GPLv3
Group: Sound
Url: http://pragha.wikispaces.com/

Source: %name-%version.tar.gz
# adapt to newer keybinder
Patch: pragha-1.3.3-alt-configure.patch

%define gtk_ver 3.14

Requires: gst-plugins-base1.0
Requires: gst-plugins-good1.0

BuildRequires: libcddb-devel libcdio-devel libcdio-paranoia-devel libclastfm-devel
BuildRequires: libexo-devel libglyr-devel
BuildRequires: libkeybinder-devel libnotify-devel libtag-devel
BuildPreReq: gstreamer1.0-devel gst-plugins1.0-devel libgtk+3-devel >= %gtk_ver libpeas-devel
BuildPreReq:  libtotem-pl-parser-devel
BuildPreReq: libgudev-devel libsoup-devel libgrilo-devel libmtp-devel
# works only rygel-2.2
#BuildPreReq: rygel-devel
# requires for autogen.sh
BuildRequires: xfce4-dev-tools
%{?_enable_libxfce4ui:BuildRequires: libxfce4ui-devel}

%description
Pragha is a reproducer and administrator of music for GNU/Linux, based
on Gtk, sqlite, and completely written in C, constructed to be fast,
light, and simultaneously complete without obstructing the daily work.

%prep
%setup
%patch

%build
. autogen.sh
%configure \
	%{subst_enable libxfce4ui}
%make_build V=1

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_datadir/appdata/*
%_bindir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/pragha.png
%_man1dir/%name.1.*
%_pixmapsdir/%name
%_libdir/%name
%doc ChangeLog FAQ NEWS README


%changelog
* Sun Jan 24 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt2
- fixed files list

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3.2.2-alt2
- rebuilt against libgrilo-0.2.so.10

* Sun Aug 09 2015 Yuri N. Sedunov <aris@altlinux.org> 1.3.2.2-alt1
- 1.3.2.2 release
- updated {build,}reqs
- disabled xfce integration to avoid using GTK+2 and GTK+3 in the same process.

* Sat Sep 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt2.git20140727
- rebuilt without rygel support, not ready for 2.4

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140727
- Version 1.3.1

* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Disabled -Werror flag

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
