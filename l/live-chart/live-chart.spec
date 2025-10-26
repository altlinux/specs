%define _unpackaged_files_terminate_build 1

%def_with check

Name: live-chart
Version: 2.0.0
Release: alt1

Summary: A real-time charting library for Vala and GTK4 based on Cairo
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/elementary/live-chart

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: libgee0.8-devel
BuildRequires: libgtk4-devel
BuildRequires: xvfb-run
BuildRequires: vala-tools

%if_with check
BuildRequires: libGLES
%endif

%description
Live Chart is a real-time charting library for GTK4 and Vala, based on
Cairo.

Features:

* Live animated series (lines, smooth lines, area, bar) within a single
  chart
* Smart y-axis computation
* Highly configurable
* Extendable

%package -n liblivechart2
Summary: real-time charting library
Group: System/Libraries

%description -n liblivechart2
Live Chart is a real-time charting library for GTK4 and Vala, based on
Cairo.

This package contains the shared library.

%package -n liblivechart2-devel
Summary: real-time charting library (development files)
Group: Development/C

%description -n liblivechart2-devel
Live Chart is a real-time charting library for GTK4 and Vala, based on
Cairo.

This package contains the static library and header files.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n liblivechart2
%doc CONTRIBUTING.md LICENSE NEWS.md  README.md
%_libdir/liblivechart-2.so.2
%_libdir/liblivechart-2.so.2.0.0

%files -n liblivechart2-devel
%doc examples
%_includedir/livechart-2.h
%_libdir/liblivechart-2.so
%_pkgconfigdir/livechart-2.pc
%_datadir/vala/vapi/livechart-2.vapi

%changelog
* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
