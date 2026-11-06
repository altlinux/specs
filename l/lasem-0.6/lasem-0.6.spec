%def_enable snapshot
%define _name lasem
%define ver_major 0.6
%define namespace Lasem
%define api_ver %ver_major

%def_enable docs
%def_enable check

Name: %_name-%api_ver
Version: %ver_major.0
Release: alt1

Summary: C/Gobject based SVG/Mathml renderer and editor - tools
License: LGPL-2.0-or-later
Group: Graphics
Url: https://github.com/LasemProject/lasem

Vcs: https://github.com/LasemProject/lasem.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Requires(pre): lib%name = %EVR

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson bison flex
BuildRequires: libgio-devel libxml2-devel
BuildRequires: libcairo-devel libcairo-gobject-devel
BuildRequires: libgdk-pixbuf-devel libpango-devel
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: libgdk-pixbuf-gir-devel libpango-gir-devel
%{?_enable_docs:BuildRequires: gi-docgen}

%description
Lasem aims to be a C/Gobject based SVG/Mathml renderer and editor,
supporting CSS style sheets. It uses cairo and pango as it's rendering
abstraction layer, and then support numerous output formats: xlib, PNG,
SVG, PDF, PS, EPS...

%package -n lib%name
Summary: C/Gobject based SVG/Mathml renderer and editor - library
Group: System/Libraries
# cmr10, cmmi10, cmex10 and cmsy10 fonts (see README)
Requires: fonts-ttf-latex-xft

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: C/Gobject based SVG/Mathml renderer and editor - development files
Group: Development/C
Requires(pre): lib%name = %EVR

%description -n lib%name-devel
%summary

%package -n lib%name-gir
Summary: GObject introspection data for the Lasem library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
%summary

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Lasem library
Group: Development/Other
Requires: lib%name-gir = %EVR

%description -n lib%name-gir-devel
%summary

%package -n lib%name-devel-doc
Summary: Development documentation for Lasem library
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
%summary

This package provides documentation needed for developing Lasem
applications.

%prep
%setup -n %_name-%version

%build
%meson -Dbuildtype=release \
    %{subst_enable_meson_feature docs documentation}
%nil
%meson_build

%install
%meson_install
%find_lang %_name-%api_ver

%check
%meson_test

%files
%_bindir/%_name-render-%api_ver
%_man1dir/%_name-render-*
%doc README* NEWS* TODO

%files -n lib%name -f %_name-%api_ver.lang
%_libdir/lib%_name-%api_ver.so.*

%files -n lib%name-devel
%_includedir/%_name-%api_ver
%_pkgconfigdir/%_name-%api_ver.pc
%_libdir/lib%_name-%api_ver.so

%files -n lib%name-gir
%_typelibdir/%namespace-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/%namespace-%api_ver.gir

%if_enabled docs
%files -n lib%name-devel-doc
%_datadir/doc/%_name-%api_ver/
%endif

%changelog
* Fri Nov 06 2026 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- updated to 0.6.0-8-ge657038

* Fri May 24 2019 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Fri May 04 2018 Grigory Ustinov <grenka@altlinux.org> 0.4.3-alt1.1
- NMU: Rebuilt for e2k.

* Sun Feb 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Feb 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Wed Dec 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1
- updated buildreqs
- added fonts-ttf-latex-xft to dependencies (see README)
- new -devel-doc subpackage

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

