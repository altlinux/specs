# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		sergueis-destiny
Version:	1.1
Release:	alt4_17
Summary:	Serguei's Destiny, an AGI adventure game

Group:		Games/Other
License:	Redistributable, no modification permitted
URL:		http://membres.lycos.fr/agisite/serguei.htm
Source0:	serguei.zip
#Original from http://membres.lycos.fr/agisite/serguei.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content, running dos2unix on the text file, and changing
#all filenames to lowercase for agistudio compatibility.
Source1:	sergueis-destiny.desktop
Source2:	sergueis-destiny-wrapper.sh
Source3:	sergueis-destiny.xpm
Source4:	sergueis-destiny-LICENSE.fedora
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi, icon-theme-hicolor
Source44: import.info

%description
A bad wizard Blackmagic has cast his evil spell to the peaceful village
Jolimy. 50 years later, an apprentice sorcerer Serguei must break the
Blackmagic's spell and free Jolimy.

%prep
%setup -q -c

%build
iconv -f IBM850 -t UTF8 serguei.txt > tmp
mv tmp serguei.txt
cp %{SOURCE4} .

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
%doc serguei.txt sergueis-destiny-LICENSE.fedora
%{_datadir}/sergueis-destiny
%{_datadir}/applications/sergueis-destiny.desktop
%{_datadir}/icons/hicolor/32x32/apps/sergueis-destiny.xpm
%{_bindir}/sergueis-destiny-wrapper.sh

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_15
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_11
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7
- converted from Fedora by srpmconvert script

