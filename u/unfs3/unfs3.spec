Name: unfs3
Version: 0.9.22
Release: alt4

Summary: UNFS3 user-space NFSv3 server
License: BSD (revised)
Group: System/Servers

Url: http://unfs3.sourceforge.net
Source0: %name-%version.tar.gz
Source1: unfs3.init
Source2: unfs3.monit
Source100: unfs3.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Dec 04 2007
BuildRequires: flex

Requires: monit-base
Conflicts: nfs-server nfs-server-userland

%description
UNFS3 user-space NFSv3 server

%prep
%setup

%build
%configure --enable-cluster
%make

%install
%makeinstall
install -pDm755 %SOURCE1 %buildroot%_initdir/nfs
install -pDm644 %SOURCE2 %buildroot%_sysconfdir/monitrc.d/%name.auto

%description
UNFS3 is a user-space implementation of the NFS
(Network File System) version 3 server specification.

This implementation has specific support for clustering
and removable media.

%files
%doc CREDITS README README.nfsroot LICENSE NEWS contrib doc
%_sbindir/unfsd
%_man7dir/*
%_man8dir/*
%_initdir/*
%_sysconfdir/monitrc.d/%name.auto

%post
%post_service nfs

%preun
%preun_service nfs

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 0.9.22-alt4
- added watch file

* Sat Aug 01 2009 Michael Shigorin <mike@altlinux.org> 0.9.22-alt3
- added Conflicts: nfs-server-userland (repocop)

* Sun Jun 07 2009 Michael Shigorin <mike@altlinux.org> 0.9.22-alt2
- added initial monit support

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 0.9.22-alt1
- 0.9.22

* Mon Dec 10 2007 Michael Shigorin <mike@altlinux.org> 0.9.20-alt2
- fixed typo in spec (/etc/sysconfig/unfs3 would be ignored),
  thanks led@ for bringing attention to that

* Wed Dec 05 2007 Michael Shigorin <mike@altlinux.org> 0.9.20-alt1
- 0.9.20
  + patch removed

* Tue Dec 04 2007 Michael Shigorin <mike@altlinux.org> 0.9.19-alt2
- added dir_access upstream patch -- huge thanks to 
  Sergey Bolshakov <sbolshakov@>, now aux groups really work
- buildreq

* Wed Nov 28 2007 Michael Shigorin <mike@altlinux.org> 0.9.19-alt1
- 0.9.19 with major bugfixes:
  + auxiliary group support 
  + changing the ownership of symbolic links
- removed patches (which were unused by now)

* Wed Sep 05 2007 Michael Shigorin <mike@altlinux.org> 0.9.18-alt1
- 0.9.18 (adds -T switch to test /etc/exports validity)
- updated initscript to take advantage of this new feature
- pidfile patch removed (merged upstream)
- package description modified a bit

* Tue Aug 07 2007 Michael Shigorin <mike@altlinux.org> 0.9.17-alt3
- added Conflicts: nfs-server (fixes #12488)

* Sat Jan 27 2007 Michael Shigorin <mike@altlinux.org> 0.9.17-alt2
- updated pidfile patch (it was actually sent upstream just yesterday
  and Pascal Schmidt promptly replied with more aligned version
  which would work for Windows and non-root users and generally
  create less divergence for upgrades) [rediffed as patch2]

* Tue Jan 23 2007 Michael Shigorin <mike@altlinux.org> 0.9.17-alt1
- 0.9.17 (considerable bugfixes)
- updated patch (sent upstream)

* Mon Dec 18 2006 Michael Shigorin <mike@altlinux.org> 0.9.16-alt2
- additionally fixed initscript, thanks gns@ again (see reopened #10407)

* Sat Dec 16 2006 Michael Shigorin <mike@altlinux.org> 0.9.16-alt1
- 1.9.16
- applied pidfile creation patch, updated initscript -- both by
  Nick S. Grechukh (gns@); closes #10407

* Wed Nov 01 2006 Michael Shigorin <mike@altlinux.org> 0.9.15-alt1
- rebuilt for Sisyphus

* Fri Sep 22 2006 Michael Shigorin <mike@altlinux.org> 0.9.15-alt0.M30.1
- 0.9.15
- built for 3.0
- added Url, s/Copyright:/License:/

* Mon Jan 16 2006 Anton Farygin <rider@altlinux.ru> 0.9.13-alt2
- use UNFS_OPTS from /etc/sysconfig/unfs3 in initscript

* Sun Jan 15 2006 Anton Farygin <rider@altlinux.ru> 0.9.13-alt1
- first build for Sisyphus
