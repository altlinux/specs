%define gdk_pixbuf_moduledir  %(pkg-config --variable gdk_pixbuf_moduledir gdk-pixbuf-2.0)
%define api_ver 0.1

Name: libopenraw
Version: 0.1.0
Release: alt1

Summary: Decode camera RAW files
Group: System/Libraries
License: LGPLv3+
Url: http://libopenraw.freedesktop.org/wiki

Source: http://libopenraw.freedesktop.org/download/libopenraw-%version.tar.bz2

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

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/%name.so.*
%gdk_pixbuf_moduledir/*.so
%exclude %gdk_pixbuf_moduledir/*.la
%doc AUTHORS NEWS README TODO

%files devel
%dir %_includedir/%name-%api_ver
%_includedir/%name-%api_ver/%name
%_libdir/%name.so
%_pkgconfigdir/%name-%api_ver.pc

%files gnome
%_libdir/%{name}gnome.so.*

%files gnome-devel
%_includedir/%name-%api_ver/%name-gnome/
%_libdir/%{name}gnome.so
%_pkgconfigdir/%name-gnome-%api_ver.pc

%changelog
* Wed Jan 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- 0.1.0

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.0.9-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

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
