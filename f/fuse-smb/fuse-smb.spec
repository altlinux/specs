%define distname fusesmb

Name: fuse-smb
Version: 0.8.7
Release: alt3

Summary: SMB filesystem using FUSE - mount network neighbourhood
Group: System/Kernel and hardware
License: GPL
Url: http://hannibal.lr-s.tudelft.nl/~vincent/fusesmb/

Packager: Roman Savochenko <rom_as at altlinux.ru>

Source: %distname-%version.tar.gz
Patch0: %name-ResFix-RenameFix-WriteSpeedIncr.patch
Patch1: %name-CacheThreadRemove.patch

Requires: fuse

# Automatically added by buildreq on Sat Aug 27 2005
BuildRequires: libfuse-devel libsmbclient-devel samba-client

%description
Mount network neighbourhood

%prep
%setup -q -n %distname-%version
%patch0 -p1
%patch1 -p1

%build
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS COPYING ChangeLog NEWS README

%_bindir/*
%_man1dir/*
%_man5dir/*

%changelog
* Wed Oct 5 2011 Roman Savochenko <rom_as@altlinux.ru> 0.8.7-alt3
- Removed not resourced threads from fusesmb.cache for correct work allow.

* Thu May 26 2011 Roman Savochenko <rom_as@altlinux.ru> 0.8.7-alt2
- Apply path for correct resource using on multicore systems and prevent crash on write.
- Apply path for correct cache problem at node rename.
- Apply path for write speed some increase.

* Tue Jan 05 2010 Denis Smirnov <mithraen@altlinux.ru> 0.8.7-alt1
- update to 0.8.7

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.8.5-alt4
- cleanup spec

* Wed Jan 10 2007 Denis Smirnov <mithraen@altlinux.ru> 0.8.5-alt3
- don't require fixed version of fuse

* Fri Dec 15 2006 Denis Smirnov <mithraen@altlinux.ru> 0.8.5-alt2
- rebuild with last fuse

* Sun Oct 08 2006 Denis Smirnov <mithraen@altlinux.ru> 0.8.5-alt1
- update to 0.8.5

* Sun Nov 27 2005 Denis Smirnov <mithraen@altlinux.ru> 0.8.1-alt3
- rebuild with last fuse

* Tue Nov 22 2005 Denis Smirnov <mithraen@altlinux.ru> 0.8.1-alt2
- rebuild with last fuse

* Sat Aug 27 2005 Denis Smirnov <mithraen@altlinux.ru> 0.8.1-alt1
- packaged for Sisyphus

* Fri May 26 2005 Led <led@linux.kiev.ru> 0.7.0-alt0.1
- initial build

