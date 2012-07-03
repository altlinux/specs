Name: ggaoed
Version: 1.1
Release: alt1

Summary: AoE target implementation for Linux
License: GPL
Group: Networking/Other
Url: http://code.google.com/p/ggaoed/

Source: %name-%version-%release.tar

BuildRequires: glib2-devel docbook2X libaio-devel libatomic_ops-devel-static libblkid-devel xsltproc

%description
ggaoed is an AoE target implementation for Linux, with the following features:
- A single process can handle any number of devices and any number of
  network interfaces
- Uses kernel AIO to avoid blocking on I/O
- Request merging: read/write requests for adjacent data blocks can
  be submitted as a single I/O request
- Request batching: multiple I/O requests can be submitted with a
  single system call
- Supports hotplugging/unplugging of network interfaces
- Uses eventfd for receiving notifications about I/O completion
- Uses epoll for handling event notifications
- Uses memory mapped packets to lower system call overhead when receiving and
  sending data
- Devices to export can be identified either by path or by UUID (using the
  libblkid library)
- Delayed I/O submission utilizing timerfd (experimental)

%prep
%setup

%build
%autoreconf
%configure --localstatedir=/var
%make_build

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_localstatedir/ggaoed
install -pm0755 -D aoed.init %buildroot%_initdir/aoed
install -pm0600 -D ggaoed.conf.dist %buildroot%_sysconfdir/ggaoed.conf

%post
%post_service aoed

%preun
%preun_service aoed

%files
%doc README COPYING NEWS

%_initdir/aoed
%attr(0600,root,root) %config(noreplace) %_sysconfdir/ggaoed.conf

%_sbindir/ggaoectl
%_sbindir/ggaoed

%_localstatedir/ggaoed

%_man5dir/ggaoed.conf.5*
%_man8dir/ggaoectl.8*
%_man8dir/ggaoed.8*

%changelog
* Thu Jun 02 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1-alt1
- initial
