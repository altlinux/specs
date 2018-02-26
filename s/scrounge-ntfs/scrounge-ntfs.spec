Name: scrounge-ntfs
Version: 0.9
Release: alt2

Summary: Data recovery program for NTFS file systems

License: GPL
Group: System/Libraries
Url: http://memberwebs.com/stef/software/scrounge/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://memberwebs.com/stef/software/scrounge/%name-%version.tar

%description
Data recovery program for NTFS file systems.
Reads each block of the hard disk to and retrieves rebuilds file system tree on another partition.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_sbindir/%name
%_man8dir/*

%changelog
* Sun Jul 25 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt2
- fix build, build from git

* Sat Aug 04 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus

