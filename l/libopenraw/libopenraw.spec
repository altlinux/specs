%define gdk_pixbuf_moduledir  %(pkg-config --variable gdk_pixbuf_moduledir gdk-pixbuf-2.0)

Name: libopenraw
Version: 0.0.9
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Decode camera RAW files
License: LGPLv3+
Group: System/Libraries

URL: http://libopenraw.freedesktop.org/wiki
Source: http://libopenraw.freedesktop.org/download/libopenraw-%version.tar.bz2
Patch1: libopenraw-0.0.8-fixtypo.patch

BuildRequires: boost-devel gcc-c++ libcurl-devel libgio-devel libgdk-pixbuf-devel libjpeg-devel libxml2-devel

%description
libopenraw is an ongoing project to provide a free software implementation for
camera RAW files decoding. One of the main reason is that dcraw is not suited
for easy integration into applications, and there is a need for an easy to use
API to build free software digital image processing application.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for developing
applications that use %name.

%package gnome
Summary: GUI components of libopenraw
Group: System/Libraries
Requires: %name = %version-%release

%description gnome
The %name-gnome package contains gui components of %name.

%package gnome-devel
Summary: Development files for %name-gnome
Group: Development/C
Requires: %name-gnome = %version-%release
Requires: %name-devel = %version-%release

%description gnome-devel
The %name-gnome-devel package contains libraries and header files for developing
applications that use %name-gnome.

%prep
%setup
%patch1 -p1

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/libopenraw.so.*
%gdk_pixbuf_moduledir/*.so
%exclude %gdk_pixbuf_moduledir/*.la
%doc AUTHORS NEWS README TODO

%files devel
%dir %_includedir/libopenraw-1.0
%_includedir/libopenraw-1.0/libopenraw
%_libdir/libopenraw.so
%_pkgconfigdir/libopenraw-1.0.pc

%files gnome
%_libdir/libopenrawgnome.so.*

%files gnome-devel
%_includedir/libopenraw-1.0/libopenraw-gnome
%_libdir/libopenrawgnome.so
%_pkgconfigdir/libopenraw-gnome-1.0.pc

%changelog
* Thu Dec 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0.0.9-alt1
- 0.0.9
- removed upstreamed patch2

* Thu Sep 16 2010 Victor Forsiuk <force@altlinux.org> 0.0.8-alt2
- Add patches to fix ALT #24093.

* Wed Jul 08 2009 Victor Forsyuk <force@altlinux.org> 0.0.8-alt1
- 0.0.8

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 0.0.5-alt2
- Remove obsolete ldconfig calls.

* Thu Mar 13 2008 Victor Forsyuk <force@altlinux.org> 0.0.5-alt1
- 0.0.5

* Mon Nov 26 2007 Victor Forsyuk <force@altlinux.org> 0.0.3-alt1
- 0.0.3

* Thu May 17 2007 Victor Forsyuk <force@altlinux.org> 0.0.2-alt1
- Initial build.
