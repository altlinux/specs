%define _name nice
%def_disable static
%def_disable gtk_doc

Name: libnice
Version: 0.1.1
Release: alt1

Summary: Connectivity Establishment standard (ICE) library
Group: System/Libraries
License: LGPLv2+/MPL
URL: http://nice.freedesktop.org

Source: http://nice.freedesktop.org/releases/%name-%version.tar.gz

BuildRequires: glib2-devel gtk-doc gst-plugins-devel libgupnp-igd-devel

%description
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

This package contains files needed to develop applications using Nice

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

This package contains development documentation for %name.

%package devel-static
Summary: Static library for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

This package contains a statically-linked variant of %name

%package -n gst-plugins-nice
Summary: UDP connectivity establishment plugin for Gstreamer based on libnice
Group: System/Libraries
Requires: %name = %version-%release

%description -n gst-plugins-nice
Nice is an implementation of the IETF's draft Interactice Connectivity
Establishment standard (ICE). It provides GLib-based library, libnice.

This package provides Interactive UDP connectivity establishment plugin
for Gstreamer

%prep
%setup -q

%build
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable static}

%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS README

%files devel
%_libdir/*.so
%_pkgconfigdir/*
%_includedir/*

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files -n gst-plugins-nice
%_libdir/gstreamer-*/libgstnice.so

%exclude %_libdir/gstreamer-*/*.la

# don't package tools
%exclude %_bindir/stun*

%changelog
* Tue Nov 08 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- 0.1.1

* Wed Jun 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- 0.1.0
- dropped obsolete libnice-Compatibility-with-OC2007-R2.patch

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.0.13-alt2
- rebuild for debuginfo

* Thu Nov 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.0.13-alt1
- 0.0.13

* Tue May 25 2010 Yuri N. Sedunov <aris@altlinux.org> 0.0.12-alt1
- 0.0.12
- applied patch for compatibility with OC2007-R2 (shaba@)

* Wed Aug 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.9-alt1
- 0.0.9

* Mon Apr 27 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.6-alt1
- 0.0.6

* Sun Jan 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.0.4-alt1
- 0.0.4

* Fri Nov 28 2008 Yuri N. Sedunov <aris@altlinux.org> 0.0.3-alt1
- first build for Sisyphus

