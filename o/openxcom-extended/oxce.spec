%define alias oxce
Name: openxcom-extended
Epoch: 1
Version: 7.8.4
Release: alt1

Summary: OpenXcom Extended is an open-source clone of the original X-COM
License: GPLv3+
Group: Games/Strategy

Url: http://openxcom.org/
Source: https://github.com/SupSuper/OpenXcom/%name-%version.tar
Source2: openxcom16.png
Source3: openxcom32.png
Patch0: openxcom.desktop-to-oxce.patch
Patch1: openxcom-man6.patch
# there are tags from both openxcom and oxce
#VCS: git+https://github.com/MeridianOXC/OpenXcom.git

BuildRequires: cmake gcc-c++ libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libyaml-cpp-devel zlib-devel doxygen /usr/bin/git libGLU-devel libglvnd-devel pkgconfig(sdl)

# Recommends
Requires: zenity

%description
OpenXcom Extended (OXCE) is an open-source clone of the popular
UFO: Enemy Unknown (X-Com: UFO Defense in USA) videogame by Microprose,
licensed under the GPL and written in C++ / SDL.

OpenXcom Extended is a game engine required to run properly
some OpenXcom.org mods such as Pirates!, Area 51 or X-Files.

%prep
%setup -n %name-%version
%patch0
%patch1 -p1

sed -i 's,DATADIR}/openxcom",DATADIR}/%name",g' src/CMakeLists.txt

%ifarch %e2k
# unsupported as of lcc 1.25.23
sed -i 's,^.*femit-struct-debug-reduced,#&,' src/CMakeLists.txt
%endif

%build
cmake --debug-output -D CMAKE_INSTALL_PREFIX="/usr" -D CMAKE_CXX_FLAGS="%optflags" -D CMAKE_C_FLAGS="%optflags" CMakeLists.txt
%make_build VERBOSE=1


%install
%makeinstall_std

mv %buildroot%_desktopdir/{openxcom,%name}.desktop
sed -i s,openxcom,%name,g %buildroot%_desktopdir/%name.desktop

install -pm 644 -D %{SOURCE3} %buildroot%_niconsdir/%name.png
install -pm 644 -D %{SOURCE2} %buildroot%_miconsdir/%name.png
#rm -f %buildroot%_iconsdir/hicolor/*/apps/openxcom*
mv %buildroot%_liconsdir/{openxcom,%{name}}.png
mv %buildroot%_iconsdir/hicolor/128x128/apps/{openxcom,%{name}}.png
mv %buildroot%_iconsdir/hicolor/scalable/apps/{openxcom,%{name}}.svg
mv %buildroot%_bindir/{openxcom,%{name}}
ln -s %{name} %buildroot%_bindir/%alias
mv %buildroot%_man6dir/{openxcom.6,%{name}.6}

%files
%doc CHANGELOG.txt README.* LICENSE.txt
%_bindir/%name
%_bindir/%alias
%_datadir/%name
%_man6dir/*
%_iconsdir/hicolor/*/apps/%name.*
%_desktopdir/%name.desktop

%changelog
* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 1:7.8.4-alt1
- new version

* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 1:7.7.3-alt1
- new version

* Sat Sep 10 2022 Igor Vlasenko <viy@altlinux.org> 1:7.7.2-alt1
- new version

* Thu Sep 08 2022 Michael Shigorin <mike@altlinux.org> 1:7.7.0-alt2
- E2K: avoid lcc-unsupported option

* Mon Aug 29 2022 Igor Vlasenko <viy@altlinux.org> 1:7.7.0-alt1
- new version

* Thu Aug 18 2022 Igor Vlasenko <viy@altlinux.org> 1:7.6.8-alt1
- new version

* Thu Aug 04 2022 Igor Vlasenko <viy@altlinux.org> 1:7.6.3-alt1
- new version

* Sun Jun 05 2022 Igor Vlasenko <viy@altlinux.org> 1:7.5.15-alt1
- new version

* Tue May 10 2022 Igor Vlasenko <viy@altlinux.org> 1:7.5.14-alt1
- new version

* Tue Jan 25 2022 Igor Vlasenko <viy@altlinux.org> 1:7.4.4-alt1
- new version

* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 1:7.1.7-alt1
- new version

* Tue Aug 03 2021 Igor Vlasenko <viy@altlinux.org> 1:7.0.13-alt1
- new version

* Thu May 20 2021 Igor Vlasenko <viy@altlinux.org> 7.0_2021.05.18-alt1
- nightly 2021.05.18

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 6.6_2020.09.01-alt1
- nightly 2020.09.01

