%define _unpackaged_files_terminate_build 1

Name: forgejo-cli
Version: 0.4.1
Release: alt1
Url: https://codeberg.org/forgejo-contrib/forgejo-cli
Vcs: https://codeberg.org/forgejo-contrib/forgejo-cli.git
Summary: CLI tool for interacting with Forgejo
License: Apache-2.0 or MIT
Group: Development/Other

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust libssl-devel

%description
%summary.

%prep
%setup -a1
%autopatch -p1
%rust_prep

%build
%rust_build

%install
%rust_install -- fj

%files
%doc README.md LICENSE-APACHE LICENSE-MIT
%_bindir/fj
%changelog
* Mon Mar 16 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.4.1-alt1
- New version 0.4.1.

* Sun Jan 18 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.4.0-alt1
- New version 0.4.0.
- Enable OAuth authentication for altlinux.space.

* Sun Oct 12 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.3.0-alt1
- Initial build.

