Name: open-isns
Version: 0.99
Release: alt1
Summary: The iSNS daemon and utility programs

Group: System/Servers
License: LGPLv2+
Url: https://github.com/open-iscsi/open-isns
Source: %name-%version.tar
Source2: isnsd.init
Patch: %name-%version.patch

BuildRequires: libssl-devel

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

%build
%autoreconf
%configure --enable-shared --disable-static
%make_build

%install
%make_install install DESTDIR=%buildroot
%make_install install_hdrs DESTDIR=%buildroot
%make_install install_lib DESTDIR=%buildroot

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
%dir %_var/lib/isns
%dir %_sysconfdir/isns
%config(noreplace) %_sysconfdir/isns/*

%files -n libisns
%_libdir/libisns.so.*

%files -n libisns-devel
%dir %_includedir/libisns
%_includedir/libisns/*.h
%_libdir/libisns.so

%changelog
* Fri Dec 21 2018 Alexey Shabalin <shaba@altlinux.org> 0.99-alt1
- Initial build.
