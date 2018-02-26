# release timestamp of gradm
%define timestamp 200904141815

# don't want a debubinfo package
%define debug_package %nil

Summary: grsecurity RBAC Administration Toolset
Name: gradm
Version: 2.1.12
Release: alt1
License: GPL
Group: System/Kernel and hardware
Url: http://www.grsecurity.net
Packager: Michail Yakushin <silicium@altlinux.ru>
Source: %name-%version-%timestamp.tar
Source1: regression.tar
BuildRequires: libpam-devel flex

%description
The gradm packages provides userspace administration tools for
the RBAC portion of a grsecurity patched kernel.

%prep
%setup -q -n gradm2
tar xf $RPM_SOURCE_DIR/regression.tar

%build
make
cd regression
make

%install
mkdir -p %buildroot%_sysconfdir/grsec \
		%buildroot%_sysconfdir/makedev.d \
		%buildroot%_sysconfdir/udev/makedev.d \
		%buildroot%_sysconfdir/pam.d \
		%buildroot%_sysconfdir/init.d \
		%buildroot/sbin

%makeinstall_std \
	MKNOD=/bin/true MANDIR=%_mandir

echo "c 622 root root 1 13 1 1 grsec" > %buildroot%_sysconfdir/makedev.d/grsec
echo "grsec" > %buildroot%_sysconfdir/udev/makedev.d/90-grsec.nodes

ln -s login %buildroot%_sysconfdir/pam.d/grsec

install -m 0755 regression/grtest %buildroot/sbin/


%files
/sbin/gradm
/sbin/gradm_pam
/sbin/grlearn
/sbin/grtest
%_mandir/man*/*
%_sysconfdir/udev/makedev.d/90-grsec.nodes
%dir
%_sysconfdir/grsec

%changelog
* Thu Jun 04 2009 Michail Yakushin <silicium@altlinux.ru> 2.1.12-alt1
- initial build for ALT 

