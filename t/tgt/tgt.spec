Name: tgt
Version: 1.0.81
Release: alt1
License: %gpl2only
Group: System/Configuration/Networking
Source: %name-%version.tar
Patch: %name-%version-alt.patch
URL: https://github.com/fujita/tgt
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

ExclusiveArch: x86_64 ppc64le aarch64

BuildRequires(pre): rpm-build-licenses
BuildRequires: libssl-devel perl-Config-General rdma-core-devel xsltproc docbook-style-xsl libaio-devel ceph-devel

Summary: iSCSI utilities

%description
The %name aims to simplify various SCSI target driver (iSCSI, Fibre Channel, SRP, etc) 
creation and maintenance. Our key goals are the clean integration into the scsi-mid 
layer and implementing a great portion of tgt in user space. 

This package provides utils to create an iSCSI storage.

%prep
%setup
%patch -p1

%build
%make_build ISCSI=1 ISCSI_RDMA=1 CEPH_RBD=1

%install
%make DESTDIR=%buildroot docdir=%_docdir/%name-%version install

%__mkdir_p %buildroot%_initrddir
%__mkdir_p %buildroot%_sysconfdir/tgt/include.d
%__install -p -m 755 scripts/initd.alt  %buildroot%_initrddir/tgtd

%post
%post_service tgtd

%preun
%preun_service tgtd

%files
%doc doc/README.* doc/*.txt
%doc doc/htmlpages
%dir %_sysconfdir/tgt
%dir %_sysconfdir/tgt/include.d
%config %_sysconfdir/tgt/targets.conf
%_sysconfdir/tgt/examples
%_initdir/*
%_sbindir/*
%_man5dir/*
%_man8dir/*

%changelog
* Wed Feb 16 2022 Pavel Vasenkov <pav@altlinux.org> 1.0.81-alt1
- New version

* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.42-alt1
- New version
- Change URL

* Sat May 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.36-alt1
- New version
- Change URL
- Add support CEPH as backend

* Sun Jul 08 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.29-alt1
- New version
- Add libaio-devel to BuildRequires (Closes: #27526)

* Sun Feb 26 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.24-alt1
- New version

* Wed Dec 14 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.22-alt1
- New version

* Wed Apr 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.15-alt1
- New version

* Sat Nov 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.10-alt1
- New version

* Sun Sep 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.8-alt1
- New version

* Sat Feb 20 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt1
- New version

* Sun Jan 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- New version

* Sat Oct 31 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.10-alt1
- New version
- Update spec

* Wed Jul 29 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.7-alt1
- New version

* Thu Apr 09 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.5-alt1
- Build for ALT
