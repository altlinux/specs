Name:     slop
Version:  7.5
Release:  alt1

Summary:  slop (Select Operation) is an application that queries for a selection from the user and prints the region to stdout.
License:  GPLv3
Group:    Graphics
Url:      https://github.com/naelstrof/slop

Packager: Pavel Skrylev <majioa@altlinux.org>

# Source-git: https://github.com/naelstrof/slop.git
Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libglm-devel libX11-devel libGLEW-devel libXrender-devel
BuildRequires: libXext-devel libEGL-devel libicu-devel

%description
slop (Select Operation) is an application that queries for a selection from
the user and prints the region to stdout.
Features:
 * Hovering over a window will cause a selection rectangle to appear over it.
 * Clicking on a window makes slop return the dimensions of the window, and it's ID.
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


%package -n lib%name-devel
Summary:  Development files for %name
Group:    Development/C++

%description -n lib%name-devel
Development files for %name.


%package -n lib%name
Summary:  Libraries for %name
Group:    System/Libraries

%description -n lib%name
Libraries for %name.


%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std
%find_lang %name
#ln -sf X11/libGLX.so.0 %buildroot/%_libdir/libGLX.so

%files
%_bindir/*
%_man1dir/*
%doc README.md COPYING

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so

%files -n lib%name
%_libdir/*.so.%version

%changelog
* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 7.5-alt1
- new version 7.5

* Wed Oct 10 2018 Pavel Skrylev <majioa@altlinux.org> 7.4-alt1
- Initial build for Sisyphus
