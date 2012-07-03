%def_enable tdb
%def_disable oss
%def_enable gtk
%def_enable gtk3

%define ver_major 0.29
%define gtk_api_ver 2.0
%define gtk3_api_ver 3.0

Name: libcanberra
Version: %ver_major
Release: alt1

Summary: Portable Sound Event Library
Group: System/Libraries
License: LGPLv2+
Url: http://0pointer.de/lennart/projects/libcanberra

Source: http://0pointer.de/lennart/projects/libcanberra/%name-%version.tar.xz

%define pa_ver 0.9.11
%define gtk_ver 2.20
%define gtk3_ver 3.0.0
%define tdb_ver 1.1

Requires: sound-theme-freedesktop
Requires: libpulseaudio >= %pa_ver

BuildPreReq: libpulseaudio-devel >= %pa_ver
%{?_enable_gtk:BuildPreReq: libgtk+2-devel >= %gtk_ver}
%{?_enable_gtk3:BuildPreReq: libgtk+3-devel >= %gtk3_ver}
BuildRequires: gcc-c++ gstreamer-devel gtk-doc libalsa-devel libudev-devel
BuildRequires: libltdl-devel libvorbis-devel vala-tools
%{?_enable_tdb:BuildRequires: libtdb-devel >= %tdb_ver}

%description
A small and lightweight implementation of the XDG Sound Theme Specification
(http://0pointer.de/public/sound-theme-spec.html).

%package gtk2
Summary: Gtk+ Bindings for libcanberra
Group: System/Libraries
Provides: %name-gtk = %version-%release
Requires: %name = %version-%release

%description gtk2
Gtk+ bindings for libcanberra

%package gtk3
Summary: Gtk+3 Bindings for libcanberra
Group: System/Libraries
Provides: %name-gtk = %version-%release
Requires: %name = %version-%release

%description gtk3
Gtk+3 bindings for libcanberra

%package gnome
Summary: GNOME-specific part of libcanberra
Group: Graphical desktop/GNOME
BuildArch: noarch

%description gnome
This package provides some .desktop files needed for GNOME.

%package devel
Summary: Development files for libcanberra
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains files for libcanberra client development

%package gtk-common-devel
Summary: Development files of Gtk+ bindings for libcanberra
Group: Development/C
Requires: %name = %version-%release
Requires: %name-devel = %version-%release

%description gtk-common-devel
This package contains common header for libcanberra-gtk{2,3} client development

%package gtk2-devel
Summary: Development files for libcanberra-gtk2
Group: Development/C
Requires: %name-gtk2 = %version-%release
Requires: %name-devel = %version-%release
Requires: %name-gtk-common-devel = %version-%release

%description gtk2-devel
This package contains files for libcanberra-gtk2 client development

%package gtk3-devel
Summary: Development files for libcanberra-gtk3
Group: Development/C
Requires: %name-gtk3 = %version-%release
Requires: %name-devel = %version-%release
Requires: %name-gtk-common-devel = %version-%release

%description gtk3-devel
This package contains files for libcanberra-gtk3 client development

%package devel-doc
Summary: Development documentation for libcanberra
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains development documentation for libcanberra

%package vala
Summary: Vala Bindings for libcanberra
Group: Development/C
BuildArch: noarch
Requires: %name = %version-%release

%description vala
This package provides Vala language bindings for libcanberra and
libcanberra-gtk libraries

%prep
%setup -q

%build
%configure --disable-static \
	--enable-pulse \
	--enable-alsa \
	--enable-null \
	%{subst_enable oss} \
	%{subst_enable tdb} \
	--with-builtin=dso \
	--with-systemdsystemunitdir=%systemd_unitdir

%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install
rm -f %buildroot%_docdir/libcanberra/README


%files
%_libdir/libcanberra.so.*
%dir %_libdir/libcanberra-%ver_major
%_libdir/libcanberra-%ver_major/libcanberra-null.so
%_libdir/libcanberra-%ver_major/libcanberra-alsa.so
%_libdir/libcanberra-%ver_major/libcanberra-pulse.so
%_libdir/libcanberra-%ver_major/libcanberra-multi.so
%_libdir/libcanberra-%ver_major/libcanberra-gstreamer.so
%if_enabled oss
%_libdir/libcanberra-%ver_major/libcanberra-oss.so
%endif
# systemd files
%_bindir/canberra-boot
%systemd_unitdir/canberra-system-bootup.service
%systemd_unitdir/canberra-system-shutdown-reboot.service
%systemd_unitdir/canberra-system-shutdown.service

%doc README

%files devel
%_includedir/canberra.h
%_libdir/libcanberra.so
%_libdir/pkgconfig/libcanberra.pc

%files gnome
%_datadir/gnome/autostart/libcanberra-login-sound.desktop
%_datadir/gnome/shutdown/libcanberra-logout-sound.sh
%_datadir/gdm/autostart/LoginWindow/libcanberra-ready-sound.desktop

%files gtk-common-devel
%_includedir/canberra-gtk.h

%if_enabled gtk
%files gtk2
%{?_disable_gtk3:%_bindir/canberra-gtk-play}
%_libdir/libcanberra-gtk.so.*
%_libdir/gtk-%gtk_api_ver/modules/libcanberra-gtk-module.so

%files gtk2-devel
%_libdir/libcanberra-gtk.so
%_libdir/pkgconfig/libcanberra-gtk.pc
%endif

%if_enabled gtk3
%files gtk3
%_bindir/canberra-gtk-play
%_libdir/libcanberra-gtk3.so.*
%_libdir/gtk-%gtk3_api_ver/modules/libcanberra-gtk-module.so
%_libdir/gtk-%gtk3_api_ver/modules/libcanberra-gtk3-module.so
%_libdir/gnome-settings-daemon-3.0/gtk-modules/canberra-gtk-module.desktop

%files gtk3-devel
%_libdir/libcanberra-gtk3.so
%_libdir/pkgconfig/libcanberra-gtk3.pc
%endif

%files vala
%_datadir/vala/vapi/libcanberra-gtk.vapi
%_datadir/vala/vapi/libcanberra.vapi

%files devel-doc
%_datadir/gtk-doc/html/*

%exclude %_libdir/libcanberra-%ver_major/*.la
%{?_enable_gtk:%exclude %_libdir/gtk-%gtk_api_ver/modules/*.la}
%{?_enable_gtk3:%exclude %_libdir/gtk-%gtk3_api_ver/modules/*.la}

%changelog
* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 0.29-alt1
- 0.29

* Thu May 12 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28-alt2
- systemd files included in package

* Wed Mar 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28-alt1
- 0.28

* Thu Dec 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt2
- gtk3 support enabled

* Sun Oct 31 2010 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt1
- 0.26
- build libcanberra-gnome subpackage as noarch

* Tue Jun 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.25-alt1
- 0.25
- new -gtk{2,3}{,-devel} subpackages

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.24-alt1
- 0.24

* Fri Feb 26 2010 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt1
- 0.23

* Fri Jan 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt1
- 0.17

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt1
- 0.15

* Thu Apr 30 2009 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10
- remove obsolete ldconfig in %%post{,un}
- new devel-doc noarch subpackage

* Mon Sep 29 2008 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- adopted for Sisyphus 

* Thu Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9-1
- New version

* Thu Aug 28 2008 Lennart Poettering <lpoetter@redhat.com> 0.8-2
- Fix build-time dep on Gstreamer

* Thu Aug 28 2008 Lennart Poettering <lpoetter@redhat.com> 0.8-1
- New version

* Thu Aug 14 2008 Lennart Poettering <lpoetter@redhat.com> 0.7-1
- New version

* Mon Aug 4 2008 Lennart Poettering <lpoetter@redhat.com> 0.6-1
- New version

* Wed Jul 30 2008 Lennart Poettering <lpoetter@redhat.com> 0.5-4
- Really add versioned dependency on libpulse

* Wed Jul 30 2008 Lennart Poettering <lpoetter@redhat.com> 0.5-3
- Ship libcanberra-gtk-module.sh directly in CVS

* Wed Jul 30 2008 Lennart Poettering <lpoetter@redhat.com> 0.5-2
- Fix build

* Wed Jul 30 2008 Lennart Poettering <lpoetter@redhat.com> 0.5-1
- New version

* Mon Jul 28 2008 Lennart Poettering <lpoetter@redhat.com> 0.4-3
- Add versioned dependency on libpulse

* Sun Jul 27 2008 Lennart Poettering <lpoetter@redhat.com> 0.4-2
- Fix module name in libcanberra-gtk-module.sh

* Fri Jul 25 2008 Lennart Poettering <lpoetter@redhat.com> 0.4-1
- New version
- Install libcanberra-gtk-module.sh

* Mon Jun 16 2008 Lennart Poettering <lpoetter@redhat.com> 0.3-2
- Add dependency on sound-theme-freedesktop

* Fri Jun 13 2008 Lennart Poettering <lpoetter@redhat.com> 0.3-1
- Initial package, based on Colin Guthrie's Mandriva package

