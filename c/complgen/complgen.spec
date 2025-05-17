%define _unpackaged_files_terminate_build 1

Name: complgen
Version: 0.4.0
Release: alt1

Summary: Bash/fish/zsh completions generator
License: GPLv3
Group: Development/Tools
Vcs: https://github.com/adaszko/complgen

Source: %name-%version.tar
Source1: vendor.tar
BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo git
BuildRequires: /proc

%description
Generate bash/fish/zsh completions from a single declarative grammar familiar
from man pages.

%prep
%setup -q
tar xf %SOURCE1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install
mkdir -p %buildroot%_bindir
install -Dm0755 target/release/%name %buildroot%_bindir/

%check
%rust_test

%files
%doc CHANGELOG* CONTRIBUTING* README.md examples
%_bindir/%name

%changelog
* Thu May 08 2025 Ildar Mulyukov <ildar@altlinux.ru> 0.4.0-alt1
- new version
- fix (ALT #52557)
- move vendored code to a separate branch (for clearness)

* Wed May 15 2024 Michael Chernigin <chernigin@altlinux.org> 0.2.0-alt1
- Update to 0.2.0.

* Wed May 15 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.8-alt1
- Initial build for ALT Linux.

