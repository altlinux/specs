%define ver_major 3.4
%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: cheese
Version: %ver_major.2
Release: alt1

Summary: Cheese is a Photobooth-inspired application for taking pictures and videos
License: GPL
Group: Video
Url: http://www.gnome.org/projects/cheese

Source: ftp://ftp.gnome.org/pub/gnome/sources/cheese/%ver_major/%name-%version.tar.xz

%define glib_ver 2.28.0
%define gtk_ver 3.2.0
%define desktop_ver 3.0.0
%define gst_ver 0.10.32
%define vala_ver 0.14.0

Requires: lib%name = %version-%release
Requires: gnome-video-effects
# camerabin used for taking photos and videos
Requires: gst-plugins-bad
# matroska (webmmux)
Requires: gst-plugins-good

BuildPreReq: gnome-doc-utils gnome-common intltool yelp-tools itstool
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgnome-desktop3-devel >= %desktop_ver
BuildPreReq: gst-plugins-devel >= %gst_ver
BuildRequires: libgnome-menus-devel libgnomekbd-devel
BuildRequires: librsvg-devel libgee-devel libcanberra-gtk3-devel
BuildRequires: libdbus-devel libdbus-glib-devel libgudev-devel
BuildRequires: libX11-devel libXtst-devel libXext-devel
BuildRequires: libclutter-devel libclutter-gst-devel libclutter-gtk3-devel libmx-devel
BuildRequires: gnome-doc-utils-xslt docbook-dtds gtk-doc
BuildRequires: gnome-video-effects-devel gsettings-desktop-schemas-devel
BuildRequires: vala-tools >= %vala_ver
%{?_enable_introspection:BuildRequires: libgdk-pixbuf-gir-devel libclutter-gir-devel gstreamer-gir-devel}

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
%setup -q

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--disable-schemas-compile \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/cheese
%_datadir/applications/cheese.desktop
%_datadir/cheese/
%_datadir/icons/hicolor/*/*/*.*
%config %_datadir/glib-2.0/schemas/*
%_man1dir/%name.1.*
%doc AUTHORS NEWS README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Cheese-3.0.typelib

%files -n lib%name-gir-devel
%_girdir/Cheese-3.0.gir
%endif

%changelog
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


