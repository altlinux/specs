Name: openxcom
Version: 1.0_2022.10.24
Release: alt1
Summary: OpenXcom is an open-source clone of the original X-COM
License: GPLv3+
Group: Games/Strategy
Url: http://openxcom.org/

Source: https://github.com/SupSuper/OpenXcom/%name-%version.tar
Source2: openxcom16.png
Source3: openxcom32.png
Patch: openxcom-man6.patch

# Automatically added by buildreq on Sat May 31 2014
# optimized out: boost-devel-headers cmake-modules libGL-devel libGLU-devel libSDL-devel libX11-devel libcloog-isl4 libstdc++-devel libyaml-cpp0 pkg-config xorg-kbproto-devel xorg-xproto-devel
BuildRequires: cmake gcc-c++ libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libyaml-cpp-devel

# Recommends
Requires: zenity

%description
OpenXcom is an open-source clone of the popular UFO: Enemy Unknown
(X-Com: UFO Defense in USA) videogame by Microprose, licensed
under the GPL and written in C++ / SDL.

%prep
%setup -n %name-%version
%patch -p1

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
%_man6dir/%{name}.6*
%_iconsdir/hicolor/*/apps/%name.*
%_desktopdir/%name.desktop

%changelog
* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 1.0_2022.10.24-alt1
- nightly 2022.10.24

* Thu Aug 18 2022 Igor Vlasenko <viy@altlinux.org> 1.0_2022.08.16-alt1
- nightly 2022.08.16

* Thu Aug 04 2022 Igor Vlasenko <viy@altlinux.org> 1.0_2022.07.06-alt1
- nightly 2022.07.06

* Tue May 10 2022 Igor Vlasenko <viy@altlinux.org> 1.0_2022.04.23-alt1
- nightly 2022.04.23

* Tue Jan 25 2022 Igor Vlasenko <viy@altlinux.org> 1.0_2021.12.21-alt1
- nightly 2021.12.21

* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 1.0_2021.11.24-alt1
- nightly 2021.11.24

* Wed Nov 03 2021 Igor Vlasenko <viy@altlinux.org> 1.0_2021.09.20-alt1
- nightly 2021.09.20

* Tue Aug 03 2021 Igor Vlasenko <viy@altlinux.org> 1.0_2021.06.11-alt1
- nightly 2021.06.11

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 1.0_2021.05.17-alt1
- nightly 2021.05.17

* Sat May 15 2021 Igor Vlasenko <viy@altlinux.org> 1.0_2021.05.13-alt1
- nightly 2021.05.13

* Fri Apr 23 2021 Igor Vlasenko <viy@altlinux.org> 1.0_2021.04.22-alt1
- nightly 2021.04.22

* Sat Apr 03 2021 Igor Vlasenko <viy@altlinux.org> 1.0_2021.03.29-alt1
- nightly 2021.03.29

* Sun Jan 17 2021 Igor Vlasenko <viy@altlinux.ru> 1.0_2021.01.11-alt1
- nightly 2021.01.11

* Mon Oct 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.0_2020.10.10-alt1
- nightly 2020.10.10

* Sun Aug 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.0_2020.08.02-alt1
- nightly 2020.08.02

* Sat Jun 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.0_2019.06.28-alt1
- nightly 2019.06.28

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
