Name: bontmia
Version: 0.14
Release: alt3.1

Summary: bontmia (Backup Over Network To Multiple Incremental Archives)
License: GPL
Group: Archiving/Backup
Url: http://folk.uio.no/johnen/bontmia/
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: http://folk.uio.no/johnen/bontmia/%name-%version.tar.gz
Source1: %name.html

BuildArch: noarch

%description
%name stands for Backup Over Network To Multiple Incremental Archives and
is a network based backup with similar backup scheme as with tapes.
Saves configurable numbers of last month, week, day, hour and minute
backups.  Each backup is a complete snapshot of the original
directories.  Only new/changed files takes up space when generating a
new snapshot.  Remote access is done over ssh.  More info is available
at http://folk.uio.no/johnen/bontmia/

%prep
%setup -q -n %name-%version
cp %SOURCE1 ./

%build
%install
mkdir -p %buildroot/%_sbindir
install bontmia %buildroot/%_sbindir/

%files
%_sbindir/*
%doc README COPYING bontmia.html

%changelog
* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt3.1
- rebuild (with the help of girar-nmu utility)

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt3
- fix build with new gear

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt2
- cleanup spec

* Sun Sep 19 2004 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt1
- Updated to 0.14
- html doc from site packaged

* Wed Mar 10 2004 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt1
- packaged for sisyphus
