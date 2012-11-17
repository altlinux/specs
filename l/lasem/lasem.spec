Name: lasem
Version: 0.3.4
Release: alt1

Summary: C/Gobject based SVG/Mathml renderer and editor - tools
License: GPL
Group: Graphics

Url: https://live.gnome.org/Lasem

# Cloned from git://git.gnome.org/lasem as subtree lasem
#
# To update sources from upstream git:
#
#   $ git remote add upstream git://git.gnome.org/lasem
#   $ git pull -s subtree -X subtree=lasem upstream LASEM_0_3_4
Source: %name-%version.tar

BuildRequires: glib2-devel libgio-devel libgtk+2-devel libxml2-devel libpango-devel libcairo-devel autogen intltool flex libgtk+2-gir-devel gtk-doc
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
%find_lang %name-0.4

%files
%_bindir/lasem-render-0.4
%doc README COPYING ChangeLog AUTHORS NEWS

%files -n lib%name -f %name-0.4.lang
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
* Sat Nov 17 2012 Vladimir Lettiev <crux@altlinux.ru> 0.3.4-alt1
- New version 0.3.4 (Closes: #27993)
- Dropped patch

* Thu Jul 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.1
- Fixed build

* Sat Sep 11 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.0-alt1
- New version 0.3.0
- Added gir subpackages

* Thu Mar 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.0-alt1
- New version 0.2.0

* Tue Nov 03 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.2-alt1
- initial build

