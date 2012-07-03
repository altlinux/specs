Name:           vegastrike-music
Version:        0.5.1
Release:        alt2_2.r1
Summary:        Music for Vega Strike
Group:          Games/Other
License:        GPL+
URL:            http://vegastrike.sourceforge.net/
# Despite the confusing LICENSE.STANDALONE file, this is all fully GPL licensed
# see: http://vegastrike.sourceforge.net/forums/viewtopic.php?p=97573#97573
#Source0:        %{name}-%{version}.tar.gz
Source0:        http://downloads.sourceforge.net/vegastrike/vegastrike-music-0.5.1.r1.tar
Source1:        http://downloads.sourceforge.net/vegastrike/vegastrike-speech-0.5.1.r1.tar
BuildArch:      noarch
Requires:       vegastrike-data >= %{version}
Source44: import.info

%description
Music for Vega Strike, a GPL 3D OpenGL Action RPG space sim that allows
a player to trade and bounty hunt. This archive contains the music files
necessary to hear music in VegaStrike. These files are *not* essential to
play the game.

%package -n vegastrike-speech
summary: Vocal sounds for Vega Strike
Group:          Games/Other
Requires:       vegastrike-data >= %{version}

%description -n vegastrike-speech
Vocal sounds for Vega Strike, a GPL 3D OpenGL Action RPG space sim that allows
a player to trade and bounty hunt. This archive contains vocal sounds and
are *not* essential to play the game.

%prep
%setup -q -b1 -n vegastrike-speech-%{version}.r1
cd ..
%setup -q -n %{name}-%{version}.r1
cd ..
mv vegastrike-speech-%{version}.r1/* %{name}-%{version}.r1
cd %{name}-%{version}.r1
mv music/AUTHORS music/COPYING .
# The files are GPL
rm -f music/LICENSE.STANDALONE

# A copy of a spec file is in the music directory, that we don't want.
rm -f music/vegastrike-music.spec

# Some of the data files are marked executable and they shouldn't be
find . -type f -exec chmod a-x '{}' ';'

%build
# nothing to build data only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vegastrike
cp -r music communications sounds $RPM_BUILD_ROOT%{_datadir}/vegastrike

%files -n vegastrike-speech
%{_datadir}/vegastrike/communications
%{_datadir}/vegastrike/sounds

%files
%doc AUTHORS COPYING
%{_datadir}/vegastrike/music


%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_2.r1
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_0.2.beta1
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_0.2.beta1
- update to new release by fcimport

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_0.1.beta1
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_5
- converted from Fedora by srpmconvert script

