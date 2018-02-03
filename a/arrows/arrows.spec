# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           arrows
Version:        0.6
Release:        alt3_22
Summary:        Neat little maze game
Group:          Games/Other
License:        GPLv2+
URL:            http://noreason.ca/?file=software
Source0:        http://noreason.ca/data/arrows-%{version}.tar.gz
Source1:        arrows.desktop
Source2:        arrows.png
Patch0:         arrows-level-5.patch 
BuildRequires:  gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
It's a maze game of sorts. Guide the spinning blue thing through
the maze of arrows, creating and destroying arrows as necessary
to collect the green things.

%prep
%setup -q
%patch0 -p1
make clean

%build
%make_build CCOPTS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -m 644 arrfl.? $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE2}\
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_21
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_19
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_15
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_14
- update to new release by fcimport

* Fri Feb 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_13
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_12
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3_11
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_11
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_10
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_9
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_9
- converted from Fedora by srpmconvert script

