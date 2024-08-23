%def_with check

Name: bottom
Version: 0.10.2
Release: alt1
Summary: Yet another cross-platform graphical process/system monitor
License: MIT
Group: Monitoring
Url: https://clementtsang.github.io/bottom
Vcs: https://github.com/ClementTsang/bottom
Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo rpm-build-rust
BuildRequires: /proc /dev/pts

%description
A customizable cross-platform graphical process/system monitor for the terminal.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export CFLAGS="-O3 -DPIC -fPIC"
export RUSTFLAGS="-Clink-args=-fPIC -Cdebuginfo=1 --cfg rustix_use_libc"
export RUST_BACKTRACE=1
export BTM_GENERATE=true
%rust_build

%install
%rust_install btm
install -D -m 644 target/tmp/bottom/manpage/btm.1 %buildroot%_man1dir/btm.1
install -D -m 644 target/tmp/bottom/completion/btm.bash %buildroot%_datadir/bash-completion/completions/btm
install -D -m 644 target/tmp/bottom/completion/btm.fish %buildroot%_datadir/fish/vendor_completions.d/btm.fish
install -D -m 644 target/tmp/bottom/completion/_btm %buildroot%_datadir/zsh/site-functions/_btm


%check
%rust_test

%files
%doc LICENSE CHANGELOG.md README.md sample_configs
%_bindir/btm
%_man1dir/*
%_datadir/bash-completion/completions/btm
%_datadir/fish/vendor_completions.d/btm.fish
%_datadir/zsh/site-functions/_btm

%changelog
* Fri Aug 23 2024 Alexey Shabalin <shaba@altlinux.org> 0.10.2-alt1
- New version 0.10.2.

* Wed May 22 2024 Alexey Shabalin <shaba@altlinux.org> 0.9.6-alt2
- Add completions to package.
- Add docs and sample_configs to package.

* Sun Oct 22 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.6-alt1
- Updated to version 0.9.6.

* Thu Jan 26 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.0-alt1
- Initial build for ALT

