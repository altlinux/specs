Name:           asc-music
Version:        1.0
Release:        alt2_6
Summary:        Background music for the game asc
Group:          Games/Other
License:        GPLv2+
URL:            http://www.asc-hq.org/
# transcoded from: http://downloads.sourceforge.net/asc-hq/*.mp3
Source0:        %{name}-%{version}.tar.gz
Buildarch:      noarch
Requires:       asc
Source44: import.info

%description
Music created by Michael Kievernagel for the game Advanced Strategic Command
(asc).

Note that if you have run asc before installing the music you must remove the
asc cache file: $HOME/.asc/asc.cache, otherwise asc will not find the music.


%prep
%setup -q


%build
# nothing todo content only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/asc/music
install -p -m 644 *.ogg $RPM_BUILD_ROOT%{_datadir}/asc/music


%files
%doc README.fedora
%{_datadir}/asc/music


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6
- update to new release by fcimport

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- converted from Fedora by srpmconvert script

