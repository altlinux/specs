Name:    xrizer
Version: 0.5
Release: alt1

Summary: XR-ize your favorite OpenVR games
License: GPL-3.0
Group:   Other
Url:     https://github.com/Supreeeme/xrizer

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires: rpm-build-rust
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
cat > .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/ralith/openxrs?rev=d0afdd3"]
git = "https://github.com/ralith/openxrs"
rev = "d0afdd3"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[profile.release]
strip = false
EOF

sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/*/.cargo-checksum.json

%build
%rust_build

%install
install -Dm755 target/release/libxrizer.so %buildroot%_libdir/%name/libxrizer.so

%files
%doc LICENSE README.md
%dir %_libdir/%name/
%_libdir/%name/libxrizer.so

%changelog
* Fri Jun 12 2026 Sergey Palcheh <minergenon@altlinux.org> 0.5-alt1
- new version 0.5

* Sun Feb 16 2025 Sergey Palcheh <minergenon@altlinux.org> 0.2-alt1
- Initial build for Sisyphus
