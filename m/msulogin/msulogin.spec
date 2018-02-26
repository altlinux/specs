Name: msulogin
Version: 0.9.1.1
Release: alt1

Summary: The single user mode login program (sulogin)
License: GPLv2+
Group: System/Base
Url: http://www.openwall.com/msulogin/
Packager: Dmitry V. Levin <ldv@altlinux.org>

%def_with selinux

# git://git.altlinux.org/gears/m/msulogin
Source: %name-%version-%release.tar

%{?_with_selinux:BuildRequires: libselinux-devel}

#Conflicts: SysVinit < 2.85-alt3

%description
sulogin is a program to force the console user to login under a root
account before a shell is started.  Unlike other implementations of
sulogin, this one supports having multiple root accounts on a system.

%prep
%setup -n %name-%version-%release

%build
make CFLAGS="-c %optflags" LDFLAGS= %{?_with_selinux:WITH_SELINUX=1}

%install
%make_install install DESTDIR=%buildroot MANDIR=%_mandir

%files
%doc LICENSE
/sbin/sulogin
%_mandir/man?/*

%changelog
* Mon Aug 02 2010 Dmitry V. Levin <ldv@altlinux.org> 0.9.1.1-alt1
- Implemented SELinux support (by Mikhail Efremov).

* Fri Apr 25 2008 Dmitry V. Levin <ldv@altlinux.org> 0.9.1-alt4
- Removed explicit pathname provides.
- Removed conflict with SysVinit < 2.85-alt3, with hope that
  all sulogin users already updated their systems to msulogin.

* Sat Apr 07 2007 Dmitry V. Levin <ldv@altlinux.org> 0.9.1-alt3
- Suppressed compilation warning.

* Sat Oct 18 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.1-alt2
- Rebuilt.

* Fri May 23 2003 Solar Designer <solar@owl.openwall.com> 0.9.1-owl1
- Avoid a race condition in the handling of timeout pointed out by
  Pavel Kankovsky on owl-devel.

* Sun Apr 27 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9-alt1
- Built for ALT Linux.

* Sun Apr 27 2003 Solar Designer <solar@owl.openwall.com> 0.9-owl1
- Wrote this program and the accompanying files.
