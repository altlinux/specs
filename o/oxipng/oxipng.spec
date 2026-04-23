%def_disable snapshot
%define ver_major 10.1

%def_disable bootstrap
%def_enable check

Name: oxipng
Version: %ver_major.1
Release: alt1

Summary: PNG compression optimizer
License: MIT
Group: Graphics
Url: https://github.com/shssoichiro/oxipng

Vcs: https://github.com/shssoichiro/oxipng.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
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
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
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
* Thu Apr 23 2026 Yuri N. Sedunov <aris@altlinux.org> 10.1.1-alt1
- 10.1.1

* Mon Jan 26 2026 Yuri N. Sedunov <aris@altlinux.org> 10.1.0-alt1
- 10.1.0

* Sun Dec 07 2025 Yuri N. Sedunov <aris@altlinux.org> 10.0.0-alt1
- 10.0.0

* Sat Apr 26 2025 Yuri N. Sedunov <aris@altlinux.org> 9.1.5-alt1
- 9.1.5

* Sat Feb 15 2025 Yuri N. Sedunov <aris@altlinux.org> 9.1.4-alt1
- 9.1.4

* Sat Nov 30 2024 Yuri N. Sedunov <aris@altlinux.org> 9.1.3-alt1
- 9.1.3

* Sat Jul 13 2024 Yuri N. Sedunov <aris@altlinux.org> 9.1.2-alt1
- 9.1.2

* Tue Apr 23 2024 Yuri N. Sedunov <aris@altlinux.org> 9.1.1-alt1
- 9.1.1

* Mon Apr 22 2024 Yuri N. Sedunov <aris@altlinux.org> 9.1.0-alt1
- 9.1.0

* Wed Oct 11 2023 Yuri N. Sedunov <aris@altlinux.org> 9.0.0-alt1
- 9.0.0

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 8.0.0-alt1
- first build for Sisyphus


