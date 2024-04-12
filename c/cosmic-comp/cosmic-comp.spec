Name: cosmic-comp
Version: 0.0.1012.895e
Release: alt1

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

[source."git+https://github.com/DioxusLabs/taffy?rev=7781c70"]
git = "https://github.com/DioxusLabs/taffy"
rev = "7781c70"
replace-with = "vendored-sources"

[source."git+https://github.com/Drakulix/id-tree.git?branch=feature/copy_clone"]
git = "https://github.com/Drakulix/id-tree.git"
branch = "feature/copy_clone"
replace-with = "vendored-sources"

[source."git+https://github.com/Smithay/smithay-egui.git?rev=cdc652e0"]
git = "https://github.com/Smithay/smithay-egui.git"
rev = "cdc652e0"
replace-with = "vendored-sources"

[source."git+https://github.com/gfx-rs/wgpu?rev=20fda69"]
git = "https://github.com/gfx-rs/wgpu"
rev = "20fda69"
replace-with = "vendored-sources"

[source."git+https://github.com/jackpot51/rust-atomicwrites"]
git = "https://github.com/jackpot51/rust-atomicwrites"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-protocols?branch=main"]
git = "https://github.com/pop-os/cosmic-protocols"
branch = "main"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/cosmic-text.git"]
git = "https://github.com/pop-os/cosmic-text.git"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/glyphon.git?tag=v0.5.0"]
git = "https://github.com/pop-os/glyphon.git"
tag = "v0.5.0"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/libcosmic/"]
git = "https://github.com/pop-os/libcosmic/"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/smithay-clipboard?tag=pop-mime-types"]
git = "https://github.com/pop-os/smithay-clipboard"
tag = "pop-mime-types"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/softbuffer?tag=cosmic-4.0"]
git = "https://github.com/pop-os/softbuffer"
tag = "cosmic-4.0"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/window_clipboard.git?tag=pop-mime-types"]
git = "https://github.com/pop-os/window_clipboard.git"
tag = "pop-mime-types"
replace-with = "vendored-sources"

[source."git+https://github.com/smithay//smithay?rev=ba0121a"]
git = "https://github.com/smithay//smithay"
rev = "ba0121a"
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
* Fri Apr 12 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1012.895e-alt1
- New version 0-1012-g895ea6aec.

* Wed Aug 09 2023 Leontiy Volodin <lvol@altlinux.org> 0-alt3.git4bf1acb
- Updated from git commit 4bf1acb954ec6690e5ed91bbf76d54a5d9db4996.

* Wed May 31 2023 Leontiy Volodin <lvol@altlinux.org> 0-alt2.git3271f53
- Updated from git commit 3271f539bfddcf1badb0362f29095118ba195cb2.

* Thu Feb 02 2023 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git649b900
- Initial build for ALT Sisyphus (thanks archlinux for the spec).
