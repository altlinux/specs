# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
Name:           flight-of-the-amazon-queen
Version:        1.0
Release:        alt4_13
Summary:        Flight of the Amazon Queen - Adventure Game
Group:          Games/Other
# For further discussion on distribution rights see:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
License:        Freely redistributable without restriction
URL:            http://www.scummvm.org/downloads.php
Source0:        http://downloads.sourceforge.net/scummvm/FOTAQ_Floppy.zip
Source1:        %{name}.desktop
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Requires:       scummvm >= 0.9.1
Source44: import.info

%description
It is 1949 and you play Joe King, pilot for hire with his small private plane
the 'Amazon Queen'. The game is a spoof of old timey radio adventure serials,
and as it begins we find Joe in one of those typical situations. It is 11:58
and 36 seconds and counting, Joe and his date are tied up in an abandoned
warehouse ("you really know how to show a girl a good time, Joe!"), and a bomb
is set to go off at midnight!

Of course they escape, in the nick of time, and immediately set us up for the
next 'adventure'. Joe suddenly remembers that he is scheduled to fly the famous
movie star, Faye Russell, to a photo shoot in the Amazon jungle the next
morning.

Notice that this package contains the floppy version, the CD version is also
available in the %{name}-cd package. The CD version contains
additional / longer cutscenes and voice acting, but also is much larger: the CD
version ways in at 37 MB where as this version is only 7 MB.


%prep
%setup -q -n FOTAQ_Floppy


%build
# Nothing to build data only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 queen.1 $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}


%files
%doc readme.txt
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_10
- update to new release by fcimport

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_6
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_5
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_5
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- converted from Fedora by srpmconvert script

