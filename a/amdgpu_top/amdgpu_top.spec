%define _unpackaged_files_terminate_build 1
%define git %nil

Name: amdgpu_top
Version: 0.11.0
Release: alt1

Summary: Tool that display AMD GPU utilization
Group: System/Configuration/Hardware
License: MIT
Url: https://github.com/Umio-Yasuno/amdgpu_top

Source0: %name-%version.tar

BuildRequires: libdrm-devel
BuildRequires: /proc rust rust-cargo rust-cargo-c rpm-macros-rust

# x86 fails to compile with type overflow errors
ExclusiveArch: x86_64 aarch64

%description
amdgpu_top is tool that display AMD GPU information gathered from performance
counters (GRBM, GRBM2), sensors, fdinfo, and AMDGPU driver.

%prep
%setup

mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/Umio-Yasuno/libdrm-amdgpu-sys-rs?rev=8d0029b4cf8f3b995728614f96c03f6e3dcf4f9e"]
git = "https://github.com/Umio-Yasuno/libdrm-amdgpu-sys-rs"
rev = "8d0029b4cf8f3b995728614f96c03f6e3dcf4f9e"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
strip = "none"
lto= "thin"
debug = "full"
EOF

%build
%rust_build

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -pm755 target/release/%name %buildroot%_bindir/
install -pm644 docs/%name.1 %buildroot%_man1dir/

%files
%doc README.md LICENSE AUTHORS
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Tue Sep 02 2025 L.A. Kostis <lakostis@altlinux.ru> 0.11.0-alt1
- 0.11.0.

* Fri May 30 2025 L.A. Kostis <lakostis@altlinux.ru> 0.10.5-alt1
- 0.10.5.

* Mon May 12 2025 L.A. Kostis <lakostis@altlinux.ru> 0.10.4-alt1.g136e5a1
- Initial build for ALTLinux.
