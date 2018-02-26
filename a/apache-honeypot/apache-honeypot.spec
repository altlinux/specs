Name: apache-honeypot
Version: 0.2
Release: alt1

Summary: Setup for ALT Linux Apache 1.3 to help spot kiddies
License: GPL v2
Group: Security/Networking

Source1: %name-wget
Source2: %name.README
Packager: Michael Shigorin <mike@altlinux.org>

Requires: apache-common >= 1.3.33rusPL30.20-alt2.M24.1

BuildArch: noarch

%define conffile %_sysconfdir/sysconfig/apache
%define potdir %_libexecdir/%name/bin

%description
This package includes settings and scripts to help kiddies
warn the hostmaster of security breaches they could have
exploited successfully.  It's not warranty or 100%% solution
but yet another inconvenience for a casual attacker of
a casual web application on the hosting.

%prep

%install
install -pDm755 %SOURCE1 %buildroot%potdir/wget
install -pm644  %SOURCE2 README

%post
if ! grep -qs "^export PATH" "%conffile"; then
	echo "export PATH=%potdir:$PATH" >> %conffile
fi

%postun
# maybe there should be %conffile cleanup...
# doesn't really hurt

%files
%potdir/*
%doc README

%changelog
* Thu Mar 11 2010 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- quote script arguments just in case
- replaced $0 with explicit string

* Mon Oct 06 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- s,%%_libdir,%%_libexecdir,g

* Thu Jan 10 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- fixed harmless but non-aesthetical thinko in %%post
  (would add "export PATH=..." each time when installed),
  removed unneeded message ("already there") too

* Fri Dec 02 2005 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- built for ALT Linux Sisyphus

* Thu Aug 25 2005 Michael Shigorin <mike@altlinux.org> 0.1-alt0
- initial release
