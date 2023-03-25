Name: dlm
Version: 4.2.0
Release: alt1

Summary: dlm control daemon and tool
License: GPLv2 and GPLv2+ and LGPLv2+
Group: System/Servers

Url: https://pagure.io/dlm
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: libsystemd-devel libcorosync-devel libuuid-devel
%ifnarch %e2k
BuildRequires: libpacemaker-devel
%endif

Requires: corosync >= 1.99.9

%description
The kernel dlm requires a user daemon to control membership.

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
The lib%name package contains the libraries needed to use the dlm
from userland applications.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch0 -p1
%ifarch %e2k
# unsupported as of lcc 1.32.21
sed -i 's,-fstack-clash-protection,,' */Makefile
# needs libpacemaker-devel (ftbfs atm)
sed -i 's,fence,,' Makefile
%endif
%ifnarch x86_64
sed -i 's, -fcf-protection=full,,' */Makefile
%endif

%build
export CFLAGS="$CFLAGS -fPIC $(pkg-config --cflags pacemaker) -I../libdlm -I../dlm_controld -I../include"
export LDCONF
%make CFLAGS="$CFLAGS" LLT_LDFLAGS="-lpthread"
%ifnarch %e2k
%make -C fence CFLAGS="$CFLAGS"
%endif

%install
%makeinstall_std LIBNUM=/%_lib UDEVDIR=%_udevrulesdir
%ifnarch %e2k
%makeinstall_std -C fence
%endif

install -Dm 0644 init/dlm.service %buildroot%_unitdir/dlm.service
install -Dm 0644 init/dlm.sysconfig %buildroot%_sysconfdir/sysconfig/dlm

mkdir -p %buildroot%_sysconfdir/dlm
touch %buildroot%_sysconfdir/dlm/dlm.conf

%files
%doc README.license
%config(noreplace) %_sysconfdir/sysconfig/dlm
%dir %_sysconfdir/dlm
%ghost %_sysconfdir/dlm/dlm.conf
%_unitdir/dlm.service
%_sbindir/dlm_controld
%_sbindir/dlm_tool
%ifnarch %e2k
%_sbindir/dlm_stonith
%endif
%_man8dir/dlm*
%_man5dir/dlm*
%_man3dir/*dlm*

%files -n lib%name
%_udevrulesdir/*-dlm.rules
%_libdir/libdlm*.so.*

%files -n lib%name-devel
%_includedir/libdlm*.h
%_libdir/libdlm*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Oct 12 2022 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version.

* Tue Nov 16 2021 Andrey Cherepanov <cas@altlinux.org> 4.1.1-alt1
- New version.

* Mon Jul 26 2021 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt2
- Rebuild with -fPIC for all architectures.

* Mon Jul 26 2021 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- 4.1.0

* Fri Apr 03 2020 Michael Shigorin <mike@altlinux.org> 4.0.9-alt2
- E2K: build without fence (BR: libpacemaker-devel, unavailable now)

* Sun Aug 11 2019 Alexey Shabalin <shaba@altlinux.org> 4.0.9-alt1
- 4.0.9

* Wed Aug 02 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Wed Sep 14 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Mon Sep 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.2-alt2
- fixed build with latest systemd

* Mon Mar 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.2-alt1
- 4.0.2
