%def_disable snapshot
%define _unpackaged_files_terminate_build 1

%define ver_major 43
%define beta %nil
%define api_ver 3.0
%define xdg_name org.gnome.Cheese
%define gst_api_ver 1.0
%define _libexecdir %_prefix/libexec

%def_enable gtk_doc
%def_enable man
%def_enable introspection
%def_disable check

Name: cheese
Version: %ver_major.0
Release: alt1%beta

Summary: Cheese is a Photobooth-inspired application for taking pictures and videos
License: GPL-2.0
Group: Video
Url: https://wiki.gnome.org/Apps/Cheese

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/cheese/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.40.0
%define gtk_ver 3.14.0
%define desktop_ver 3.0.0
%define gst_ver 1.4.0
%define vala_ver 0.18.0
%define clutter_ver 1.13.2
%define clutter_gst_ver 3.0.16

Requires: lib%name = %version-%release
Requires: gnome-video-effects
Requires: gst-plugins-base%gst_api_ver
# camerabin used for taking photos and videos
Requires: gst-plugins-bad%gst_api_ver
# matroska (webmmux), vp8enc
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson vala-tools >= %vala_ver
BuildRequires: yelp-tools desktop-file-utils libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgnome-desktop3-devel >= %desktop_ver
BuildRequires: libdbus-devel
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_ver
BuildRequires: gst-plugins-bad%gst_api_ver-devel >= %gst_ver
BuildRequires: gstreamer%gst_api_ver-utils >= %gst_ver
BuildRequires: gst-plugins-good%gst_api_ver >= %gst_ver
BuildRequires: libclutter-devel >= %clutter_ver
BuildRequires: libclutter-gst3.0-devel >= %clutter_gst_ver
BuildRequires: librsvg-devel libcanberra-gtk3-devel libcanberra-vala
BuildRequires: libgudev-devel libclutter-gtk3-devel
BuildRequires: libX11-devel libXtst-devel libXext-devel
BuildRequires: gnome-video-effects-devel gsettings-desktop-schemas-devel
#BuildRequires: nautilus-sendto-devel
BuildRequires: libappstream-glib-devel
%{?_enable_introspection:BuildRequires: libgdk-pixbuf-gir-devel libcogl-gir-devel libclutter-gir-devel libgstreamer%gst_api_ver-gir-devel}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: /proc xvfb-run dbus-tools-gui}

%description
Cheese is a Photobooth-inspired GNOME application for taking pictures
and videos from a webcam. It also includes fancy graphical effects
based on the gstreamer-backend.

%package -n lib%name
Summary: Cheese libraries
Group: System/Libraries

%description -n lib%name
Cheese is a Photobooth-inspired GNOME application for taking pictures
and videos from a webcam. It also includes fancy graphical effects
based on the gstreamer-backend. This package contains Cheese libraries.

%package -n lib%name-devel
Summary: Cheese development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains files necessary to develop applications that use
Cheese libraries.

%package -n lib%name-devel-doc
Summary: Cheese development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
This package contains documentation necessary to develop applications
that use Cheese libraries.

%package -n lib%name-gir
Summary: GObject introspection data for the Cheese
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Cheese library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Cheese
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Cheese library.


%prep
%setup -n %name-%version%beta

%build
%meson \
	%{?_disable_gtk_doc:-Dgtk_doc=false} \
	%{?_disable_man:-Dman=false}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/icons/hicolor/*/*/*.*
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/*
%{?_enable_man:%_man1dir/%name.1.*}
%doc AUTHORS NEWS README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Cheese-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Cheese-%api_ver.gir
%endif

%changelog
* Tue Dec 13 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Thu Sep 08 2022 Yuri N. Sedunov <aris@altlinux.org> 43-alt0.1.alpha
- 43.alpha

* Mon Nov 15 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Mon Sep 20 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Tue Apr 13 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt2
- updated to 3.38.0-32-gdf2c5f2c

* Tue Sep 15 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Tue Mar 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt2.1
- fixed typo in meson options

* Fri Feb 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt2
- rebuilt against libgnome-desktop-so.19

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0 (ported to Meson build system)

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt2
- fixed %%files section

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Sat Nov 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt2
- added gst-libav to reqs

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Sat Jul 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Jul 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Mar 10 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.91.1-alt1
- 2.91.91.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt2
- 2.30.1

* Sun Apr 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- updated buildreqs

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Wed Feb 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90
- new libcheese-devel-doc noarch subpackage

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5
- new libcheese{,-devel} subpackages

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0
- updated buildreqs

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Tue Aug 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Sun Mar 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Fri Nov 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Fri Jul 04 2008 Igor Zubkov <icesik@altlinux.org> 2.22.3-alt1
- 2.22.2 -> 2.22.3

* Tue May 27 2008 Igor Zubkov <icesik@altlinux.org> 2.22.2-alt1
- 2.22.1 -> 2.22.2

* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 2.22.1-alt2
- exec %%update_menus after install and %%clean_menus after uninstall

* Thu Apr 24 2008 Igor Zubkov <icesik@altlinux.org> 2.22.1-alt1
- 2.22.0 -> 2.22.1

* Thu Apr 24 2008 Igor Zubkov <icesik@altlinux.org> 2.22.0-alt2
- fix build ob x86_64

* Thu Apr 03 2008 Igor Zubkov <icesik@altlinux.org> 2.22.0-alt1
- build for Sisyphus


