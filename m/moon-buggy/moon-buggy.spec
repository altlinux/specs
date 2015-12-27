# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# Enable oldstyle to have a nearly nothing requiring package after rebuilding
%global oldstyle 0

Summary:         Drive and jump with some kind of car across the moon
Name:            moon-buggy
Version:         1.0.51
Release:         alt2_16
License:         GPL+
Group:           Games/Other
URL:             http://seehuhn.de/pages/%{name}
Source0:         http://seehuhn.de/media/programs/%{name}-%{version}.tar.gz
Source1:         http://seehuhn.de/media/programs/%{name}-sound-%{version}.tar.gz
Source2:         %{name}.desktop
Source3:         %{name}-sound.desktop
Patch0:          moon-buggy-1.0.51-pause.patch
Patch1:          moon-buggy-1.0.51-sound.patch
BuildRequires:   ncurses-devel, texinfo
%if !%{oldstyle}
BuildRequires:   esound-devel, desktop-file-utils, autoconf, automake
%endif
Source44: import.info

%description
Moon-buggy is a simple character graphics game where you drive some kind
of car across the moon's surface. Unfortunately there are dangerous craters
there. Fortunately your car can jump over them! 

The game has some resemblance of the classic arcade game moon-patrol which
was released in 1982. A clone of this game was relased for the Commodore
C64 in 1983. The present, ASCII art version of moon-buggy was written many
years later by Jochen Voss.

%prep
%setup -q -a 1
%patch0 -p1 -b .pause
%if !%{oldstyle}
%patch1 -p1 -b .sound
mv -f %{name}-%{version}/* .
autoreconf -f -i
%endif

%build
%configure --sharedstatedir=%{_var}/games
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install

# Create zero-sized highscore file
touch $RPM_BUILD_ROOT%{_var}/games/%{name}/mbscore

# Install working *.desktop files and an icon
%if !%{oldstyle}
desktop-file-install --vendor "" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
desktop-file-install --vendor "" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}

install -D -p -m 644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%endif

# Some file cleanups
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o ChangeLog.utf8 ChangeLog
sed -i 's|\r$||g' ChangeLog.utf8
touch -c -r ChangeLog ChangeLog.utf8
mv -f ChangeLog.utf8 ChangeLog

iconv -f iso-8859-1 -t utf-8 -o TODO.utf8 TODO
sed -i 's|\r$||g' TODO.utf8
touch -c -r TODO TODO.utf8
mv -f TODO.utf8 TODO

%files 
%doc ANNOUNCE AUTHORS ChangeLog COPYING README THANKS
%if !%{oldstyle}
%doc README.sound
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-sound.desktop
%endif
%attr(2711,root,games) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_infodir}/%{name}.info.*
%attr(0775,root,games) %{_var}/games/%{name}
%verify(not md5 size mtime) %config(noreplace) %attr(664,root,games) %{_var}/games/%{name}/mbscore

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt2_16
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt2_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt2_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt2_12
- update to new release by fcimport

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.51-alt2_10.1
- Fixed build

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt2_10
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt2_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt1_6
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.51-alt1_5
- converted from Fedora by srpmconvert script

