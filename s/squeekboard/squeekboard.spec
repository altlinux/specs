%def_enable check
%def_disable bootstrap

Name: squeekboard
Version: 1.41.0
Release: alt1

Summary: A Wayland on-screen keyboard
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://gitlab.gnome.org/World/Phosh/squeekboard

Vcs: https://gitlab.gnome.org/World/Phosh/squeekboard.git
Source0: %name-%version.tar
Source1: %name-%version-crates.tar
Patch3500: squeekboard-1.23-alt-nix-loongarch64.patch

Provides: osk-wayland

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-macros-alternatives
BuildRequires: meson rust-cargo /proc
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(libfeedback-0.0)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cargo-vendor-checksum diffstat
%{?_enable_check:BuildRequires: clippy xkeyboard-config}

%description
%summary

%prep
%setup
%if_enabled bootstrap
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar cf %SOURCE1 vendor .cargo/config.toml
%else
tar xf %SOURCE1
%patch3500 -p1
diffstat -l -p1 %PATCH3500 | sed -re 's@vendor/@@' | xargs -r cargo-vendor-checksum -f
%endif

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/osk-wayland	%_bindir/%name 90
EOF

%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/*
%_altdir/%name
%_desktopdir/*.desktop

%changelog
* Thu Aug 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.41.0-alt1
- 1.41.0

* Mon May 06 2024 Yuri N. Sedunov <aris@altlinux.org> 1.39.0-alt1
- 1.39.0

* Sun Mar 24 2024 Yuri N. Sedunov <aris@altlinux.org> 1.38.0-alt1
- 1.38.0

* Sat Mar 09 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.23.0-alt2
- NMU: fixed FTBFS on LoongArch (trivial patch for nix crate)

* Sat Mar 09 2024 Yuri N. Sedunov <aris@altlinux.org> 1.23.0-alt1
- updated to v1.23.0-3-ge3d08ff
- enabled %%check

* Mon Jul 31 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt2
- provides osk-wayland (ALT #47074)

* Mon Apr 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22.0-alt1
- 1.22.0 released

* Thu Oct 06 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20.0-alt1
- 1.20.0 released

* Wed Apr 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17.1-alt1
- initial
