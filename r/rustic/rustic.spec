%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name:    rustic
Version: 0.11.3
Release: alt1

Summary: rustic - fast, encrypted, deduplicated backups powered by pure Rust
License: Apache-2.0
Group:   Archiving/Backup
Url:     https://rustic.cli.rs/
Vcs:     https://github.com/rustic-rs/rustic

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: pkgconfig(libzstd)

%description
Rustic is a backup tool that provides fast, encrypted, deduplicated
backups. It reads and writes the restic repo format described in the
design document and can therefore be used as a complete replacement
for restic.

NB: rustic currently is in beta state and misses regression tests.
    It is not recommended to use it for production backups, yet.

%prep
%setup
mkdir -p .cargo
tee -a .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[env]
ZSTD_SYS_USE_PKG_CONFIG = "1"

[profile.release]
strip = false
%if 0%{!?_is_lp64:1}
lto = false
codegen-units = 16
%endif
EOF

%build
# Default features include 'self-update'.
%rust_build --no-default-features --features webdav,tui

%install
%rust_install
mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completions zsh > %buildroot%_datadir/zsh/site-functions/_%name
%buildroot%_bindir/%name completions bash > %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name completions fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
export TZ=America/New_York
%rust_test
%buildroot%_bindir/rustic --version | grep -Fx '%name %version'
ldd %buildroot%_bindir/rustic | grep libzstd.so
grep -sF 'https://cloud-api.yandex.net/v1/disk' %buildroot%_bindir/rustic
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
%define _customdocdir %_docdir/%name
%doc *.md config rustic-docs/src/*
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Thu Jun 25 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.3-alt1
- new version 0.11.3

* Fri Apr 17 2026 Vitaly Chikunov <vt@altlinux.org> 0.11.2-alt1
- Update to v0.11.2 (2026-04-05).

* Sun Mar 08 2026 Vitaly Chikunov <vt@altlinux.org> 0.11.1-alt1
- Update to v0.11.1 (2026-03-05).

* Sun Feb 15 2026 Vitaly Chikunov <vt@altlinux.org> 0.11.0-alt1
- Update to v0.11.0 (2026-02-12).

* Tue Dec 30 2025 Vitaly Chikunov <vt@altlinux.org> 0.10.3-alt1
- Update to v0.10.3 (2025-12-28).

* Wed Nov 12 2025 Vitaly Chikunov <vt@altlinux.org> 0.10.2-alt1
- Update to v0.10.2 (2025-11-11).

* Sat Sep 13 2025 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt1
- Update to v0.10.0 (2025-09-12).

* Wed Dec 04 2024 Vitaly Chikunov <vt@altlinux.org> 0.9.5-alt1
- Update to v0.9.5 (2024-12-03).

* Sat Oct 26 2024 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt1
- Update to v0.9.4 (2024-10-24).

* Thu Oct 10 2024 Vitaly Chikunov <vt@altlinux.org> 0.9.3-alt1
- Update to v0.9.3 (2024-10-10).

* Fri Oct 04 2024 Vitaly Chikunov <vt@altlinux.org> 0.9.1-alt1
- Update to v0.9.1 (2024-10-03).

* Mon Sep 30 2024 Vitaly Chikunov <vt@altlinux.org> 0.9.0-alt1
- Update to v0.9.0 (2024-09-29).
  Note: this release has Breaking Changes (see breaking_changes.md).
- spec: Package documentation (which was in another repo).

* Sun Sep 29 2024 Vitaly Chikunov <vt@altlinux.org> 0.8.1-alt3
- Experimentally enable YandexDisk backend.

* Wed Sep 18 2024 Vitaly Chikunov <vt@altlinux.org> 0.8.1-alt2
- Build without self-update feature.
- spec: Link with system libzstd.

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
