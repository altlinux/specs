# -*- rpm-spec -*-
# $Id: chrootuid,v 1.2 2002/12/11 13:54:13 ab Exp $

Name: chrootuid
Version: 1.3
Release: alt2

Summary: Chrootuid is a tool to one-step chroot and drop privilleges operation
License: Distributable
Group: System/Base
Url: ftp://ftp.porcupine.org/pub/security
Packager: Alexander V. Nikolaev <avn@altlinux.org>

Source: %name-%version.tar.gz
Patch0: %name-1.3-alt.patch

%description
Chrootuid makes it easy to run a network service at low privilege
level and with restricted file system access.  The daemons have access only
to their own directory tree, and run under a low-privileged userid.

%prep
%setup -q
%patch0 -p1 -b .alt

%build
make clean
%make_build

%install
%__mkdir -p %buildroot/{%_bindir,%_man1dir}
install -m 755 chrootuid %buildroot%_bindir
install chrootuid.1 %buildroot%_man1dir
%files
%_bindir/*
%_man1dir/*
%doc README* *license

%changelog
* Wed Dec 11 2002 Alexander Bokovoy <ab@altlinux.ru> 1.3-alt2
- Fixed:
    + return codes for errors
    + error management switched from syslog to stderr

* Mon Nov 18 2002 Alexander V. Nikolaev <avn@altlinux.org> 1.3-alt1
- 1.3


