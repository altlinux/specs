Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
Name:		mnemosyne
Summary:	Flash-card learning tool
Version:	2.3.5
Release:	alt1_1
URL:		http://www.mnemosyne-proj.org/
Source0:	http://downloads.sourceforge.net/sourceforge/mnemosyne-proj/Mnemosyne-%{version}.tar.gz
Patch0:		mnemosyne-desktop.patch
License:	AGPLv3

BuildArch:	noarch
BuildRequires:	desktop-file-utils
BuildRequires:	python-devel
BuildRequires:	python-module-setuptools
Requires:	icon-theme-hicolor
Requires:	python-module-PyQt4
Requires:	python-module-matplotlib-qt4
# Until bug #1219556 is fixed
Requires:	python-module-matplotlib-qt5
Requires:	python-module-cherrypy
Requires:	python-module-webob
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

%build
%python_build

%install
%python_install

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
%{python_sitelibdir_noarch}/mnemosyne
%{python_sitelibdir_noarch}/Mnemosyne-%{version}-*.egg-info
%{python_sitelibdir_noarch}/openSM2sync
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
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

