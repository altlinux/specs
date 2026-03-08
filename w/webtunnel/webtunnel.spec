Name:    webtunnel
Version: 0.0.3
Release: alt1

Summary: How to use tor webtunnel project
License: MIT
Group:   Networking/Other

Url:     https://github.com/gh4rib/webtunnel
Vcs:     https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/webtunnel

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang

BuildRequires: golang

%description
 pluggable transport for Tor mimicking encrypted web traffic (client and server)
 WebTunnel is a censorship-resistant pluggable transport designed to mimic
 encrypted web traffic (HTTPS) inspired by HTTPT. It works by wrapping the
 payload connection into a WebSocket-like HTTPS connection, appearing to
 network observers as an ordinary HTTPS (WebSocket) connection.
 .
 This package provides binaries for webtunnel client and server


%prep
%setup

%build
cd ./release
./build.sh

%install
install -d %buildroot/%_bindir/
install ./release/build/-/client %buildroot/%_bindir/webtunnel-client
install ./release/build/-/server %buildroot/%_bindir/webtunnel-server

install -d %buildroot%_man1dir/
install -D  ./debian/*.1  %buildroot%_man1dir

%files
%doc *.md
%_bindir/*
%_man1dir/*

%changelog
* Sat Mar 07 2026 Hihin Ruslan <ruslandh@altlinux.ru> 0.0.3-alt1
- Initial build for Sisyphus
- Add mandir from https://salsa.debian.org/go-team/packages/webtunnel.git

