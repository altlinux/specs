%def_enable snapshot

%define _name cosmic-workspaces
%define git_name %_name-epoch
%define ver_major 1.0
%define beta .alpha.1
%define rdn_name com.system76.CosmicWorkspaces

%def_disable bootstrap
%def_enable check

Name: %_name
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC Workspaces
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-workspaces-epoch

Vcs: https://github.com/pop-os/cosmic-workspaces-epoch.git

Provides: %git_name = %EVR

%if_disabled snapshot
Source: %url/archive/%version/%git_name-%version.tar.gz
%else
Source: %git_name-%version%beta.tar
%endif
Source1: %git_name-%version%beta-cargo.tar
Patch10: cosmic-term-1.0.0-alt-linux-raw-sys-char-loongarch64.patch

# rustc-LLVM ERROR: out of memory
# Allocation failed
ExcludeArch: %ix86 armh

BuildRequires(pre): rpm-build-rust
BuildRequires: make
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(gbm)

%description
%summary

%prep
%setup -n %git_name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%git_name-%version%beta-cargo.tar .cargo/ vendor/}

%patch10 -p1
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    vendor/linux-raw-sys/.cargo-checksum.json

%build
%rust_build

%install
%makeinstall_std prefix=%_prefix

%check
%rust_test

%files
%_bindir/%_name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.svg
#%_datadir/metainfo/%rdn_name.metainfo.xml
#%doc README*

%changelog
* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-1-g70d6c41)


