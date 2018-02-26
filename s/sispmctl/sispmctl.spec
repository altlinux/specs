Name: sispmctl
Version: 3.1
Release: alt2

Summary: GEMBIRD Silver Shield PM Control
License: GPL
Group: System/Kernel and hardware

Url: http://sispmctl.sourceforge.net
Source0: %name-%version.tar.gz
Source1: 74-sispmctl.rules
Source100: sispmctl.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Fri Sep 23 2011
BuildRequires: libusb-compat-devel

%description
SIS-PM Control for Linux aka sispmctl is an application
enabling the use of the GEMBIRD (m)SiS-PM device family
(or a Revolt Power Switch) under Linux.

Add users who need to control the device to _sispm group.

%prep
%setup

%build
%configure --enable-webless
%make_build

%install
%makeinstall
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/udev/rules.d/74-sispmctl.rules

%files
%_bindir/*
%_man1dir/*
%config(noreplace) %_sysconfdir/udev/rules.d/74-sispmctl.rules
%doc AUTHORS ChangeLog README

%pre
%_sbindir/groupadd -r -f _sispm >/dev/null 2>&1

# TODO:
# - consider web part

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 3.1-alt2
- added watch file

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 3.1-alt1
- 3.1

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 3.0-alt1
- 3.0
- dropped patches (ours merged upstream, debian's irrelevant)

* Thu Jul 23 2009 Michael Shigorin <mike@altlinux.org> 2.7-alt3
- introduced udev rules and a pseudogroup

* Thu Jul 23 2009 Michael Shigorin <mike@altlinux.org> 2.7-alt2
- it works!
  + fixed a buffer overflow when scanning (thanks led@)
  + applied a tail of debian patch as well
- verified against mSIS-PM helpfully provided by these nice folks:
  http://www.e-napruga.com.ua/good_details.php?good_key=648

* Tue Jul 21 2009 Michael Shigorin <mike@altlinux.org> 2.7-alt1
- built for ALT Linux

