Name: kvmd-janus
Version: 1.4.1
Release: alt1

Summary: PiKVM -- WebRTC server
License: GPLv3
Group: System/Servers
VCS: https://github.com/meetecho/janus-gateway

Source: %name-%version.tar

BuildRequires: gengetopt
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libconfig)
BuildRequires: pkgconfig(nice)
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libsrtp)
BuildRequires: pkgconfig(libwebsockets)

%package devel
Summary: PiKVM -- WebRTC server
Group: Development/C

%description
%summary

%description devel
%summary

%prep
%setup

%build
%autoreconf
%configure	--disable-docs \
		--disable-data-channels \
		--disable-turn-rest-api \
		--disable-all-plugins \
		--disable-all-loggers \
		--disable-all-transports \
		--enable-websockets \
		--disable-sample-event-handler \
		--disable-websockets-event-handler \
		--disable-gelf-event-handler \
		--program-suffix=-kvmd

%make_build

%install
%makeinstall_std
# https://webrtc.github.io/adapter/adapter-latest.js
install -pm0644 .gear/adapter.js %buildroot%_datadir/kvmd-janus/javascript/
mv %buildroot%_pkgconfigdir/janus-gateway.pc %buildroot%_pkgconfigdir/kvmd-janus.pc
find %buildroot%_libdir -type f -name \*.la -delete
rm -rf %buildroot%_datadir/janus

%files
%_bindir/*
%_libdir/kvmd-janus
%_datadir/kvmd-janus/javascript
%_man1dir/*.1*

%files devel
%_includedir/kvmd-janus
%_pkgconfigdir/kvmd-janus.pc

%changelog
* Tue Sep 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.1-alt1
- 1.4.1 released

* Mon Sep 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.0-alt1
- 0.14.0 released

* Mon Apr 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.3-alt1
- 0.13.3 released

* Fri Dec 23 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.1-alt1
- 0.13.1 released
