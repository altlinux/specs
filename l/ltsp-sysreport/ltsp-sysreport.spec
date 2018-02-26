Name: ltsp-sysreport
Version: 0.1
Release: alt1

Summary: a script to gather thin client's system/hardware info
License: Public domain
Group: System/Base

Url: http://www.altlinux.org/LTSP
Source: ltsp-sysreport.sh
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
This package automates analyzing thin client state and
submitting bug reports a bit by gathering the most likely
needed bits together.  You still need to grab these off
the thin client, have a look at those, and consider what
to do with the information.

%prep

%build

%install
install -pDm755 %SOURCE0 %buildroot%_sbindir/%name

%files
%_sbindir/%name

%changelog
* Thu Mar 08 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

