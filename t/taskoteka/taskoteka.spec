ExcludeArch: %ix86
Name: taskoteka
Version: 1.6.0
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
* Fri Jul 03 2026 Anton Farygin <rider@altlinux.org> 1.6.0-alt1
- added force task refresh via GET /tasks/{id}?refresh=1 with per-task
  cooldown and global rate limit
- access log now includes client IP and User-Agent

* Wed Apr 15 2026 Anton Farygin <rider@altlinux.org> 1.5.0-alt1
- added approved_by and disapproved_by fields to list endpoint subtasks

* Wed Apr 01 2026 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- fixed OpenAPI spec returning literal %%VERSION%% instead of actual version
- compact GC heap after initial cache load and periodically to limit memory growth

* Tue Mar 17 2026 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- added GET /events SSE endpoint for real-time task change notifications
- added broadcast hub with per-client buffers and connection limits
- added --max-sse-connections, --max-sse-per-ip, --sse-max-lifetime,
  --sse-heartbeat-interval, --sse-buffer-size, --sse-ip-header,
  --sse-trusted-proxy CLI options
- fixed EPERM approval detection (re-read every 30s)
- fixed arbitrary file read via symlinks (lstat hardening)
- fixed partial task rejection (require state/owner/repo)
- fixed consistent GET /tasks/{id} for EPERM tasks
- removed per-request thread spawning in read_build_status

* Mon Mar 16 2026 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- detect failed subtask builds via try_iter filtering
- build results filtered by try_iter to exclude stale data from previous iterations
- optimize refresh: 1 stat for cold states (FAILED, TESTED, EPERM) instead of 4

* Sat Mar 14 2026 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- added full-text search API (GET /tasks?q=...)
- added EVR fields (epoch, version, release) to subtask output
- added build status per architecture and approval comments to task output
- added message field to task output
- fixed archived task comments/build_status reading from wrong directory
- fixed age field staleness in cached tasks (computed at serialization time)
- hardened file readers with size limits (1MB for read_file, 10K lines for plan)
- improved cache refresh performance (2x faster via lock-free parallel workers)

* Tue Mar 10 2026 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- added ACL module and needs_approval query parameter for GET /tasks
  (--acl-dir, --allow-unlisted options)
- needs_approval filter matches girar three-state logic exactly:
  superuser handling, qualified disapproval, maint-first semantics
- added relax_git_inheritance_check_for_commit and
  relax_lastchange_inheritance_check_for_evr fields to subtask output
- optimized refresh: removed unnecessary stat() calls, EPERM tasks
  check acl dirs for new approvals, full reread every 10 minutes

* Tue Mar 10 2026 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- initial build for Sisyphus
