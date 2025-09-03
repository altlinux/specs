%define _unpackaged_files_terminate_build 1

Name: bandwhich
Version: 0.23.1
Release: alt1

Summary: Terminal bandwidth utilization tool
License: MIT
Group: File tools
Url: https://github.com/imsnif/bandwhich
Vcs: https://github.com/imsnif/bandwhich

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires: rust-cargo
BuildRequires: pkgconfig(openssl)

Patch: Add-packet-builder-source-to-vendor-for-offline-usag.patch 

%description
This is a CLI utility for displaying current network utilization by process,
connection and remote IP/hostname.

%prep
%setup -a1
%patch -p1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
cargo build %_smp_mflags --offline --release

%install
install -D -m 755 target/release/%name %{buildroot}%{_bindir}/%name
install -Dm 0644 target/release/build/bandwhich-*/out/%name.1 -t %buildroot%_man1dir
install -Dm 0644 target/release/build/bandwhich-*/out/%name.bash \
        -t %buildroot%_datadir/bash-completion/completions/
install -Dm 0644 target/release/build/bandwhich-*/out/_%name \
        -t %buildroot%_datadir/zsh/site-functions/
install -Dm 0644 target/release/build/bandwhich-*/out/%name.fish \
        -t %buildroot%_datadir/fish/vendor_completions.d/

%check
cargo test --release

%files
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md LICENSE.md
%_bindir/%name
%_man1dir/%name.1*
%_datadir/bash-completion/completions/%name.bash
%_datadir/zsh/site-functions/_%{name}
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Tue Sep 02 2025 Denis Rastyogin <gerben@altlinux.org> 0.23.1-alt1
- Initial build for ALT Sisyphus.
