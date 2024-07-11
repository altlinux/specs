%define _unpackaged_files_terminate_build 1

Name: complgen
Version: 0.2.0
Release: alt1

Summary: Bash/fish/zsh completions generator
License: Apache-2.0
Group: Development/Tools
Vcs: https://github.com/adaszko/complgen

Source: %name-%version.tar
BuildRequires: rust-cargo git
BuildRequires: /proc

%description
Generate bash/fish/zsh completions from a single declarative grammar familiar
from man pages.

%prep
%setup -q
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --offline --release

%install
mkdir -p %buildroot%_bindir
install -Dm0755 target/release/%name %buildroot%_bindir/

%check
cargo test

%files
%doc LICENSE
%doc README.md
%_bindir/%name

%changelog
* Wed May 15 2024 Michael Chernigin <chernigin@altlinux.org> 0.2.0-alt1
- Update to 0.2.0.

* Wed May 15 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.8-alt1
- Initial build for ALT Linux.

