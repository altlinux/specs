Name: unet
Version: 0.1
Release: alt1

Summary: unet - an userspace network events management
License: GPL3
Group: System/Base
Packager: Alexey Gladkov <legion@altlinux.ru>

Source: unet-%version.tar

%description
Unet is a generic kernel network events manager. It runs as a daemon
on a Linux system and listens (via netlink socket) to events the kernel sends
out whan a network configuration is changed.

%prep
%setup -q

%build
%make_build

%install
%make_install install \
	DESTDIR=%buildroot

mkdir -p -- \
	%buildroot/%_sysconfdir/unet/rules.d \
	%buildroot/run/net
cp ./unetfs.conf %buildroot/%_sysconfdir/

%post
%post_service unetd

%preun
%preun_service unetd

%files
%_initddir/unetd
/sbin/unetd
/lib/unet
%_sysconfdir/unet

# unetfs
%config %_sysconfdir/unetfs.conf
#ghost %dir /run/net

%changelog
* Wed Jun 20 2012 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- Initial build.

