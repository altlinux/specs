# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global waddir  %{_datadir}/doom

Name:           freedoom

Version:        0.11.3
Release:        alt1_2
Summary:        Doom styled first person shooter game

Group:          Games/Other
License:        BSD
URL:            https://freedoom.github.io/
Source0:        https://github.com/freedoom/freedoom/releases/download/v0.11.3/freedoom-0.11.3.zip
Source1:        freedoom1.desktop
Source2:        freedoom2.desktop
Source3:        freedoom.png
Source4:        freedoom1.appdata.xml
Source5:        freedoom2.appdata.xml

BuildArch:      noarch
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       prboom icon-theme-hicolor
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


%prep
%setup -q


%build
# Game data files.  Nothing to build!


%install
mkdir -p %{buildroot}/%{waddir}
install -p -m 0644 freedoom1.wad freedoom2.wad %{buildroot}/%{waddir}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 %{SOURCE4} %{SOURCE5} %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.xml
ln -s /usr/share/doom/freedoom2.wad %{buildroot}%{waddir}/freedoom.wad

%files
%doc README.html CREDITS.txt
%doc COPYING.txt
%{waddir}/%{name}1.wad
%{_datadir}/appdata/%{name}1.appdata.xml
%{_datadir}/applications/%{name}1.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files -n freedoom2
%doc README.html CREDITS.txt
%doc COPYING.txt
%{waddir}/%{name}.wad
%{waddir}/%{name}2.wad
%{_datadir}/appdata/%{name}2.appdata.xml
%{_datadir}/applications/%{name}2.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
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
