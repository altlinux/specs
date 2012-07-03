# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           rafkill
Version:        1.2.3
Release:        alt4_9
Summary:        Top-down shooter with powerups
Group:          Games/Other
License:        GPLv2
URL:            http://raptorv2.sourceforge.net/
Source0:        http://downloads.sourceforge.net/raptorv2/%{name}-%{version}.tar.gz
Source1:        rafkill.desktop
Source2:        rafkill.6
Source3:        rafkill.png
Patch0:         rafkill-1.2.2-shatter-crash.patch
Patch1:         rafkill-1.2.2-gcc43.patch
Patch2:		rafkill-1.2.3-gcc470.patch
BuildRequires:  liballegro-devel dumb-devel scons desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Rafkill is a vertical scrolling shoot-em up game. You can collect powerups
during gameplay and you can goto the store with your spaceship and buy
powerups or even a complete new ship with the points you've earned sofar.


%prep
%setup -q 
%patch0 -p1 -z .shatter
%patch1 -p1 -z .gcc43
%patch2 -p0 -z .gcc470
# sigh hack hack hack
FLAGS=""
for i in $RPM_OPT_FLAGS; do
  FLAGS="$FLAGS '$i',"
done
FLAGS="$FLAGS '-DINSTALL_DIR=\\\\\\\\\"%{_datadir}\\\\\\\\\"'"
sed -i "s!flags = .*!flags = [ $FLAGS ];!" SConstruct


%build
scons prefix=%{_datadir}


%install
#scons won't install into a buildroot, only into the real root so DIY
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name} $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a data music $RPM_BUILD_ROOT%{_datadir}/%{name}
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/*/.sconsign
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/data/*.h

# manpage courtesy of Debian
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man6 

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps


%files
%doc README COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt4_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt3_8
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt3_7
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt3_6
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt2_6
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_6
- converted from Fedora by srpmconvert script

