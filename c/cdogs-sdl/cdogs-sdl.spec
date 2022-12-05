Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-validate gcc-c++ libGLU-devel libSDL2-devel libglvnd-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#global extra_version -2

Name:           cdogs-sdl
Version:        1.4.0
Release:        alt1
Summary:        C-Dogs is an arcade shoot-em-up
# The game-engine is GPLv2+
# The game art is CC
License:        GPLv2+ and CC-BY and CC-BY-SA and CC0
URL:            http://cxong.github.io/cdogs-sdl/
Source0:        https://github.com/cxong/cdogs-sdl/archive/%{version}%{?extra_version}.tar.gz#/%{name}-%{version}%{?extra_version}.tar.gz
Patch0:         cdogs-sdl-0.5.8-cmake.patch
Patch1:         cdogs-sdl-0.7.3-fcommon-fix.patch
Patch2:			fix-build.patch
BuildRequires:  gcc
BuildRequires:  ctest cmake libSDL2_mixer-devel libSDL2_image-devel libGL-devel
BuildRequires:  libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel libphysfs-devel libenet-devel
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       icon-theme-hicolor
Obsoletes:      cdogs-data < 0.5
Provides:       cdogs-data = %{version}-%{release}
Source44: import.info

%description
C-Dogs SDL is a port of the old DOS arcade game C-Dogs to modern operating
systems utilizing the SDL Media Libraries. C-Dogs is an arcade shoot-em-up
which lets players work alone and cooperatively during missions or fight
against each other in the a.'dogfighta.' death-match mode. The DOS version of
C-Dogs came with several built in missions and dogfight maps. This version
does too. The author of the DOS version of C-Dogs was Ronny Wester. We would
like to thank Ronny for releasing the C-Dogs sources to the public.


%prep
%setup -q -n %{name}-%{version}%{?extra_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# We use the system enet
rm -r src/cdogs/enet
# Misc. cleanups
sed -i 's/\r//' doc/original_readme.txt
find graphics sounds -name "*.sh" -delete

%ifarch %e2k
# unsupported as of lcc 1.25.17
sed -i 's,-freg-struct-return,,' CMakeLists.txt
%endif



%build
%{fedora_v2_cmake} \
					-DCDOGS_DATA_DIR=/usr/share/cdogs-sdl/\
					-DUSE_SHARED_ENET=ON

%fedora_v2_cmake_build


%install
%fedora_v2_cmake_install

install -D -m 0644 build/linux/io.github.cxong.cdogs-sdl.appdata.xml %buildroot%{_datadir}/appdata/io.github.cxong.%{name}.appdata.xml
mkdir -p %buildroot%_datadir/%name/
%check
desktop-file-validate \
  $RPM_BUILD_ROOT%{_datadir}/applications/io.github.cxong.%{name}.desktop
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/io.github.cxong.%{name}.appdata.xml


%files
%doc doc/AUTHORS doc/CREDITS doc/original_readme.txt doc/README_DATA.md
%doc --no-dereference doc/COPYING.BSD doc/COPYING.GPL doc/COPYING.MJSON.txt doc/COPYING.xgetopt.txt doc/COPYING.yajl.txt doc/LICENSE.nanopb.txt doc/license.rlutil.txt
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/appdata/io.github.cxong.%{name}.appdata.xml
%{_datadir}/applications/io.github.cxong.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.cxong.%{name}.png


%changelog
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

