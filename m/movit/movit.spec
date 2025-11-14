
%define sover 8
%define libmovit libmovit%sover

Name: movit
Version: 1.7.1
Release: alt1

Group: System/Libraries
Summary: GPU video filter library
License: GPL-2.0-or-later
Url: https://movit.sesse.net


Source: %name-%version.tar
Patch1: data.patch

BuildRequires: gcc-c++
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(SDL2_image)

%description
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

%package devel
Group: Development/Other
Summary: Development files for the Movit GPU video filter library
%description devel
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the development files (library and header files).

%package -n %libmovit
Summary: %name library
Group: System/Libraries
Requires: %name-data >= %EVR
%description -n %libmovit
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the Movit shared library.

%package data
Group: System/Libraries
Summary: Data files for the Movit GPU video filter library
BuildArch: noarch
%description data
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the architecture-independent data files.

%prep
%setup
%patch1 -p1
%autoreconf -fisv

%build
%configure --disable-static
%make_build TESTS=

%install
%makeinstall DESTDIR= TESTS=

%files -n %libmovit
%doc README NEWS
%_libdir/libmovit.so.%sover
%_libdir/libmovit.so.*

%files data
%_datadir/movit/

%files devel
%_libdir/lib*.so
%_includedir/movit/
%_pkgconfigdir/movit.pc

%changelog
* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 1.7.1-alt1
- initial build
