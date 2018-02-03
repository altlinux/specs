# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		naturette
Version:	1.3
Release:	alt4_15
Summary:	An AGI adventure game

Group:		Games/Other
License:	Redistributable, no modification permitted
URL:		http://membres.lycos.fr/agisite/rette.htm
Source0:	rette13e.zip
#Original from http://membres.lycos.fr/agisite/rette13e.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content.
Source1:	naturette.desktop
Source2:	naturette-wrapper.sh
Source3:	naturette.xpm
Source4:	naturette-LICENSE.fedora
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi, icon-theme-hicolor
Source44: import.info

%description
Naturette was made using AgiStudio. Naturette must find eight 
diamonds to go back to her house. Contains nude scenes.

%prep

%setup -q -c

#drop case
mv LOGDIR logdir
mv OBJECT object
mv PICDIR picdir
mv SNDDIR snddir
mv VIEWDIR viewdir
mv VOL.0 vol.0
mv WORDS.TOK words.tok

#char fix
sed -i 's/\r//' Readme.txt

%build
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
%doc Readme.txt naturette-LICENSE.fedora
%{_datadir}/naturette
%{_datadir}/applications/naturette.desktop
%{_datadir}/icons/hicolor/32x32/apps/naturette.xpm
%{_bindir}/naturette-wrapper.sh

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_15
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_13
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_9
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt4_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt3_6
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt3_5
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_5
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_5
- converted from Fedora by srpmconvert script

