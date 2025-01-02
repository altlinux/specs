%def_disable snapshot
%define _name ruffle
%define ver_major 2025.01
%define rdn_name rs.ruffle.Ruffle

%def_disable bootstrap
%def_enable check

Name: %_name
Version: %ver_major.02
Release: alt1

Summary: A Flash Player emulator written in Rust
License: Apache-2.0 and MIT
Group: Graphics
Url: https://ruffle.rs/

Vcs: https://github.com/ruffle-rs/ruffle.git

%define git_ver nightly-%(echo %version|tr . -)

%if_disabled snapshot
Source: %url/archive/%git_ver/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Source1: %_name-%version-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: gcc-c++
BuildRequires: itstool
BuildRequires: libalsa-devel
BuildRequires: pkgconfig(udev)
# for ruffle_core
BuildRequires: /usr/bin/java /proc
# mentioned in README but not used
#BuildRequires: pkgconfig(xcb-cursor)
#BuildRequires: pkgconfig(xcb-shape)
#BuildRequires: pkgconfig(xcb-xfixes)
#BuildRequires: pkgconfig(xcb-xinput)
#BuildRequires: pkgconfig(xcb-xkb)
#BuildRequires: pkgconfig(gtk+-3.0)

%description
Ruffle is an Adobe Flash Player emulator written in the Rust programming
language. Ruffle targets both the desktop and the web using WebAssembly.

%package desktop
Summary: %summary
Group: Graphics

%description desktop
Ruffle is an Adobe Flash Player emulator written in the Rust.

This package provides Ruffle for desktop.

%prep
%setup -n %_name-%{?_enable_snapshot:%version}%{?_disable_snapshot:%git_ver} %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' >> .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
%rust_build --package %{_name}_desktop

pushd desktop/packages/linux
%make
popd

%install
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
%rust_install %{_name}_desktop

pushd desktop/packages/linux
install -v -Dm644 %rdn_name.desktop \
    -t %buildroot%_datadir/applications
install -v -Dm644 %rdn_name.svg \
    -t %buildroot%_iconsdir/hicolor/scalable/apps
install -v -Dm644 %rdn_name.metainfo.xml \
    -t %buildroot%_datadir/metainfo
popd

%find_lang %rdn_name

%check
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
%rust_test

%files desktop -f %rdn_name.lang
%_bindir/%{_name}_desktop
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/scalable/apps/%rdn_name.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Thu Jan 02 2025 Yuri N. Sedunov <aris@altlinux.org> 2025.01.02-alt1
- nightly-2025-01-02

* Wed Jan 01 2025 Yuri N. Sedunov <aris@altlinux.org> 2024.12.31-alt1
- first build for Sisyphus (nightly-2024-12-31-1-g1d0576766)


