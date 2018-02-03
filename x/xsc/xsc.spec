# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ imake libXt-devel xorg-cf-files
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: xsc
Version:  1.6
Release:  alt1_5
Summary: A clone of the old vector graphics video game Star Castle

Group: Games/Other
License: GPLv2+
URL: http://www.panix.com/~mbh/projects.html
Source0: http://www.panix.com/~mbh/xsc/xsc-%{version}.tar.gz
Source1: xsc.desktop
Source2: xsc.png
BuildRequires: desktop-file-utils, libX11-devel
Requires: icon-theme-hicolor
Source44: import.info

%description
The object is to blast a hole in the rings and destroy the enemy ship.
The only problem is that it tracks your every move and as soon as you 
knock a hole in all three rings, and they all line up, it lets loose  
with the big nasty green fireballs.  Avoid them.  Avoid the little green
buzzers, too.  Shoot 'em if you want.

%prep
%setup -q

%build

%configure --x-includes="" --x-libraries=""
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p  %{buildroot}%{_bindir}
install -m 755 xsc %{buildroot}%{_bindir}/xsc

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install           \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

%files
%{_bindir}/xsc
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_datadir}/applications/xsc.desktop
%{_datadir}/icons/hicolor/32x32/apps/xsc.png

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_5
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_2
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_1
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_10
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_7
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_6
- converted from Fedora by srpmconvert script

