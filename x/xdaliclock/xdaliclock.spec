Group: Graphics
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install perl(diagnostics.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: A clock for the X Window System
Name: xdaliclock
Version: 2.43
Release: alt2_16
License: BSD
URL: http://www.jwz.org/xdaliclock/
Source0: http://www.jwz.org/xdaliclock/xdaliclock-%{version}.tar.gz
Source1: xdaliclock.desktop
Patch0: xdaliclock-configure-c99.patch
BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: libICE-devel, libXmu-devel, libSM-devel, xorg-proto-devel
BuildRequires: libXext-devel, libXaw-devel, libXt-devel
Source44: import.info

%description
XDaliClock is a large digital clock for the X Window System, with digits
that "melt" into their new shapes when the time changes. XDaliClock
supports 12 and 24 hour modes, and displays the date when you hold a mouse
button down over it. It also can be configured to do colormap cycling, and
for window transparency.

%prep
%setup -q
%patch0 -p1


%build
cp -at . -- /usr/share/gnu-config/config.{guess,sub}
# easier than patching configure to read those files from own directory
# cp /usr/lib/rpm/redhat/config.{guess,sub} .

cd X11
%configure
%make_build

%install
cd X11

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_x11appconfdir}

install -p -m 0755 xdaliclock $RPM_BUILD_ROOT%{_bindir}
install -p -m 0644 xdaliclock.man \
	$RPM_BUILD_ROOT%{_mandir}/man1/xdaliclock.1
install -p -m 0644 XDaliClock.ad \
	$RPM_BUILD_ROOT%{_x11appconfdir}/XDaliClock

desktop-file-install  \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--add-category "X-Fedora" \
	--add-category "Graphics" \
	%{SOURCE1}

%files
%doc README
%{_bindir}/xdaliclock
%{_mandir}/man1/xdaliclock.1*
%{_x11appconfdir}/XDaliClock
%{_datadir}/applications/*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 2.43-alt2_16
- update to new release by fcimport

* Sat Dec 07 2019 Igor Vlasenko <viy@altlinux.ru> 2.43-alt2_9
- merged e2k patch

* Mon Sep 30 2019 Michael Shigorin <mike@altlinux.org> 2.43-alt2_5
- fix build on newer arches

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 2.43-alt1_5
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.43-alt1_2
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 2.43-alt1_1
- new version

* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 2.25-alt3_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.25-alt3_9
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 2.25-alt3_8
- fixed build

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 2.25-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.25-alt2_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.25-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1_6
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1_5
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1_4
- initial release by fcimport

