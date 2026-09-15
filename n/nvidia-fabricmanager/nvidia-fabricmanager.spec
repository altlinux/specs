%set_verify_elf_method skip
%global __find_debuginfo_files %nil

%define sover_nvfm 1
%define libnvfm libnvfm%sover_nvfm

%define archsuffix x86_64
%define srctar %SOURCE1
%ifarch aarch64
%define archsuffix sbsa
%define srctar %SOURCE2
%endif

# ALTBUG#60545
%filter_from_requires /^\/usr\/lib\/ld-linux-/d

Name:    nvidia-fabricmanager
Version: 595.91.07
Release: alt1

Group:   System/Kernel and hardware
Summary: Fabric Manager for NVSwitch based systems
License: NVIDIA 
URL:     http://www.nvidia.com

ExclusiveArch: x86_64 aarch64

Provides: nvidia-fabricmanager-570 = %{version}
Obsoletes: nvidia-fabricmanager-570 < %{version}
Requires: nvidia_glx_%version
Requires: %libnvfm > 0

#Source: https://developer.download.nvidia.com/compute/nvidia-driver/redist/fabricmanager/
Source1: fabricmanager-linux-x86_64-%{version}-archive.tar
Source2: fabricmanager-linux-sbsa-%{version}-archive.tar

%description
%summary.

%package -n %libnvfm
Group: System/Libraries
Summary: NVIDIA library
%description -n %libnvfm
NVIDIA library.

%prep
%setup -T -c -n fabricmanager-linux-%archsuffix-%version-archive
tar --strip-components=1 -xf %srctar

%install
mkdir -p %buildroot/{%_bindir,%_datadir/nvidia/nvswitch,%_libdir,%_unitdir,%_includedir,%_sysconfdir/nvidia/nvswitch}

install -m 0755 bin/*           %buildroot/%_bindir/
cp -ar share/nvidia/nvswitch/* %buildroot/%_datadir/nvidia/nvswitch
cp -ar etc/*                   %buildroot/%_datadir/nvidia/nvswitch
cp -ar lib/*                   %buildroot/%_libdir/
cp -ar systemd/*               %buildroot/%_unitdir/
cp -ar include/*               %buildroot/%_includedir/

%files
%doc LICENSE third-party-notices.txt
%_bindir/nv-fabricmanager
%_bindir/nvidia-fabricmanager-start.sh
%_bindir/nvswitch-audit
%_datadir/nvidia/nvswitch
%config(noreplace) %_datadir/nvidia/nvswitch/fabricmanager.cfg
%_includedir/*
%_unitdir/nvidia-fabricmanager.service

%files -n %libnvfm
%_libdir/libnvfm.so.*
%_libdir/libnvfm.so.%sover_nvfm

%changelog
* Thu Sep 03 2026 Sergey V Turchin <zerg@altlinux.org> 595.91.07-alt1
- new version
- update packaging

* Wed Jul 09 2025 Maxim Slipenko <maks1ms@altlinux.org> 570.158.01-alt1
- Initial build
