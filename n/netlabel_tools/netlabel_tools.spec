Name:     netlabel_tools
Version:  0.20
Release:  alt3
Summary:  Configuration tools for the Linux NetLabel subsystem
License:  %gpl2only
Group:    System/Base
Packager: Andriy Stepanov <stanv@altlinux.ru>
Source:   %name-%version.tar
Patch1:   alt-build-netlabelctl-0.20.patch
Patch2:   alt-s0-mark-flag-0.20.patch
Patch3:   fedora-Port-to-libnl3.patch

BuildRequires: libnl-devel doxygen rpm-build-licenses

%description
NetLabel is a packet labeling framework that has been present in the upstream
Linux Kernel since 2.6.19. The NetLabel Tools project is a set of userspace
tools and libraries designed to make it easier to use and manage the Linux
Kernel's NetLabel configuration.

%prep
%setup -n %name-%version
%patch1 -p2
%patch2 -p2
%patch3 -p1

%build
./configure --enable-systemd --libdir=%_libdir --prefix=%_prefix
%make_build

%install
make DESTDIR=%buildroot install

%files
%_sysconfdir/netlabel.rules
%systemd_unitdir/netlabel.service
%_sbindir/netlabel-config
%_sbindir/netlabelctl
%_man8dir/netlabel-config.8.*
%_man8dir/netlabelctl.8.*

%changelog
* Tue Jan 12 2016 Mikhail Efremov <sem@altlinux.org> 0.20-alt3
- Don't specify extensions for man pages.
- Port to libnl3.

* Wed Jul 17 2013 Andriy Stepanov <stanv@altlinux.ru> 0.20-alt2
- Add mark s0 flag

* Thu Jun 20 2013 Andriy Stepanov <stanv@altlinux.ru> 0.20-alt1
- Initial build for ALT Linux
