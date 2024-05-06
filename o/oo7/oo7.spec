%def_enable snapshot
%define ver_major 0.3

%def_disable bootstrap
%def_enable check

Name: oo7
Version: %ver_major.2
Release: alt1

Summary: Secret Service provider
License: MIT
Group: System/Libraries
Url: https://github.com/bilelmoussaoui/oo7

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/bilelmoussaoui/oo7.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

BuildRequires(pre): rpm-build-rust

%description
The repository consists of the following projects:

- cli: a secret-tool replacement
- client: the client side library
- portal: https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.impl.portal.Secret.html implementation

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
%rust_install %name-cli %name-portal

%check
%rust_test

%files
%_bindir/%name-cli
%_bindir/%name-portal
%doc README*

%changelog
* Mon May 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Sat May 04 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Sat Feb 24 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first preview for Sisyphus (0.3.0-5-gad713f5)

