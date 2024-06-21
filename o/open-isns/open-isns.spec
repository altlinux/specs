%define _unpackaged_files_terminate_build 1
%define _localstatedir %_var

Name: open-isns
Version: 0.102
Release: alt2
Summary: The iSNS daemon and utility programs

Group: System/Servers
License: LGPLv2+
Url: https://github.com/open-iscsi/open-isns
Source: %name-%version.tar
Source2: isnsd.init
Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.54.0
BuildRequires: libssl-devel libopenslp-devel

%description
The iSNS package contains the daemon and tools to setup a iSNS server,
and iSNS client tools. The Internet Storage Name Service (iSNS) protocol
allows automated discovery, management and configuration of iSCSI and
Fibre Channel devices (using iFCP gateways) on a TCP/IP network.

%package -n libisns
Group: System/Libraries
Summary: Shared library files for iSNS

%description -n libisns
Shared library files for iSNS

%package -n libisns-devel
Group: Development/C
Summary: Development files for iSNS
Requires: libisns = %EVR

%description -n libisns-devel
Development files for iSNS

%prep
%setup
%patch -p1
%if "%_lib" == "lib"
sed -i -e 's|libdir=/usr/lib64|libdir=%_libdir|' libisns.pc
%endif

%build
%meson \
    -Dsystemddir=%_systemd_dir \
    -Drundir=/run

%meson_build

%install
%meson_install
install -p -m 755 -D %SOURCE2 %buildroot%_initdir/isnsd

%post
%post_service isnsd

%preun
%preun_service isnsd

%files
%doc COPYING README
%_sbindir/*
%_man5dir/*
%_man8dir/*
%_unitdir/*
%_initdir/*
%dir %_sharedstatedir/isns
%dir %_sysconfdir/isns
%config(noreplace) %_sysconfdir/isns/*

%files -n libisns
%_libdir/libisns.so.*

%files -n libisns-devel
%dir %_includedir/libisns
%_includedir/libisns/*.h
%_libdir/libisns.so
%_pkgconfigdir/*.pc

%changelog
* Fri Jun 21 2024 Alexey Shabalin <shaba@altlinux.org> 0.102-alt2
- build with libopenslp

* Thu May 02 2024 Alexey Shabalin <shaba@altlinux.org> 0.102-alt1
- 0.102

* Sun Apr 11 2021 Alexey Shabalin <shaba@altlinux.org> 0.101-alt1
- 0.101

* Fri Dec 21 2018 Alexey Shabalin <shaba@altlinux.org> 0.99-alt1
- Initial build.
