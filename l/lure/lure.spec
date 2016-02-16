# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
Name:           lure
Version:        1.1
Release:        alt2_13
Summary:        Lure of the Temptress - Adventure Game
Group:          Games/Other
# For further discussion on distribution rights see:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
License:        Freely redistributable without restriction
URL:            http://www.revolution.co.uk/_display.php?id=10
Source0:        http://downloads.sourceforge.net/scummvm/%{name}-%{version}.zip
Source1:        %{name}.desktop
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Requires:       scummvm >= 0.12.0
Source44: import.info

%description
Lure of the Temptress was Revolution's very first adventure game and work began
on it in 1989, even before Revolution's inception as an actual games
development company. From the start our aim was to consider the contemporary
adventures of the day and then bring something new to the genre. From this came
the Virtual Theatre engine. VT allowed in-game characters to wander around the
gameworld indepently of each other, living their own lives and doing their own
thing. Another feature allowed the player to give direct orders to Helper
characters - in this case Ratpouch - who would then go off to perform the task.

The result is a quirky and entertaining adventure game that kicked off
Revolution's fondness for characterisation and in-game humour.


%prep
%setup -q -n %{name}
sed -i 's/\r//g' notes.txt README


%build
# Nothing to build data only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 *.vga *.ega $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}


%files
%doc *.txt Manual.pdf PROTECT.PDF README
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop


%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_10
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5
- converted from Fedora by srpmconvert script

