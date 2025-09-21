%define _unpackaged_files_terminate_build 1

%define bash_completions_dir %_datadir/bash-completion/completions
%define fish_completions_dir %_datadir/fish/vendor_completions.d
%define zsh_completions_dir %_datadir/zsh/site-functions

Name: sequoia-sqv
Version: 1.3.0
Release: alt1
Summary: Simple OpenPGP signature verification program

License: LGPL-2.0-or-later
Group: File tools
Url: https://gitlab.com/sequoia-pgp/sequoia-sqv
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libnettle-devel
BuildRequires: clang-devel

%description
A simple signature verification program. sqv verifies detached OpenPGP
signatures.  It is a replacement for gpgv.  Unlike gpgv, it can take
additional constraints on the signature into account.

%prep
%setup

%build
export ASSET_OUT_DIR=target/assets
%rust_build

%install
%rust_install -- sqv

mkdir -p %buildroot/%_man1dir/
cp -pav target/assets/man-pages/sqv*.1 %buildroot/%_man1dir/

install -pDm 644 -- \
    target/assets/shell-completions/sqv.bash \
    %buildroot/%bash_completions_dir/sqv

install -pDm 644 -- \
    target/assets/shell-completions/sqv.fish \
    %buildroot/%fish_completions_dir/sqv

install -pDm 644 -- \
    target/assets/shell-completions/_sqv \
    %buildroot/%zsh_completions_dir/_sqv

%check
%rust_test

%files
%doc LICENSE.txt README.md NEWS
%_bindir/sqv
%bash_completions_dir/sqv
%fish_completions_dir/sqv
%zsh_completions_dir/_sqv
%_man1dir/sqv*

%changelog
* Fri Sep 19 2025 Vladislav Tsarev <tyaplyapych@altlinux.org> 1.3.0-alt1
- initial build
