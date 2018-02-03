# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: xgrav
Version:  1.2.0
Release:  alt2_21
Summary: A simple physics simulation for a large number of particles

Group: Games/Other
License: GPLv2+
URL: http://aass.oru.se/~mbl/xgrav/
Source0: http://www.aass.oru.se/~mbl/xgrav/xgrav-%{version}.tgz
Source1: xgrav.desktop
#Created from screenshot of example1.g run.
Source2: xgrav.png
BuildRequires: desktop-file-utils, libSDL-devel, flex, zlib-devel
Requires: icon-theme-hicolor
Source44: import.info

%description
X-Grav simulates the effect of gravity, collisions, heat dissipation and
a simple chemical reaction. The simulation is in no way meant to be 
realistic but rather a toy with which you can create stars, planets 
and even simple solar systems.

%prep
%setup -qn xgrav

chmod -x COPYING

%build

make LINUX_CFLAGS="-c $RPM_OPT_FLAGS `pkg-config --cflags sdl` \
-DWITH_ROOTWINDOW" LINUX_LDFLAGS="$RPM_OPT_FLAGS `pkg-config \
--libs sdl` -lGL `pkg-config --libs x11` -lm"

%install
mkdir -p  %{buildroot}%{_bindir}
install -p -m 755 xgrav %{buildroot}%{_bindir}/xgrav

mkdir -p  %{buildroot}%{_datadir}/xgrav
install -p -m 644 example* %{buildroot}%{_datadir}/xgrav

sed 's;/usr/share;%_datadir;' %{SOURCE1} > xgrav.desktop

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install             \
  --dir %{buildroot}%{_datadir}/applications \
  xgrav.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

%files
%doc COPYING documentation.html README README.html TODO VERSION
%{_bindir}/xgrav
%{_datadir}/xgrav
%{_datadir}/applications/xgrav.desktop
%{_datadir}/icons/hicolor/32x32/apps/xgrav.png

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_21
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_20
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_18
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_16
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_13
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_12
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_11
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_10
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_10
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_9
- converted from Fedora by srpmconvert script

