Name: lasem
Version: 0.3.0
Release: alt1
Summary: C/Gobject based SVG/Mathml renderer and editor - tools

Group: Graphics
License: GPL
Url: http://blogs.gnome.org/emmanuel/category/lasem

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: glib2-devel libgio-devel libgtk+2-devel libxml2-devel libpango-devel libcairo-devel autogen intltool flex libgtk+2-gir-devel
PreReq: lib%name = %version-%release

%description
Lasem aims to be a C/Gobject based SVG/Mathml renderer and editor,
supporting CSS style sheets. It uses cairo and pango as it's rendering
abstraction layer, and then support numerous output formats: xlib, PNG,
SVG, PDF, PS, EPS...

%package -n lib%name
Summary: C/Gobject based SVG/Mathml renderer and editor - library
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: C/Gobject based SVG/Mathml renderer and editor - development files
Group: Development/C
PreReq: lib%name = %version-%release

%description -n lib%name-devel
%summary

%package -n lib%name-gir
Summary: GObject introspection data for the lasem library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
%summary

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the lasem library
Group: System/Libraries
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
%summary

%prep
%setup

%build
NOCONOFIGURE=true ./autogen.sh
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/lasemrender
%doc README COPYING ChangeLog AUTHORS NEWS

%files -n lib%name
%_libdir/lib%name-0.4.so.*

%files -n lib%name-devel
%_includedir/%name-0.4
%_libdir/pkgconfig/%name-0.4.pc
%_libdir/lib%name-0.4.so

%files -n lib%name-gir
%_libdir/girepository-1.0/Lasem-0.4.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/Lasem-0.4.gir

%changelog
* Sat Sep 11 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.0-alt1
- New version 0.3.0
- Added gir subpackages

* Thu Mar 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.0-alt1
- New version 0.2.0

* Tue Nov 03 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.2-alt1
- initial build

