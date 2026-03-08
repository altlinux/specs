%define cargo_prep %nil
%define cargo_build %rust_build
%define cargo_install %rust_install

Name: stl-thumb
Version: 0.5.0
Release: alt1

Summary: Fast lightweight thumbnail generator for STL files

License: MIT
Group: Graphics
URL: https://github.com/unlimitedbacon/stl-thumb
# Source-url: https://github.com/unlimitedbacon/stl-thumb.git
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: cmake gcc-c++
BuildRequires: libGL-devel libfreetype-devel libexpat-devel
BuildRequires: libwayland-client-devel libwayland-server-devel
BuildRequires: libxkbcommon-devel libxkbcommon-x11-devel

%description
stl-thumb is a fast lightweight thumbnail generator for STL, OBJ, and 3MF
files. It can show previews for 3D model files in your file manager on Linux.
It generates thumbnail images using OpenGL rendering.

%prep
%setup -a1
%cargo_prep
# Remove the existing .cargo/config which has Debian-specific paths
rm -f .cargo/config
mkdir -p .cargo
cat <<EOF >> .cargo/config
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%cargo_build

%install
%cargo_install
install -Dm644 stl-thumb.thumbnailer %buildroot%_datadir/thumbnailers/stl-thumb.thumbnailer

%files
%_bindir/stl-thumb
%_datadir/thumbnailers/stl-thumb.thumbnailer
%doc README.md
%doc LICENSE

%changelog
* Fri Mar 06 2026 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- initial build for ALT Sisyphus

