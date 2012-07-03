Name: srptools
Version: 0.0.4.1
Release: alt2
Summary: Tools for SRP/IB
Group: Networking/Other
License: %gpl2only
Url: http://www.openfabrics.org
Source: %name-%version.tar
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libibumad-devel libibverbs-devel

%define IB_CONF_DIR /etc/infiniband
%define ib_conf_dir %_sysconfdir/infiniband

%description
In conjunction with the kernel ib_srp driver, %name allows you to
discover and use SCSI devices via the SCSI RDMA Protocol over
InfiniBand.


%prep
%setup


%build
%configure
%make_build


%install
%make_install DESTDIR=%buildroot install


%post
if [ $1 = 1 -a -w %ib_conf_dir/openib.conf ]; then
    echo >> %ib_conf_dir/openib.conf
    echo "# Enable SRP High Availability daemon" >> %ib_conf_dir/openib.conf
    echo "SRPHA_ENABLE=no" >> %ib_conf_dir/openib.conf
    echo "SRP_DAEMON_ENABLE=no" >> %ib_conf_dir/openib.conf
fi


%files
%doc README NEWS ChangeLog COPYING
%config(noreplace) %_sysconfdir/srp_daemon.conf
%_sbindir/*
%_man1dir/*


%changelog
* Thu Sep 02 2010 Andriy Stepanov <stanv@altlinux.ru> 0.0.4.1-alt2
- Rebuild with new libibumad

* Wed Aug 18 2010 Andriy Stepanov <stanv@altlinux.ru> 0.0.4.1-alt1
- OFED 1.5.1

* Mon Oct 27 2008 Led <led@altlinux.ru> 0.0.4-alt1
- initial build for ALTLinux

* Wed Aug 22 2007 Vladimir Sokolovsky <vlad@mellanox.co.il>
- Added srp_daemon.conf
* Tue Sep  5 2006 Vladimir Sokolovsky <vlad@mellanox.co.il>
- Added srp_daemon and scripts to execute this daemon
* Tue Mar 21 2006 Roland Dreier <rdreier@cisco.com> - 0.0.4-1
- Initial attempt at a working spec file
