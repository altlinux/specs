# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           drascula-music
Version:        1.0
Release:        alt2_11
Summary:        Background music for Drascula: The Vampire Strikes Back
Group:          Games/Other
# For further discussion on distribution rights see:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
License:        Freely redistributable without restriction
URL:            http://wiki.scummvm.org/index.php/Drascula:_The_Vampire_Strikes_Back
Source0:        http://downloads.sourceforge.net/scummvm/drascula-audio-%{version}.zip
Buildarch:      noarch
Requires:       drascula
Source44: import.info

%description
Background music for Drascula: The Vampire Strikes Back.


%prep
%setup -q -c


%build
# nothing todo content only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/drascula
install -p -m 644 audio/*.ogg $RPM_BUILD_ROOT%{_datadir}/drascula


%files
%doc readme.txt
%{_datadir}/drascula/*.ogg


%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_6
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_5
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4
- converted from Fedora by srpmconvert script

