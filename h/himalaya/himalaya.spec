Name: himalaya
Version: 0.8.1
Release: alt2
Summary: CLI to manage your emails
License: MIT
Group: Networking/Mail
Url: https://pimalaya.org/himalaya/
Vcs: https://github.com/soywod/himalaya
Source: %name-%version.tar
Source2: %name.service

ExcludeArch: ppc64le

BuildRequires: rust-cargo

%description
CLI to manage your emails, based on the pimalaya-email library.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --offline --release

%install
# install bin
cargo install --path . --root %buildroot%_usr
# install man
mkdir -p %buildroot%_man1dir
%buildroot%_bindir/%name man %buildroot%_man1dir
# install shell completions
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
# install service file
mkdir -p %buildroot%_userunitdir
install -p -m 644 %SOURCE2 %buildroot%_userunitdir/%name.service

%files
%_bindir/%name
%_man1dir/%{name}*.1.xz
%_userunitdir/%name.service
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Sat Jun 17 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt2
- Added systemd service

* Fri Jun 16 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt1
- Initial build for ALT
