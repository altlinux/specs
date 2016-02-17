# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%define fedora 23
Name:           tunneler
Version:        1.1.1
Release:        alt2_17
Summary:        Clone of legendary Tunneler game

Group:          Games/Other
License:        GPLv2+
URL:            http://users.jyu.fi/~tvkalvas/code/tunneler/
Source0:        http://users.jyu.fi/~tvkalvas/code/tunneler/%{name}-%{version}.tar.gz
Source1:        tunneler.svg
Source2:        tunneler.desktop
Patch0:         tunneler-1.1.1-lm.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libSDL-devel
BuildRequires:  autoconf automake
Source44: import.info

%description
A clone of legendary game made by Geoffrey Silverton in 1991. In the game
two players using the same keyboard and the same screen each control an
underground tank. Goal is to find and destroy the opponent's tank. Since
only small part of the map is displayed on the split screen, you might
actually have some searching to do.


%prep
%setup -q
%patch0 -p1 -b .lm


%build
autoreconf -i
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 -p %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
desktop-file-install %{SOURCE2} \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rheld} < 7)
         \
%endif
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications


%files
%{_bindir}/tunneler
%{_datadir}/icons/hicolor/scalable/apps/tunneler.svg
%{_datadir}/applications/*.desktop
%doc COPYING INSTALL README


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_16
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_14
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_12
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_8
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_7
- converted from Fedora by srpmconvert script

