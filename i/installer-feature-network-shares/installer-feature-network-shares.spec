Name: installer-feature-network-shares
Version: 0.8.2
Release: alt1

%define hookdir %_datadir/install2/postinstall.d

%add_findreq_skiplist %hookdir/*

Summary: Installer stage3 NFS/SMB/FTP shares hooks
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%package stage3
Summary: %summary
Group: System/Configuration/Other
Requires: coreutils libshell sed

%description stage3
This package contains installer stage2 hooks for NFS, SMB and FTP services.

%prep
%setup

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot/%hookdir
install -pm755 *.sh %buildroot/%hookdir/

%files stage3
%hookdir/*

%changelog
* Tue Oct 04 2022 Dmitry Terekhin <jqt4@altlinux.org> 0.8.2-alt1
- Remove smb.conf fix causing the problem

* Tue Jun 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1
- Return 0 in any case in last conditionals

* Thu Jun 18 2015 Andrey Cherepanov <cas@altlinux.org> 0.8-alt1
- Fix continue work in empty installation

* Fri May 08 2015 Andrey Cherepanov <cas@altlinux.org> 0.7-alt1
- Conditional FTP settings changes

* Wed May 06 2015 Andrey Cherepanov <cas@altlinux.org> 0.6-alt1
- Replace /var/ftp by symlink to ../srv/public and do not treat it as fatal

* Mon Oct 13 2014 Mikhail Efremov <sem@altlinux.org> 0.5-alt1
- Don't require install2-init-functions.
- Move hook to preinstall.

* Mon Nov 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- s/portmap/rpcbind/

* Thu Sep 30 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt2
- rewrite smb.conf if exists

* Tue Sep 28 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- no secure NFS by default (enabled secure NFS without
  customized Kerberos means no NFS)

* Tue Aug 31 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt2
- backup original smb.conf

* Wed Aug 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- modified for samba 3.5

* Wed Feb 24 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt13
- use predefined fsid for public nfs share

* Mon Aug 24 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt12
- made smb [homes] exported too

* Thu May  7 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt11
- made shared directory sticky

* Tue Apr 28 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt10
- announce via avahi smb share name, not path

* Mon Apr 27 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt9
- turn on nfs & smb services

* Mon Apr 27 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt8
- do not check for dedicated /srv

* Thu Apr 23 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt7
- turn on svcgssd by default

* Thu Apr 23 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt6
- add export and announce for nfs shares

* Wed Apr 15 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt5
- dedicated /srv detection fixed

* Fri Apr 10 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt4
- samba-related hooks added

* Mon Mar 30 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt3
- avoid autogenerated req on installer-common-stage2

* Fri Mar 27 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt2
- made ftp service discoverable too

* Thu Mar 26 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- Initial revision
