Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global waddir  %{_datadir}/doom

Name:           freedoom

Version:        0.13.0
Release:        alt2
Summary:        Doom styled first person shooter game

License:        BSD
URL:            https://freedoom.github.io/
Source0:        https://github.com/freedoom/freedoom/releases/download/v0.13.0/freedoom-0.13.0.zip
Source1:        freedoom1.desktop
Source2:        freedoom2.desktop
Source3:        freedoom.png
Source4:        freedoom1.appdata.xml
Source5:        freedoom2.appdata.xml
Source6:        freedm.appdata.xml
Source7:        freedm.desktop

BuildArch:      noarch
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       russian-doom icon-theme-hicolor
Source44: import.info

%description
Freedoom: Phase 1 is a Doom styled first person shooter game using the
Doom engine, featuring Four chapters, nine levels each, totalling 36
levels.

There is a massive back catalog, spanning over two decades, containing
thousands of Doom levels and other modifications (a.'modsa.') made by fans
of the original Doom game. Freedoom aims to be compatible with these and
allows most to be played without the original Doom datafiles.
Freedoom: Phase 1 aims for compatibility with The Ultimate Doom,
also known as plain Doom or Doom 1. 


%package -n     freedoom2
Group: Games/Other
Summary:        Doom2 styled first person shooter game
Requires:       prboom icon-theme-hicolor

%description -n freedoom2
Freedoom: Phase 2 is a Doom2 styled first person shooter game using the
Doom engine. Freedoom: Phase 2 has 32 levels in one long chapter,
featuring extra monsters and a double-barrelled shotgun.

There is a massive back catalog, spanning over two decades, containing
thousands of Doom levels and other modifications (a.'modsa.') made by fans
of the original Doom game. Freedoom aims to be compatible with these and
allows most to be played without the original Doom datafiles.
Freedoom: Phase 2 aims for compatibility with Doom II and Final Doom.


%package -n     freedm
Group: Games/Other
Summary:        A 32-level game designed for competitive deathmatch play.
Requires:       russian-doom icon-theme-hicolor

%description -n freedm
FreeDM is a fast-paced competitive deathmatch game, part of the Freedoom project.
Rather than the usual single-player focused levels, these contain no monsters
and are intended for deathmatch only. It is compatible with mods for Doom II.

There is a massive back catalog, spanning over two decades, containing
thousands of Doom levels and other modifications (a.'modsa.') made by fans
of the original Doom game. Freedoom aims to be compatible with these and
allows most to be played without the original Doom datafiles.
Freedoom: Phase 2 aims for compatibility with Doom II and Final Doom.

%prep
%setup -q


%build
# Game data files.  Nothing to build!


%install
mkdir -p %{buildroot}/%{waddir}
install -p -m 0644 freedoom1.wad freedoom2.wad freedm.wad %{buildroot}/%{waddir}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{SOURCE2}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{SOURCE7}
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 %{SOURCE4} %{SOURCE5} %{SOURCE6} %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.xml
ln -s /usr/share/doom/freedoom2.wad %{buildroot}%{waddir}/freedoom.wad
# create  cmdline launchers from desktop commands
mkdir -p %{buildroot}/%{_bindir}
echo "#!/bin/sh" > %{buildroot}/%{_bindir}/%{name}1
echo "#!/bin/sh" > %{buildroot}/%{_bindir}/%{name}2
echo "#!/bin/sh" > %{buildroot}/%{_bindir}/freedm
cat  %{SOURCE1} | grep "Exec" | sed "s/Exec.//" >> %{buildroot}/%{_bindir}/%{name}1
cat  %{SOURCE2} | grep "Exec" | sed "s/Exec.//" >> %{buildroot}/%{_bindir}/%{name}2
cat  %{SOURCE7} | grep "Exec" | sed "s/Exec.//" >> %{buildroot}/%{_bindir}/freedm
chmod 755 %{buildroot}/%{_bindir}/%{name}1
chmod 755 %{buildroot}/%{_bindir}/%{name}2
chmod 755 %{buildroot}/%{_bindir}/freedm

%files
%doc README.html CREDITS.txt
%doc --no-dereference COPYING.txt
%{waddir}/%{name}1.wad
%{_datadir}/appdata/%{name}1.appdata.xml
%{_datadir}/applications/%{name}1.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_bindir}/%{name}1

%files -n freedoom2
%doc README.html CREDITS.txt
%doc --no-dereference COPYING.txt
%{waddir}/%{name}.wad
%{waddir}/%{name}2.wad
%{_datadir}/appdata/%{name}2.appdata.xml
%{_datadir}/applications/%{name}2.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_bindir}/%{name}2


%files -n freedm
%doc README.html CREDITS.txt
%doc --no-dereference COPYING.txt
%{waddir}/freedm.wad
%{_datadir}/appdata/freedm.appdata.xml
%{_datadir}/applications/freedm.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_bindir}/freedm

%changelog
* Wed Jul  3 2024 Artyom Bystrov <arbars@altlinux.org> 0.13.0-alt2
- New package - FreeDM
- Switch to russian-doom

* Sat Feb 24 2024 Artyom Bystrov <arbars@altlinux.org> 0.13.0-alt1
- Update to new version

* Mon May 10 2021 Ilya Mashkin <oddity@altlinux.ru> 0.12.1-alt1
- 0.12.1
- added cmdline launchers from FC

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.11.3-alt1_6
- update to new release by fcimport

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.3-alt1_2
- NMU (for oddity@): new version by fcimport

* Mon Jan 09 2012 Ilya Mashkin <oddity@altlinux.ru> 0.7-alt1
- 0.7
- add desktop file

* Fri Jul 31 2009 Igor Zubkov <icesik@altlinux.org> 0.6.4-alt1
- 0.6.3 -> 0.6.4

* Fri Mar 20 2009 Igor Zubkov <icesik@altlinux.org> 0.6.3-alt1
- 0.6.2 -> 0.6.3

* Thu Mar 27 2008 Igor Zubkov <icesik@altlinux.org> 0.6.2-alt1
- 0.6.1 -> 0.6.2

* Sun Mar 16 2008 Igor Zubkov <icesik@altlinux.org> 0.6.1-alt1
- 0.6 -> 0.6.1

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 0.6-alt1
- 0.5 -> 0.6

* Wed Sep 27 2006 Igor Zubkov <icesik@altlinux.org> 0.5-alt1
- 0.4.1 -> 0.5

* Mon Mar 13 2006 Igor Zubkov <icesik@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Sat Jan 21 2006 Igor Zubkov <icesik@altlinux.ru> 0.4-alt1
- 0.4

* Wed Nov 09 2005 Igor Zubkov <icesik@altlinux.ru> 0.3-alt1
- Initial build for Sisyphus
