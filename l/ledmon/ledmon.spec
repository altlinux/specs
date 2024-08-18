%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:     ledmon
Version:  1.0.0
Release:  alt1

Summary:  Enclosure LED Utilities
License:  GPL-2.0-only or LGPL-2.1-or-later
Group:    System/Kernel and hardware
Url:      https://github.com/intel/ledmon

Source:   %name-%version.tar

BuildRequires: libpci-devel
BuildRequires: libsgutils-devel
BuildRequires: libudev-devel
BuildRequires: /usr/bin/pod2man
BuildRequires: autoconf-archive

%description
The ledmon and ledctl are user space applications designed to control
LED associated with each slot in an enclosure or a drive bay.

%prep
%setup

%build
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --enable-systemd
%make_build

%install
%makeinstall_std
install -Dpm644 systemd/ledmon.service -t %buildroot%_unitdir
rm %buildroot%_docdir/%name/README.md

%post
%post_service ledmon

%preun
%preun_service ledmon

%files
%doc COPYING* *.md
%_sbindir/ledctl
%_sbindir/ledmon
%_unitdir/ledmon.service
%_man5dir/ledmon.conf.5*
%_man8dir/ledctl.8*
%_man8dir/ledmon.8*

%changelog
* Sun Aug 18 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.0.0-alt1
- 1.0.0

* Wed Feb 14 2024 Vitaly Chikunov <vt@altlinux.org> 0.97-alt2
- spec: Packaging improvements.
- Enable systemd service.

* Wed Feb 14 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.97-alt1
- 0.97

* Wed Sep 04 2019 Andrew A. Vasilyev <andy@altlinux.org> 0.92-alt1
- Initial import for ALT
