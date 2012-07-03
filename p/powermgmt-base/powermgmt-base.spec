Name: powermgmt-base
Version: 1.22
Release: alt1

Summary: Common utils and configs for power management
License: GPL
Group: System/Base
%define srcname %{name}_%version

Source: ftp://ftp.debian.org/debian/pool/main/p/%name/%srcname.tar.gz
Source1: apm-scripts.tar.gz

Patch: %name-1.20-alt-fixes.patch

# due to clock_unsynced
Requires: hwclock >= 0:2.23-alt6

%description
This package contains utilities and configuration files for power
management that are common to APM and ACPI.

%prep
%setup -q -a1
%patch -p1

%build
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
%__mkdir_p $RPM_BUILD_ROOT{%_bindir,%_man1dir,{%_sysconfdir,/var/run}/apm}
%make_install install DESTDIR=$RPM_BUILD_ROOT
%__install -m644 man/*.1 $RPM_BUILD_ROOT%_man1dir/
%__cp -a apm-scripts/* $RPM_BUILD_ROOT%_sysconfdir/apm/
%__chmod 700 $RPM_BUILD_ROOT/var/run/apm

%files
%_bindir/*
%_man1dir/*
%dir %_sysconfdir/apm
%dir %_sysconfdir/apm/*.d
%_sysconfdir/apm/resume.d/*
%_sysconfdir/apm/suspend.d/*
%config %_sysconfdir/apm/scripts.d/*
%dir /var/run/apm

%changelog
* Sat Jun 11 2005 Dmitry V. Levin <ldv@altlinux.org> 1.22-alt1
- Updated to 1.21.
- scripts.d/hwclock: do nothing if clock is in synced mode.

* Mon Sep 06 2004 Dmitry V. Levin <ldv@altlinux.org> 1.21-alt1
- Updated to 1.21.
- Disabled console script (#4725).

* Mon Apr 19 2004 Dmitry V. Levin <ldv@altlinux.org> 1.20-alt1
- Imported from Debian.
- Implemented several basic apm scripts.
