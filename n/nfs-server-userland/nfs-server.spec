Name: nfs-server-userland
%define sname nfs-server
License: GPL
Group: Networking/Other
Requires: portmap
Conflicts: nfs-server
Version: 2.2beta51
Release: alt1
Summary: Userspace NFS server daemons
URL: ftp://linux.mathematik.tu-darmstadt.de/pub/linux/people/okir
Source: %sname-2.2beta47.tar.bz2
Source1: nfs.init
Source2: rpc.ugidd.init
Patch0: %sname-2.2b47-2.2b51.patch
Patch1: %sname-%version-destdir.patch
Patch2: %sname-%version-manpages.patch
Patch3: %sname-%version-strsignal.patch
Patch4: %sname-%version-sys-time.patch
Patch5: %sname-%version-reiserfs.patch
Patch6: %sname-%version-map.patch
Patch7: %sname-%version-configure.patch
Patch8: %sname-%version-multirw.patch
Patch9: %sname-%version-rmtab.patch

# Automatically added by buildreq on Fri Jan 09 2004
BuildRequires: libwrap-devel

%description
The NFS server daemons are needed when you wish to export directories
on your machine to other hosts via the NFS protocol.

There are 2 NFS Server: the userspace NFS server and the kernel NFS
server. This package contains the userspace NFS server. The utilities
for the kernel NFS server can be found in the "nfs-utils" package.

For quota over NFS support please install the "quota" package.

%prep
%setup -n %sname-2.2beta47 -q
%patch0 -p1
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9 -p1

%build
autoconf
%configure \
	--enable-ugid-dynamic \
	--enable-ugid-nis \
	--enable-host-access \
	--with-exports-uid=0 \
	--with-exports-gid=0 \
	--enable-mount-logging \
	--with-devtab=/var/lib/nfs/devtab
%make

%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/var/lib/nfs
install -d $RPM_BUILD_ROOT/var/adm/fillup-templates
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 744 %SOURCE1 $RPM_BUILD_ROOT/etc/rc.d/init.d/nfs
install -m 744 %SOURCE2 $RPM_BUILD_ROOT/etc/rc.d/init.d/ugidd
rm -f $RPM_BUILD_ROOT/usr/sbin/showmount
rm -f $RPM_BUILD_ROOT/usr/share/man/man8/showmount*

%post
%post_service nfs

%preun
%preun_service nfs


%files
%doc BUGS COPYING ChangeLog HALL_OF_FAME NEWS README README.HISTORIC TODO
%doc %_mandir/man?/*
/var/lib/nfs
/usr/sbin/*
/etc/rc.d/init.d/*

%changelog
* Tue Jan 13 2004 Anton Farygin <rider@altlinux.ru> 2.2beta51-alt1
- first build for Sisyphus
