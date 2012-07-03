Name: cifs-utils
Version: 5.4
Release: alt1

Summary: Utilities for doing and managing mounts of the Linux CIFS filesystem
Group: System/Kernel and hardware
License: GPLv3+
Url: https://wiki.samba.org/index.php/LinuxCIFS_utils

Source: %name-%version.tar

BuildRequires: libcap-ng-devel libkeyutils-devel libkrb5-devel libtalloc-devel samba-winbind-devel

Conflicts: samba-client < 3.6.0-alt1

%description
This is the release version of cifs-utils, a package of utilities for
doing and managing mounts of the Linux CIFS filesystem. These programs
were originally part of Samba, but have now been split off into a
separate package.

%prep
%setup

%build
%autoreconf
%configure \
       --enable-cifsupcall \
       --enable-cifsidmap \
       --enable-cifscreds
%make_build

%install
%makeinstall_std
mv %buildroot/%_sbindir/cifs.upcall %buildroot/sbin/

%files
/sbin/mount.cifs
/sbin/cifs.upcall
%_sbindir/cifs.idmap
%_bindir/cifscreds
%_bindir/getcifsacl
%_bindir/setcifsacl
%_man8dir/cifs.idmap.8*
%_man8dir/cifs.upcall.8*
%_man8dir/mount.cifs.8*
%_man1dir/getcifsacl.1*
%_man1dir/setcifsacl.1*
%_man1dir/cifscreds.1*
%doc AUTHORS ChangeLog README

%changelog
* Sat Apr 28 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.4-alt1
- 5.4 (cifs-utils-5.3-19-ga91fb06)

* Tue Sep 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1-alt1
- 5.1

* Mon Aug 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt3
- conflicts with samba-client < 3.6.0-alt1

* Mon Aug 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt2
- CVE-2011-2724
- move cifs.upcall to /sbin
- build with libpcap and libwbclient

* Mon Aug 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt1
- 5.0

* Sun Mar 20 2011 Michael Shigorin <mike@altlinux.org> 4.9-alt1
- 4.9
- fix BuildRequires:

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 4.8-alt1
- 4.8 (thanks force@)

* Wed Mar 31 2010 Michael Shigorin <mike@altlinux.org> 4.1-alt2
- added Conflicts: samba-client (should be removed after
  that package drops these files as anticipated)

* Wed Mar 31 2010 Michael Shigorin <mike@altlinux.org> 4.1-alt1
- built for ALT Linux
  + thanks ab@ for advice
  + somewhat based on Debian/Fedora/openSUSE packages
