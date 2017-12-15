# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-validate gcc-c++ libGLU-devel libSDL2-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#global extra_version -2

Name:           cdogs-sdl
Version:        0.6.6
Release:        alt1
Summary:        C-Dogs is an arcade shoot-em-up
Group:          Games/Other
# The game-engine is GPLv2+
# The game art is CC
License:        GPLv2+ and CC-BY and CC-BY-SA and CC0
URL:            http://cxong.github.io/cdogs-sdl/

Source0:        https://github.com/cxong/cdogs-sdl/archive/%{version}%{?extra_version}.tar.gz#/%{name}-%{version}%{?extra_version}.tar.gz
Patch0:         cdogs-sdl-0.5.8-cmake.patch
Patch1:         cdogs-sdl-0.6.6-alt-install-icons.patch
Source44:       import.info

BuildRequires:  ctest cmake libSDL2_mixer-devel libSDL2_image-devel libGL-devel
BuildRequires:  libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel libphysfs-devel libenet-devel
BuildRequires:  desktop-file-utils libicns-utils libappstream-glib

Requires:       icon-theme-hicolor
Obsoletes:      cdogs-data < 0.5
Provides:       cdogs-data = %EVR

# don't depend on blender just for helper scripts
%add_findreq_skiplist %_datadir/%{name}/graphics/chars/*/render.py*
%add_findreq_skiplist %_datadir/%{name}/graphics/chars/*/make_spritesheet.sh
%add_findprov_skiplist %_datadir/%{name}/graphics/chars/*/render.py*
%add_findprov_skiplist %_datadir/%{name}/graphics/chars/*/make_spritesheet.sh

%description
C-Dogs SDL is a port of the old DOS arcade game C-Dogs to modern operating
systems utilising the SDL Media Libraries. C-Dogs is an arcade shoot-em-up
which lets players work alone and cooperatively during missions or fight
against each other in the a.'dogfighta.' deathmatch mode. The DOS version of
C-Dogs came with several built in missions and dogfight maps. This version
does too. The author of the DOS version of C-Dogs was Ronny Wester. We would
like to thank Ronny for releasing the C-Dogs sources to the public.

%prep
%setup -q -n %{name}-%{version}%{?extra_version}
%patch0 -p1 -b .cmake
%patch1 -p2
# We use the system enet
rm -r src/cdogs/enet
# Misc. cleanups
sed -i 's/\r//' doc/original_readme.txt
rm graphics/make_bullet_spritesheet.sh
chmod -x src/tinydir/tinydir.h


%build
%{fedora_cmake} -DCDOGS_DATA_DIR=/usr/share/cdogs-sdl/ -DUSE_SHARED_ENET=1
%make_build
icns2png -x build/macosx/cdogs-icon.icns

%install
%makeinstall_std

desktop-file-validate %buildroot%_desktopdir/%{name}.desktop

appstream-util validate-relax --nonet \
  %buildroot%_datadir/appdata/%{name}.appdata.xml

%files
%doc doc/AUTHORS doc/CREDITS doc/original_readme.txt doc/README_DATA.md
%doc doc/COPYING.BSD doc/COPYING.GPL doc/COPYING.MJSON.txt doc/COPYING.xgetopt.txt doc/COPYING.yajl.txt doc/LICENSE.nanopb.txt doc/license.rlutil.txt
%_bindir/%{name}*
%_datadir/%name
%_datadir/appdata/%{name}.appdata.xml
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/*/apps/%{name}-icon.png

%changelog
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

