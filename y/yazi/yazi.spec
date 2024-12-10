Name: yazi
Version: 0.4.1
Release: alt1

Summary: Blazing fast terminal file manager written in Rust, based on async I/O
License: MIT
Group: File tools
Url: https://yazi-rs.github.io
Vcs: https://github.com/sxyazi/yazi.git

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
install -D target/release/%name -t %buildroot%_bindir
install -D target/release/ya -t %buildroot%_bindir
install -D yazi-boot/completions/yazi.bash %buildroot%_datadir/bash-completion/completions/yazi
install -D yazi-boot/completions/yazi.fish -t %buildroot%_datadir/fish/vendor_completions.d/
install -D yazi-boot/completions/_yazi -t %buildroot%_datadir/zsh/site-functions/
install -D yazi-cli/completions/ya.bash %buildroot%_datadir/bash-completion/completions/ya
install -D yazi-cli/completions/ya.fish -t %buildroot%_datadir/fish/vendor_completions.d/
install -D yazi-cli/completions/_ya -t %buildroot%_datadir/zsh/site-functions/

%check
# Has no tests.

%files
%doc LICENSE README.md
%_bindir/%name
%_bindir/ya

%files bash-completion
%_datadir/bash-completion

%files fish-completion
%_datadir/fish

%files zsh-completion
%_datadir/zsh

%changelog
* Tue Dec 10 2024 Anton Kurachenko <srebrov@altlinux.org> 0.4.1-alt1
- New version 0.4.1.

* Wed Sep 04 2024 Anton Kurachenko <srebrov@altlinux.org> 0.3.3-alt1
- New version 0.3.3.

* Sat Aug 03 2024 Anton Kurachenko <srebrov@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Sat Jun 29 2024 Anton Kurachenko <srebrov@altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus.
