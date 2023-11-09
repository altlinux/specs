Name: netatop
Version: 3.1
Release: alt1
Summary: Daemon fo gather statistics about the TCP and UDP packets
License: GPLv2
Group: Monitoring
URL: https://www.atoptool.nl
Source: %url/%name-%version.tar
Patch: %name-%version-%release.patch
Provides: %{name}d = %version-%release

BuildPreReq: rpm-build-kernel
BuildRequires: zlib-devel

%description
The optional kernel module netatop can be loaded to gather statistics about the
TCP and UDP packets that have been transmitted/received per process and per
thread. As soon as atop discovers that this module is active, it shows columns in
the generic screen for the number of transmitted and received packets per
process.
The daemon netatopd takes care that information is gathered about processes that
are finished. For every finished process that has transferred network packets, a
binary record is written to a logfile. The added records in the logfile are read
by atop with every sample to show information about the network activity of
finished processes as well.
The daemon is started automatically in the init script after the kernel module
has been loaded. However, the kernel module netatop can be used without the
netatopd daemon.


%package -n kernel-source-%name
Summary: Kernel source for %name module
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
This is the source of the kernel %name module.


%prep
%setup
%patch -p1
sed -i 's|\.\./\(%name\)|\1|' module/{Makefile,*.c}
ln -s ../%name{,version}.h module/
ln -sf module kernel-source-%name-%version


%build
./mkversion
%make_build -C daemon CFLAGS="%optflags"


%install
install -d -m 0755 %buildroot{%_sbindir,%_man4dir,%_man8dir} %kernel_srcdir
install -pD -m 0755 %name.init %buildroot%_initddir/%name
install -pD -m 0644 %name.service %buildroot%_unitdir/%name.service
install -p -m 0755 daemon/%{name}d %buildroot%_sbindir/
install -p -m 0644 man/*.4 %buildroot%_man4dir/
install -p -m 0644 man/*.8 %buildroot%_man8dir/

tar --transform='s,^module,%name-%version,' -cJhf %kernel_srcdir/%name-%version.tar.xz module


%post
%post_service %name


%preun
%preun_service %name


%files
%_sbindir/*
%_initddir/*
%_unitdir/*
%_man4dir/*
%_man8dir/*


%files -n kernel-source-%name
%_usrsrc/kernel


%changelog
* Thu Nov 09 2023 Leontiy Volodin <lvol@altlinux.org> 3.1-alt1
- 3.1

* Sun Sep 01 2013 Led <led@altlinux.ru> 0.3-alt1
- 0.3

* Wed Apr 17 2013 Led <led@altlinux.ru> 0.2-alt1
- 0.2

* Mon Dec 24 2012 Led <led@altlinux.ru> 0.1.1-alt2
- service disabled by default

* Sun Dec 23 2012 Led <led@altlinux.ru> 0.1.1-alt1
- initial build
