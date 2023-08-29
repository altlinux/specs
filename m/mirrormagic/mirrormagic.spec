Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           mirrormagic
Version:        3.0.0
Release:        alt1_14
Summary:        Puzzle game where you steer a beam of light using mirrors
License:        GPL+
URL:            http://www.artsoft.org/mirrormagic/
Source0:        http://www.artsoft.org/RELEASES/unix/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
Patch0:         %{name}-%{version}-yesno.patch
Patch1:         %{name}-%{version}-fcommon-fix.patch
BuildRequires:  gcc
BuildRequires:  libSDL2_image-devel libSDL2_mixer-devel libSDL2_net-devel
BuildRequires:  libappstream-glib libappstream-glib-gir desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
MirrorMagic is a game where you shoot around obstacles to collect energy using
your beam. It is similar to "Mindbender" (Amiga) from the same author. The goal
is to work out how to get around obstacles to shoot energy containers with your
beam, thereby opening the path to the next level. Included are many levels
familiar from the games "Deflektor" and "Mindbender".


%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm levels/Classic_Games/classic_mindbender/*.level.orig
iconv -f ISO_8859-1 -t UTF8 CREDITS > CREDITS.tmp
touch -r CREDITS CREDITS.tmp
mv CREDITS.tmp CREDITS


%build
# parallel build has been disabled because for some unknown reason
# it leads to unknown symbols during the linking of the mirrormagic binary
make PROGBASE=%{name} RO_GAME_DIR=%{_datadir}/%{name} \
  OPTIONS="$RPM_OPT_FLAGS -DUSE_USERDATADIR_FOR_COMMONDATA" \
  EXTRA_LDFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS" sdl2


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a graphics levels music sounds $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc CREDITS
%doc --no-dereference COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png


%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt1_14
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_6
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_1
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_23
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_22
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_20
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_18
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_15
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_13
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_12
- fc update

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt5_9
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt4_9
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt4_8
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt3_8
- rebuild with new rpm desktop cleaner

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_8
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_8
- converted from Fedora by srpmconvert script

