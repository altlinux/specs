%define _unpackaged_files_terminate_build 1

%define binname dust

Name: du-dust
Version: 1.1.1
Release: alt1

Summary: A more intuitive version of du in rust
License: Apache-2.0
Group: File tools
Url: https://crates.io/crates/du-dust
Vcs: https://github.com/bootandy/dust

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires: /proc
BuildRequires: rust-cargo

%description
%summary

Because I want an easy way to see where my disk is being used.

%prep
%setup -a1
%autopatch -p1
mkdir .cargo
cat << EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false
EOF

%build
cargo build %_smp_mflags --offline --release

%install
install -Dp target/release/%binname -t %buildroot%_bindir
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
%_man1dir/%binname.1.*
%_datadir/zsh/site-functions/_%binname
%_datadir/bash-completion/completions/%binname
%_datadir/fish/vendor_completions.d/%binname.fish

%changelog
* Wed Aug 07 2024 Alexandr Shashkin <dutyrok@altlinux.org> 1.1.1-alt1
- Updated to 1.1.1.

* Fri Mar 29 2024 Alexandr Shashkin <dutyrok@altlinux.org> 1.0.0-alt1
- 0.8.6 -> 1.0.0.

* Wed Nov 22 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.8.6-alt1
- Initial build for ALT Sisyphus

