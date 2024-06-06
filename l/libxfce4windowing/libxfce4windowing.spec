%def_enable introspection
%def_disable docs

Name: libxfce4windowing
Version: 4.19.3
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
BuildRequires: libgtk+3-devel libgdk-pixbuf-devel
BuildRequires: libX11-devel libwnck3-devel
BuildRequires: wayland-devel libwayland-client-devel wlr-protocols
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
# NOTE: gtk-doc is required by build system even if docs are disabled.
BuildRequires: gtk-doc


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

%prep
%setup
#patch -p1

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	%{subst_enable introspection} \
%if_enabled docs
	--enable-gtk-doc \
%else
	--disable-gtk-doc \
%endif
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md NEWS
%_libdir/*.so.*

%files devel
%if_enabled docs
%doc %_datadir/gtk-doc/html/%name
%endif
%dir %_includedir/xfce4/%name
%_includedir/xfce4/
%_pkgconfigdir/*.pc
%_libdir/*.so

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*.typelib

%files gir-devel
%_datadir/gir-1.0/*.gir
%endif

%changelog
* Tue May 28 2024 Mikhail Efremov <sem@altlinux.org> 4.19.3-alt1
- Initial build.
