Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: slingshot
Version:  0.9
Release:  alt2_21
Summary: A Newtonian strategy game

License: GPL-2.0-or-later        
URL: https://github.com/ryanakca/slingshot
Source0: https://github.com/ryanakca/slingshot/archive/%{version}/slingshot-%{version}.tar.gz
Source1: slingshot.desktop
Source2: slingshot.appdata.xml
# Port to Python 3
Patch0: 243aef95dde390f97f1e0abbbdb646b3e5b97f7d.patch
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib libappstream-glib-gir
BuildRequires: python3-devel
BuildRequires: python3-module-pkg_resources python3-module-setuptools
Requires: fonts-ttf-gnu-freefont-sans
Requires: icon-theme-hicolor
Requires: python3-module-pygame
Source44: import.info

%description
Slingshot is a two dimensional, turn based simulation-strategy game 
set in the gravity fields of several planets. It is a highly 
addictive game, and never the same from round to round due to its 
randomly generated playing fields.

%prep
%setup -q
%patch0 -p1

rm -f src/slingshot/data/FreeSansBold.ttf

%build
%python3_build

%install
%python3_install

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
mkdir -p $RPM_BUILD_ROOT/%{_metainfodir}
install -p -m 664 %{SOURCE2} $RPM_BUILD_ROOT/%{_metainfodir}
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_metainfodir}/*.appdata.xml

#Link to font
ln -s %{_datadir}/fonts/ttf/gnu-free/FreeSansBold.ttf $RPM_BUILD_ROOT%{python3_sitelibdir_noarch}/%{name}/data/FreeSansBold.ttf

%files
%{_bindir}/slingshot
%{python3_sitelibdir_noarch}/%{name}-*.egg-info
%{python3_sitelibdir_noarch}/%{name}/
%doc README
%doc --no-dereference LICENSE
%{_datadir}/applications/slingshot.desktop
%{_datadir}/icons/hicolor/64x64/apps/slingshot.png
#%{_datadir}/pixmaps/slingshot.xpm
%{_metainfodir}/slingshot.appdata.xml

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 0.9-alt2_21
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_12
- update to new release by fcimport

* Mon Mar 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9-alt2
- Porting to python3.

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_8
- update to new release by fcimport

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

