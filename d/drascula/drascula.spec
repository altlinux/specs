# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
Name:		drascula
Version:	1.0
Release:	alt2_14
Summary:	The Vampire Strikes Back
Group:		Games/Other
# For further discussion on distribution rights see:
# http://www.redhat.com/archives/fedora-extras-list/2006-November/msg00030.html
License:	Freely redistributable without restriction
URL:		http://www.scummvm.org/downloads.php
Source0:	http://downloads.sourceforge.net/scummvm/%{name}-%{version}.zip
#Source1:	http://scummvm.svn.sourceforge.net/svnroot/scummvm/scummvm/tags/release-0-12-0/dists/engine-data/drascula.dat
#Source2:	http://downloads.sourceforge.net/scummvm/%{name}-audio-%{version}.zip
Source3:	%{name}.desktop
BuildRequires:	desktop-file-utils
BuildArch:	noarch
Requires:	scummvm >= 0.12.0
Source44: import.info

%description
You play the role of John Hacker, a British estate agent, who travels to a
small village of Transylvania in order to negotiate the sale of some ground
of Gibraltar with the Count Drascula. 
But unfortunately Hacker is not aware of who is Drascula in reality: the most
terrible vampire with just one idea on his mind: DOMINATING the World
demonstrating that he is even more evil than his brother Vlad.

Notice that music for the game is available as an addon in the separate
drascula-music package. As are Spanish, German, French and Italian subtitles
in the drascula-international package.



%prep
%setup -q -n %{name} -c %{name}


%build
# Nothing to build, data only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 Packet.001 $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE3}


%files
%doc readme.txt drascula.doc
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop



%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_8
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7
- converted from Fedora by srpmconvert script

