%def_enable snapshot

%define ver_major 3.0

%def_disable check
%def_disable bootstrap

Name: artem
Version: %ver_major.0
Release: alt1

Summary: Artem is a ascii art cli converter
License: MPL-2.0
Group: Graphics
Url: https://github.com/FineFindus/artem

Vcs: https://github.com/FineFindus/artem.git

%if_disabled snapshot
Source: https://github.com/FineFindus/artem/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo >= 1.80
%{?_enable_check:BuildRequires: clippy}

%description
Artem is a small cli program, written in rust, to easily convert images
to ascii art, named after the latin word for art. By default it tries to
use truecolor, if the terminal does not support truecolor, it falls back
to 16 Color ANSI. When the ascii image is wr It supports `.jpeg`,
`.png`, `.gif`, `.webp` and many more.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
%rust_install
%find_lang %name

%check
%rust_test

%files -f %name.lang
%_bindir/%name
%doc README*

%changelog
* Sun Nov 02 2025 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for Sisyphus (v3.0.0-9-g77495e9)

