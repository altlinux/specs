%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: thinkfan
Version: 1.3.1
Release: alt2
Summary: simple and lightweight fan control program
Group: System/Configuration/Hardware
License: GPL-3.0+
Url: https://sourceforge.net/projects/thinkfan/
VCS: https://github.com/vmatare/thinkfan.git
Source: %name-%version.tar
Source100: %name.watch

Patch1: %name-%version-%release.patch

BuildRequires: cmake gcc-c++ libatasmart-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: libsystemd-devel >= 255.6

%description
Thinkfan is a simple, lightweight fan control program. Originally designed
specifically for IBM/Lenovo Thinkpads, it now supports any kind of system via
the sysfs hwmon interface (/sys/class/hwmon). It is designed to eat as little
CPU power as possible.

%prep
%setup
%patch1 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%cmake \
	-DUSE_ATASMART:BOOL=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std
rm -rf %buildroot%_docdir/%name

%files
%doc COPYING
%doc README.md examples/*
%dir %_sysconfdir/systemd/system/thinkfan.service.d
%config(noreplace) %_sysconfdir/systemd/system/thinkfan.service.d/override.conf
%_unitdir/*.service
%_sbindir/%name
%_man1dir/%name.1*
%_man5dir/*.5*

%changelog
* Sun Jul 14 2024 Anton Farygin <rider@altlinux.ru> 1.3.1-alt2
- fixed build in environment with merged /usr

* Thu Feb 10 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.1-alt1
- Updated to upstream version 1.3.1.

* Thu Dec 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt1
- Updated to upstream version 1.3.0.

* Mon Jun 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.2-alt1
- Updated to upstream version 1.2.2.
- Added watch file.

* Tue Apr 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.1-alt1
- Updated to upstream version 1.2.1.

* Sun Sep 14 2014 Terechkov Evgenii <evg@altlinux.org> 0.9.1-alt1
- Initial build for ALT Linux Sisyphus
