Name: checkpolicy
Version: 2.0.23
Release: alt1
License: GPL
Url: http://userspace.selinuxproject.org/

Source: %name-%version.tar
Summary: This package contains the checkpolicy policy compiler, which is needed to compile policies to the binary form used by the kernel
Group: System/Configuration/Other
# Automatically added by buildreq on Sun Mar 09 2008
BuildRequires: flex libselinux-devel libsepol-devel libsepol-devel-static

%description
SELinux policy compiler
Security-enhanced Linux is a patch of the Linux(R) kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement(R), Role-based Access
Control, and Multi-level Security.

This package contains checkpolicy, the SELinux policy compiler.
Only required for building policies.

%prep
%setup

%build
%make_build LIBDIR=%_libdir CFLAGS="%optflags -Wshadow -fno-strict-aliasing"

%install
%make DESTDIR=%buildroot install

%files
%_man8dir/*
%_bindir/*

%changelog
* Wed Dec 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.23-alt1
- Updated to 2.0.23.

* Wed Aug 25 2010 Mikhail Efremov <sem@altlinux.org> 2.0.22-alt1
- 2.0.22
- drop Packager from spec.
- fix Url.
- use %%optflags.

* Thu Mar 04 2010 Mikhail Efremov <sem@altlinux.org> 2.0.21-alt1
- new version

* Thu May 07 2009 Anton Farygin <rider@altlinux.ru> 2.0.19-alt1
- new version

* Mon Dec 22 2008 Anton Farygin <rider@altlinux.ru> 2.0.18-alt1
- new version

* Sat Dec 20 2008 Anton Farygin <rider@altlinux.ru> 2.0.16-alt1
- new (development) version
- specfile cleanup

* Sun Mar 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.34.5-alt1
- Initial build
