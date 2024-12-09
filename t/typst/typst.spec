%def_with check

Name:    typst
Version: 0.12.0
Release: alt1

Summary: New markup-based typesetting system that is powerful and easy to learn
License: Apache-2.0
Group:   Text tools
Url:     https://typst.app
Vcs:     https://github.com/typst/typst.git

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: libssl-devel
BuildRequires: rust-cargo /proc

%description
Typst is a new markup-based typesetting system that is designed to be
as powerful as LaTeX while being much easier to learn and use.

Typst has
- Built-in markup for the most common formatting tasks
- Flexible functions for everything else
- A tightly integrated scripting system
- Math typesetting, bibliography management, and more
- Fast compile times thanks to incremental compilation
- Friendly error messages in case something goes wrong

%package -n bash-completion-%name
Summary:        Bash completion routines for %name
Group:          Shells
BuildArch:      noarch
Requires:       %name
Requires:       bash-completion

%description -n bash-completion-%name
Bash command-line completion support for %name.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/typst/typst-dev-assets?tag=v0.12.0"]
git = "https://github.com/typst/typst-dev-assets"
tag = "v0.12.0"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
export GEN_ARTIFACTS=artifacts
export 'RUSTFLAGS= -g'
# Reduce build jobs count for i586 arch to avoid OOM.
%ifarch %ix86
export NJOBS='-j4'
%else
export NJOBS=%{?_smp_mflags}
%endif
cargo build --release $NJOBS --offline

%install
%rust_install
%__mkdir_p %buildroot{%_man1dir,%_datadir/bash-completion/completions}
cp -av ./crates/%name-cli/artifacts/%{name}*.1 %buildroot%_man1dir
cp -av ./crates/%name-cli/artifacts/%name.bash \
%buildroot%_datadir/bash-completion/completions

%check
%rust_test --workspace

%files
%doc *.md LICENSE NOTICE docs/{guides,tutorial}
%_bindir/%name
%_man1dir/*.1.*

%files -n bash-completion-%name
%_datadir/bash-completion/completions/%name.bash

%changelog
* Mon Dec 09 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.12.0-alt1
- Initial build for ALT (Closes #50403), thx Aleksander Kamilatov aka zander@.
