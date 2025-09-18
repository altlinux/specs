%define _unpackaged_files_terminate_build 1

Name:    carbon-c-relay
Version: 3.8.1
Release: alt1

Summary: Enhanced C implementation of Carbon relay, aggregator and rewriter
License: Apache-2.0
Group:   System/Libraries 
Url:     https://github.com/grobian/carbon-c-relay

Source0: %name-%version.tar
Source1: carbon-c-relay.conf
Source2: carbon-c-relay.service
Source3: carbon-c-relay.sysconfig.systemd

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-intro
BuildRequires: zlib-devel
BuildRequires: liblz4-devel
BuildRequires: libssl-devel
BuildRequires: libpcre2-devel

%description
Carbon-like Graphite line mode relay. This project aims to be a replacement of
the original Carbon relay. The main reason to build a replacement is
performance and configurability. Carbon is single threaded, and sending
metrics to multiple consistent-hash clusters requires chaining of relays. This
project provides a multithreaded relay which can address multiple targets and
clusters for each and every metric based on pattern matches.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure \
  --with-gzip \
  --with-lz4 \
  --with-snappy=no \
  --with-ssl \
  --with-oniguruma=no \
  --with-pcre2 \
  --with-pcre=no 
%make_build

%install
install -Dp -m0755 relay %buildroot%_bindir/%name
install -Dp -m0644 %SOURCE1 %buildroot%_sysconfdir/%name.conf

install -Dp -m0644 relay.1 %buildroot%_man1dir/%name.1

install -Dp -m0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dp -m0644 %SOURCE3 %buildroot%_sysconfigdir/%name


%pre
getent group carbon-c-relay >/dev/null || groupadd -r carbon-c-relay
getent passwd carbon-c-relay >/dev/null || \
    useradd -r -g carbon-c-relay -d / -s /sbin/nologin \
    -c "Carbon C Relay Daemon" carbon-c-relay
exit 0

%post
%systemd_post %name.service

%preun
%systemd_preun %name.service

%postun
%systemd_postun_with_restart %name.service

%files
%doc *.md
%_bindir/%name
%_man1dir/%name.1.*
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfigdir/%name
%_unitdir/%name.service

%changelog
* Mon Sep 17 2025 Nikita Shmatko <nash@altlinux.org> 3.8.1-alt1
- Initial build for Sisyphus.
