Name:    kakoune-lsp
Version: 18.1.2
Release: alt1

Summary: Kakoune Language Server Protocol Client
License: Unlicense or MIT
Group:   Editors

URL:     https://github.com/kakoune-lsp/kakoune-lsp/

Source0: %name-%version.tar
Source1: vendor.tar

# Build failed
ExcludeArch: %ix86

BuildRequires(pre): rpm-build-rust

%description
This is a Language Server Protocol client for the Kakoune editor.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%rust_build

%install
%rust_install kak-lsp

%files
%_bindir/kak-lsp

%changelog
* Wed Jan 29 2025 Ilya Sorochan <k0tran@altlinux.org> 18.1.2-alt1
- Initial build.
