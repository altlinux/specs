%define ppp_version %((%{__awk} '/^#define VERSION/ { print $NF }' /usr/include/pppd/patchlevel.h 2>/dev/null||echo none)|/usr/bin/tr -d '"')

Name: sstp-client
Version: 1.0.11
Release: alt1
Summary: Secure Socket Tunneling Protocol (SSTP) Client
Group: System/Servers
License: GPLv2+

Url: http://sstp-client.sourceforge.net/
Source: %name-%version.tar
Source2: %name.tmpfiles

Requires: ppp = %ppp_version
Requires: libsstp = %version-%release
BuildRequires: libevent-devel >= 2.0.10
BuildRequires: libssl-devel glibc-devel ppp-devel

%description
Client for the proprietary Microsoft Secure Socket Tunneling Protocol, SSTP.
Allows connection to a SSTP based VPN as used by employers and some cable
and ADSL service providers.

%package -n libsstp
Summary: Provide development headers for sstp-client
Group: System/Libraries

%description -n libsstp
This package contains the necessary header files for sstp-client development

This package is required to compile plugin's for sstp-client.

%package -n libsstp-devel
Summary: Provide development headers for sstp-client
Group: Development/C
Requires: libsstp = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release

%description -n libsstp-devel
This package contains the necessary header files for sstp-client development

This package is required to compile plugin's for sstp-client.

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
install -Dpm 644 %SOURCE2 %buildroot%_tmpfilesdir/%name.conf

%pre
%_sbindir/groupadd -r -f sstpc
%_sbindir/useradd -M -r -d %_runtimedir/sstpc -s /bin/false -c "Secure Socket Tunneling Protocol (SSTP) Client" -g sstpc sstpc >/dev/null 2>&1 || :

%files
%doc AUTHORS COPYING DEVELOPERS NEWS README TODO USING
%doc ChangeLog
%doc sstp-test-nopty.example sstp-test.example
%_sbindir/sstpc
%_man8dir/sstpc.8*
%_libdir/pppd/%ppp_version/*.so
%dir %attr(755,sstpc,sstpc) %_runtimedir/sstpc
%_tmpfilesdir/%name.conf
%exclude %_libdir/pppd/%ppp_version/*.la

%files -n libsstp
%_libdir/libsstp_api-0.so

%files -n libsstp-devel
%_libdir/libsstp_api.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Mon Jan 09 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Mon Jan 19 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.9-alt3
- rebuild with ppp-2.4.7

* Fri Sep 12 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.9-alt2
- move tmpfiles conf from /etc to /lib

* Wed Jan 30 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Thu Oct 25 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.8-alt1
- 1.0.8
- add libsstp package
- rename sstp-client to libsstp-devel

* Mon May 21 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Wed Mar 07 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.5-alt1
- initial build for ALT Linux Sisyphus
