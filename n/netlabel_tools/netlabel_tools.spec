Name:     netlabel_tools
Version:  0.21
Release:  alt1%ubt
Summary:  Configuration tools for the Linux NetLabel subsystem
License:  %gpl2only
Group:    System/Base
Source:   %name-%version.tar
Patch1:   alt-build-netlabelctl-0.21.patch
Patch2:   alt-s0-mark-flag-0.21.patch
Patch3:   upstream-add-missingfiles-0.21.patch

BuildRequires: libnl-devel doxygen systemd-devel
BuildRequires(pre):rpm-build-licenses rpm-build-ubt

%description
NetLabel is a packet labeling framework that has been present in the upstream
Linux Kernel since 2.6.19. The NetLabel Tools project is a set of userspace
tools and libraries designed to make it easier to use and manage the Linux
Kernel's NetLabel configuration.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fisv
%configure --with-systemdsystemunitdir=auto
%make_build

%install
%makeinstall_std

%files
%config(noreplace) %_sysconfdir/netlabel.rules
%systemd_unitdir/netlabel.service
%_sbindir/netlabel-config
%_sbindir/netlabelctl
%_man8dir/netlabel-config.8.*
%_man8dir/netlabelctl.8.*

%changelog
* Wed Jan 18 2017 Anton Farygin <rider@altlinux.ru> 0.21-alt1%ubt
- added ubt tag
- netlabel.rules marked as non-replaced config

* Tue Jan 17 2017 Anton Farygin <rider@altlinux.ru> 0.21-alt1
- updated to 0.21

* Tue Jan 12 2016 Mikhail Efremov <sem@altlinux.org> 0.20-alt3
- Don't specify extensions for man pages.
- Port to libnl3.

* Wed Jul 17 2013 Andriy Stepanov <stanv@altlinux.ru> 0.20-alt2
- Add mark s0 flag

* Thu Jun 20 2013 Andriy Stepanov <stanv@altlinux.ru> 0.20-alt1
- Initial build for ALT Linux
