Name:     cargo-vendor-checksum
Version:  0.1.1
Release:  alt1

Summary:  It is a tool for updating checksum files in vendor directories
License:  MIT
Group:    Development/Other
Url:      https://github.com/alt-chill/cargo-vendor-checksum

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
It is a tool for updating checksum files in vendor directories. After
modifying files, e.g. when patching sources for building packages.

%prep
%setup

%build
%rust_build

%install
%rust_install

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name --completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name --completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name --completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%_bindir/%name
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%doc *.md

%changelog
* Tue Nov 14 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.1-alt1
- Add threads

* Thu Nov 09 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
