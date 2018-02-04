# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		dgae
Version:	1.1
Release:	alt4_17
Summary:	DG, a short AGI adventure game

Group:		Games/Other
License:	Public Domain
URL:		http://membres.lycos.fr/agisite/agisite.htm
Source0:	dgae.zip
#Original from http://membres.lycos.fr/agisite/dgae.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content, running dos2unix on the text file, and changing
#all filenames to lowercase for agistudio compatibility.
Source1:	dgae.desktop
Source2:	dgae-wrapper.sh
Source3:	dgae.xpm
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi, icon-theme-hicolor
Source44: import.info

%description
Help DG to seek out his twin brother's stick.
This game is a public domain: you can look out the codes and make your own
AGI game.

%prep
%setup -q -c

%build
iconv -f IBM850 -t UTF8 readme.txt > readme.txt.tmp
mv readme.txt.tmp readme.txt

%install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -D -m0644 -p * $RPM_BUILD_ROOT%{_datadir}/%{name}
install -D -m0755 -p %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}

# desktop file
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%files
%doc readme.txt
%{_datadir}/dgae
%{_datadir}/applications/dgae.desktop
%{_datadir}/icons/hicolor/32x32/apps/dgae.xpm
%{_bindir}/dgae-wrapper.sh

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_15
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_11
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7
- converted from Fedora by srpmconvert script

