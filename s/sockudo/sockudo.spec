%define _unpackaged_files_terminate_build 1

%define _pseudouser_user     _sockudo
%define _pseudouser_group    _sockudo
%define _pseudouser_home     %_localstatedir/sockudo

Name: sockudo
Version: 4.7.0
Release: alt1

Summary: A self-hosted realtime platform
License: MIT
Group: System/Servers
Url: https://sockudo.io
Vcs: https://github.com/sockudo/sockudo.git

ExcludeArch: i586

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-build-systemd
BuildRequires: rpm-build-rust
BuildRequires: rpm-build-systemd
BuildRequires: libssl-devel
BuildRequires: libprotobuf-devel
BuildRequires: make

Source: %name-%version.tar
Source1: vendor.tar
Source2: sockudo.service
Source3: 50-sockudo.preset

%description
Sockudo is a high-performance Rust realtime server for WebSocket and
HTTP publish workloads. It keeps strict Protocol V1 compatibility with
the Pusher protocol, then adds Protocol V2 features for teams that need
stronger delivery semantics and product-level control.

%prep
%setup -a1
cat > .cargo/config.toml <<'EOF'
[build]
rustflags = ["--cfg", "tokio_unstable"]
EOF
%rust_prep

%build
export RUSTFLAGS="--cfg tokio_unstable"
%rust_build

%install
%rust_install sockudo
install -Dm644 %{SOURCE2} %buildroot%_unitdir/sockudo.service
install -Dm644 %{SOURCE3} %buildroot%_presetdir/50-sockudo.preset
install -dm0750 %buildroot%_sysconfdir/sockudo
install -Dpm0640 config/config.toml %buildroot%_sysconfdir/sockudo/config.toml
install -dm0750 %buildroot%_pseudouser_home

%check
export RUSTFLAGS="--cfg tokio_unstable"
%rust_test

%pre
%_sbindir/groupadd -r -f %_pseudouser_group 2>/dev/null ||:
%_sbindir/useradd -r -g %_pseudouser_group -c 'The Sockudo realtime server' \
    -d %_pseudouser_home -M -s /sbin/nologin %_pseudouser_user >/dev/null 2>&1 ||:

%post
%systemd_post sockudo.service

%preun
%systemd_preun sockudo.service

%postun
%systemd_postun_with_restart sockudo.service

%files
%doc LICENSE README.md
%_bindir/sockudo
%_unitdir/sockudo.service
%_presetdir/50-sockudo.preset
%dir %attr(0750,root,%_pseudouser_group) %_sysconfdir/sockudo
%config(noreplace) %attr(0640,root,%_pseudouser_group) %_sysconfdir/sockudo/config.toml
%dir %attr(0750,%_pseudouser_user,%_pseudouser_group) %_pseudouser_home

%changelog
* Tue Jul 28 2026 Mikhail Nogin <joycap@altlinux.org> 4.7.0-alt1
- Initial build for Sisyphus.
