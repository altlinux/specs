%define sover 0

Name: wiiuse
Version: 0.15.6
Release: alt1
Summary: The wiiuse library is used to access and control multiple Nintendo Wiimotes
License: GPL-3.0-or-later
Group: System/Libraries
Url: https://github.com/wiiuse/wiiuse
VCS: https://github.com/wiiuse/wiiuse.git

Source: %url/archive/%version/wiiuse-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja dos2unix
BuildRequires: gcc-c++ cmake libbluez-devel libGL-devel libfreeglut-devel libSDL-devel

%description
Wiiuse is a library written in C that connects with several Nintendo
Wii remotes.  Supports motion sensing, IR tracking, nunchuk, classic
controller, and the Guitar Hero 3 controller.  Single threaded and
nonblocking makes a light weight and clean API.

%package -n lib%name%sover
Summary: wiiuse library
Group: Development/C

%description -n lib%name%sover
This package provides the wiiuse library.

%package -n lib%name-devel
Summary: Developer tools for the wiiuse library
Group: Development/C
Requires: libbluez-devel
Provides: pkgconfig(wiiuse)

%description -n lib%name-devel
Header files needed to develop programs that link against the wiiuse library.

%package -n lib%name-examples
Summary: Example programs for the wiiuse library
Group: Documentation

%description -n lib%name-examples
Example programs to test accessing wiiremote controllers

%prep
%setup -n wiiuse-%version
%autopatch -p1
dos2unix CHANGELOG.mkd README.mkd

%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install
# Packed using %%doc
rm -rf %buildroot%_docdir/wiiuse

%files -n lib%name%sover
%_libdir/libwiiuse.so.%{sover}*

%files -n lib%name-devel
%doc LICENSE CHANGELOG.mkd README.mkd
%_includedir/wiiuse.h
%_libdir/libwiiuse.so
%_pkgconfigdir/wiiuse.pc

%files -n lib%name-examples
%doc example/example.c example-sdl/sdl.c
%_bindir/wiiuseexample
%_bindir/wiiuseexample-sdl

%changelog
* Fri Jul 25 2025 Leontiy Volodin <lvol@altlinux.org> 0.15.6-alt1
- New version 0.15.6.
- Changed url tag.
- Added VCS tag.
- Switched source package: libwiiuse -> wiiuse.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.15.5-alt2.1
- NMU: spec: adapted to new cmake macros.

* Tue Aug 11 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.5-alt2
- Removed chrpath from BR.
- Built with ninja instead make.

* Fri Jan 31 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.5-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec) (ALT #37832).
