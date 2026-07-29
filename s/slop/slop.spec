Name:          slop
Version:       7.7
Release:       alt1
Summary:       slop (Select Operation) is an application that queries for a selection from the user and prints the region to stdout
License:       GPLv3
Group:         Graphics
Url:           https://github.com/naelstrof/slop
Vcs:           https://github.com/naelstrof/slop.git

Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libglm-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(glew)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(icu-uc)

%description
slop (Select Operation) is an application that queries for a selection from
the user and prints the region to stdout.
Features:
* Hovering over a window will cause a selection rectangle to appear over it.
* Clicking on a window makes slop return the dimensions of the window, and
  it's ID.
* OpenGL accelerated graphics where possible.
* Supports simple arguments:
 * Change selection rectangle border size.
 * Select X display.
 * Set padding size.
 * Force window, or pixel selections with the tolerance flag.
 * Set the color of the selection rectangles to match your theme! (Even supports
    transparency!)
 * Remove window decorations from selections.
* Supports custom programmable shaders.


%package       -n lib%name-devel
Summary:       Development files for %name
Group:         Development/C++

%description   -n lib%name-devel
Development files for %name.

slop (Select Operation) is an application that queries for a selection from
the user and prints the region to stdout.
Features:
* Hovering over a window will cause a selection rectangle to appear over it.
* Clicking on a window makes slop return the dimensions of the window, and
  it's ID.
* OpenGL accelerated graphics where possible.
* Supports simple arguments:
 * Change selection rectangle border size.
 * Select X display.
 * Set padding size.
 * Force window, or pixel selections with the tolerance flag.
 * Set the color of the selection rectangles to match your theme! (Even supports
    transparency!)
 * Remove window decorations from selections.
* Supports custom programmable shaders.


%package       -n lib%name
Summary:       Libraries for %name
Group:         System/Libraries

%description   -n lib%name
Libraries for %name.

slop (Select Operation) is an application that queries for a selection from
the user and prints the region to stdout.
Features:
* Hovering over a window will cause a selection rectangle to appear over it.
* Clicking on a window makes slop return the dimensions of the window, and
  it's ID.
* OpenGL accelerated graphics where possible.
* Supports simple arguments:
 * Change selection rectangle border size.
 * Select X display.
 * Set padding size.
 * Force window, or pixel selections with the tolerance flag.
 * Set the color of the selection rectangles to match your theme! (Even supports
    transparency!)
 * Remove window decorations from selections.
* Supports custom programmable shaders.


%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std 
%find_lang %name

%files
%_bindir/*
%_man1dir/*
%doc README.md COPYING

%files         -n lib%name-devel
%_includedir/*
%_libdir/lib*.so

%files         -n lib%name
%_libdir/*.so.%version

%changelog
* Tue Jul 28 2026 Pavel Skrylev <majioa@altlinux.org> 7.7-alt1
- ^ 7.6p15 -> 7.7
- > used pkgconfig indirect deps for build stage

* Tue Mar 18 2025 Ivan A. Melnikov <iv@altlinux.org> 7.6.15-alt0.2
- NMU: build with recent libicu (fixes FTBFS on loongarch64)

* Tue Mar 04 2025 Pavel Skrylev <majioa@altlinux.org> 7.6.15-alt0.1
- ^ 7.6 -> 7.6p15

* Tue Oct 12 2021 Pavel Skrylev <majioa@altlinux.org> 7.6-alt1
- ^ 7.5 -> 7.6

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 7.5-alt1
- new version 7.5

* Wed Oct 10 2018 Pavel Skrylev <majioa@altlinux.org> 7.4-alt1
- Initial build for Sisyphus
