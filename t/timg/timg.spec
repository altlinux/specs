%def_disable snapshot

Name: timg
Version: 1.5.3
Release: alt1

Summary: terminal image viewer
License: GPL-2.0
Group: Graphics
Url: https://timg.sh

%if_disabled snapshot
Source: https://github.com/hzeller/timg/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/hzeller/timg.git
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ninja-build
BuildRequires: pkgconfig(libdeflate)
BuildRequires: pkgconfig(libsixel)
BuildRequires: pkgconfig(libturbojpeg)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(GraphicsMagick++)

%description
A user-friendly terminal image viewer that uses graphic capabilities of
terminals (Sixel, Kitty or iterm2), or 24-Bit color capabilities and unicode
character blocks if these are not available.

%prep
%setup -n %name-%version

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
    -GNinja \
    -DTIMG_VERSION_FROM_GIT=OFF
%nil
%cmake_build

%install
%cmake_install
%find_lang --all-name --output=%name.lang %name

%files -f %name.lang
%_bindir/%name
%_man1dir/%name.1*
%doc README*

%changelog
* Wed Nov 29 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Fri Sep 01 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- first build for Sisyphus

