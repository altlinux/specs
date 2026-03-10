ExcludeArch: %ix86
Name: taskoteka
Version: 1.0.0
Release: alt1
Summary: Fast HTTP/JSON API for girar build tasks
License: GPL-2.0-or-later
Group: System/Servers
Url: https://altlinux.space/rider/taskoteka
Source: %name-%version.tar
BuildRequires(pre): rpm-build-ocaml
BuildRequires: ocaml >= 5.0
BuildRequires: dune >= 3.0
BuildRequires: ocaml-tiny_httpd-devel >= 0.20
BuildRequires: ocaml-yojson-devel >= 2.0
BuildRequires: ocaml-alcotest-devel

%description
Taskoteka is a fast HTTP/JSON API server for girar build tasks.
It serves cached task data from the /tasks/ NFS filesystem with
sub-millisecond response times via in-memory caching.

Provides REST API compatible with girar task ls and girar task show --json.

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

%check
%dune_check

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md README.ru.md LICENSE AUTHORS
%_bindir/%name
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Tue Mar 10 2026 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- initial build for Sisyphus
