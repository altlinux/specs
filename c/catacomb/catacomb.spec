Name: catacomb
Version: 1.4.0
Release: alt1

Summary: Wayland mobile compositor
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/catacombing/catacomb

# Source-url: https://github.com/catacombing/catacomb/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(libseat)

%description
Catacomb is a Wayland compositor for Linux smartphones.
It aims to provide responsive window management without
cutting down on useful features.

%prep
%setup -a1

mkdir -p .cargo
cat <<EOF >> .cargo/config
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/smithay/smithay?rev=4a21f22ee96831376b5c4fef5bd1876433853963"]
git = "https://github.com/smithay/smithay"
rev = "4a21f22ee96831376b5c4fef5bd1876433853963"
replace-with = "vendored-sources"

[source."git+https://github.com/catacombing/catacomb_common?rev=512e9cadfbec50d60dc7f64415383526ff3e6a9f"]
git = "https://github.com/catacombing/catacomb_common"
rev = "512e9cadfbec50d60dc7f64415383526ff3e6a9f"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install
install -Dpm755 session/catacomb-session %buildroot%_bindir/catacomb-session
install -Dpm644 session/catacomb.service %buildroot%_userunitdir/catacomb.service
install -Dpm644 session/catacomb-shutdown.target %buildroot%_userunitdir/catacomb-shutdown.target
install -Dpm644 session/catacomb.desktop %buildroot%_datadir/wayland-sessions/catacomb.desktop

%files
%doc README.md
%_bindir/%name
%_bindir/catacomb-session
%_userunitdir/catacomb.service
%_userunitdir/catacomb-shutdown.target
%_datadir/wayland-sessions/catacomb.desktop

%changelog
* Mon Apr 06 2026 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0

* Fri Mar 06 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0

* Sat Dec 27 2025 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- initial build for ALT Sisyphus
