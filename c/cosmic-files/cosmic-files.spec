%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.1
%define rdn_name com.system76.CosmicFiles

%def_disable bootstrap
%def_enable check

Name: cosmic-files
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC File Manager
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-files

Vcs: https://github.com/pop-os/cosmic-files.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar
Patch1: %name-1.0.0-alt-no-vergen.patch

Requires: cosmic-icons

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: /usr/bin/appstreamcli /usr/bin/desktop-file-validate

%description
File manager for the COSMIC desktop environment

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%patch1
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%build
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
%rust_build

%install
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
just rootdir=%buildroot install

%check
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
%rust_test

%files
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/metainfo/%rdn_name.metainfo.xml
%_iconsdir/hicolor/*/apps/*.svg
%doc README*

%changelog
* Sat Aug 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-29-gaebc652)


