Name: dlm
Version: 4.0.2
Release: alt2
Summary: dlm control daemon and tool
License: GPLv2 and GPLv2+ and LGPLv2+
Group: System/Servers
URL: https://fedorahosted.org/cluster

Requires: corosync2

Source0: http://people.redhat.com/teigland/%name-%version.tar.gz
Patch0: 0001-dlm_stonith-add-man-page.patch
Patch1: 0002-dlm_stonith-install-man-page.patch
Patch2: 0003-libdlm-udev-dir-now-under-usr-lib.patch
Patch3: 0005-dlm_tool-fix-status-printing-in-libdlmcontrol.patch
Patch4: 0008-dlm-clear-out-addrs-before-calling-into-corosync_cft.patch
Patch5: 0010-dlm_controld-don-t-log-error-from-cpg_dispatch.patch
Patch6: dlm-4.0.2-systemd-pkg.patch

BuildRequires: libpacemaker-devel libsystemd-devel

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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%make
%make -C fence

%install
%make LIBNUM=/%_lib UDEVDIR=%_udevrulesdir DESTDIR=%buildroot install
%make -C fence DESTDIR=%buildroot install

install -Dm 0644 init/dlm.service %buildroot%_unitdir/dlm.service
install -Dm 0644 init/dlm.sysconfig %buildroot/etc/sysconfig/dlm

%post
%post_service dlm

%preun
%preun_service dlm

%files
%doc README.license
%config(noreplace) %_sysconfdir/sysconfig/dlm
%_unitdir/dlm.service
%_sbindir/dlm_controld
%_sbindir/dlm_tool
%_sbindir/dlm_stonith
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
* Mon Sep 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.2-alt2
- fixed build with latest systemd

* Mon Mar 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.2-alt1
- 4.0.2
