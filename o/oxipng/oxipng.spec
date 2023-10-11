%def_disable snapshot
%define ver_major 9.0

%def_disable bootstrap
%def_enable check

Name: oxipng
Version: %ver_major.0
Release: alt1

Summary: PNG compression optimizer
License: MIT
Group: Graphics
Url: https://github.com/shssoichiro/oxipng

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/shssoichiro/oxipng.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

BuildRequires(pre): rpm-build-rust

%description
Oxipng is a multithreaded lossless PNG compression optimizer. It can be
used via a command-line interface or as a library in other Rust programs.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name
%doc README* CHANGELOG* MANUAL*

%changelog
* Wed Oct 11 2023 Yuri N. Sedunov <aris@altlinux.org> 9.0.0-alt1
- 9.0.0

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 8.0.0-alt1
- first build for Sisyphus


