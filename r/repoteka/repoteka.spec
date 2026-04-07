ExcludeArch: %ix86
Name: repoteka
Version: 1.1.0
Release: alt1
Summary: Fast HTTP/JSON API for ALT Linux apt-rpm repository metadata
License: GPL-2.0-or-later
Group: System/Servers
Url: https://altlinux.space/rider/repoteka
VCS: https://altlinux.space/rider/repoteka
Source: %name-%version.tar
BuildRequires(pre): rpm-build-ocaml
BuildRequires: ocaml >= 5.0
BuildRequires: dune >= 3.0
BuildRequires: ocaml-tiny_httpd-devel >= 0.16
BuildRequires: ocaml-yojson-devel >= 2.0
BuildRequires: ocaml-toml-devel
BuildRequires: ocaml-lzma-devel
BuildRequires: liblzma-devel
BuildRequires: ocaml-alcotest-devel

%description
Repoteka is a fast HTTP/JSON API server for ALT Linux apt-rpm
repository metadata. It loads pkglist, srclist, and release files
into memory and serves package data with millisecond latency.

Features: parallel XZ decompression via OCaml 5 Domains, zero-copy
RPM header parsing, aggressive string interning, per-branch indexes,
prefix binary search for TAB completion, full dependency/file/changelog
extraction.

%prep
%setup

%build
%dune_build

%install
%dune_install

# Install systemd unit
install -D -m 0644 %name.service %buildroot%_unitdir/%name.service

# Install sysconfig
install -D -m 0644 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name

# Install example config
install -D -m 0644 %name.toml.example %buildroot%_sysconfdir/%name.toml

%check
%dune_check

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md README.ru.md COPYING AUTHORS
%_bindir/%name
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/%name.toml

%changelog
* Tue Apr 07 2026 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- fixed: forward kind filter to global /names and /packages search
- addded strict kind validation on all six kind-aware endpoints (HTTP 400)
- perf: loader hot path and dedup keys - total load -25%, p50 -60% on
  listing endpoints

* Sat Apr 04 2026 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- initial build for Sisyphus
