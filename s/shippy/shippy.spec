%define _unpackaged_files_terminate_build 1

Name: shippy
Version: 1.5.6
Release: alt1

Summary: Space invaders / Galaxians like game with power-ups
License: GPL-2.0-or-later
Group: Games/Other

Obsoletes: shippy-allegro <= 1.5.0-alt1_1
Obsoletes: shippy-common <= 1.5.0-alt1_1

Url: http://identicalsoftware.com/shippy1984
Vcs: https://github.com/dulsi/shippy1984

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: gcc cmake
BuildRequires: dumb-devel libSDL2_mixer-devel pkgconfig(SDL2_ttf)
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: /usr/bin/desktop-file-install fontconfig-devel

%description
Shippy1984 is a small, portable game designed to bring back nostalgia for the
ways games used to be made--addicting as hell! Mash buttons on your way to the
high score! Shippy1984 is designed from the ground up for the avid casual
gamer who feels left behind by the technological overload of today's games!
No longer! Shippy1984 is the game you have been waiting for!

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
cp -a data/%name.ogg %buildroot%_datadir/%name/%name.ogg

%files
%doc --no-dereference LICENSE.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/metainfo/%name.metainfo.xml
%_datadir/%name

%changelog
* Mon Aug 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.5.6-alt1
- 1.5.0 -> 1.5.6
- spec cleanup
- builded with cmake
- dropped old patches

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_25
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_24
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_22
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_19
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_18
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_17
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_16
- update to new release by fcimport

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_15
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_14
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_13
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt2_12
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt1_12
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt1_11
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.3.3.7-alt1_10
- converted from Fedora by srpmconvert script

