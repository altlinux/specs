%def_enable snapshot
%define ver_major 1.0
%define beta .alpha.1
%define rdn_name com.system76.Cosmic

%def_disable bootstrap
%def_enable check

Name: cosmic-comp
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC Wayland Compositor
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-comp

Vcs: https://github.com/pop-os/cosmic-comp.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar
Patch10: cosmic-term-1.0.0-alt-linux-raw-sys-char-loongarch64.patch

ExcludeArch: %ix86 armh ppc64le

BuildRequires(pre): rpm-build-rust
BuildRequires: make
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libseat)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(gbm)

%description
Wayland compositor for the COSMIC desktop environment.

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
%makeinstall_std prefix=%_prefix

%check
%rust_test

%files
%_bindir/%name
%_datadir/cosmic/com.system76.CosmicSettings.Shortcuts/v1/defaults

%changelog
* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-13-ga3c8111)


