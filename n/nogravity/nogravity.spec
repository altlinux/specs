Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           nogravity
Version:        2.00
Release:        alt2_49
Summary:        Space shooter in 3D
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.realtech-vr.com/nogravity/
Source0:        http://downloads.sourceforge.net/%{name}/rt-%{name}-src.zip
Source2:        %{name}.desktop
Source3:        %{name}.png
Source4:        nogravity--Makefile.am
Source5:        nogravity--bootstrap
Source6:        nogravity--configure.in
Source7:        nogravity.sh
Source8:        %{name}.appdata.xml
Patch0:         nogravity--snd_sdlmixer_c-powerpc-fix.diff
Patch1:         nogravity--fullscreen_as_option.patch
Patch2:         nogravity--fixed_path_to_game_data.diff
Patch3:         nogravity--64-bit.patch
Patch4:         nogravity--cvs.patch
Patch5:         nogravity--openal.patch
# See: https://www.redhat.com/archives/fedora-games-list/2007-June/msg00000.html
Patch6:         nogravity--README.patch
Patch7:         nogravity--bufer-overflows.patch
Patch8:         nogravity--strcpy-abuse.patch
Patch9:         nogravity-2.00-rhbz699274.patch
Patch10:        nogravity-2.00-libpng15.patch
Patch11:        0001-v3xscene-Remove-some-unused-code.patch
Patch12:        0002-rlx32-Stop-using-MaxExtentableObjet.patch
Patch13:        nogravity-2.00-stdint_h.patch
Patch14:        nogravity--gcc6.patch
Patch15:        nogravity-2.00-build-fixes.patch
Requires:       %{name}-data = %{version}
BuildRequires:  gcc-c++
BuildRequires:  libSDL_mixer-devel libopenal-devel libpng-devel libpng17-tools libvorbis-devel
BuildRequires:  automake desktop-file-utils libappstream-glib libappstream-glib-gir
BuildRequires:  zlib-devel
Requires:       icon-theme-hicolor mesa-gears mesa-info
Source44: import.info
Patch33: nogravity-2.00-alt-libpng15.patch

%description
No Gravity is a fantastic and futuristic universe made of five
intergalactic worlds. An arcade type game with great play-ability,
where it is easy to plunge into space battles against space-fighters,
space stations and more!


%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
#patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

cp %{SOURCE4} ./src/Linux/Makefile.am
cp %{SOURCE5} ./src/Linux/bootstrap
cp %{SOURCE6} ./src/Linux/configure.in
sed -i 's/\r//g' GNU.TXT README.TXT
pushd src/Linux
sh bootstrap
popd
%patch33 -p2


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
export CFLAGS="%optflags -std=gnu17"
pushd src/Linux

%configure --enable-sound=sdl_mixer --disable-opengl
%make_build LDADD=-lz
mv %{name} %{name}-software

make distclean

%configure --enable-sound=openal --enable-opengl
%make_build LDADD=-lz
mv %{name} %{name}-opengl

popd


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -m 755 src/Linux/%{name}-software $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/Linux/%{name}-opengl   $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/%{name}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README.TXT
%doc --no-dereference GNU.TXT
%{_bindir}/%{name}*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Thu Apr 23 2026 Andrew A. Vasilyev <andy@altlinux.org> 2.00-alt2_49
- NMU: fix FTBFS with gcc15

* Sat Mar 14 2026 Andrew A. Vasilyev <andy@altlinux.org> 2.00-alt2_48
- NMU: fix FTBFS

* Tue Apr 08 2025 Igor Vlasenko <viy@altlinux.org> 2.00-alt2_47
- update to new release by fcimport

* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 2.00-alt2_37
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_29
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_28
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_26
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_25
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_23
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_22
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_21
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_20
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_19
- update to new release by fcimport

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_18
- fc update

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.00-alt2_17.1
- Rebuilt with libpng15

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_17
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_16
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_15
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_15
- update to new release by fcimport

* Mon Dec 12 2011 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_14
- updated by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_12
- converted from Fedora by srpmconvert script

