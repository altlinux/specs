Name: yazi
Version: 0.3.0
Release: alt1

Summary: Blazing fast terminal file manager written in Rust, based on async I/O
License: MIT
Group: File tools
Url: https://yazi-rs.github.io
Vcs: https://github.com/sxyazi/yazi

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires: rust-cargo
BuildRequires: /proc

%description
Yazi (means "duck") is a terminal file manager written in Rust, based on
non-blocking async I/O. It aims to provide an efficient, user-friendly, and
customizable file management experience.

%package bash-completion
Summary: Bash Completion for %name
Group: Shells
BuildArch: noarch

%description bash-completion
The official bash completion script for %name.

%package fish-completion
Summary: Fish Completion for %name
Group: Shells
BuildArch: noarch

%description fish-completion
The official fish completion script for %name.

%package zsh-completion
Summary: ZSH Completion for %name
Group: Shells
BuildArch: noarch

%description zsh-completion
The official zsh completion script for %name.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/notify-rs/notify.git?rev=96dec74316a93bed6eec9db177b233e6e017275e"]
git = "https://github.com/notify-rs/notify.git"
rev = "96dec74316a93bed6eec9db177b233e6e017275e"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=0"]

[profile.release]
strip = false
EOF

%build
export YAZI_GEN_COMPLETIONS=true
cargo build %_smp_mflags --offline --release

%install
install -Dp target/release/%name -t %buildroot%_bindir
install -Dm 644 yazi-boot/completions/yazi.bash %buildroot%_datadir/bash-completion/completions/yazi
install -Dm 644 yazi-boot/completions/yazi.fish %buildroot%_datadir/fish/vendor_completions.d/yazi.fish
install -Dm 644 yazi-boot/completions/_yazi %buildroot%_datadir/zsh/site-functions/_yazi

%check
# Has no tests.

%files
%doc LICENSE README.md
%_bindir/%name

%files bash-completion
%_datadir/bash-completion

%files fish-completion
%_datadir/fish

%files zsh-completion
%_datadir/zsh

%changelog
* Sat Aug 03 2024 Anton Kurachenko <srebrov@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Sat Jun 29 2024 Anton Kurachenko <srebrov@altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus.
