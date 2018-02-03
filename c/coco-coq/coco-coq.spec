# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		coco-coq
Version:	0.1
Release:	alt4_16
Summary:	Coco Coq in Grostesteing's base, an AGI adventure game

Group:		Games/Other
License:	Redistributable, no modification permitted
URL:		http://membres.lycos.fr/agisite/coco-c.htm
Source0:	cococe.zip
#Original from http://membres.lycos.fr/agisite/cococe.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content.
Source1:	coco-coq.desktop
Source2:	coco-coq-wrapper.sh
Source3:	coco-coq.xpm
Source4:	coco-coq-LICENSE.fedora
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi, icon-theme-hicolor
Source44: import.info

%description
Grostesteing is back for troubles: he's kidnapped the Coco Coq's friends
to turn them into monsters. Coco must go inside the deadly base, avoids 
traps, free his friends and beat the bad scientist Grostesteing.

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
%doc coco-coq-LICENSE.fedora
%{_datadir}/coco-coq
%{_datadir}/applications/coco-coq.desktop
%{_datadir}/icons/hicolor/32x32/apps/coco-coq.xpm
%{_bindir}/coco-coq-wrapper.sh

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_16
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_14
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_10
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_7
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_7
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_6
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_6
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_6
- converted from Fedora by srpmconvert script

