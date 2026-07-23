%define _unpackaged_files_terminate_build 1

Name: gitoskop
Version: 1.2.0
Release: alt1

Summary: Read-only HTTP API for browsing trees of bare git repositories
License: AGPL-3.0-or-later
Group: System/Servers
Url: https://altlinux.space/rider/gitoskop
Vcs: https://altlinux.space/rider/gitoskop.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-systemd
BuildRequires: rust rust-cargo gcc
# test fixtures shell out to git
BuildRequires: git-core

%description
gitoskop serves trees of bare git repositories (gear/gitery mirrors) over a
read-only HTTP API: browsing, log with ref decorations, commit details,
tree/blob/raw access, unified diffs and byte-exact patches that apply with
git am, plus substring search over the repository index. Everything is
bounded (blob/patch size caps, tree entry caps, request concurrency and
timeouts) so it can face untrusted clients.

%prep
%setup
# The vendored crates are committed to the packaging branch by
# .gear/merge-up.d/01-vendor.sh; wire cargo to them and stay offline.
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
[net]
offline = true
EOF

%build
cargo build --release --locked --offline

%install
install -Dm755 target/release/%name %buildroot%_bindir/%name
install -Dm644 dist/%name.service %buildroot%_unitdir/%name.service
install -Dm644 dist/%name.conf.example %buildroot%_sysconfdir/%name/%name.conf

%pre
/usr/sbin/groupadd -r -f %name 2>/dev/null ||:
/usr/sbin/useradd -r -g %name -d /var/lib/%name -s /dev/null \
	-c 'gitoskop git browsing API' %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%check
cargo test --release --locked --offline

%files
%doc README.md CHANGELOG.md AUTHORS
%_bindir/%name
%_unitdir/%name.service
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf

%changelog
* Thu Jul 23 2026 Anton Farygin <rider@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0

* Tue Jul 21 2026 Anton Farygin <rider@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus (v1.1.0).
