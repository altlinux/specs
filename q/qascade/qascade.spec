# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           qascade
Version:        0.1
Release:        alt2_26
Summary:        Classic puzzle game

Group:          Games/Other
License:        GPLv2+
URL:            http://www.bitsnpieces.org.uk/qascade/
Source0:        http://www.bitsnpieces.org.uk/qascade/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         %{name}-dblsep.patch

BuildRequires:  libqt3-devel
BuildRequires:  desktop-file-utils
Source44: import.info

%description
Qascade is a port of the simple yet addictive and enjoyable puzzle
game that came with the Psion Revo PDA.


%prep
%setup -q
%patch0


%build
[ -n "$QTDIR" ] || . /etc/profile.d/qt3dir.sh; export PATH=%_libdir/qt3/bin:$PATH
qmake-qt3 INSTALL_ROOT=$RPM_BUILD_ROOT qascade.pro
perl -pi -e 's|^(C(XX)?FLAGS\s*=.*)$|$1 \$(RPM_OPT_FLAGS)|g' Makefile
%make_build


%install
[ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
%makeinstall
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --mode 644 \
  %{SOURCE1}
install -D -p -m 644 %{name}.hscr \
  $RPM_BUILD_ROOT%{_localstatedir}/lib/games/%{name}.hscr
install -D -p -m 644 blue.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/qascade.png


%files
%doc *.htm
%attr(2711,root,games) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/qascade.png
%attr(0664,games,games) %config(noreplace) %{_localstatedir}/lib/games/%{name}*


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_26
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_25
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_23
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_22
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_21
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_19
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_18
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_17
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_16
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_15
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_14
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_14
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_13
- converted from Fedora by srpmconvert script

