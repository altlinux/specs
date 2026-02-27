%define _unpackaged_files_terminate_build 1
%def_with check

Name: kdotool
Version: 0.2.2
Release: alt1

Summary: Xdotool-like for KDE Wayland
License: Apache-2.0
Group: Development/Other
Url: https://crates.io/crates/kdotool
Vcs: https://github.com/jinliu/kdotool

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: libdbus-devel

%description
Wayland, for security concerns, removed most of the X11 APIs that
xdotool uses to simulate user input and control windows. ydotool solves
the input part by talking directly to the kernel input device. However,
for the window control part, you have to use each Wayland compositor's
own APIs.

This program uses KWin's scripting API to control windows. In each
invocation, it generates a KWin script on-the-fly, loads it into KWin,
runs it, and then deletes it, using KWin's DBus interface.

%prep
%setup -a 1
%autopatch -p 1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[profile.release]
strip = false
codegen-units = 1
opt-level = 3
debug = 2
EOF

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/kdotool

%changelog
* Thu Feb 26 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.2.2-alt1
- New version (0.2.2).

* Tue Dec 23 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.2.1-alt2
- Fix FTBFS with new rust.

* Wed Jun 11 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.2.1-alt1
- First build for alt.
