%def_disable snapshot
%define ver_major 1.0
%define beta .alpha.6
%define rdn_name com.system76.CosmicGreeter

%def_disable bootstrap
%def_enable check

Name: cosmic-greeter
Version: %ver_major.0
Release: alt0.60%beta

Summary: COSMIC Greeter
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-greeter

Vcs: https://github.com/pop-os/cosmic-greeter.git

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar
Patch10: cosmic-term-1.0.0-alt-linux-raw-sys-char-loongarch64.patch

Requires: greetd cosmic-comp

BuildRequires(pre): rpm-build-rust rpm-macros-pam0
BuildRequires: just clang-devel
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(pam)

# no cosmic-comp for ppc64le
ExcludeArch: %ix86 armh ppc64le

%description
COSMIC greeter for greetd, which can be run inside cosmic-comp.

%prep
%setup -n %name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver} %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%patch10 -p1
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    vendor/linux-raw-sys/.cargo-checksum.json

%build
export RUSTFLAGS="${RUSTFLAGS} -g"
just build-release
#%rust_build

%install
just rootdir=%buildroot install

%check
%rust_test

%files
%_bindir/%name
%_bindir/%name-daemon
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%_datadir/dbus-1/system.d/%rdn_name.conf
%doc README*

%changelog
* Sat Feb 22 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.60.alpha.6
- 1.0.0-alpha.6

* Wed Jan 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.51.alpha.5.1
- 1.0.0-alpha.5.1

* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- 1.0.0-alpha.5

* Sat Dec 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.4.alpha.4
- 1.0.0-alpha.4

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.2
- 1.0.0-alpha.2

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-5-g3679ee5)


