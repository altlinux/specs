# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%define snapshot 20060225
Name:           duel3
Version:        0.1
Release:        alt3_0.12.20060225
Summary:        One on one spaceship duel in a 2D arena
Group:          Games/Other
License:        BSD
# Upstream has vanished
#URL:            http://ts-games.com/duel3.php
Source0:        http://downloads.sourceforge.net/%{name}/Duel3_%{snapshot}_src.zip
Source1:        http://downloads.sourceforge.net/%{name}/Duel3_%{snapshot}_bin.zip
Source2:        %{name}.desktop
Source3:        %{name}.png
Source4:        music-credits.txt
Patch0:         Duel3_20060225-fixes.patch
Patch1:         Duel3_20060225-windowed-mode.patch
Patch2:         Duel3_20060225-fix-buf-oflow.patch
Patch3:         Duel3_20060225-extra-fix-buf-oflow.patch
BuildRequires:  liballegro-devel dumb-devel libGLU-devel desktop-file-utils
Requires:       icon-theme-hicolor opengl-games-utils
Source44: import.info
Patch33: Duel3_20060225-alt-as-needed.patch

%description
The sudden attack from the Martain Rim miners caught the Earth by surprise,
there was no way the meager Earth Space Fleet could defend themselves. The
miners attacked, and eliminated their enemies, and then returned to the
asteroid belt. However, Earth could not accept such an embarrassing defeat. The
military developed new space fighters, and trained several squadrons of elite
pilots. The task force was then deployed against the miners. These trained
pilots utterly defeated the miners in a matter of weeks, and the first space
war in human history was finished.

The military, however, now had a new problem on their hands. These new elite
pilots were becoming restless, and there was no way for them to test their
skills. The military dare not disband the force, or let their skills dull, so
the Duel Combat League was formed. The newly formed league quickly became the
premier entertainment form on the planet, and the military's largest source of
income.

Take control of a Duel fighter, and test your skills against your opponents and
the arena itself in fast-paced space combat.


%prep
%setup -q -a 1 -n Duel3_%{snapshot}_src
mv Duel3_%{snapshot}_bin/* Source
cp %{SOURCE4} .
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i 's/\r//' Source/readme.txt license.txt music-credits.txt
iconv -f iso8859-1 -t utf-8 music-credits.txt > temp
mv temp music-credits.txt
%patch33 -p0


%build
pushd Source
make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations -Wno-non-virtual-dtor"
popd


%install
pushd Source
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps


%files
%doc Source/readme.txt license.txt music-credits.txt
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png


%changelog
* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_0.12.20060225
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_0.11.20060225
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_0.11.20060225
- update to new release by fcimport

* Mon Oct 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_0.10.20060225
- bugfix release

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_0.10.20060225
- initial release by fcimport

