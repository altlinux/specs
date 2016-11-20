Name: checkpolicy
Epoch: 1
Version: 2.5
Release: alt1
Summary: SELinux policy compiler
Group: System/Configuration/Other
License: GPLv2
Url: http://userspace.selinuxproject.org
Source: %name-%version.tar
Patch1: alt-ddecl.patch

BuildRequires: flex libselinux-devel >= 2.5 libsepol-devel >= 2.5 libsepol-devel-static >= 2.5

%description
Security-enhanced Linux is a patch of the Linux(R) kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement(R), Role-based Access
Control, and Multi-level Security.

This package contains checkpolicy, the SELinux policy compiler.
Only required for building policies.


%prep
%setup -q
%patch1 -p1


%build
%make_build LIBDIR=%_libdir CFLAGS="%optflags"


%install
%makeinstall_std
for f in dis{mod,pol}; do
	install test/$f %buildroot%_bindir/se$f
done


%files
%_bindir/*
%_man8dir/*


%changelog
* Thu Oct 27 2016 Anton Farygin <rider@altlinux.ru> 1:2.5-alt1
- new version

* Thu Sep 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:2.3-alt1
- downgraded due regression (closes: #32254)

* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 2.4-alt1
- new version

* Thu Feb 05 2015 Anton Farygin <rider@altlinux.ru> 2.3-alt1
- new version

* Tue Nov 19 2013 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- New version

* Thu Jun 27 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.12-alt1
- New version

* Mon Sep 24 2012 Led <led@altlinux.ru> 2.1.11-alt1
- 2.1.11
- cleaned up spec
- fixed License
- added test utils

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
