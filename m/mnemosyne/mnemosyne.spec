Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%{!?qt5_qtwebengine_arches:%global qt5_qtwebengine_arches %{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}

Name:		mnemosyne
Summary:	Flash-card learning tool
Version:	2.5
Release:	alt1_3
URL:		http://www.mnemosyne-proj.org/
Source0:	https://downloads.sourceforge.net/sourceforge/mnemosyne-proj/Mnemosyne-%{version}.tar.gz
Patch0:		mnemosyne-desktop.patch
License:	AGPLv3

BuildArch:	noarch
# no python3-qt5-webengine on power64
ExclusiveArch:	noarch %{qt5_qtwebengine_arches}
BuildRequires:	desktop-file-utils
BuildRequires:	python3-devel
BuildRequires:	python3-module-distribute
Requires:	icon-theme-hicolor
Requires:	python3-module-PyQt5
Requires:	python3-module-PyQt5
Requires:	python3-module-matplotlib-qt5
Requires:	python3-module-cherrypy
Requires:	python3-module-webob
Requires:	python3-module-Pillow
Source44: import.info

%description
Mnemosyne resembles a traditional flash-card program but with an
important twist: it uses a sophisticated algorithm to schedule the best
time for a card to come up for review.

Optional dependencies:
* latex: enables entering formulas using latex syntax.

%prep
%setup -q -n Mnemosyne-%{version}
%patch0 -p1 -b .d
rm -r Mnemosyne.egg-info

%build
%python3_build

%install
%python3_install

install -d %{buildroot}%{_datadir}/applications
desktop-file-install --vendor="" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{name}.desktop

install -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps
pushd %{buildroot}/%{_datadir}/icons
mv %{name}.png hicolor/128x128/apps/%{name}.png
popd

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README
# https://bugs.launchpad.net/mnemosyne-proj/+bug/1346903
# http://bazaar.launchpad.net/~peter-bienstman/mnemosyne-proj/trunk/view/head:/mnemosyne/mnemosyne/LICENSE
#%%license docmnemosyne/libmnemosyne/LICENSE
%{_bindir}/%{name}
%{python3_sitelibdir_noarch}/%{name}
%{python3_sitelibdir_noarch}/Mnemosyne-%{version}-py%{__python3_version}.egg-info
%{python3_sitelibdir_noarch}/openSM2sync
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_3
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.6-alt1_2
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.6-alt1_1
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_3
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_1
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.4-alt1_1
- new version

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_1
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2
- update to new release by fcimport

* Fri Apr 19 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_1
- update to new release by fcimport

* Tue Feb 05 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_3.a
- fc update

* Mon Jan 28 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2.a
- update to new release by fcimport

* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_1
- update to new release by fcimport

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_1
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_1
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt2_5
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_5
- update to new release by fcimport

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.2-alt1_4.1
- Rebuild with Python-2.7

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_4
- converted from Fedora by srpmconvert script

