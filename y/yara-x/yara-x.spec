Name:    yara-x
Version: 1.23.0
Release: alt1

Summary: A rewrite of YARA in Rust
License: BSD-3-Clause
Group:   Development/Tools
Url:     https://github.com/VirusTotal/yara-x

Source: %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
YARA-X is a re-incarnation of YARA, a pattern matching tool designed with
malware researchers in mind. This new incarnation intends to be faster, safer
and more user-friendly than its predecessor. The ultimate goal of YARA-X is
replacing YARA as the default pattern matching tool for malware researchers.



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
%rust_install yr

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/yr completion zsh > %buildroot%_datadir/zsh/site-functions/_yr
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/yr completion bash > %buildroot%_datadir/bash-completion/completions/yr
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/yr completion fish > %buildroot%_datadir/fish/vendor_completions.d/yr.fish

%check
%ifarch %ix86
%define rust_debug 0
%endif
%rust_test

%files
%doc *.md
%_bindir/yr
%_datadir/zsh/site-functions/_yr
%_datadir/bash-completion/completions/yr
%_datadir/fish/vendor_completions.d/yr.fish

%changelog
* Wed Nov 11 2026 Mikhail Gordeev <obirvalger@altlinux.org> 1.23.0-alt1
- new version 1.23.0

* Fri Oct 30 2026 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.1-alt1
- Initial build for Sisyphus
