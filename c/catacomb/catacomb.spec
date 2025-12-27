Name: catacomb
Version: 1.0.6
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

[source."git+https://github.com/smithay/smithay?rev=06c9930f2b61f7d4b08a1f525fa114fd4492ac98"]
git = "https://github.com/smithay/smithay"
rev = "06c9930f2b61f7d4b08a1f525fa114fd4492ac98"
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
* Sat Dec 27 2025 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- initial build for ALT Sisyphus
