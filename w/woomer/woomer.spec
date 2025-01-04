%def_enable snapshot

%define _name woomer
%define ver_major 0.1

%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Zoomer application for wayland
License: MIT
Group: Accessibility
Url: https://github.com/coffeeispower/woomer

Vcs: https://github.com/coffeeispower/woomer.git

%if_disabled snapshot
Source: https://github.com/coffeeispower/woomer/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

# due raylib
ExcludeArch: aarch64 ppc64le

%define glfw_ver 3.3.3

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(glfw3) >= %glfw_ver cmake
# for raylib
BuildRequires: gcc-c++
# for bindgen
BuildRequires: clang-devel

%description
Zoomer application for wayland inspired by [tsoding's
boomer (https://github.com/tsoding/boomer) written in rust.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ -d .cargo ] || mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
%rust_install

%files
%_bindir/%_name
%doc README*

%changelog
* Sat Jan 04 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus (0.1.0-12-g62400d1)

