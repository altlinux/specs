%define oname io.github.cxong.cdogs-sdl

Name: cdogs-sdl
Version: 2.4.0
Release: alt1

Summary: C-Dogs is an arcade shoot-em-up
License: BSD-2-Clause AND GPL-2.0-only AND CC-BY-3.0 AND CC-BY-SA-3.0
Group: Games/Other

Url: http://cxong.github.io/cdogs-sdl
Vcs: https://github.com/cxong/cdogs-sdl

Source: %name-%version.tar
Patch: fix-build.patch

Requires: icon-theme-hicolor

Obsoletes: cdogs-data < 0.5
Provides: cdogs-data = %EVR

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ libGLU-devel libSDL2-devel
BuildRequires: libglvnd-devel libtinfo-devel libphysfs-devel libenet-devel
BuildRequires: ctest cmake libSDL2_mixer-devel libSDL2_image-devel libGL-devel
BuildRequires: libncurses++-devel libncurses-devel libncursesw-devel libtic-devel
BuildRequires: desktop-file-utils libappstream-glib libwebp-devel libtiff-devel 
BuildRequires: libtiffxx-devel libjpeg-devel libpng-devel

%description
C-Dogs SDL is a port of the old DOS arcade game C-Dogs to modern operating
systems utilizing the SDL Media Libraries. C-Dogs is an arcade shoot-em-up
which lets players work alone and cooperatively during missions or fight
against each other in the a.'dogfighta.' death-match mode. The DOS version of
C-Dogs came with several built in missions and dogfight maps. This version
does too. The author of the DOS version of C-Dogs was Ronny Wester. We would
like to thank Ronny for releasing the C-Dogs sources to the public.

%prep
%setup
%patch -p1

%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' CMakeLists.txt
# unsupported as of lcc 1.25.17
sed -i 's,-freg-struct-return,,' CMakeLists.txt
%endif

# We use the system enet
rm -r src/cdogs/enet
# Misc. cleanups
sed -i 's/\r//' doc/original_readme.txt
find graphics sounds -name "*.sh" -delete
#fixed segmentation fault
#https://github.com/cxong/cdogs-sdl/issues/888
subst 's|Mix_CloseAudio();|//Mix_CloseAudio();|' src/cdogs/sounds.c
subst 's|SoundReconfigure(s);|//SoundReconfigure(s);|' src/cdogs/sounds.c

%build
%cmake \
	-DCDOGS_DATA_DIR=/usr/share/cdogs-sdl/\
	-DUSE_SHARED_ENET=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc COPYING README.md
%_bindir/%{name}*
%_datadir/%name
%_datadir/applications/%oname.desktop
%_iconsdir/hicolor/*/apps/%oname.png
%_datadir/metainfo/%oname.appdata.xml

%changelog
* Fri Jan 30 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.4.0-alt1
- 2.3.2 -> 2.4.0
- spec cleanup

* Thu Nov 20 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.3.2-alt2
- e2k build fix

* Sun Oct 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.3.2-alt1
- 2.0.0 -> 2.3.2
- drop old patchs
- fixed segmentation fault

* Mon Jun 09 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.0.0-alt3
- NMU: fixed FTBFS

* Wed Mar 19 2025 Artyom Bystrov <arbars@altlinux.org> 2.0.0-alt2
- Add few deps in BR

* Sat Mar  9 2024 Artyom Bystrov <arbars@altlinux.org> 2.0.0-alt1
- update to new version
- fix path of appdata file

* Tue Aug  8 2023 Artyom Bystrov <arbars@altlinux.org> 1.5.0-alt1
- update to new version

* Mon Dec 05 2022 Artyom Bystrov <arbars@altlinux.org> 1.4.0-alt1
- update to new version;
- add patch for fix data path (thanks survolog@ from rosalab)

* Wed Aug 18 2021 Igor Vlasenko <viy@altlinux.org> 0.7.3-alt1_5
- e2k support

* Thu Apr 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.7.3-alt1_1
- update to new release by fcimport

* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt2
- fixed build

* Thu Dec 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.6-alt1
- Updated to upstream version 0.6.6.
- Removed dependencies on blender.

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.5-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_1
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt1_1
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_1
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_12
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt3_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_7
- rebuild with new rpm desktop cleaner

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_7
- converted from Fedora by srpmconvert script

