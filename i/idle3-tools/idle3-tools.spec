Name: idle3-tools
Version: 0.9.1
Release: alt1

Summary: Utility for change idle3 timer on Western Digital drives

License: GPLv3
Group: File tools

Url: http://idle3-tools.sourceforge.net/

Source: http://prdownloads.sf.net/idle3-tools/%name-%version.tar

# Automatically added by buildreq on Fri Jul 19 2013
BuildRequires: ruby ruby-stdlibs

%description
This linux/unix utility can be used to remove or set
the infamous idle3 timer found on recent
Western Digital Hard Disk Drives.

Note: the best place for this functions is hdparm:
http://sourceforge.net/p/hdparm/feature-requests/10/

%prep
%setup

%build
%make_build

%install
%makeinstall_std binprefix=%prefix

%files
%_sbindir/idle3ctl
%_man8dir/*

%changelog
* Fri Jul 19 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- initial build for ALT Linux Sisyphus
