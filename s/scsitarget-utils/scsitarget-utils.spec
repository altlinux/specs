%ifnarch s390 s390x
%global with_rdma 1
%endif

Name:		scsitarget-utils
Version:	1.0.30
Release:	alt6

Summary:	The SCSI target daemon and utility programs

Group:		System/Configuration/Hardware
License:	GPLv2
URL:		http://stgt.sourceforge.net/

Source0:	%name-%version.tar
Source1:	tgt.service
Source2:	sysconfig.tgtd
Source3:	targets.conf
Source4:	sample.conf
Source5:	tgtd.conf
Source6:	tgt.init
Patch0:		%name-redhatify-docs.patch
Patch1:		%name-remove-xsltproc-check.patch
Patch2:		%name-include-dirs.patch

BuildRequires:	pkgconfig
BuildRequires:	libxslt
BuildRequires:	docbook-style-xsl
BuildRequires:	xsltproc
BuildRequires:	perl-Config-General
%if 0%{?with_rdma}
BuildRequires:	libibverbs-devel
BuildRequires:	librdmacm-devel
Requires:	libibverbs
Requires:	librdmacm
%endif
Requires:	lsof
Requires:	sg3_utils


%description
The SCSI target package contains the daemon and tools to setup a SCSI
targets. Currently, software iSCSI targets are supported.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%__subst 's|-g -O2 -Wall|%optflags|' Makefile
%make_build %{?with_rdma:ISCSI_RDMA=1} libdir=%_libdir/tgt

%install
install -d %buildroot%_sbindir
install -d %buildroot%_man5dir
install -d %buildroot%_man8dir
install -d %buildroot%_unitdir
install -d %buildroot%_initdir
install -d %buildroot%_sysconfdir/tgt
install -d %buildroot%_sysconfdir/tgt/conf.d
install -d %buildroot%_sysconfdir/sysconfig

install -p -m 0755 scripts/tgt-setup-lun %buildroot%_sbindir
install -p -m 0755 %SOURCE1 %buildroot%_unitdir
install -p -m 0755 scripts/tgt-admin %buildroot/%_sbindir/tgt-admin
install -p -m 0644 doc/manpages/targets.conf.5 %buildroot/%_man5dir
install -p -m 0644 doc/manpages/tgtadm.8 %buildroot/%_man8dir
install -p -m 0644 doc/manpages/tgt-admin.8 %buildroot/%_man8dir
install -p -m 0644 doc/manpages/tgt-setup-lun.8 %buildroot/%_man8dir
install -p -m 0600 %SOURCE2 %buildroot%_sysconfdir/sysconfig/tgtd
install -p -m 0600 %SOURCE3 %buildroot%_sysconfdir/tgt
install -p -m 0600 %SOURCE4 %buildroot%_sysconfdir/tgt/conf.d
install -p -m 0600 %SOURCE5 %buildroot%_sysconfdir/tgt
install -p -m 0755 %SOURCE6 %buildroot%_initdir/tgt

pushd usr
%makeinstall_std %{?with_rdma:ISCSI_RDMA=1} sbindir=%_sbindir libdir=%_libdir/tgt

%post
%post_service tgt

%preun
%preun_service tgt

%files
%doc README doc/README.iscsi doc/README.iser doc/README.lu_configuration doc/README.mmc doc/README.ssc
%_sbindir/tgtd
%_sbindir/tgtadm
%_sbindir/tgt-setup-lun
%_sbindir/tgt-admin
%_sbindir/tgtimg
%_man5dir/*
%_man8dir/*
%_unitdir/tgt.service
%_initdir/tgt
%dir %_sysconfdir/tgt
%dir %_sysconfdir/tgt/conf.d
%attr(0600,root,root) %config(noreplace) %_sysconfdir/sysconfig/tgtd
%attr(0600,root,root) %config(noreplace) %_sysconfdir/tgt/targets.conf
%attr(0600,root,root) %config(noreplace) %_sysconfdir/tgt/tgtd.conf
%attr(0600,root,root) %config(noreplace) %_sysconfdir/tgt/conf.d/sample.conf

%changelog
* Tue Sep 03 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt6
- Rename tgtd.{init,service} files to tgt.{init,service}

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.30-alt5
- cleanup spec

* Sat Mar 30 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt4.1
- Add SysVinit support

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt4
- Fix unowned files

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt3
- Use post/preun_service scripts in spec

* Tue Jan 29 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt2
- Fix build with new docbook-style-xsl

* Wed Oct 03 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt1
- Initial release for Sisyphus
