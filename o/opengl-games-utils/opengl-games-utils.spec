Name:           opengl-games-utils
Version:        0.2
Release:        alt2_8
Summary:        Utilities to check proper 3d support before launching 3d games
Group:          Games/Other
License:        Public Domain
URL:            http://fedoraproject.org/wiki/SIGs/Games
Source0:        opengl-game-wrapper.sh
Source1:        opengl-game-functions.sh
Source2:        README
BuildArch:      noarch
Requires:       zenity xdriinfo glxinfo
Source44: import.info

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


%files
%doc README
%{_bindir}/opengl-game-wrapper.sh
%{_datadir}/%{name}


%changelog
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

