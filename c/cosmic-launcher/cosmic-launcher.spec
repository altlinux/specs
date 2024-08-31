%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.1
%define rdn_name com.system76.CosmicLauncher

%def_disable bootstrap
%def_enable check

Name: cosmic-launcher
Version: %ver_major.0
Release: alt0.2%beta

Summary: COSMIC Launcher
License: MPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-launcher

Vcs: https://github.com/pop-os/cosmic-launcher.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar
Patch10: cosmic-term-1.0.0-alt-linux-raw-sys-char-loongarch64.patch

# no pop-launcher for ppc64le
ExcludeArch: ppc64le armh

Requires: pop-launcher

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: pkgconfig(xkbcommon)

%description
%summary

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%patch10 -p1
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    vendor/linux-raw-sys/.cargo-checksum.json

%build
%rust_build

%install
just rootdir=%buildroot install

%check
%rust_test

%files
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sat Aug 31 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.1
- required pop-launcher
- fixed build for loongarch64

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus


