Summary: NFS Utils for NFS-RDMA
Name: rnfs-utils
Group: System/Servers
License: GPL
Version: 1.1.5
Release: alt2

BuildRequires: libblkid-devel libevent-devel libnfsidmap-devel >= 0.20-alt1 libwrap-devel
BuildRequires: libkrb5-devel libgssglue-devel librpcsecgss-devel >= 0.17-alt1
BuildRequires: libcap-devel

Source: nfs-utils-%version.tar

Patch0: nfs-utils-ignore_kernel_version.patch
Patch1: rnfsv4_support.patch

%description
This package provides only the mount binary necessary to mount NFS-RDMA
connections.  All other NFS utilities are provided by the nfs-utils RPM
(which is required by this package).  The installed binary will be named
mount.rnfs

This package should be unnecessary on systems with kernels newer than
2.6.22 and nfs-utils newer than 1.1.2.

%prep
%setup -n nfs-utils-%version
%patch0 -p1
%patch1 -p1

%build
%autoreconf -fisv
%configure --disable-gss --without-tcp-wrappers --program-transform-name="s/nfs/rnfs/g"
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/sbin
#if [ ! -e /sbin/rpc.statd ]; then
#	cp utils/statd/statd $RPM_BUILD_ROOT/sbin/rpc.statd
#fi
cp utils/mount/mount.nfs $RPM_BUILD_ROOT/sbin/mount.rnfs
cp utils/mount/mount.nfs $RPM_BUILD_ROOT/sbin/mount.rnfs4
cp utils/mount/mount.nfs $RPM_BUILD_ROOT/sbin/umount.rnfs
cp utils/mount/mount.nfs $RPM_BUILD_ROOT/sbin/umount.rnfs4

%files
%defattr(-,root,root)
/sbin/*

%changelog
* Fri Aug 13 2010 Andriy Stepanov <stanv@altlinux.ru> 1.1.5-alt2
- Don't pack rpc.statd. Use nfs-clients instead.

* Thu Aug 12 2010 Andriy Stepanov <stanv@altlinux.ru> 1.1.5-alt1
- Initial build for ALT Linux

