Name:    xrizer
Version: 0.2
Release: alt1

Summary: XR-ize your favorite OpenVR games
License: GPL-3.0
Group:   Other
Url:     https://github.com/Supreeeme/xrizer

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: cmake gcc-c++
BuildRequires: libGLEW-devel libvulkan-devel jsoncpp-devel libX11-devel
BuildRequires: clang-devel glslc

ExclusiveArch: x86_64

%description
xrizer is a reimplementation of OpenVR on top of OpenXR. This enables you
to run OpenVR games through any OpenXR runtime without running SteamVR.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/ralith/openxrs?rev=d0afdd3"]
git = "https://github.com/ralith/openxrs"
rev = "d0afdd3"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/bytemuck/.cargo-checksum.json

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/bytemuck_derive/.cargo-checksum.json

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/epaint/.cargo-checksum.json

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/env_logger/.cargo-checksum.json

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/clang-sys/.cargo-checksum.json

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/slotmap/.cargo-checksum.json

%build
%rust_build

%install
install -Dm644 target/release/libxrizer.so -t %buildroot%_libdir/xrizer

%files
%doc LICENSE README.md
%_libdir/xrizer/libxrizer.so

%changelog
* Sun Feb 16 2025 Sergey Palcheh <minergenon@altlinux.org> 0.2-alt1
- Initial build for Sisyphus
