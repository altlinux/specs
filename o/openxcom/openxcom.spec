%define rev 598395d1
Name: openxcom
Version: 1.0
Release: alt4.%rev
Summary: OpenXcom is an open-source clone of the original X-COM
License: GPL
Group: Games/Strategy
Url: http://openxcom.org/
Packager: Andrew Clark <andyc@altlinux.org>

Source: https://github.com/SupSuper/OpenXcom/%name-%version.tar.bz2
Source3: %name.png
Source4: %name.desktop

# Automatically added by buildreq on Sat May 31 2014
# optimized out: boost-devel-headers cmake-modules libGL-devel libGLU-devel libSDL-devel libX11-devel libcloog-isl4 libstdc++-devel libyaml-cpp0 pkg-config xorg-kbproto-devel xorg-xproto-devel
BuildRequires: cmake gcc-c++ libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libyaml-cpp0-devel

%description
OpenXcom is an open-source clone of the popular UFO: Enemy Unknown
(X-Com: UFO Defense in USA) videogame by Microprose, licensed
under the GPL and written in C++ / SDL.

%prep
%setup -n %name-%version

%build
cmake --debug-output -D CMAKE_INSTALL_PREFIX="/usr" -D CMAKE_CXX_FLAGS="%optflags" -D CMAKE_C_FLAGS="%optflags" CMakeLists.txt
%make_build VERBOSE=1


%install
# let's create directory structure...
mkdir -p %buildroot{%_bindir,%_niconsdir,%_desktopdir,%_datadir/%name}

# and install what we need where we need it to be...
install -pm 755 bin/%name %buildroot%_bindir/
mv bin/data %buildroot%_datadir/%name/
install -pm 644 %SOURCE3 %buildroot%_niconsdir/%name.png
install -pm 644 %SOURCE4 %buildroot%_desktopdir/%name.desktop

%files
%doc CHANGELOG.txt COPYING README.* LICENSE.txt
%_bindir/%name
%_datadir/%name
%_niconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Sat Dec 6 2014 Andrew Clark <andyc@altlinux.org> 1.0-alt4.598395d1
- version update to 1.0-alt4.598395d1

* Sat Aug 30 2014 Andrew Clark <andyc@altlinux.org> 1.0-alt3.6ad5cf9b
- version update to 1.0-alt3.6ad5cf9b

* Mon Jun 9 2014 2014 Andrew Clark <andyc@altlinux.org> 1.0-alt2.65334d6f
- version update to 1.0-alt2.65334d6f

* Sat May 31 2014 Andrew Clark <andyc@altlinux.org> 1.0-alt1.9f60cbd8
- version update to 1.0-alt1.9f60cbd8
