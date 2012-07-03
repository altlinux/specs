# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           beneath-a-steel-sky-cd
Version:        0.0372
Release:        alt4_6
Summary:        Beneath a Steel Sky - Adventure Game - CD version
Group:          Games/Other
# For further discussion on distribution rights see:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
License:        Freely redistributable without restriction
URL:            http://www.revolution.co.uk/_display.php?id=16
Source0:        http://dl.sf.net/sourceforge/scummvm/bass-cd-1.2.zip
Source1:        %{name}.desktop
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Requires:       scummvm >= 0.9.1 icon-theme-hicolor
Source44: import.info

%description
After the Dungeons and Dragons fantasy setting of Revolution's first game, Lure
of the Temptress, Revolution decided to go down a completely different avenue
with its second adventure game, Beneath a Steel Sky, that of Science Fiction.
A bleak vision of the future was imagined, where mind control and medical
science combined forces to repress the populace. Leading comic artist, Dave
Gibbons, joined the design team to visualise this desperate landscape. The
result is the cult classic Beneath a Steel Sky.

This package contains the CD version, which contains additional / longer
cutscenes and voice acting, but also is much larger: 70 MB where as the also
available floppy version (package name beneath-a-steel-sky) is only 8 MB.


%prep
%setup -q -n bass-cd-1.2


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
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.0372-alt4_6
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.0372-alt3_6
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.0372-alt3_5
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.0372-alt2_5
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.0372-alt1_5
- converted from Fedora by srpmconvert script

