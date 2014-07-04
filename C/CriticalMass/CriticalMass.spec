# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libGL-devel libSDL-devel zlib-devel
# END SourceDeps(oneline)
%define fedora 21
Name:           CriticalMass
Version:        1.5
Release:        alt2_11
Summary:        SDL/OpenGL space shoot'em up game also known as critter
Group:          Games/Other
License:        GPLv2+
URL:            http://criticalmass.sourceforge.net/critter.php
Source0:        http://downloads.sourceforge.net/criticalmass/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         CriticalMass-1.0.2-res-change-rh566533.patch
Patch1:         CriticalMass-1.5-libpng15.patch
Patch2:         CriticalMass-1.5-gcc47.patch
BuildRequires:  libSDL_image-devel libSDL_mixer-devel libpng-devel curl-devel
BuildRequires:  tinyxml-devel desktop-file-utils
Requires:       icon-theme-hicolor opengl-games-utils
# Also known as critter, so make "yum install critter" work
Provides:       critter = %{version}-%{release}
Source44: import.info

%description
Critical Mass (aka Critter) is an SDL/OpenGL space shoot'em up game. Your
world has been infested by an aggressive army of space critters. Overrun and
unprepared, your government was unable to defend its precious resources. As
a last effort to recapture some of the "goodies", you have been placed into
a tiny spacecraft and sent after them.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i 's/curl-gnutls/curl/g' configure


%build
%configure
# ./configure doesn't properly pick up our CFLAGS, and we need to override
# the CFLAGS anyways, so as to not define USE_ONLINE_UPDATE, to stop critter
# from phoning home
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE=1 -D_REENTRANT -DGAME_HAS_HERO_PARTICLE -I/usr/include/SDL"
make CFLAGS="$CFLAGS" CXXFLAGS="$CFLAGS -std=c++0x"


%install
%makeinstall_std
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/critter-wrapper

# remove unwanted utility
rm $RPM_BUILD_ROOT%{_bindir}/Packer

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
              \
%endif
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 critter.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps


%files
%doc COPYING Readme.html TODO
%{_bindir}/critter*
%{_datadir}/Critical_Mass
%{_mandir}/man6/critter.6*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/critter.png

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_10
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_9
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_8
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_6
- update to new release by fcimport

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2_5.1
- Rebuilt with libpng15

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_5
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_4
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_3
- rebuild with fixed sourcedep analyser (#27020)

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_3
- update to new release by fcimport

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- update to new release by fcimport

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_9
- converted from Fedora by srpmconvert script

