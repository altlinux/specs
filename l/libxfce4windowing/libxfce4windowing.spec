%def_enable introspection
%def_enable vala
%def_enable docs
%define soname 0

Name: libxfce4windowing
Version: 4.20.6
Release: alt1

Summary: Xfce-related windowing concept abstraction library for X11 and Wayland
License: LGPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/xfce/libxfce4windowing/start

Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/xfce/libxfce4windowing.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-xfce4 xfce4-dev-tools
BuildRequires(pre): meson rpm-macros-meson >= 1.3.1-alt1
BuildRequires: libgtk+3-devel libgdk-pixbuf-devel
BuildRequires: libX11-devel libwnck3-devel libdisplay-info-devel libXrandr-devel
BuildRequires: wayland-devel libwayland-client-devel wlr-protocols wayland-protocols
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_docs:BuildRequires: gtk-doc}
# libxfce4windowing >= 4.19.6 breaks API/ABI whithout soname change
Conflicts: xfdesktop < 4.19.5 xfce4-panel < 4.19.5 libxfce4panel-gtk3 < 4.19.5

%define _unpackaged_files_terminate_build 1

%description
Libxfce4windowing is an abstraction library that attempts to present windowing
concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.
Currently, X11 is fully supported, via libwnck. Wayland is partially supported,
through various Wayland protocol extensions. However, the full range of
operations available on X11 is not available on Wayland, due to missing features
in these protocol extensions.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for the %name library.

%if_enabled introspection
%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for %name.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for %name.
%endif

%if_enabled vala
%package vala 
Summary: Vala bindings for %name
Group: System/Libraries
Requires: %name-devel = %EVR 
BuildArch: noarch

%description vala
Vala bindings for %name.
%endif

%prep
%setup
#patch -p1

%build
%meson \
	-Dx11=enabled \
	-Dwayland=enabled \
	%{subst_enable_meson_bool introspection introspection} \
	%{subst_enable_meson_bool docs gtk-doc} \
	-Dtests=false

%meson_build -v

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md NEWS
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*

%files devel
%if_enabled docs
%doc %_datadir/gtk-doc/html/%{name}*
%endif
%_includedir/xfce4/
%_pkgconfigdir/*.pc
%_libdir/*.so

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*.typelib

%files gir-devel
%_datadir/gir-1.0/*.gir
%endif

%if_enabled vala
%files vala
%_datadir/vala/vapi/%{name}*
%endif 

%changelog
* Mon May 25 2026 Mikhail Efremov <sem@altlinux.org> 4.20.6-alt1
- Explicitly disabled tests.
- Enabled vala support
- Enabled devel docs.
- Switched to meson build.
- Updated to 4.20.6.

* Mon Dec 29 2025 Mikhail Efremov <sem@altlinux.org> 4.20.5-alt1
- Updated to 4.20.5.

* Thu Aug 14 2025 Mikhail Efremov <sem@altlinux.org> 4.20.4-alt1
- Updated to 4.20.4.

* Thu May 22 2025 Mikhail Efremov <sem@altlinux.org> 4.20.3-alt1
- Updated to 4.20.3.

* Mon Feb 03 2025 Mikhail Efremov <sem@altlinux.org> 4.20.2-alt1
- Added soname check.
- Updated to 4.20.2.

* Mon Dec 16 2024 Mikhail Efremov <sem@altlinux.org> 4.20.0-alt1
- Updated to 4.20.0.

* Mon Dec 02 2024 Mikhail Efremov <sem@altlinux.org> 4.19.10-alt1
- Updated to 4.19.10.

* Fri Nov 01 2024 Mikhail Efremov <sem@altlinux.org> 4.19.9-alt1
- Updated to 4.19.9.

* Wed Oct 23 2024 Mikhail Efremov <sem@altlinux.org> 4.19.8-alt1
- Updated to 4.19.8.

* Wed Oct 16 2024 Mikhail Efremov <sem@altlinux.org> 4.19.7-alt1
- Updated to 4.19.7.

* Thu Oct 03 2024 Mikhail Efremov <sem@altlinux.org> 4.19.5-alt1
- Updated to 4.19.5.

* Tue Aug 27 2024 Mikhail Efremov <sem@altlinux.org> 4.19.4-alt1
- Explicitly enabled both Wayland and X11 support.
- Updated to 4.19.4.

* Tue May 28 2024 Mikhail Efremov <sem@altlinux.org> 4.19.3-alt1
- Initial build.
