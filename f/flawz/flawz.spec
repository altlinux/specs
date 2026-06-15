%def_without check
# test args::tests::test_args ... ok
# test widgets::tests::test_selectable_list ... ok
# test error::tests::test_error ... ok
#
# test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

%define bash_completionsdir %_datadir/bash-completion/completions
%define zsh_completionsdir %_datadir/zsh/site-functions
%define fish_completionsdir %_datadir/fish/vendor_completions.d

Name:    flawz
Version: 0.4.1
Release: alt1

Summary: A Terminal UI for browsing security vulnerabilities (CVEs)
License: Apache-2.0 and MIT
Group:   Security/Networking
Url:     https://github.com/orhun/flawz

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: /proc

%description
As default it uses the vulnerability database (NVD) from NIST and provides
search and listing functionalities in the terminal with
different theming options.

%prep
%setup -a1
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
# Install manpage
install -dv %buildroot%_man1dir
OUT_DIR=%buildroot%_man1dir ./target/release/flawz-mangen

# Install completions
install -dv completionsdir
OUT_DIR=completionsdir ./target/release/flawz-completions
install -Dm 0644 completionsdir/%name.bash %buildroot%bash_completionsdir/%name
install -Dm 0644 completionsdir/%name.fish %buildroot%fish_completionsdir/%name.fish
install -Dm 0644 completionsdir/_%name %buildroot%zsh_completionsdir/_%name

%check
%rust_test --workspace

%files
%doc *.md LICENSE-*
%_bindir/%name
%_man1dir/%name.1.*
%bash_completionsdir/%name
%fish_completionsdir/%name.fish
%zsh_completionsdir/_%name

%changelog
* Mon Jun 15 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.4.1-alt1
- New version.

* Thu Nov 20 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
