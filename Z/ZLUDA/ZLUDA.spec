%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define llvm_major_version 19
%define llvm_minor_version 1
%define llvm_version %llvm_major_version.%llvm_minor_version

%define zluda_dir %_libdir/ZLUDA

Name: ZLUDA
Version: 4
Release: alt2

Summary: CUDA on non-NVIDIA GPUs
License: Apache-2.0 or MIT
Group: Development/Other
Url: https://github.com/vosen/ZLUDA
Vcs: https://github.com/vosen/ZLUDA

ExclusiveArch: x86_64

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Source3: zluda_with.in
Patch0: %name-%version-alt.patch

Provides: zluda = %EVR

BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: llvm%llvm_version-devel
BuildRequires: hip-runtime-amd
BuildRequires: rocm-comgr-devel

%description
LUDA is a drop-in replacement for CUDA on non-NVIDIA GPU. ZLUDA allows
to run unmodified CUDA applications using non-NVIDIA GPUs with
near-native performance.

ZLUDA supports AMD Radeon RX 5000 series and newer GPUs (both desktop
and integrated).

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE2 .cargo/config.toml

%build
export LLVM_CONFIG="llvm-config-%llvm_major_version"
cargo build --release %{?_smp_mflags} --offline -p zluda -p zluda_ml

%install
for lib in $(find target/release -maxdepth 1 -type f -executable -name '*.so'); do
    install -vD $lib -t %buildroot%zluda_dir
done

# make some symlinks for compatibility
pushd %buildroot%zluda_dir/
    ln -vs libnvcuda.so libcuda.so
    ln -vs libnvcuda.so libcuda.so.1
    ln -vs libnvml.so libnvidia-ml.so
    ln -vs libnvml.so libnvidia-ml.so.1
popd

# create a script for convenient use of the library
mkdir -p %buildroot%_bindir
sed 's|@ZLUDA_DIR@|%zluda_dir|' %SOURCE3 > %buildroot%_bindir/zluda_with
chmod -v ugo+x %buildroot%_bindir/zluda_with

%files
%doc README.md
%zluda_dir/
%_bindir/zluda_with

%changelog
* Mon Mar 17 2025 Anton Zhukharev <ancieg@altlinux.org> 4-alt2
- Built using LLVM 19.1.

* Mon Mar 17 2025 Anton Zhukharev <ancieg@altlinux.org> 4-alt1
- Built for ALT Sisyphus.

