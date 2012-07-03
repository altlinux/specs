%define api_ver 1.0
%def_enable introspection

Name: clutter-gst
Version: 1.5.6
Release: alt1

Summary: Library integrating clutter with GStreamer
License: LGPL v2+
Group: System/Libraries
Url: http://www.clutter-project.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.xz

BuildRequires: gst-plugins-devel gtk-doc libclutter-devel libgtk+2-devel
# for gstreamer-basevideo
BuildRequires: gst-plugins-bad-devel
%{?_enable_introspection:BuildRequires: libclutter-gir-devel gst-plugins-gir-devel}

%description
Library integrating clutter with GStreamer

%package -n lib%name
Summary: Library integrating clutter with GStreamer
Group: System/Libraries

%description -n lib%name
Library integrating clutter with GStreamer

%package -n lib%name-devel
Summary: Header files for clutter-gst library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files for clutter-gst library

%package -n lib%name-gir
Summary: GObject introspection data for the Clutter-Gst
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Clutter-Gst library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Clutter-Gst
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Clutter-Gst library.

%prep
%setup -q

%build
#%%autoreconf
%configure \
	--enable-gtk-doc \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files -n lib%name
%_libdir/libclutter-gst-*.so.*
%_libdir/gstreamer-0.10/libgstclutter.so
%exclude %_libdir/gstreamer-0.10/libgstclutter.la

%files -n lib%name-devel
%_includedir/clutter-*
%_libdir/libclutter-gst-*.so
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/ClutterGst-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/ClutterGst-%api_ver.gir
%endif


%changelog
* Fri May 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.5.6-alt1
- 1.5.6

* Tue Mar 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Wed Jan 18 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.6-alt1
- 1.4.6

* Thu Jan 12 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt2
- introspection enabled

* Mon Oct 03 2011 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Mon Oct 03 2011 Yuri N. Sedunov <aris@altlinux.org> 1.3.14-alt2
- updated from upstream git (really this is 1.4.0 release)

* Tue Sep 13 2011 Yuri N. Sedunov <aris@altlinux.org> 1.3.14-alt1
- 1.3.14

* Wed Feb 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Tue Aug 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Fri Nov 28 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)

* Tue May 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Fri Jan 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- new version 0.4.0 (with rpmrb script)

* Sat Jul 28 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

