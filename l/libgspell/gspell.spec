%define _name gspell
%define ver_major 1.2
%define api_ver 1

Name: lib%_name
Version: %ver_major.3
Release: alt1

Summary: A spell-checking library for GTK+ applications
Group: System/Libraries
License: LGPLv2.1+
Url: https://wiki.gnome.org/Projects/gspell

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
#Source: %name-%version.tar
#Patch: %name-%version-%release.patch

%define gtk_ver 3.20.0
%define enchant_ver 1.6.0

Requires: iso-codes

BuildRequires: libgtk+3-devel >= %gtk_ver libenchant-devel >= %enchant_ver iso-codes-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel vala-tools gtk-doc

%description
gspell library provides a flexible API to add spell checking to a GTK+
applications.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
Development files for %_name, spell-checking library for GTK+
applications.

%package gir
Summary: GObject introspection data for the Gspell
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Gspell library.

%package gir-devel
Summary: GObject introspection devel data for the Gspell
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the Gspell library.

%package devel-doc
Summary: Development documentation for Gspell
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for Gspell library.


%prep
%setup -n %_name-%version
#%patch -p1

%build
# pkg-config >= 0.27 required
#%%autoreconf
%configure

%install
%makeinstall_std

%check
#%make check

%find_lang --output=%name.lang %_name-%api_ver

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.*

%files gir
%_typelibdir/Gspell-%api_ver.typelib

%files gir-devel
%_girdir/Gspell-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/%_name-*/

%changelog
* Fri Feb 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Fri Dec 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Sun Nov 06 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sat Jul 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Fri Jun 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Apr 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Mar 13 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Fri Feb 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- first build for sisyphus

