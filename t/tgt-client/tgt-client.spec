%define _unpackaged_files_terminate_build 1
%define tdlib_ver 1.8.29
%define tdlib_installdir target/tdlib

Name: tgt-client
Version: 1.0.0
Release: alt2

Summary: A simple TUI for Telegram
License: Apache-2.0 and MIT
Group: Networking/Instant messaging
Url: https://github.com/FedericoBruzzone/tgt
VCS: https://github.com/FedericoBruzzone/tgt

# Source-url: https://github.com/FedericoBruzzone/tgt/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar
Source2: tdlib-%tdlib_ver.tar
Patch1: alt-add-static-tdlib-build.patch
Patch2: alt-use-hardcoded-appname.patch

# tgt-client dependencies
BuildRequires(pre): rpm-macros-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: libssl-devel
BuildRequires: rust-cargo

# tdlib dependencies
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: zlib-devel

%description
TUI for Telegram written in Rust.

%prep
%setup -a1 -a2
%patch1 -p1
%patch2 -p1
%rust_prep
cat >> .cargo/config.toml <<EOF

[env]
LOCAL_TDLIB_PATH = "$PWD/tdlib/%tdlib_installdir"
EOF

%ifnarch x86_64
sed -i 's;\([[:space:]]\+\)#.*\(target_os = "linux"\).*;\1#[cfg(\2)];' \
    vendor/tdlib-rs/{,src/}build.rs 2>/dev/null
%endif

cargo-vendor-checksum --vendor vendor --all

%build
# build tdlib
pushd tdlib >/dev/null
mkdir -p %_cmake__builddir
%__cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_FLAGS="-O2 -g" \
    -DCMAKE_CXX_FLAGS="-O2 -g" \
    -DCMAKE_INSTALL_PREFIX="" \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -S . -B %_cmake__builddir \
    #
%cmake_build
DESTDIR=$PWD/%tdlib_installdir %__cmake --install %_cmake__builddir
popd

# build tgt
%rust_build --no-default-features --features static-tdlib

%install
%rust_install -- tgt
mv %buildroot%_bindir/tgt{,-bin}

mkdir -p %buildroot%_datadir/%name/config
install -pm 755 config/*.toml %buildroot%_datadir/%name/config/

cat > %buildroot%_bindir/tgt <<EOF
#!/bin/sh
if [[ -z \$HOME ]]; then
    echo "\`HOME\` environment variable is unset"
    exit 1
fi

tgt_conf_dir="\$HOME/.tgt/config"
if [[ ! -d \$tgt_conf_dir ]]; then
    mkdir -p \$tgt_conf_dir &&\\
    install -pm 644 %_datadir/%name/config/*.toml \$tgt_conf_dir/
fi
%_bindir/tgt-bin "\$@"
EOF
chmod +x %buildroot%_bindir/tgt

%files
%doc README.md CHANGELOG.md
%_bindir/tgt
%_bindir/tgt-bin
%_datadir/%name

%changelog
* Tue Mar 03 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0.0-alt2
- fix a crash during authorization (closes: 58018)

* Fri Feb 06 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0.0-alt1
- initial build for ALT Linux
