%define _unpackaged_files_terminate_build 1

%define binname dust

Name: du-dust
Version: 0.8.6
Release: alt1

Summary: A more intuitive version of du in rust
License: Apache-2.0
Group: File tools
Url: https://crates.io/crates/du-dust
Vcs: https://github.com/bootandy/dust

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo

%description
%summary

Because I want an easy way to see where my disk is being used.

%prep
%setup -a1
mkdir .cargo
cat << EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%{rust_install %binname}
install -pDv -m644 man-page/%binname.1 %buildroot%_man1dir/%binname.1
install -pD -m644 completions/%binname.bash \
    %buildroot%_datadir/bash-completion/completions/%binname
install -pD -m644 completions/_%binname \
    %buildroot%_datadir/zsh/site-functions/_%binname
install -pD -m644 completions/%binname.fish \
    %buildroot%_datadir/fish/vendor_completions.d/%binname.fish

%files
%doc README.md LICENSE*
%_bindir/%binname
%_man1dir/%binname.1.xz
%_datadir/zsh/site-functions/_%binname
%_datadir/bash-completion/completions/%binname
%_datadir/fish/vendor_completions.d/%binname.fish

%changelog
* Wed Nov 22 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.8.6-alt1
- Initial build for ALT Sisyphus

