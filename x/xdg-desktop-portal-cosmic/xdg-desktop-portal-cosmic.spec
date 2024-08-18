%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 1.0
%define beta .alpha.1
%define rdn_name com.system76.CosmicPortal
%define dbus_name org.freedesktop.impl.portal.desktop.cosmic

%def_disable bootstrap
%def_enable check

Name: xdg-desktop-portal-cosmic
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC Desktop Portal
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/xdg-desktop-portal-cosmic

Vcs: https://github.com/pop-os/xdg-desktop-portal-cosmic.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar
Patch1: cosmic-files-1.0.0-alt-vendor-no-vergen.patch

Requires: xdg-desktop-portal-gtk

BuildRequires(pre): rpm-build-rust
BuildRequires: make
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libpipewire-0.3) clang-devel
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gstreamer-1.0)

%description
XDG Desktop Portal implementation for COSMIC desktop environment.

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%patch1
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    vendor/cosmic-files/.cargo-checksum.json

%build
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
%rust_build

%install
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
%makeinstall_std prefix=%_prefix

%check
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
%rust_test

%files
%_libexecdir/%name
%_datadir/dbus-1/services/%dbus_name.service
%_datadir/xdg-desktop-portal/portals/cosmic.portal
%_datadir/xdg-desktop-portal/cosmic-portals.conf
%_iconsdir/hicolor/*/*/*.svg
#%doc README*

%changelog
* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus


