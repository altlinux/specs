%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: wlgreet
Version: 0.5.0
Release: alt1
Summary: Wayland greeter for greetd
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://git.sr.ht/~kennylevinsen/wlgreet
VCS: https://git.sr.ht/~kennylevinsen/wlgreet
Source: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo

%description
Raw wayland greeter for greetd, to be run under sway or similar.

Note that cage is currently not supported
due to it lacking wlr-layer-shell-unstable support.

%prep
%setup -a1

mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
cargo build \
	--release \
	%{?_smp_mflags} \
	--offline \
	%nil

%install
install -Dm755 target/release/wlgreet %buildroot%_bindir/wlgreet

%check
cargo test --release

%files
%doc LICENSE
%doc README.md
%_bindir/*

%changelog
* Fri May 03 2024 Anton Farygin <rider@altlinux.ru> 0.5.0-alt1
- 0.3 -> 0.5.0

* Thu Nov 02 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.3-alt3
- NMU: fixed FTBFS on LoongArch.

* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt2
- Applied stricter build checks.

* Fri Mar 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt1
- Initial build for ALT.
