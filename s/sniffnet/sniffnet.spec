%define _unpackaged_files_terminate_build 1

Name: sniffnet
Version: 1.5.0
Release: alt1

Summary: Application to comfortably monitor your network traffic
License: Apache-2.0 or MIT
Group: Networking/Other
Url: https://sniffnet.net/
Vcs: https://github.com/GyulyVGC/sniffnet

Source0: %name-%version.tar
Source1: vendor.tar
Source2: cargo-vendor-config.py

Requires(post,preun): libcap-utils

BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libalsa-devel
BuildRequires: fontconfig-devel
BuildRequires: libpcap-devel
BuildRequires: desktop-file-utils

%description
%summary

%prep
%setup -a1
# Disable LTO entirely to avoid LLVM "out of memory" error on 32-bit
# machines (even thin LTO is too much for the limited address space).
%SOURCE2 --root "%buildroot%prefix" \
%ifarch i586 armh
    --opt-level=0 \
    --debuginfo=0 \
    --lto=false \
    --codegen-units=16 \
    --panic=abort \
%endif
    %nil

# allow patching vendored rust code
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/linux-raw-sys/.cargo-checksum.json

%build
cargo build %_smp_mflags --offline --release

%install
install -Dp target/release/%name -t %buildroot%_bindir
resources="resources/packaging/linux"
desktop-file-install --dir %buildroot%_desktopdir $resources/sniffnet.desktop
for icon in $resources/graphics/*; do
    resolution=$(basename $icon | grep -Eo "[[:digit:]]+x[[:digit:]]+")
    install -pDm644 "$icon" \
        %buildroot%_iconsdir/hicolor/$resolution/apps/%name.png
done

%post
setcap cap_net_raw,cap_net_admin=eip %_bindir/%name

%preun
setcap '' %_bindir/%name

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/%name.png
%doc README.md LICENSE*

%changelog
* Wed Apr 22 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.

* Tue Oct 07 2025 Andrey Kovalev <ded@altlinux.org> 1.4.1-alt1
- Updated to 1.4.1.

* Thu Aug 08 2024 Ivan A. Melnikov <iv@altlinux.org> 1.3.1-alt2
- Add patch that fixes linux-raw-sys C_char for loongarch64 (by k0tran@).

* Wed Aug 07 2024 Alexandr Shashkin <dutyrok@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.

* Tue May 07 2024 Alexandr Shashkin <dutyrok@altlinux.org> 1.3.0-alt1
- 1.1.3 -> 1.3.0.
- Added desktop file (Closes: 47273).

* Mon Jul 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus

