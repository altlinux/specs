Summary: A clock for the X Window System
Name: xdaliclock
Version: 2.25
Release: alt2_6
Group: Graphics
License: BSD
URL: http://www.jwz.org/xdaliclock/
Source0: http://www.jwz.org/xdaliclock/xdaliclock-%{version}.tar.gz
Source1: xdaliclock.desktop
BuildRequires: desktop-file-utils
BuildRequires: libICE-devel libXmu-devel libSM-devel xorg-x11-proto-devel
BuildRequires: libXext-devel libXaw-devel libXt-devel
Source44: import.info

%description
XDaliClock is a large digital clock for the X Window System, with digits
that "melt" into their new shapes when the time changes. XDaliClock
supports 12 and 24 hour modes, and displays the date when you hold a mouse
button down over it. It also can be configured to do colormap cycling, and
for window transparency.

%prep
%setup

%build
cd X11
%configure
make %{?_smp_mflags}

%install
cd X11

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults

install -p -m 0755 xdaliclock $RPM_BUILD_ROOT%{_bindir}
install -p -m 0644 xdaliclock.man \
	$RPM_BUILD_ROOT%{_mandir}/man1/xdaliclock.1
install -p -m 0644 XDaliClock.ad \
	$RPM_BUILD_ROOT%{_datadir}/X11/app-defaults/XDaliClock

desktop-file-install --vendor fedora \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--add-category "X-Fedora" \
	--add-category "Graphics" \
	%{SOURCE1}

%files
%doc README
%{_bindir}/xdaliclock
%{_mandir}/man1/xdaliclock.1*
%{_datadir}/X11/app-defaults/XDaliClock
%{_datadir}/applications/*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.25-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1_6
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1_5
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1_4
- initial release by fcimport

