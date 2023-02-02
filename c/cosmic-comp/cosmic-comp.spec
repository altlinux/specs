Name: cosmic-comp
Version: 0
Release: alt1.git649b900

Summary: Wayland compositor for the COSMIC DE

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-comp

Source: %url/archive/%version/%name-%version.tar.gz
Source1: vendor.tar

ExcludeArch: armh i586 ppc64le

BuildPreReq: rpm-build-rust
BuildRequires: /proc
BuildRequires: libudev-devel libEGL-mesa libGL-devel libgbm-devel libinput-devel libxcb-devel libxkbcommon-devel libsystemd-devel libseat1-devel

%description
%summary.

%prep
%setup
# Unpacked vendor/ into the source (used .gear/tags).
tar -xf %SOURCE1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."https://github.com/Smithay/smithay-egui.git"]
git = "https://github.com/Smithay/smithay-egui.git"
rev = "610a7dbf80"
replace-with = "vendored-sources"

[source."https://github.com/edfloreshz/directories-rs"]
git = "https://github.com/edfloreshz/directories-rs"
replace-with = "vendored-sources"

[source."https://github.com/pop-os/cosmic-protocols"]
git = "https://github.com/pop-os/cosmic-protocols"
branch = "main"
replace-with = "vendored-sources"

[source."https://github.com/pop-os/cosmic-theme.git"]
git = "https://github.com/pop-os/cosmic-theme.git"
replace-with = "vendored-sources"

[source."https://github.com/pop-os/libcosmic"]
git = "https://github.com/pop-os/libcosmic"
rev = "abf8fc96c"
replace-with = "vendored-sources"

[source."https://github.com/pop-os/smithay"]
git = "https://github.com/pop-os/smithay"
rev = "3437fe15ca"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%make_build

%install
%makeinstall_std

install -Dm0644 "data/cosmic.desktop" "%buildroot%_datadir/wayland-sessions/cosmic.desktop"
install -Dm0644 "data/cosmic-session.target" "%buildroot%_prefix/lib/systemd/user/cosmic-session.target"
install -Dm0644 "data/cosmic-session-pre.target" "%buildroot%_prefix/lib/systemd/user/cosmic-session-pre.target"
install -Dm0644 "data/cosmic-comp.service" "%buildroot%_prefix/lib/systemd/user/cosmic-comp.service"
install -Dm0755 "data/cosmic-service" "%buildroot%_bindir/cosmic-service"

%files
%doc LICENSE
%_bindir/*
%_datadir/wayland-sessions/cosmic.desktop
%_prefix/lib/systemd/user/cosmic-session.target
%_prefix/lib/systemd/user/cosmic-session-pre.target
%_prefix/lib/systemd/user/cosmic-comp.service

%changelog
* Thu Feb 02 2023 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git649b900
- Initial build for ALT Sisyphus (thanks archlinux for the spec).
