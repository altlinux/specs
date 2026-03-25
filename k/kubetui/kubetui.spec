%global _unpackaged_files_terminate_build 1

Name:    kubetui
Version: 1.12.1
Release: alt1

Summary: An intuitive Terminal User Interface (TUI) tool for real-time monitoring and exploration of Kubernetes resources
License: MIT
Group:   Monitoring
Url:     https://github.com/sarub0b0/kubetui

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: pkgconfig(libzstd)
BuildRequires: /proc

%description
Kubetui is a terminal user interface (TUI) tool designed for monitoring
Kubernetes resources. It provides an easy-to-use interface for developers
and operators to access important information about their applications and
infrastructure.

%prep
%setup
%patch -p1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[env]
ZSTD_SYS_USE_PKG_CONFIG = "1"
EOF

%build
%rust_build

%install
%rust_install
target/release/%name completion bash | install -Dm644 /dev/stdin "%buildroot%_datadir/bash-completion/completions/%name"
target/release/%name completion zsh  | install -Dm644 /dev/stdin "%buildroot%_datadir/zsh/site-functions/_%name"
target/release/%name completion fish | install -Dm644 /dev/stdin "%buildroot%_datadir/fish/vendor_completions.d/%name.fish"

%check
%rust_test

%files
%doc *.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Wed Mar 25 2026 Nadezhda Fedorova <fedor@altlinux.org> 1.12.1-alt1
- 1.9.0 -> 1.12.1

* Mon Aug 25 2025 Nadezhda Fedorova <fedor@altlinux.org> 1.9.0-alt1
- 1.7.0 -> 1.9.0

* Fri Apr 04 2025 Nadezhda Fedorova <fedor@altlinux.org> 1.7.0-alt1
- Initial build for ALTLinux.
