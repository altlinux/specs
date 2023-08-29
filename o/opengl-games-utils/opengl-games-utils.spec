Group: Games/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           opengl-games-utils
Version:        0.2
Release:        alt2_25
Summary:        Utilities to check proper 3d support before launching 3d games
License:        LicenseRef-Fedora-Public-Domain
URL:            http://fedoraproject.org/wiki/SIGs/Games
Source0:        opengl-game-wrapper.sh
Source1:        opengl-game-functions.sh
Source2:        README
BuildArch:      noarch
Requires:       zenity glxgears glxinfo
Source44: import.info
# for autoimports
Provides: /usr/share/opengl-games-utils/opengl-game-functions.sh

%description
This package contains various shell scripts which are intented for use by
3D games packages. These shell scripts can be used to check if direct rendering
is available before launching an OpenGL game. This package is intended for use
by other packages and is not intended for direct end user use!


%prep
%setup -c -T
cp %{SOURCE2} .


%build
# nothing to build


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}

if [ "%{_prefix}" != "/usr" ]; then
  sed -i "s/\/usr/\%{_prefix}/g" $RPM_BUILD_ROOT%{_bindir}/opengl-game-wrapper.sh
fi


%files
%doc README
%{_bindir}/opengl-game-wrapper.sh
%{_datadir}/%{name}


%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.2-alt2_25
- update to new release by fcimport

* Mon Aug 16 2021 Igor Vlasenko <viy@altlinux.org> 0.2-alt2_20
- added provides for external symlinks in autoimports

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_16
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_9
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_3
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_2
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_2
- update to new release by fcimport

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_1
- update to new release by fcimport

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_10
- converted from Fedora by srpmconvert script

