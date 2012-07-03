%define _name nautilus2
%define ver_major 3.4
%define api_ver 3.0

%def_enable exempi
%def_disable packagekit
%def_enable tracker
%def_enable introspection
%def_enable selinux

Name: nautilus
Version: %ver_major.2
Release: alt1

Summary: Nautilus is a network user environment
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Patch11: %name-rtl-fix.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=519743 
Patch17: %name-filetype-symlink-fix.patch

# (fc) 2.22.2-2mdv auto-unmount ejected medias when mount points are in fstab (Mdv bug #39540) 
Patch35: %name-2.22.1-umountfstab.patch

Obsoletes: %_name <= 2.14.1
Provides: %_name = %version-%release
Obsoletes: gnome-volume-manager
Provides: gnome-volume-manager

%define pkgconfig_ver 0.8
%define icon_theme_ver 2.10.0
%define desktop_file_utils_ver 0.8

# From configure.in
%define glib_ver 2.31.9
%define desktop_ver 3.3.3
%define pango_ver 1.28.3
%define gtk_ver 3.3.18
%define libxml2_ver 2.4.7
%define exif_ver 0.5.12
%define exempi_ver 2.1.0
%define gir_ver 0.10.2
%define notify_ver 0.7.0
%define tracker_ver 0.12

PreReq: lib%name = %version-%release
PreReq: gnome-icon-theme >= %icon_theme_ver

Requires: shared-mime-info
Requires: common-licenses
Requires: gvfs >= 1.9.1

BuildPreReq: pkgconfig >= %pkgconfig_ver
BuildPreReq: desktop-file-utils >= %desktop_file_utils_ver
BuildPreReq: rpm-build-gnome rpm-build-licenses
# for %%check
BuildPreReq: xvfb-run dbus-tools-gui /proc

# From configure.in
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgnome-desktop3-devel >= %desktop_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: gsettings-desktop-schemas-devel
BuildPreReq: libgail3-devel
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: intltool >= 0.40.1
BuildPreReq: libexif-devel >= %exif_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildRequires: libX11-devel xorg-xproto-devel
BuildRequires: docbook-utils gtk-doc
%{?_enable_exempi:BuildPreReq: libexempi-devel >= %exempi_ver}
%{?_enable_tracker:BuildPreReq: tracker-devel >= %tracker_ver}
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}
%{?_enable_selinux:BuildRequires: libselinux-devel}

%description
Nautilus integrates access to files, applications, media, Internet-based
resources and the Web.  Nautilus delivers a dynamic and rich user
experience.  Nautilus is an free software project developed under the
GNU General Public License and is a core component of the GNOME desktop
project.

%package -n lib%name
Summary: Shared libraries needed to run Nautilus
Group: System/Libraries

%description -n lib%name
This package contains shared libraries needed to run Nautilus and its
components.

%package -n lib%name-devel
Summary: Libraries and include files for developing Nautilus components
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides the necessary development libraries and include
files to allow you to develop Nautilus components.

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: lib%name-devel < %version-%release
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for the %name.

%package -n lib%name-gir
Summary: GObject introspection data for the nautilus-extension library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the nautilus-extension library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the nautilus-extension library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the nautilus-extension library


%define _bonobo_servers_dir %_libdir/bonobo/servers
%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -q
%patch11 -p1 -b .rtl-fix
%patch17 -p0 -b .symlink
#%patch35 -p1 -b .umountfstab

rm -f data/*.desktop

# make check using xvfb-run
subst 's@\.\/@xvfb-run -a ./@' eel/check-eel src/check-nautilus

%build
%autoreconf
%configure \
    --disable-update-mimedb \
    --disable-schemas-compile \
    %{subst_enable packagekit}

%make_build

%if 0
%check
for d in eel src; do
pushd $d
make check
popd
done
%endif

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot%_libdir/%name-%api_ver/components
bzip2 -9fk NEWS

# The license
ln -sf %_licensedir/LGPL-2 COPYING

%find_lang %name

%files -f %name.lang
%_bindir/*
%_libexecdir/nautilus-convert-metadata
%dir %_libdir/%name-%api_ver
%dir %_libdir/%name-%api_ver/components
%_datadir/mime/packages/nautilus.xml
%_datadir/applications/*.desktop
%_sysconfdir/xdg/autostart/nautilus-autostart.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/dbus-1/services/org.gnome.Nautilus.service
%_datadir/dbus-1/services/org.freedesktop.FileManager1.service
# gsettings schemas
%config %_datadir/glib-2.0/schemas/org.gnome.nautilus.gschema.xml
%_datadir/GConf/gsettings/nautilus.convert
# docs
%doc --no-dereference COPYING
%doc AUTHORS MAINTAINERS NEWS.bz2 README THANKS TODO
%_man1dir/*

%files -n lib%name
%_libdir/libnautilus-extension.so.*
%dir %_libdir/%name/extensions-%api_ver
%_libdir/%name/extensions-%api_ver/libnautilus-sendto.so
%exclude %_libdir/%name/extensions-3.0/libnautilus-sendto.la

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_gtk_docdir/*
%doc docs/*.{txt,pdf,sxw,html} README.commits

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/*

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*
%endif


%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- tracker support using tracker-sparql-0.12

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed May 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Dec 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.2.1-alt1
- 2.32.2.1

* Fri Dec 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Sat Nov 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Mon Sep 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.92-alt1
- 2.31.92

* Mon Aug 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.90-alt1
- 2.31.90

* Sun Aug 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.5-alt1
- 2.31.5
- introspection support

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Wed Mar 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92.1-alt1
- 2.29.92.1

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92
- removed upstreamed dynamic-search patch

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.2-alt1
- 2.29.2

* Mon Jan 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt2
- updated buildreqs

* Tue Dec 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt1
- 2.28.4

* Mon Nov 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2
- upstreamed patches removed
- %%check section

* Wed Nov 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1
- updated dynamic-search.patch (fedora)
- patch from upstream that fixes unsuccessful connection to tracker daemon 0.7 series

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Fri Apr 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Mar 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.93-alt1
- 2.25.93

* Wed Feb 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.4-alt1
- 2.25.4
- removed upstreamed patches

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.3-alt1
- 2.25.3
- updated buildreqs

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts
- patches from bugzilla.gnome.org (15-19)
- disabled kdedesktop.patch (28)

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)
- update patches for bugs:
  + Gnome: #171655, #519743
  + MDK: #4844, #39540
- add patch for selinux, but don't apply
- build devel-doc as noarch

* Sat Jul 19 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.5.1-alt1
- new version

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.4-alt1
- new version (2.22.4)

* Fri Jun 06 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt2
- rebuild with versionized libeel

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version (2.22.3)
- drop patch12 (hide white screen)
- Enables the classic Nautilus behavior, where all windows are browsers(#15847)

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)
- moved settings from post-script to patch1

* Wed Apr 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt2
- build for Sisyphus
- remove BuildPreReq gnome-vfs-devel
- Remove buildreqs for beagle and tracker , as they are not necessary with
  the dynamic work (patch10 from fedora)

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)
- enabled support beagle, tracker, exempi

* Sun Mar 09 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- new version (2.21.92)

* Thu Sep 20 2007 Igor Zubkov <icesik@altlinux.org> 2.20.0-alt1
- 2.18.3 -> 2.20.0

* Fri Jul 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt1
- new version (2.18.3)

* Mon May 07 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.1-alt0.1
- 2.18.1 (NMU)

* Thu Mar 15 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.0-alt0.1
- 2.18.0 (NMU)

* Tue Feb 27 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.3-alt0.1
- 2.16.3 (NMU)

* Tue Sep 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- added COPYING symlink to nautilus subpackage.
- removed explicit deps of -devel subpackage, as they are now handled by
  pkgconfig.
- removed ALL_LINGUAS workaround.

* Fri Sep 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92.1-alt2
- re-fixed bug #6457

* Mon Aug 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92.1-alt1
- new version (2.15.92.1)

* Sun Jul 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt5
- fixed bug #6457; also removed unused directories from the package.

* Sun Jun 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt4
- new version
- fixed ALL_LINGUAS initialization.
- should also build on x86_64.

* Mon May 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt3
- fixed a typo that resulted in a dependency on libnautilus2 (no such
  package).

* Mon May 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt2
- Renamed the package from nautilus2 to nautilus.

* Thu Apr 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version (2.14.1)
- new file permissions interface patch (see GNOME Bug 44767).

* Sun Apr 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version (2.14.0)
- Added a patch for file/folder permissions UI.

* Wed Feb 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.91-alt1
- new version
- updated buildreqs, cleaned up spec
- introduced beagle and tracker switches (disabled, both do-nothing at the moment)
- removed Debian-style menus

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version
- updated dependencies

* Tue Oct 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version
- Updated dependencies from configure.in and .pc files.

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed more excess buildreqs.

* Sun Sep 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92
- Removed excess buildreqs.

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1.1
- rebuild against libexif.so.12.

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Tue Mar 01 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92

* Thu Feb 10 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1
- 2.9.91

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90-alt1
- 2.9.90.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Tue Oct 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Fri Jul 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt2.1
- enable to switch to spatial mode in preferences dialog. Thanks vk@.

* Sun Jul 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt2
- fix starthere URL (close #4575).

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Sat Jun 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Mon Apr 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Fri Mar 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.91-alt1
- 2.5.91

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Mon Feb 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.8-alt1
- 2.5.8

* Wed Feb 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.7-alt1
- 2.5.7

* Sat Jan 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt1
- 2.5.6

* Thu Jan 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Tue Dec 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt2
- do not package .la files.

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Sep 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Thu Sep 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.9-alt1
- 2.3.9

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.8-alt1
- 2.3.8

* Mon Jul 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.7-alt1
- 2.3.7

* Sat Jun 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Tue Jun 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Wed Jun 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Wed Jun 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Tue May 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Tue Apr 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3.1-alt1
- 2.2.3.1

* Tue Apr 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Feb 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Jan 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.2-alt1
- 2.2.0.2

* Sun Jan 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt3
- subpackages with useless old themes removed.

* Fri Jan 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt2
- added missing /etc/X11/starthere/*.desktop to work "start here".

* Thu Jan 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.91-alt1
- 2.1.91

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Mon Dec 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Sat Nov 30 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt2
- Fixed dependence on gnome-icone-theme (#1645)
- Fixed *.server for hardware component

* Tue Nov 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3
- Obsoletes %name-music-view, %name-content-loser,
  %name-sample-content-view, %name-sidebar-loser
- default-schemas.patch removed, %%gcon2_set macro used.

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Thu Oct 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1.1
- %name-themes subpackage renamed to %name-themes-default.
- Removed dependence on Nautilus for default theme.
- Fixed %%post/%%postun for sidebar component.

* Sat Oct 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Wed Oct 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt1.2
- Nautilus themes splitted in separate packages.
- %%post/%%postun scripts for components.

* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.6-alt1.1
- change from '>' to '>=' in dependencies on scrollkeeper.
- move pkgconfig >= '' from requires to buildrequires.

* Sun Sep 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt1
- First build for Sisyphus.
