# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: slingshot
Version:  0.9
Release:  alt1_6
Summary: A Newtonian strategy game

Group: Games/Other
License: GPLv2+        
URL: https://github.com/ryanakca/slingshot
Source0: https://github.com/ryanakca/slingshot/archive/slingshot-%{version}.tar.gz
Source1: slingshot.desktop
#Source2: slingshot
Source3: slingshot.appdata.xml
#Patch0: slingshot-font-path.patch
#Patch1: slingshot-0.8.1p-type-mismatch.patch
BuildArchitectures: noarch
BuildRequires: desktop-file-utils, python-module-setuptools, python-devel
Requires: icon-theme-hicolor, pygame, fonts-ttf-gnu-freefont-sans
Source44: import.info

%description
Slingshot is a two dimensional, turn based simulation-strategy game 
set in the gravity fields of several planets. It is a highly 
addictive game, and never the same from round to round due to its 
randomly generated playing fields.

%prep
%setup -q

#%%patch0 -p0
#%%patch1 -p1

%build
%python_build

rm -f slingshot/data/FreeSansBold.ttf

%install
%python_install

rm -rf $RPM_BUILD_ROOT/slingshot
rm -rf $RPM_BUILD_ROOT/home
rm -rf $RPM_BUILD_ROOT/builddir

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mv src/slingshot/data/icon64x64.png src/slingshot/data/slingshot.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 src/slingshot/data/slingshot.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps

#install appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 664 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata

%files
%{_bindir}/slingshot
%{python_sitelibdir_noarch}/*
%doc README
%doc --no-dereference LICENSE
%{_datadir}/applications/slingshot.desktop
%{_datadir}/icons/hicolor/64x64/apps/slingshot.png
%{_datadir}/appdata/slingshot.appdata.xml

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_6
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_4
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_3
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt4_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt4_12
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt4_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt4_10
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt4_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt4_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt4_7
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt3_7
- update to new release by fcimport

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1p-alt3_6.1
- Rebuild with Python-2.7

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt3_6
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt2_6
- rebuild with new rpm desktop cleaner

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.1p-alt1_6
- converted from Fedora by srpmconvert script

