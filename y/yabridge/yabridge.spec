# Dependency versions match the upstream subprojects/*.wrap files.
%define bitsery_version 5.2.3
%define clap_version 1.1.9
%define function2_version 4.2.3
%define filesystem_version 1.5.14
%define tomlplusplus_version 3.4.0
%define vst3_version 3.7.7_build_19
%define vst3sdk_version %{vst3_version}-patched
%define snapshot 7529c2d67330f7507649e903ce90782b58153a95
%define snapshot_version 5.1.1-72-g7529c2d6
%define bitbridge_gcc 16
%define hostdir %_libexecdir/wine/yabridge
# Wine's winebuild needs native object files when linking Winelib hosts.
%define optflags_lto %nil
%remove_optflags -pipe
# Full stripping removes the Winelib CRT section markers from .dynsym.
%brp_strip_debug %hostdir/yabridge-host.exe.so %hostdir/yabridge-host-32.exe.so

Name: yabridge
Version: 5.1.1
Release: alt1.git20261108
Summary: Bridge for Windows audio plugins on Linux
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/robbert-vdh/yabridge
Vcs: https://github.com/robbert-vdh/yabridge
ExclusiveArch: x86_64 %ix86

# Source0-url: https://github.com/robbert-vdh/yabridge/archive/%snapshot.tar.gz
Source0: %name-%version.tar
Source1: %name-cargo-%version.tar
Source2: config.toml

# Source3-url: https://github.com/fraillt/bitsery/archive/refs/tags/v%bitsery_version.tar.gz
Source3: bitsery.tar

# Source4-url: https://github.com/free-audio/clap/archive/refs/tags/%clap_version.tar.gz
Source4: clap.tar

# Source5-url: https://github.com/Naios/function2/archive/refs/tags/%function2_version.tar.gz
Source5: function2.tar

# Source6-url: https://github.com/gulrak/filesystem/archive/refs/tags/v%filesystem_version.tar.gz
Source6: filesystem.tar

# Source7-url: https://github.com/marzer/tomlplusplus/archive/refs/tags/v%tomlplusplus_version.tar.gz
Source7: tomlplusplus.tar

# Source8-url: https://github.com/robbert-vdh/vst3sdk/archive/refs/tags/v%vst3sdk_version.tar.gz
Source8: vst3sdk.tar

# Source9-url: https://github.com/steinbergmedia/vst3_base/archive/refs/tags/v%vst3_version.tar.gz
Source9: vst3_base.tar

# Source10-url: https://github.com/steinbergmedia/vst3_pluginterfaces/archive/refs/tags/v%vst3_version.tar.gz
Source10: vst3_pluginterfaces.tar

# Source11-url: https://github.com/steinbergmedia/vst3_public_sdk/archive/refs/tags/v%vst3_version.tar.gz
Source11: vst3_public_sdk.tar

Patch0: yabridge-alt-winelib-clang.patch
Patch1: yabridge-alt-bitbridge-toolchain.patch
Patch2: yabridge-alt-private-paths.patch

BuildRequires(pre): rpm-macros-meson
%ifarch x86_64
BuildRequires(pre): rpm-macros-rust
%endif
BuildRequires: meson ninja-build cmake gcc-c++
BuildRequires: wine-devel-tools wine-devel
BuildRequires: asio-devel libxcb-devel libdbus-devel
Requires: wine
%ifarch x86_64
BuildRequires: rpm-build-rust
Requires: yabridgectl = %EVR
%endif

%description
Yabridge lets native 64-bit Linux audio hosts load 32- and 64-bit Windows VST2, VST3 and CLAP
plugins through Wine. It supports plugin groups for fast startup and
communication between plugin instances.

%ifarch x86_64
%package -n yabridgectl
Summary: Setup and management utility for yabridge
Group: Sound

%description -n yabridgectl
Command-line utility for registering Windows plugin directories and
synchronizing yabridge wrappers with the installed plugins.

%endif

%prep
%ifarch x86_64
%setup -a1 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11
%else
%setup -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11
%endif
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i -e 's|@ALT_LIBEXECDIR@|%hostdir|g' \
    src/common/process.cpp tools/yabridgectl/src/main.rs
sed -i -e 's|@ALT_LIBDIR@|%_libdir/%name|g' \
    src/chainloader/utils.cpp tools/yabridgectl/src/config.rs
cp -a subprojects/packagefiles/. subprojects/
%ifarch x86_64
install -Dm644 %SOURCE2 .cargo/config.toml
%endif
sed -i -e '/^  replace_string :/s/$/,/' \
    -e "/^  replace_string :/a\  fallback : '%snapshot_version'," \
    src/common/config/meson.build

%build
# The Wine host defines main. Wine's GUI startup code would add an undefined WinMain.
%ifarch x86_64
# Keep support for an externally built host32 in both native and Wine code.
%meson --cross-file=cross-wine.conf \
    --buildtype=release -Dbitbridge=false --unity=on --unity-size=4 \
    -Dcpp_args="-DWITH_BITBRIDGE" \
    -Dcpp_link_args=-mconsole \
    -Dbuild.cpp_args="%optflags -fno-gnu-unique -DWITH_BITBRIDGE"
%meson_build
%rust_build --locked
%else
cat > cross-alt.conf <<'EOF'
[properties]
bitbridge_gcc_dir = '/usr/lib/gcc/i586-alt-linux/%bitbridge_gcc'
EOF
%meson --cross-file=cross-wine.conf --cross-file=cross-alt.conf \
    --buildtype=release -Dbitbridge=true --unity=on --unity-size=4 \
    -Dcpp_link_args=-mconsole \
    -Dbuild.cpp_args="%optflags -fno-gnu-unique"
%meson_build yabridge-host-32
%endif

%install
%ifarch x86_64
install -Dm755 -t %buildroot%hostdir %{__builddir}/yabridge-host.exe
install -Dm644 -t %buildroot%hostdir %{__builddir}/yabridge-host.exe.so
install -Dm755 -t %buildroot%_libdir/%name %{__builddir}/libyabridge*.so
%rust_install yabridgectl
%else
install -Dm755 -t %buildroot%hostdir %{__builddir}/yabridge-host-32.exe
install -Dm644 -t %buildroot%hostdir %{__builddir}/yabridge-host-32.exe.so
sed -i 's|WINELOADER="wine"|WINELOADER="/usr/lib/wine/wine32"|' \
    %buildroot%hostdir/yabridge-host-32.exe
grep -Fq 'WINELOADER="/usr/lib/wine/wine32"' %buildroot%hostdir/yabridge-host-32.exe
%endif

%ifarch x86_64
%files
%doc COPYING README.md CHANGELOG.md
%hostdir/
%_libdir/%name/

%files -n yabridgectl
%doc COPYING tools/yabridgectl/README.md
%_bindir/yabridgectl
%else
%files
%doc COPYING
%hostdir/
%endif

%changelog
* Tue Nov 17 2026 Ivan Mazhukin <vanomj@altlinux.org> 5.1.1-alt1.git20261108
- Initial build for Sisyphus (upstream 5.1.1-72-g7529c2d6).
