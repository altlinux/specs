%define ppp_version 2.4.5

Name: sstp-client
Version: 1.0.7
Release: alt1
Summary: Secure Socket Tunneling Protocol (SSTP) Client
Group: System/Servers
License: GPLv2+

Url: http://sstp-client.sourceforge.net/
Source: %name-%version.tar
Source2: %name.tmpfiles

Requires: ppp >= %ppp_version
BuildRequires: libevent-devel >= 2.0.10
BuildRequires: libssl-devel glibc-devel ppp-devel

%package devel
Summary: Provide development headers for sstp-client
Group: Development/C

%description devel
This package contains the necessary header files for sstp-client development

This package is required to compile plugin's for sstp-client.

%description
Client for the proprietary Microsoft Secure Socket Tunneling Protocol, SSTP.
Allows connection to a SSTP based VPN as used by employers and some cable
and ADSL service providers.

%prep
%setup

%build
%autoreconf
%configure \
		--disable-static \
		--with-libevent=2 \
		--with-pppd-plugin-dir=%_libdir/pppd/%ppp_version \
		--with-runtime-dir="/var/run/sstpc"
%make_build

%install
%makeinstall_std
install -c -d -m 755 %buildroot%_man8dir
install -c -m 755 sstpc.8 %buildroot%_man8dir

install -c -d -m 755 %buildroot%_runtimedir/sstpc
install -Dpm 644 %SOURCE2 %buildroot%_sysconfdir/tmpfiles.d/%name.conf

%pre
%_sbindir/groupadd -r -f sstpc
%_sbindir/useradd -M -r -d %_runtimedir/sstpc -s /bin/false -c "Secure Socket Tunneling Protocol (SSTP) Client" -g sstpc sstpc >/dev/null 2>&1 || :

%files
%doc AUTHORS COPYING DEVELOPERS NEWS README TODO USING
%doc ChangeLog
%doc sstp-test-nopty.example sstp-test.example
%_sbindir/sstpc
%_man8dir/sstpc.8*
%_libdir/*.so.*
%_libdir/pppd/%ppp_version/*.so
%dir %attr(755,sstpc,sstpc) %_runtimedir/sstpc
%config(noreplace) %_sysconfdir/tmpfiles.d/%name.conf

%exclude %_libdir/pppd/%ppp_version/*.la


%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Mon May 21 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Wed Mar 07 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.5-alt1
- initial build for ALT Linux Sisyphus
