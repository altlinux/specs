Name: hasher-unpriv
Version: 0.0.2
Release: alt1

Summary: Unprivileged hasher-priv drop-in replacement for rootless containers
License: GPLv2+
Group: Development/Other

Url: https://altlinux.space/egori/hasher-unpriv
VCS: https://altlinux.space/egori/hasher-unpriv

Source: %name-%version.tar

BuildRequires: /proc

%define _libexecdir %_prefix/libexec
%define helperdir %_libexecdir/%name

%description
hasher-unpriv is a drop-in replacement for hasher-priv that lets the
hasher build tool run inside rootless (unprivileged) containers.

Instead of a privileged daemon helper, it relies on Linux user namespaces to
provide the separate rooter and builder identities that hasher expects,
exposing the same command interface (getconf, getugid, chrootuid, ...)
so that hasher works unchanged.

%prep
%setup

%build
%make_build CC="%__cc" CFLAGS="%optflags" libexecdir="%_libexecdir"

%install
%makeinstall_std \
    libexecdir="%_libexecdir"

install -Dpm 644 /dev/stdin %buildroot%_sysconfdir/hasher-unpriv/system <<EOF
user1=_rooter
user2=_builder
EOF

install -Dpm 644 hasher/config %buildroot%_datadir/hasher-unpriv/hasher/config

%post
# Create hasher users
useradd -M -U -s /dev/null _rooter 2>/dev/null ||:
useradd -M -U -s /dev/null _builder 2>/dev/null ||:

%files
%doc README.md
%helperdir
%_datadir/hasher-unpriv
%config(noreplace) %_sysconfdir/hasher-unpriv/system

%changelog
* Fri Jun 19 2026 Egor Ignatov <egori@altlinux.org> 0.0.2-alt1
- First working release.

* Wed Jun 17 2026 Egor Ignatov <egori@altlinux.org> 0.0.1-alt1
- First build for ALT.
