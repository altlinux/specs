Name:    rustic
Version: 0.5.3
Release: alt1

Summary: rustic - fast, encrypted, deduplicated backups powered by pure Rust
License: Apache-2.0
Group:   Other
Url:     https://github.com/rustic-rs/rustic

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

ExcludeArch: ppc64le

%description
Rustic is a backup tool that provides fast, encrypted, deduplicated backups. It
reads and writes the restic repo format desribed in the design document and can
therefore be used as a complete replacement for restic.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
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

%files
%doc *.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Tue May 02 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.3-alt1
- new version 0.5.3

* Tue Jan 17 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus
