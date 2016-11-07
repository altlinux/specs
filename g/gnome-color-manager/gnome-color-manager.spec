%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%define ver_major 3.22
%def_enable clutter
# tests require colord running and g-c-m installed
%def_disable check

Name: gnome-color-manager
Version: %ver_major.2
Release: alt1

Summary: Color profile manager for the GNOME desktop
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: http://www.gnome.org/projects/gnome-color-manager/

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Obsoletes: libcolor-glib
Requires: common-licenses gnome-session gnome-filesystem

BuildPreReq: gnome-common rpm-build-gnome
BuildPreReq: rpm-build-licenses

# From configure.ac
%define gio_ver 2.31.10
%define clutter_ver 1.12
%define gtk_ver 3.0
%define vte_ver 0.37.1
%define notify_ver 0.7.3
%define colord_ver 0.1.24
%define lcms_ver 2.2

BuildRequires: gcc-c++ intltool gtk-doc yelp-tools itstool libappstream-glib-devel
BuildRequires: docbook-utils xsltproc
BuildPreReq: libgio-devel >= %gio_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libvte3-devel >= %vte_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildPreReq: colord-devel >= %colord_ver
BuildPreReq: libcolord-gtk-devel >= %colord_ver
BuildRequires: libgnome-desktop3-devel libexif-devel libexiv2-devel libcanberra-gtk3-devel
BuildRequires: libtiff-devel liblcms2-devel >= %lcms_ver libXrandr-devel
%{?_enable_clutter:BuildRequires: libclutter-devel >= %clutter_ver libclutter-gtk3-devel}
%{?_enable_check:BuildRequires: /proc xvfb-run}

%description
gnome-color-manager is a session program that makes it easy to manage,
install and generate color profiles in the GNOME desktop.

This project has the following features:

* Setting output gamma tables (with local brightness and adjustments) to any
  Xrandr output (falling back to the per-screen methods for drivers that do not
  yet support Xrandr 1.3).

* Setting of settings at session start, and when monitors are hotplugged.

* Easy install of vendor supplied ICC or ICM files, just by double clicking
  on the file.

* Easy display calibration using an external calibration device, and scanner
  calibration using a inexpensive IT 8.7 target. For calibration, the ArgyllCMS
  package is required.

* Integration X11 by setting the per-screen and per-output _ICC_PROFILE atom,
  which makes applications such as the GIMP use a color managed output.

* Easy to use DBus interface for applications to query what ICC profiles should
  be used for a specific device. This is session activated and is only started
  when it is needed, and quits after a small period of idleness.

%prep
%setup

%build
%configure \
    --disable-static \
    --enable-tests \
    --disable-schemas-compile \
    %{subst_enable clutter}

%make_build

%install
%makeinstall_std

# The license
ln -sf %_licensedir/GPL-2 COPYING

%find_lang --with-gnome %name

%check
%{?_enable_check:xvfb-run %make check}

%files -f %name.lang
%_bindir/gcm-calibrate
%_bindir/gcm-import
%_bindir/gcm-inspect
%_bindir/gcm-picker
%_bindir/gcm-viewer
%_libexecdir/gcm-helper-exiv
%_datadir/%name/
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/*x*/mimetypes/*.png
%_iconsdir/hicolor/scalable/mimetypes/*.svg
%_man1dir/*
%_datadir/appdata/org.gnome.ColorProfileViewer.appdata.xml
%doc --no-dereference COPYING
%doc README NEWS AUTHORS

%changelog
* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt2
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.16.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Sun Oct 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Jul 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Sun Jun 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt2
- rebuilt against libcolord.so.2

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Fri Apr 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt2
- rebuilt against libexiv2.so.13

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Sep 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1
- enabled clutter suport

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sat Feb 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt3
- rebuilt against libcolord.so.2

* Thu Jan 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt2
- rebuilt against libexiv2.so.12

* Fri Jan 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0
- clutter support temporarily disabled (no more mx/mash for new clutter)

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Mar 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Mon Jan 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- rebuilt against libexiv2.so.11

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Fri Mar 04 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.90-alt1
- 2.91.90

* Sun Oct 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Mon Sep 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.91-alt1
- 2.31.91

* Wed Jun 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0
- updated buildreqs
- updated "lcms" patch

* Thu Mar 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt2
- rebuild against new libgnome-desktop

* Mon Mar 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4
- updated buildreqs

* Mon Feb 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3
- Fixed build against lcms. Tnx to Valery Inozemtsev (shrek@)

* Mon Dec 07 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.1-alt1
- first build for Sisyphus

