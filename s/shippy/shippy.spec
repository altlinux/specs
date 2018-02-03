# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           shippy
Version:        1.3.3.7
Release:        alt2_25
Summary:        Space invaders / Galaxians like game with powerups
Group:          Games/Other
License:        GPL+
URL:            http://www.shippysite.com/
Source0:        http://downloads.sourceforge.net/ship84/shipv%{version}UNIX.zip
Source1:        shippy.png
Source2:        shippy.desktop
Source3:        shippy.sh
Source4:        %{name}.appdata.xml
Patch0:         shippy-merged.patch
Patch1:         shippy-improved-splash.patch
BuildRequires:  dumb-devel libSDL_mixer-devel
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       %{name}-common = %{version}
Provides:       %{name}-engine = %{version}
Source44: import.info

%description
Shippy1984 is a small, portable game designed to bring back nostalgia for the
ways games used to be made--addicting as hell! Mash buttons on your way to the
high score! Shippy1984 is designed from the ground up for the avid casual
gamer who feels left behind by the technological overload of today's games!
No longer! Shippy1984 is the game you have been waiting for!


%package allegro
Summary:	Shippy1984 Allegro version
Group:		Games/Other
Requires:	%{name}-common = %{version}
Provides:       %{name}-engine = %{version}

%description allegro
Alternative version of Shippy1984 compiled to use the allegro display library.


%package common
Summary:	Shippy1984 common files
Group:		Games/Other
Requires:       %{name}-engine = %{version}
Requires:       icon-theme-hicolor

%description common
Data files, desktop entry and icon, docs and wrapper-script for the
Shippy1984 game.


%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
sed -i 's/\r//' NOTES.txt LICENSE.txt docs/manual.html
mv docs html
mv data/splash2.bmp data/splash.bmp
#see comment in %%install
rm data/scores.lst


%build
%make_build SDL=1 \
 CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DDATADIR=\\\"%{_datadir}/%{name}/\\\"" \
 LDFLAGS="-g `sdl-config --libs` -lSDL_mixer"
mv %{name} %{name}-sdl

%make_build ALLEGRO=1 \
 CFLAGS="$RPM_OPT_FLAGS -fsigned-char -DDATADIR=\\\"%{_datadir}/%{name}/\\\"" \
 LDFLAGS="-g -laldmb -ldumb `allegro-config --libs`"
mv %{name} %{name}-allegro


%install
# no make install target so DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 755 %{name}-sdl %{name}-allegro $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -p -m 644 data/* $RPM_BUILD_ROOT%{_datadir}/%{name}
# scores.lst is a binary file which is different on MSB vs LSB, so we just
# create an empty file, then the game will use its identical internal defaults
# and fill it with data in platform format after the first run.
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/games
touch $RPM_BUILD_ROOT%{_var}/lib/games/%{name}.hs
# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%attr(2711,root,games) %{_bindir}/%{name}-sdl

%files allegro
%attr(2711,root,games) %{_bindir}/%{name}-allegro

%files common
%doc NOTES.txt html
%doc --no-dereference LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%config(noreplace) %attr (0664,root,games) %{_var}/lib/games/%{name}.hs


%changelog
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

