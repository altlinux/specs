Name:    minijinja-cli
Version: 2.21.0
Release: alt1

Summary: Command-line utility for the MiniJinja template engine
License: Apache-2.0
Group:   Development/Other
Url:     https://github.com/mitsuhiko/minijinja

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

Patch1: minijinja-cli-2.7.0-alt-skip-linker.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
%summary

%prep
%setup
%patch1 -p1
cd minijinja-cli
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cd minijinja-cli
%rust_build

%install
%rust_install

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name --generate-completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name --generate-completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name --generate-completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
cd minijinja-cli
%rust_test

%files
%doc *.md
%_bindir/*
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Wed Jun 17 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.21.0-alt1
- new version 2.21.0

* Thu May 21 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.20.0-alt1
- new version 2.20.0

* Wed Apr 29 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.19.0-alt1
- new version 2.19.0

* Wed Mar 25 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.18.0-alt1
- new version 2.18.0

* Thu Mar 12 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.17.1-alt1
- new version 2.17.1

* Tue Mar 03 2026 Mikhail Gordeev <obirvalger@altlinux.org> 2.16.0-alt1
- new version 2.16.0

* Wed Feb 26 2025 Mikhail Gordeev <obirvalger@altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus
