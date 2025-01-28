Name: ttyper
Version: 1.6.0
Release: alt1
Summary: ttyper is a terminal-based typing test built with Rust and Ratatui

Group: Education
License: MIT
URL: https://github.com/max-niederman
Vcs: https://github.com/max-niederman/ttyper.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo
BuildRequires: /proc

%description
$summary.

%prep
%setup

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
%rust_install

%check
%rust_test

%files
%doc *.md
%_bindir/*

%changelog
* Tue Jan 28 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.6.0-alt1
- Initial build for ALT.

