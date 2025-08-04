%define _unpackaged_files_terminate_build 1
%set_verify_elf_method skip
%global __find_debuginfo_files %nil

Name:    nvidia-fabricmanager-570
Version: 570.158.01
Release: alt1
Summary: Fabric Manager for NVSwitch based systems

License: NVIDIA 
URL:     http://www.nvidia.com
Group:   System/Kernel and hardware

Provides:       nvidia-fabricmanager = %{version}

#Source0-url: https://developer.download.nvidia.com/compute/nvidia-driver/redist/fabricmanager/linux-x86_64/fabricmanager-linux-x86_64-%{version}-archive.tar.xz
Source0: %name-%version-x86_64.tar
#Source1-url: https://developer.download.nvidia.com/compute/nvidia-driver/redist/fabricmanager/linux-sbsa/fabricmanager-linux-sbsa-%{version}-archive.tar.xz
Source1: %name-%version-aarch64.tar

ExclusiveArch: x86_64 aarch64

%description
%summary.

%prep
%ifarch x86_64
    tar -xf %SOURCE0
%endif
%ifarch aarch64
    tar -xf %SOURCE1
%endif

%build
#

%install
cd %name-%version-%_arch

mkdir -p %buildroot%_bindir \
         %buildroot%_datadir/nvidia/nvswitch \
         %buildroot%_libexecdir \
         %buildroot%_unitdir \
         %buildroot%_includedir \
         %buildroot%_sysconfdir/nvidia/nvswitch

cp -ar bin/*                   %buildroot%_bindir
cp -ar share/nvidia/nvswitch/* %buildroot%_datadir/nvidia/nvswitch
cp -ar etc/*                   %buildroot%_datadir/nvidia/nvswitch
cp -ar lib/*                   %buildroot%_libexecdir
cp -ar systemd/*               %buildroot%_unitdir
cp -ar include/*               %buildroot%_includedir
cp LICENSE third-party-notices.txt %_builddir

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE third-party-notices.txt
%attr(0755,root,root) %_bindir/nv-fabricmanager
%attr(0755,root,root) %_bindir/nvidia-fabricmanager-start.sh
%attr(0755,root,root) %_bindir/nvswitch-audit
%_datadir/nvidia/nvswitch
%config(noreplace) %_datadir/nvidia/nvswitch/fabricmanager.cfg
%_libexecdir/*
%_includedir/*
%_unitdir/nvidia-fabricmanager.service

%changelog
* Wed Jul 09 2025 Maxim Slipenko <maks1ms@altlinux.org> 570.158.01-alt1
- Initial build

