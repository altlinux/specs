Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           clonekeen
Version:        0.8.4
Release:        alt1_28
Summary:        "Commander Keen: Invasion of the Vorticons" clone
License:        GPLv3+
URL:            http://clonekeen.sourceforge.net/
# We make a clean tarball by removing bin/data/sound*
# from http://clonekeen.sourceforge.net/files/%%{name}-src-84.tar.gz
Source0:        %{name}-src-84-clean.tar.gz
# This are the .dat files and the extra (GPL) levels from 
# http://downloads.sourceforge.net/%%{name}/CKBeta83_Bin_W32.zip
# The pristine upstream .zip's aren't used because the included sounds.ck?
# files are property of id Software
Source1:        %{name}-0.8.4-data.tar.gz
Source2:        extract.c
Source3:        clonekeen-extract-sounds.c
Source4:        %{name}.sh
Source5:        %{name}.autodlrc
Source6:        %{name}.desktop
Source7:        %{name}.png
Patch0:         %{name}-0.8.4-noSDLmain.patch
Patch1:         %{name}-0.8.4-fcommon-fix.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libSDL_mixer-devel libdynamite-devel desktop-file-utils
Requires:       icon-theme-hicolor autodownloader
Source44: import.info

%description
CloneKeen is an almost complete clone of the old classic DOS game,
"Commander Keen: Invasion of the Vorticons" by by id Software:
http://www.idsoftware.com/
CloneKeen requires the original id Software gamedata files to work.

If you posess the original DOS games. You can play all three episodes of the
game. If you don't, you can can still play the shareware episode one. Which can
be freely downloaded from Apogee, but cannot be distributed as a part of
Fedora. When you start CloneKeen for the first time it will offer to download
the shareware datafiles for you.


%prep
%setup -q -a 1 -n keen
%patch0 -p1
%patch1 -p1

find -name "*.o" -delete
cp -a %{SOURCE2} %{SOURCE3} .
sed -i 's/\r//g' README src/changelog.txt


%build
%global build_type_safety_c 0
%make_build -C src -f Makefile
gcc -o %{name}-extract $CFLAGS extract.c -ldynamite
gcc -o %{name}-extract-sounds $CFLAGS %{name}-extract-sounds.c


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/data
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/gfx

install -m 755 src/keen $RPM_BUILD_ROOT%{_libexecdir}/%{name}
install -m 755 %{name}-extract $RPM_BUILD_ROOT%{_libexecdir}
install -m 755 %{name}-extract-sounds $RPM_BUILD_ROOT%{_libexecdir}
install -p -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 bin/*.dat  $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 bin/*.ini  $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 bin/gfx/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/gfx
install -p -m 644 bin/data/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data
install -p -m 644 bin/*.ck1  $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE6}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE7} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps

sed -i s,/usr/libexec,%{_libexecdir},g %buildroot%{_libexecdir}/%{name}* %buildroot%{_bindir}/%{name}

%files
%doc README src/changelog.txt
%{_bindir}/%{name}
%{_libexecdir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.8.4-alt1_28
- update to new release by fcimport

* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 0.8.4-alt1_26
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_19
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_10
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_8
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_4
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_3
- update to new release by fcimport

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt2_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt2_9
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_9
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_8
- converted from Fedora by srpmconvert script

