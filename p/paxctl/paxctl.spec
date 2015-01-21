Name: paxctl 
Version: 0.9
Release: alt1

Summary: paxctl - user-space utility to control PaX flags
License: GPLv2
Group: System/Configuration/Other
Source: %name-%version.tar

%description
paxctl is a tool that allows PaX flags to be modified
on a per-binary basis.  PaX is part of common security-enhancing
kernel patches and secure distributions, such as GrSecurity and
Hardened Gentoo, respectively.  Your system needs to be running
properly patched and configured kernel for this program to have
any effect.


%prep
%setup

%build
%make_build

%install
make install DESTDIR=%buildroot

%files
/sbin/*
%_man1dir/*

%changelog
* Wed Jan 21 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9-alt1
- initial build

