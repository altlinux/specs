%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: xh
Version: 0.26.2
Release: alt1

Summary: Friendly and fast tool for sending HTTP requests
License: MIT
Group: Networking/WWW
Url: https://github.com/ducaale/xh
Vcs: https://github.com/ducaale/xh

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-rust

%description
xh is a friendly and fast tool for sending HTTP requests. It reimplements as
much as possible of HTTPie's excellent design, with a focus on improved
performance.

%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
debug = true
strip = "none"
EOF

%build
%rust_build

%install
%rust_install
install -D -m644 doc/xh.1 %buildroot%_man1dir/xh.1
install -D -m644 completions/xh.bash \
    %buildroot%_datadir/bash-completion/completions/xh
install -D -m644 completions/xh.fish \
    %buildroot%_datadir/fish/vendor_completions.d/xh.fish
install -D -m644 completions/_xh %buildroot%_datadir/zsh/site-functions/_xh

%check
# 15 downloading tests are disabled.
%rust_test --offline --no-default-features --features rustls,network-interface

%files
%_bindir/xh
%_datadir/bash-completion/completions/xh
%_datadir/fish/vendor_completions.d/xh.fish
%_datadir/zsh/site-functions/_xh
%_man1dir/xh.1.xz

%changelog
* Fri Sep 18 2026 Pavel Petrykin <silverducks@altlinux.org> 0.26.2-alt1
- Initial build for ALT Linux.
