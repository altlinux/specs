%define _unpackaged_files_terminate_build 1

%def_with check

Name: nspawn
Version: 3.3.1
Release: alt1
ExcludeArch: %ix86

Summary: Docker-like management of systemd-nspawn machines
License: Apache-2.0 or MIT
Group: System/Configuration/Other

Url: https://nspawn.org/
Vcs: https://github.com/nspawn/nspawn

Source: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-rust >= 0.2.0
BuildRequires(pre): rpm-macros-systemd
BuildRequires: rpm-build-rust
BuildRequires: rust >= 1.88
BuildRequires: /proc
%if_with check
BuildRequires: /dev/pts
%endif

Requires: systemd-container >= 255
Requires: iproute2 nftables

%description
Docker-like  management of  systemd-nspawn  machines. Images  come  from an  OCI
registry (the hub),  are stored as shared layers and  are started, inspected and
stopped  through  the  D-Bus  APIs   of  systemd-machined  and  systemd  itself;
machinectl and importctl are never called. The  work is done by a service on the
system bus, org.nspawn, and the command line is its client.

%prep
%setup -a 1
%patch0 -p1
%rust_prep

%build
%rust_build --locked
"%rust_build_dir/nspawn" manpage > nspawn.1
for shell in bash zsh fish; do
    "%rust_build_dir/nspawn" completions "$shell" > nspawn."$shell"
done

%install
%rust_install
install -Dm0644 nspawn.1 %buildroot%_man1dir/nspawn.1
install -Dm0644 packaging/systemd/%{name}*.service packaging/systemd/%{name}*.socket \
    packaging/systemd/nspawn-auto-update.timer -t %buildroot%_unitdir
install -Dm0644 packaging/systemd/journald@nspawn.conf %buildroot%_systemd_dir/journald@nspawn.conf
install -Dm0644 packaging/dbus/org.nspawn.service %buildroot%_datadir/dbus-1/system-services/org.nspawn.service
install -Dm0644 packaging/dbus/org.nspawn.conf %buildroot%_datadir/dbus-1/system.d/org.nspawn.conf
install -Dm0644 packaging/polkit/org.nspawn.policy %buildroot%_datadir/polkit-1/actions/org.nspawn.policy
install -Dm0644 nspawn.bash %buildroot%_datadir/bash-completion/completions/nspawn
install -Dm0644 nspawn.zsh %buildroot%_datadir/zsh/site-functions/_nspawn
install -Dm0644 nspawn.fish %buildroot%_datadir/fish/vendor_completions.d/nspawn.fish

install -d -m0755 %buildroot%_sysconfdir/nspawn
install -d -m0711 %buildroot%_sharedstatedir/nspawn
install -Dm0644 docs/COMPOSE.md docs/USAGE.md docs/ARCHITECTURE.md docs/DBUS.md -t rpm-docs/docs

%check
export TMPDIR=/tmp

set --
# The chroot root may be part of a mount outside the chroot.
if ! grep -Eq '^[^[:space:]]+[[:space:]]+/[[:space:]]' /proc/self/mounts; then
    set -- "$@" --skip backend::tests::root_is_a_mountpoint
fi
# Interface names are read from sysfs.
if [ ! -r /sys/class/net/lo/ifindex ]; then
    set -- "$@" --skip hostnet::tests::loopback_is_interface_one
fi

%rust_test --locked -- "$@"

%post
%post_systemd_postponed nspawn.service

%preun
%preun_systemd nspawn.service nspawn-api.socket nspawn-auto-update.timer nspawn-auto-update.service

%files
%doc LICENSE LICENSE-MIT LICENSE-APACHE
%doc README.md rpm-docs/docs packaging/polkit/nspawn-wheel.rules
%_bindir/nspawn
%_man1dir/nspawn.1*
%_unitdir/nspawn.service
%_unitdir/nspawn-api.service
%_unitdir/nspawn-api.socket
%_unitdir/nspawn-api@.service
%_unitdir/nspawn-api@.socket
%_unitdir/nspawn-auto-update.service
%_unitdir/nspawn-auto-update.timer
%_systemd_dir/journald@nspawn.conf
%_datadir/dbus-1/system-services/org.nspawn.service
%_datadir/dbus-1/system.d/org.nspawn.conf
%_datadir/polkit-1/actions/org.nspawn.policy
%_datadir/bash-completion/completions/nspawn
%_datadir/zsh/site-functions/_nspawn
%_datadir/fish/vendor_completions.d/nspawn.fish
%dir %_sysconfdir/nspawn
%dir %attr(0711,root,root) %_sharedstatedir/nspawn

%changelog
* Mon Nov 23 2026 Egor Ignatov <egori@altlinux.org> 3.3.1-alt1
- First build for ALT.
