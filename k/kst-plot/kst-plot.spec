%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: kst-plot
Version: 2.1
Release: alt2

Summary: Fast real-time large-dataset viewing and plotting tool for KDE
License: GPL-2.0-or-later
Group: Sciences/Mathematics
Url: https://kst-plot.kde.org
VCS: https://invent.kde.org/graphics/kst-plot

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-tools
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(matio)
BuildRequires: pkgconfig(netcdf-cxx4)
BuildRequires: pkgconfig(cfitsio)

Requires: lib%{name}libs = %{version}-%{release}

%if_with check
BuildRequires: ctest
%endif

%description
Kst is the fastest real-time large-dataset viewing and plotting tool
available and has built-in data analysis functionality.

Kst contains many powerful built-in features and is expandable with
plugins and extensions.

Features of Kst include:

- Robust plotting of live "streaming" data.
- Powerful keyboard and mouse plot manipulation.
- Powerful plugins and extensions support.
- Large selection of built-in plotting and data manipulation functions,
  such as histograms, equations, and power spectra.
- Color mapping and contour mapping capabilities for three-dimensional
  data, as well as matrix and image support.
- Built-in filtering and curve fitting capabilities.
- Convenient command-line interface.
- Powerful graphical user interface with non-modal dialogs for an
  optimized workflow.
- Support for several popular data formats.
- Multiple tabs.
- Extended annotation objects similar to vector graphics applications.
- High-quality export to bitmap or vector formats.

%package devel
Summary: Development files for Kst
Group: Development/C++
Requires: lib%{name}libs = %{version}-%{release}

%description devel
Development files for %name.

%package -n lib%{name}libs
Group: System/Libraries
Summary: libraries for %name

%description -n lib%{name}libs
This package contains libraries for %name.

%prep
%setup
%patch -p1

%build
%cmake \
       -Wno-dev \
       -Dkst_install_prefix=%_prefix \
       -Dkst_rpath=0 \
       -Dkst_install_libdir=%_libdir \
       -Dkst_release=1 \
       -Dkst_dbgsym=1 \
       -Dkst_python=0 \
       -Dkst_qt5=1 \
       -Dkst_version_string=%version
%cmake_build

%install
%cmake_install

# remove static library
rm -v %buildroot%_libdir/libkst2app.a

%files
%doc AUTHORS NEWS README COPYING*
%_bindir/kst2
%_desktopdir/kst2.desktop
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/scalable/*/*.svg
%_man1dir/kst2.1.xz
%_datadir/mime/packages/x-kst.xml

%files -n lib%{name}libs
%dir %_libdir/kst2
%dir %_libdir/kst2/plugins
%_libdir/kst2/plugins/*.*
%_libdir/libkst2core.so.2
%_libdir/libkst2core.so.2.1
%_libdir/libkst2math.so.2
%_libdir/libkst2math.so.2.1
%_libdir/libkst2widgets.so.2
%_libdir/libkst2widgets.so.2.1

%files devel
%_libdir/libkst2core.so
%_libdir/libkst2math.so
%_libdir/libkst2widgets.so

%changelog
* Thu Jun 11 2026 Nikolay Strelkov <snk@altlinux.org> 2.1-alt2
- Moved libraries to libkst-plotlibs package.

* Thu Jan 15 2026 Nikolay Strelkov <snk@altlinux.org> 2.1-alt1
- Initial build for Sisyphus
