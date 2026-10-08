Name: fnm
Version: 1.39.0
Release: alt1

Summary: Fast and simple Node.js version manager, built in Rust
Group: Development/Tools
License: GPL-3.0-only
URL: https://github.com/Schniz/fnm

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: liblzma-devel

%description
Install and use different versions of Node.js via the command line.
It is designed as a higher-performance, modern alternative to the
classic nvm (Node Version Manager).

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/fnm completions --shell bash > %buildroot%_datadir/bash-completion/completions/fnm

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/fnm completions --shell zsh > %buildroot%_datadir/zsh/site-functions/_fnm

mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/fnm completions --shell fish > %buildroot%_datadir/fish/vendor_completions.d/fnm.fish

%check
# Tests requiring network access are skipped.
%rust_test --offline -- \
    --skip test_list \
    --skip test_install_latest \
    --skip test_set_default_on_new_installation \
    --skip test_installing_node_12 \
    --skip test_installing_npm \
    --skip test_zip_extraction

%files
%doc README.md LICENSE docs
%_bindir/%name
%_datadir/bash-completion/completions/fnm
%_datadir/zsh/site-functions/_fnm
%_datadir/fish/vendor_completions.d/fnm.fish

%changelog
* Wed Sep 16 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 1.39.0-alt1
- Initial build for Sisyphus.
