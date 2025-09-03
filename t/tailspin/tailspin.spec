%define _unpackaged_files_terminate_build 1
%define short_name _tspin

%def_with check
%def_with docs

Name: tailspin
Version: 5.5.0
Release: alt1
Summary: A log file highlighter
License: MIT
Group: Shells
Url: https://github.com/bensadeh/tailspin

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
Tailspin works by reading through a log file line by line,
running a series of regexes against each line.
The regexes recognize patterns you expect to find in a logfile, like dates,
numbers, severity keywords and more.

%prep
%setup -a 1
%patch -p1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export CARGO_HOME=${PWD}/cargo
%rust_build

%install
export CARGO_HOME=${PWD}/cargo
install -Dm 755  target/release/tspin %buildroot%_bindir/tspin
install -Dm 755  completions/tspin.bash %buildroot%_datadir/bash-completion/%short_name
mkdir -p %buildroot%_datadir/zsh_completion.d
install -Dm 755  completions/tspin.zsh %buildroot%_datadir/zsh_completion.d/%short_name

%check
export CARGO_HOME=${PWD}/cargo
%rust_test

%files
%doc README.md
%_bindir/tspin
%_datadir/bash-completion/%short_name
%_datadir/zsh_completion.d/%short_name

%changelog
* Wed Sep 03 2025 Pavel Shilov <zerospirit@altlinux.org> 5.5.0-alt1
- 5.4.5 -> 5.5.0

* Wed Jul 02 2025 Pavel Shilov <zerospirit@altlinux.org> 5.4.5-alt1
- Update based on upstream

* Wed Nov 14 2024 Pavel Shilov <zerospirit@altlinux.org> 3.0.2-alt2
- Update packaging for package
- Remove requires

* Fri Aug 23 2024 Pavel Shilov <zerospirit@altlinux.org> 3.0.2-alt1
- initial build for Sisyphus
