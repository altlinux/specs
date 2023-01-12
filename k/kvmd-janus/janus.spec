Name: kvmd-janus
Version: 0.13.1
Release: alt1

Summary: PiKVM -- WebRTC server
License: GPLv3
Group: System/Servers
Url: https://github.com/meetecho/janus-gateway

Source: %name-%version-%release.tar

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
sed -ri -e '1s,^,import "./adapter.js"\n,' \
	-e '/^function Janus/ s,^,export ,' html/janus.js

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
find %buildroot%_libdir -type f -name \*.la -delete

%files
%_bindir/*
%_libdir/kvmd-janus
%_datadir/kvmd-janus/javascript
%_man1dir/*.1*

%files devel
%_includedir/kvmd-janus

%changelog
* Fri Dec 23 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.1-alt1
- 0.13.1 released
