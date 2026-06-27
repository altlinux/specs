%global _unpackaged_files_terminate_build 1
%def_with check

Name: lightningview
Version: 2.6.2
Release: alt1
Summary: A lightning-fast cross-platform image viewer
License: GPL-2.0
Group: Graphics
URL: https://lightningview.app
VCS: https://github.com/dividebysandwich/LightningView

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: clang-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)

%if_with check
BuildRequires: desktop-file-utils
%endif

%description
A lightning-fast cross-platform image viewer written in Rust.
This is a very slim image viewer that aims to replicate the most
important functions found in commercial software like ACDSee.

%prep
%setup -a1
%rust_prep
cat >> .cargo/config.toml <<EOF
[source."git+https://github.com/dividebysandwich/imagepipe?rev=cc9df677"]
git = "https://github.com/dividebysandwich/imagepipe"
rev = "cc9df677"
replace-with = "vendored-sources"

[source."git+https://patched@github.com/dividebysandwich/dnglab.git?rev=06dc3dab"]
git = "https://patched@github.com/dividebysandwich/dnglab.git"
rev = "06dc3dab"
replace-with = "vendored-sources"
EOF

%build
%rust_build

%install
%rust_install
install -Dm 0644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm 0644 %name.png %buildroot%_iconsdir/hicolor/256x256/apps/%name.png

%check
%rust_test
desktop-file-validate %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/256x256/apps/%name.png
%doc README.md

%changelog
* Sat Jun 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.6.2-alt1
- Initial build for ALT.
