%define _unpackaged_files_terminate_build 1

Name:     netlabel_tools
Version:  0.30.0
Release:  alt3
Summary:  Configuration tools for the Linux NetLabel subsystem
License:  %gpl2only
Group:    System/Base
Url:      https://github.com/netlabel/netlabel_tools

Source:   %name-%version.tar
Patch1:   %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: libnl-devel doxygen systemd-devel

%description
NetLabel is a packet labeling framework that has been present in the upstream
Linux Kernel since 2.6.19. The NetLabel Tools project is a set of userspace
tools and libraries designed to make it easier to use and manage the Linux
Kernel's NetLabel configuration.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure --with-systemdsystemunitdir=auto
%make_build

%install
%makeinstall_std

%find_lang --with-man --all-name %name

%files -f %name.lang
%config(noreplace) %_sysconfdir/netlabel.rules
%systemd_unitdir/netlabel.service
%_sbindir/netlabel-config
%_sbindir/netlabelctl
%_man8dir/netlabel-config.8*
%_man8dir/netlabelctl.8*

%changelog
* Tue Dec 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.30.0-alt3
- Added man pages translation by Olesya Gerasimenko.

* Tue Apr 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.30.0-alt2
- Updated to upstream version 0.30.0.

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.21-alt2
- NMU: added URL

* Wed Jan 18 2017 Anton Farygin <rider@altlinux.ru> 0.21-alt1
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
