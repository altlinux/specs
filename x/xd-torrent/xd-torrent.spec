%define xddir /var/lib/xd

Name: xd-torrent
Version: 0.4.6
Release: alt1

Summary: An I2P BitTorrent client

License: MIT
Group: System/Servers
Url: https://github.com/majestrate/XD

# Source0-url: https://github.com/majestrate/XD/archive/refs/tags/v%version.tar.gz
Source0: %name-%version.tar

Source1: %name-development-%version.tar

Source11: xd.conf
Source12: xd-torrent.sysusers
Source13: xd-torrent.tmpfiles

Patch1: 020-xd-torrent-rename-service-paths.patch
Patch2: 030-xd-torrent-service-hardening.patch

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): rpm-macros-systemd
BuildRequires: golang

#BuildRequires: /proc

%description
An I2P BitTorrent client.

%prep
%setup -a1
%patch1 -p1
%patch2 -p1

%build
export CGO_CPPFLAGS="%optflags"
export CGO_CFLAGS="%optflags"
export CGO_CXXFLAGS="%optflags"
#export CGO_LDFLAGS="$LDFLAGS"
export GOFLAGS='-mod=vendor -buildmode=pie'
%make_build GIT_VERSION=%EVR

%install
%make_install install PREFIX=%buildroot%prefix

# config
install -D -m644 %SOURCE11 -t "%buildroot%_sysconfdir"

# systemd
install -D -m644 %SOURCE12 %buildroot%_sysusersdir/xd-torrent.conf
install -D -m644 %SOURCE13 %buildroot%_libexecdir/tmpfiles.d/xd-torrent.conf
install -D -m644 contrib/systemd/xd.service %buildroot%_unitdir/xd-torrent.service

%check
export GOFLAGS=-mod=vendor
#make test

%pre
#sysusers_create_package %name %SOURCE12

%post
%post_service %name

%preun
%preun_service %name
%files
%doc LICENSE docs/en/readme.md
%_bindir/XD
%_bindir/XD-CLI
%_unitdir/%name.service
%_libexecdir/sysusers.d/xd-torrent.conf
%_libexecdir/tmpfiles.d/xd-torrent.conf
%config(noreplace) %_sysconfdir/xd.conf

%changelog
* Sun Feb 16 2025 Vitaly Lipatov <lav@altlinux.ru> 0.4.6-alt1
- initial build for ALT Linux Sisyphus
