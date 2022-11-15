Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: /usr/bin/desktop-file-install python3(sqlite3) python3-module-setuptools
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%{!?qt5_qtwebengine_arches:%global qt5_qtwebengine_arches %{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}

%bcond_without check

Name:		mnemosyne
Summary:	Flash-card learning tool
Version:	2.6.1
Release:	alt3_4.1
URL:		https://www.mnemosyne-proj.org/
Source0:	https://downloads.sourceforge.net/sourceforge/mnemosyne-proj/Mnemosyne-%{version}.tar.gz
# contains missing tests and LICENSE files from upstream repo
Source1:        Mnemosyne-tests-%{version}.tar.xz
# run this script to obtain the above tarball
Source10:       mnemosyne-mktarball.sh
Patch0:		mnemosyne-desktop.patch
License:	AGPLv3

# no python3-qt5-webengine on power64
ExclusiveArch:	noarch %{qt5_qtwebengine_arches}
BuildRequires(pre):	rpm-macros-qt5-webengine
BuildRequires:	desktop-file-utils
BuildRequires:	python3-devel
BuildRequires:	python3-module-distribute
%if %{with check}
# unpackaged https://pypi.python.org/pypi/Cheroot
#BuildRequires: python3-cheroot
BuildRequires:	python3-module-cherrypy
BuildRequires:	python3-module-nose
BuildRequires:	python3-module-PyQt5
BuildRequires:	texlive-collection-latexrecommended
BuildRequires:	texlive
%endif
Requires:	icon-theme-hicolor
Requires:	python3-module-PyQt5
%ifarch %qt5_qtwebengine_arches
Requires:	python3-module-PyQtWebEngine
%endif
Requires:	python3-module-matplotlib-qt5
Requires:	python3-module-cherrypy
Requires:	python3-module-webob
Requires:	python3-module-Pillow
Requires:       python3-module-OpenGL python3-module-OpenGL_accelerate
Source44: import.info

%add_python3_self_prov_path %buildroot%{python3_sitelibdir}/%{name}/libmnemosyne/renderers/

%description
Mnemosyne resembles a traditional flash-card program but with an
important twist: it uses a sophisticated algorithm to schedule the best
time for a card to come up for review.

Optional dependencies:
* latex: enables entering formulas using latex syntax.

%prep
%setup -q -n Mnemosyne-%{version} -a 1
%patch0 -p1 -b .d
rm -r Mnemosyne.egg-info
# requires unpackaged Cheroot python module
rm tests/test_sync.py
cp -p mnemosyne/LICENSE LICENSE.mnemosyne
cp -p openSM2sync/LICENSE LICENSE.openSM2sync

%build
%python3_build

%install
%python3_install
# make arch dependent
if [ "%python3_sitelibdir" != "%python3_sitelibdir_noarch" ] ; then
    mkdir -p %buildroot/%python3_sitelibdir
    mv %buildroot/%python3_sitelibdir_noarch/* %buildroot/%python3_sitelibdir/
fi

install -d %{buildroot}%{_datadir}/applications
desktop-file-install --vendor="" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{name}.desktop

install -d %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps
pushd %{buildroot}/%{_datadir}/icons
mv %{name}.png hicolor/128x128/apps/%{name}.png
popd

%find_lang %{name}

%if %{with check}
%check
# tests fail if run in parallel
#PYTHONPATH=%{buildroot}%{python3_sitelibdir_noarch} %{__python3} -m nose tests
%endif

%files -f %{name}.lang
%doc ChangeLog README
%doc --no-dereference LICENSE LICENSE.mnemosyne LICENSE.openSM2sync
%{_bindir}/%{name}
%{python3_sitelibdir}/%{name}
%{python3_sitelibdir}/Mnemosyne-%{version}-py%{__python3_version}.egg-info
%{python3_sitelibdir}/openSM2sync
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.6.1-alt3_4.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Fri Feb 04 2022 Igor Vlasenko <viy@altlinux.org> 2.6.1-alt3_4
- support for qt5_qtwebengine_arches (closes: #41870)

* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 2.6.1-alt2_4
- no python2

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_4
- update to new release by fcimport

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_4
- update to new release by fcimport

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

