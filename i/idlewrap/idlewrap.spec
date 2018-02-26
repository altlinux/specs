Name: idlewrap
Version: 0.2.1
Release: alt1

Summary: Wrap a command for idle-only execution
License: GPL
Group: Accessibility

Url: https://bugzilla.altlinux.org/show_bug.cgi?id=3193
Source0: %name
Source1: README.%name
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: schedutils schedtool

%description
Idle Wrap will run the command specified using idle I/O and CPU
so the intervention of long-running resource-hungry background
processes (like updatedb or makewhatis) can be minimized.

By default, it will also avoid running anything if the system's
on battery although that can be forced through.

%prep
cp -a %SOURCE1 README

%install
install -pDm755 %SOURCE0 %buildroot%_bindir/%name

%files
%_bindir/%name
%doc README

%changelog
* Sat Mar 26 2011 Michael Shigorin <mike@altlinux.org> 0.2.1-alt1
- silly fix to make it work within OpenVZ containers as well

* Wed Oct 29 2008 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- noarch

* Tue Oct 21 2008 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- added APM support

* Mon Oct 20 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial specfile

