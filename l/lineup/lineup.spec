Name:     lineup
Version:  0.1.0
Release:  alt1

Summary:  Lineup is a tool for running tasks on workers
License:  MIT
Group:    Emulators
Url:      https://github.com/Obirvalger/lineup

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

ExclusiveArch: aarch64 x86_64

%description
Lineup is a tool for running tasks on workers (e.g. vms or containers).

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%_bindir/%name
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%doc doc *.md

%changelog
* Tue Feb 03 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
