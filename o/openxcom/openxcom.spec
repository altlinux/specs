Name: openxcom
Version: 1.0_2019.04.28
Release: alt1
Summary: OpenXcom is an open-source clone of the original X-COM
License: GPL
Group: Games/Strategy
Url: http://openxcom.org/

Source: https://github.com/SupSuper/OpenXcom/%name-%version.tar
Source2: openxcom16.png
Source3: openxcom32.png

# Automatically added by buildreq on Sat May 31 2014
# optimized out: boost-devel-headers cmake-modules libGL-devel libGLU-devel libSDL-devel libX11-devel libcloog-isl4 libstdc++-devel libyaml-cpp0 pkg-config xorg-kbproto-devel xorg-xproto-devel
BuildRequires: cmake gcc-c++ libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libyaml-cpp0-devel

# Recommends
Requires: zenity

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
%makeinstall_std

install -pm 644 -D %{SOURCE3} %buildroot%_niconsdir/%name.png
install -pm 644 -D %{SOURCE2} %buildroot%_miconsdir/%name.png
install -pm 644 -D res/linux/icons/openxcom_48x48.png %buildroot%_liconsdir/%name.png
install -pm 644 -D res/linux/icons/openxcom_128x128.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
install -pm 644 -D res/linux/icons/openxcom.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -pm 644 -D res/linux/openxcom.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc CHANGELOG.txt README.* LICENSE.txt
%_bindir/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.*
%_desktopdir/%name.desktop

%changelog
* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.0_2019.04.28-alt1
- nightly 2019.04.28

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.0_2018.10.08-alt1
- nightly 2018.10.08

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0_2017.10.15-alt2
- NMU: rebuilt with new yaml-cpp.

* Sun Oct 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.0_2017.10.15-alt1
- picked up orphaned package from nobody@
- nightly 2017.06.15

* Wed Dec 2 2015 Vladimir Didenko <cow@altlinux.org> 1.0-alt5.598395d1
- Rebuilt for gcc5 C++11 ABI

* Sat Dec 6 2014 Andrew Clark <andyc@altlinux.org> 1.0-alt4.598395d1
- version update to 1.0-alt4.598395d1

* Sat Aug 30 2014 Andrew Clark <andyc@altlinux.org> 1.0-alt3.6ad5cf9b
- version update to 1.0-alt3.6ad5cf9b

* Mon Jun 9 2014 2014 Andrew Clark <andyc@altlinux.org> 1.0-alt2.65334d6f
- version update to 1.0-alt2.65334d6f

* Sat May 31 2014 Andrew Clark <andyc@altlinux.org> 1.0-alt1.9f60cbd8
- version update to 1.0-alt1.9f60cbd8
