# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           beneath-a-steel-sky
Version:        1.3
Release:        alt4_3
Summary:        Beneath a Steel Sky - Adventure Game
Group:          Games/Other
# For further discussion on distribution rights see:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
License:        Freely redistributable without restriction
URL:            http://www.revolution.co.uk/_display.php?id=16
Source0:        http://downloads.sourceforge.net/scummvm/BASS-Floppy-%{version}.zip
Source1:        %{name}.desktop
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Requires:       scummvm >= 0.12.0
Obsoletes:      bass <= 0-8
Provides:       bass = 0-8
Source44: import.info

%description
After the Dungeons and Dragons fantasy setting of Revolution's first game, Lure
of the Temptress, Revolution decided to go down a completely different avenue
with its second adventure game, Beneath a Steel Sky, that of Science Fiction.
A bleak vision of the future was imagined, where mind control and medical
science combined forces to repress the populace. Leading comic artist, Dave
Gibbons, joined the design team to visualise this desperate landscape. The
result is the cult classic Beneath a Steel Sky.

Notice that this package contains the floppy version, the CD version is also
available in the %{name}-cd package. The CD version contains
additional / longer cutscenes and voice acting, but also is much larger: the CD
version ways in at 70 MB where as this version is only 8 MB.


%prep
%setup -q -c


%build
# Nothing to build data only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 sky.* $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}


%files
%doc readme.txt
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_3
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt3_3
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt3_2
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_2
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2
- converted from Fedora by srpmconvert script

