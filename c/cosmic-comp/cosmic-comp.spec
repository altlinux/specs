Name: cosmic-comp
Version: 0
Release: alt2.git3271f53

Summary: Wayland compositor for the COSMIC DE

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-comp

Source: %url/archive/%version/%name-%version.tar.gz
Source1: vendor.tar

ExcludeArch: armh i586 ppc64le

BuildPreReq: rpm-build-rust
BuildRequires: /proc gcc-c++ cmake
BuildRequires: libudev-devel libEGL-mesa libGL-devel libgbm-devel libinput-devel libxcb-devel libxkbcommon-devel libsystemd-devel libseat1-devel fontconfig-devel

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

[source."git+https://github.com/Drakulix/id-tree.git?branch=feature/copy_clone"]
git = "https://github.com/Drakulix/id-tree.git"
branch = "feature/copy_clone"
replace-with = "vendored-sources"

[source."git+https://github.com/Smithay/smithay-egui.git?rev=197606f400"]
git = "https://github.com/Smithay/smithay-egui.git"
rev = "197606f400"
replace-with = "vendored-sources"

[source."git+https://github.com/edfloreshz/directories-rs"]
git = "https://github.com/edfloreshz/directories-rs"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-protocols?branch=main"]
git = "https://github.com/pop-os/cosmic-protocols"
branch = "main"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-text?rev=e788c175"]
git = "https://github.com/pop-os/cosmic-text"
rev = "e788c175"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-theme.git"]
git = "https://github.com/pop-os/cosmic-theme.git"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/libcosmic?rev=24709e9c3b"]
git = "https://github.com/pop-os/libcosmic"
rev = "24709e9c3b"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/softbuffer?rev=8dcb6438b"]
git = "https://github.com/pop-os/softbuffer"
rev = "8dcb6438b"
replace-with = "vendored-sources"

[source."git+https://github.com/smithay//smithay?rev=43ce6b4372"]
git = "https://github.com/smithay//smithay"
rev = "43ce6b4372"
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
* Wed May 31 2023 Leontiy Volodin <lvol@altlinux.org> 0-alt2.git3271f53
- Updated from git commit 3271f539bfddcf1badb0362f29095118ba195cb2.

* Thu Feb 02 2023 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git649b900
- Initial build for ALT Sisyphus (thanks archlinux for the spec).
