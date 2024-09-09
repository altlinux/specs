%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name:    rustic
Version: 0.8.1
Release: alt1

Summary: rustic - fast, encrypted, deduplicated backups powered by pure Rust
License: Apache-2.0
Group:   Archiving/Backup
Url:     https://rustic.cli.rs/
Vcs:     https://github.com/rustic-rs/rustic

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
Rustic is a backup tool that provides fast, encrypted, deduplicated backups. It
reads and writes the restic repo format described in the design document and can
therefore be used as a complete replacement for restic.

rustic currently is in beta state and misses regression tests. It is not
recommended to use it for production backups, yet.

%prep
%setup
mkdir -p .cargo
tee -a .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false
%if 0%{!?_is_lp64:1}
lto = false
codegen-units = 16
%endif
EOF

%build
%rust_build

%install
%rust_install
mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completions zsh > %buildroot%_datadir/zsh/site-functions/_%name
%buildroot%_bindir/%name completions bash > %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name completions fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
%rust_test
## Smoke test.
PATH=%buildroot%_bindir:$PATH
export RUSTIC_PASSWORD=rustic
export RUSTIC_REPOSITORY=/tmp/repo
rustic init
rustic backup --glob='!target' --as-path=/ .
rustic check
rustic restore latest ../x
rustic restore latest --verify-existing ../x
diff -qr --exclude=target . ../x

%files
%doc *.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Mon Sep 09 2024 Vitaly Chikunov <vt@altlinux.org> 0.8.1-alt1
- Update to v0.8.1 (2024-09-08).

* Fri Aug 23 2024 Vitaly Chikunov <vt@altlinux.org> 0.8.0-alt1
- Update to v0.8.0 (2024-08-22).

* Tue Feb 06 2024 Vitaly Chikunov <vt@altlinux.org> 0.7.0-alt1
- Update to v0.7.0 (2024-02-03).
- Added OpenDAL backends and WebDAV server.
- spec: Add smoke test in %%check.

* Sat Jan 27 2024 Vitaly Chikunov <vt@altlinux.org> 0.6.1-alt1
- Update to v0.6.1 (2023-11-19).

* Mon Jun 05 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.4-alt1
- new version 0.5.4

* Tue May 02 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.3-alt1
- new version 0.5.3

* Tue Jan 17 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus
