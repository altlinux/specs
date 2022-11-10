%define nm_version 1.4.1-alt1.git20160914
%define _unpackaged_files_terminate_build 1

%def_with gcr
%def_with gtk4

Name: libnma
Version: 1.10.4
Release: alt2
License: GPLv2+ and LGPLv2.1+
Group: Graphical desktop/GNOME
Summary: NetworkManager GUI library
Url: https://gitlab.gnome.org/GNOME/libnma
Vcs: https://gitlab.gnome.org/GNOME/libnma.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson

BuildRequires: libgtk+3-devel libtool
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnm-gir-devel >= %nm_version
BuildRequires: iso-codes-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: mobile-broadband-provider-info
BuildRequires: gtk-doc
%{?_with_gcr:BuildRequires: gcr4-libs-devel}
%{?_with_gtk4:BuildRequires: libgtk4-devel libgtk4-gir-devel}

Requires: %name-common = %EVR

# org.gnome.nm-applet.gschema.xml is moved to nm-applet
Conflicts: NetworkManager-applet-gtk < 1.30.0-alt1

%description
This package contains the library used for integrating GUI tools with
NetworkManager.

%package devel
Group: Development/GNOME and GTK+
Summary: Devel files for NetworkManager GUI library
Requires: %name = %version-%release
Requires: libnm-devel >= %nm_version
Requires: libgtk+3-devel

%description devel
This package contains header and pkg-config files to be used for integrating
GUI tools with NetworkManager.

%package gir
Group: System/Libraries
Summary: GObject introspection data for the libnma
Requires: %name = %version-%release

%description gir
GObject introspection data for the libnma.

%package gir-devel
Group: System/Libraries
Summary: GObject introspection devel data for the libnma
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the libnma.

%if_with gtk4
%package gtk4
Summary: Experimental GTK 4 version of NetworkManager GUI library
Group: Graphical desktop/GNOME
Requires: %name-common = %EVR

%description gtk4
This package contains the GTK4 version of library used for
integrating GUI tools with NetworkManager.

%package gtk4-devel
Group: Development/GNOME and GTK+
Summary: Devel files for GTK4 version of NetworkManager GUI library
Requires: %name-gtk4 = %EVR
Requires: libnm-devel >= %nm_version
Requires: libgtk4-devel

%description gtk4-devel
This package contains the GTK4 version of header and pkg-config
files to be used for integrating GUI tools with NetworkManager.

%package gtk4-gir
Group: System/Libraries
Summary: GObject introspection data for the libnma-gtk4
Requires: %name-gtk4 = %EVR

%description gtk4-gir
GObject introspection data for the libnma-gtk4.

%package gtk4-gir-devel
Group: System/Libraries
Summary: GObject introspection devel data for the libnma-gtk4
BuildArch: noarch
Requires: %name-gtk4-gir = %version-%release
Requires: %name-gtk4-devel = %version-%release

%description gtk4-gir-devel
GObject introspection devel data for the libnma-gtk4.
%endif

%package common
Group: System/Libraries
Summary: Common files for %name and %name-gtk4
BuildArch: noarch
Conflicts: %name < 1.8.36-alt1

%description common
This package contains the common files for both variants of %name
(GTK3 and GTK4).

%package devel-doc
Summary: Development documentation for libnma-devel-doc
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
This package contains development documentation for libnma-devel-doc.

%prep
%setup
%patch -p1

%build
%meson \
	--libexecdir==%_libexecdir/NetworkManager \
	--localstatedir=%_var \
%if_with gcr
	-Dgcr=true \
%else
	-Dgcr=false \
%endif
	-Dintrospection=true \
	-Dvapi=false \
%if_with gtk4
	-Dlibnma_gtk4=true \
%else
	-Dlibnma_gtk4=false \
%endif
	-Dmobile_broadband_provider_info=true \
	-Diso_codes=true \
	-Dgtk_doc=true

%meson_build -v

%install
%meson_install
%find_lang %name

%files
%_libdir/libnma.so.*

%files devel
%_includedir/libnma/
%_libdir/libnma.so
%_pkgconfigdir/libnma.pc

%files gir
%_libdir/girepository-1.0/NMA-1.0.typelib

%files gir-devel
%_datadir/gir-1.0/NMA-1.0.gir

%if_with gtk4
%files gtk4
%_libdir/libnma-gtk4.so.*

%files gtk4-devel
%_includedir/libnma/
%_libdir/libnma-gtk4.so
%_pkgconfigdir/libnma-gtk4.pc

%files gtk4-gir
%_libdir/girepository-1.0/NMA4-1.0.typelib

%files gtk4-gir-devel
%_datadir/gir-1.0/NMA4-1.0.gir
%endif

%files common -f %name.lang
%doc NEWS CONTRIBUTING
%_datadir/glib-2.0/schemas/org.gnome.nm-applet.eap.gschema.xml

%exclude %_datadir/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml

%files devel-doc
%doc %_datadir/gtk-doc/html/libnma

%changelog
* Fri Nov 11 2022 Mikhail Efremov <sem@altlinux.org> 1.10.4-alt2
- Move gschema to common subpackage.
- Drop path from eap schema (closes: #44273).

* Tue Nov 08 2022 Mikhail Efremov <sem@altlinux.org> 1.10.4-alt1
- Don't package org.gnome.nm-applet.gschema.xml.
- Build with gcr4.
- Updated to 1.10.4.

* Mon Sep 12 2022 Mikhail Efremov <sem@altlinux.org> 1.10.2-alt1
- Added gcr-4 knob (disabled for now).
- Updated to 1.10.2.

* Tue Jun 28 2022 Mikhail Efremov <sem@altlinux.org> 1.8.40-alt1
- Updated to 1.8.40.

* Tue Apr 19 2022 Mikhail Efremov <sem@altlinux.org> 1.8.38-alt1
- Added common subpackage.
- libnma-gtk4: Updated summary/description.
- Updated to 1.8.38.

* Wed Mar 30 2022 Mikhail Efremov <sem@altlinux.org> 1.8.36-alt1
- Updated to 1.8.36.

* Mon Mar 07 2022 Mikhail Efremov <sem@altlinux.org> 1.8.34-alt2
- Enabled experimental GTK4 version build.

* Tue Mar 01 2022 Mikhail Efremov <sem@altlinux.org> 1.8.34-alt1
- Updated to 1.8.34.

* Tue Aug 31 2021 Mikhail Efremov <sem@altlinux.org> 1.8.32-alt1
- Updated to 1.8.32.

* Fri Jul 03 2020 Mikhail Efremov <sem@altlinux.org> 1.8.30-alt1
- Updated to 1.8.30.

* Thu Mar 26 2020 Mikhail Efremov <sem@altlinux.org> 1.8.28-alt1
- Splitted out from nm-applet.

