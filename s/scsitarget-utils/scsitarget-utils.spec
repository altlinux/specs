%ifnarch s390 s390x
%global with_rdma 1
%endif

Name:		scsitarget-utils
Version:	1.0.30
Release:	alt1
Summary:	The SCSI target daemon and utility programs

Group:		System/Configuration/Hardware
License:	GPLv2
URL:		http://stgt.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Source1:	tgtd.service
Source2:	sysconfig.tgtd
Source3:	targets.conf
Source4:	sample.conf
Source5:	tgtd.conf
Patch0:		%{name}-redhatify-docs.patch
Patch1:		%{name}-remove-xsltproc-check.patch
Patch2:		%{name}-include-dirs.patch

BuildRequires:	pkgconfig
BuildRequires:	libxslt
BuildRequires:	docbook-style-xsl
BuildRequires:	systemd-units
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
Requires(post):	systemd-units

%description
The SCSI target package contains the daemon and tools to setup a SCSI
targets. Currently, software iSCSI targets are supported.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__sed} -i -e 's|-g -O2 -Wall|%{optflags}|' Makefile
%{__make} %{?_smp_mflags} %{?with_rdma:ISCSI_RDMA=1} libdir=%{_libdir}/tgt

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_sbindir}
%{__install} -d %{buildroot}%{_mandir}/man5
%{__install} -d %{buildroot}%{_mandir}/man8
%{__install} -d %{buildroot}%{_unitdir}
%{__install} -d %{buildroot}%{_sysconfdir}/tgt
%{__install} -d %{buildroot}%{_sysconfdir}/tgt/conf.d
%{__install} -d %{buildroot}%{_sysconfdir}/sysconfig

%{__install} -p -m 0755 scripts/tgt-setup-lun %{buildroot}%{_sbindir}
%{__install} -p -m 0755 %{SOURCE1} %{buildroot}%{_unitdir}
%{__install} -p -m 0755 scripts/tgt-admin %{buildroot}/%{_sbindir}/tgt-admin
%{__install} -p -m 0644 doc/manpages/targets.conf.5 %{buildroot}/%{_mandir}/man5
%{__install} -p -m 0644 doc/manpages/tgtadm.8 %{buildroot}/%{_mandir}/man8
%{__install} -p -m 0644 doc/manpages/tgt-admin.8 %{buildroot}/%{_mandir}/man8
%{__install} -p -m 0644 doc/manpages/tgt-setup-lun.8 %{buildroot}/%{_mandir}/man8
%{__install} -p -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/tgtd
%{__install} -p -m 0600 %{SOURCE3} %{buildroot}%{_sysconfdir}/tgt
%{__install} -p -m 0600 %{SOURCE4} %{buildroot}%{_sysconfdir}/tgt/conf.d
%{__install} -p -m 0600 %{SOURCE5} %{buildroot}%{_sysconfdir}/tgt

pushd usr
%{__make} install %{?with_rdma:ISCSI_RDMA=1} DESTDIR=%{buildroot} sbindir=%{_sbindir} libdir=%{_libdir}/tgt

%post
if [ $1 -eq 1 ]; then
    systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ]; then
    systemctl --no-reload disable tgtd.service >/dev/null 2>&1 || :
    systemctl stop tgtd.service >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ]; then
    systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%files
%defattr(-, root, root, -)
%doc README doc/README.iscsi doc/README.iser doc/README.lu_configuration doc/README.mmc doc/README.ssc
%{_sbindir}/tgtd
%{_sbindir}/tgtadm
%{_sbindir}/tgt-setup-lun
%{_sbindir}/tgt-admin
%{_sbindir}/tgtimg
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_unitdir}/tgtd.service
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/tgtd
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/tgt/targets.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/tgt/tgtd.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/tgt/conf.d/sample.conf

%changelog
* Wed Oct 03 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0.30-alt1
- Initial release for Sisyphus
