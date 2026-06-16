%define _unpackaged_files_terminate_build 1

Name:    garage
Version: 2.3.0
Release: alt1

Summary: S3-compatible object store for small self-hosted geo-distributed deployments
License: AGPL-3.0
Group:   Development/Other
Url:     https://garagehq.deuxfleurs.fr

Source: %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: libzstd-devel libsodium-devel libsqlite3-devel

ExcludeArch: %ix86

%description
Garage is an S3-compatible distributed object storage service designed for
self-hosting at a small-to-medium scale.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build --no-default-features --features 'system-libs,metrics,lmdb,sqlite,k2v'

%install
%rust_install

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completions zsh | sed 's/`//g' > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completions bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completions fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
%rust_test

%files
%_bindir/%name
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%doc *.md doc

%changelog
* Thu Jun 11 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus
