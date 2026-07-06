%set_verify_elf_method textrel=relaxed
%ifndef _unitdir
%define _unitdir   /usr/lib/systemd/system
%endif

%define tbname         NVIDIA-Linux-x86_64
%ifarch aarch64
%define tbname         NVIDIA-Linux-aarch64
%endif
%define dirsuffix %nil

%define nvidia_sover 1
%define nvvm_sover 4

%ifarch %ix86
%define subd ./32
%else
%define subd ./
%endif

%define nv_version 595
%define nv_release 84
%define nv_minor   %nil
%define pkg_rel alt1
%define nv_version_full %nv_version.%nv_release.%nv_minor
%if "%nv_minor" == "%nil"
%define nv_version_full %nv_version.%nv_release
%endif
Name: nvidia_glx_libs_%nv_version_full
Version: %nv_version_full
Release: %pkg_rel

ExclusiveArch: %ix86 x86_64 aarch64

Source0: null
Source201: http://http.download.nvidia.com/XFree86/Linux-x86_64/%version/%tbname-%version.run
Source202: http://http.download.nvidia.com/XFree86/Linux-x86_64/%version/%tbname-%version.run
Patch1: systemd-powerd-no-fail.patch

BuildRequires: rpm-macros-alternatives
BuildRequires: libXext-devel libEGL-devel
BuildRequires: libwayland-client-devel libwayland-server-devel
#BuildRequires: libGLdispatch libGLX

Group: System/Kernel and hardware
Summary: NVIDIA drivers and OpenGL libraries for XOrg X-server
Summary(ru_RU.UTF-8): Драйверы NVIDIA и библиотеки OpenGL для Х-сервера XOrg
Url: http://www.nvidia.com
License: NVIDIA
%description
Sources for nvidia_glx package

%package -n ocl-nvidia
Group: System/Libraries
#BuildArch: noarch
Summary: nvidia library
Requires: nvidia_glx_common
%description -n ocl-nvidia
nvidia OpenCL library

%package -n libnvidia-ptxjitcompiler
Group: System/Libraries
Summary: nvidia library
BuildArch: noarch
%description -n libnvidia-ptxjitcompiler
nvidia library

%package -n libnvidia-ml
Group: System/Libraries
Summary: nvidia library
%description -n libnvidia-ml
nvidia library

%package -n libcuda
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-cuda = %EVR
Obsoletes: libnvidia-cuda < %EVR
%description -n libcuda
nvidia CUDA library

%package -n libcudadebugger
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-cuda = %EVR
Obsoletes: libnvidia-cuda < %EVR
%description -n libcudadebugger
nvidia CUDA debugger library

%package -n libnvidia-opencl
Group: System/Libraries
Summary: nvidia library
Requires: ocl-icd
Requires: libnvidia-nvvm
%description -n libnvidia-opencl
nvidia OpenCL library

%package -n libnvcuvid
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-nvcuvid = %version-%release
#BuildArch: noarch
%description -n libnvcuvid
nvidia library

%package -n libnvoptix
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-nvcuvid = %version-%release
%description -n libnvoptix
nvidia library

%package -n libnvidia-encode
Group: System/Libraries
Summary: nvidia library
%description -n libnvidia-encode
nvidia library

%package -n libnvidia-nvvm
Group: System/Libraries
Summary: nvidia library
%description -n libnvidia-nvvm
nvidia library

%package -n libnvidia-nvvm70
Group: System/Libraries
Summary: nvidia library
%description -n libnvidia-nvvm70
nvidia library

%package -n libnvidia-ngx
Group: System/Libraries
Summary: nvidia library
%description -n libnvidia-ngx
nvidia library

%package -n libnvidia-fbc
Group: System/Libraries
Summary: nvidia library
%description -n libnvidia-fbc
nvidia library

%package -n libnvidia-api
Group: System/Libraries
Summary: nvidia library
%description -n libnvidia-api
nvidia library

%package -n libnvidia-opticalflow
Group: System/Libraries
Summary: nvidia library
%description -n libnvidia-opticalflow
nvidia library

%package -n libnvidia-sandboxutils
Group: System/Libraries
Summary: nvidia library
#BuildArch: noarch
%description -n libnvidia-sandboxutils
nvidia library

%package -n libnvidia-vksc-core
Group: System/Libraries
Summary: nvidia library
%description -n libnvidia-vksc-core
nvidia library

%package -n nvidia-smi
Group: System/Libraries
Summary: NVIDIA System Management Interface program
%description -n nvidia-smi
nvidia-smi (also NVSMI) provides monitoring and management capabilities for each of
NVIDIA's Tesla, Quadro, GRID and GeForce devices from Fermi and higher architecture families.

%package -n nvidia-powerd
Group: System/Libraries
Summary: NVIDIA Dynamic Boost daemon
Requires: nvidia_glx_common
%description -n nvidia-powerd
Daemon that manages the Dynamic Boost feature on compatible NVIDIA GPUs.

%prep
%setup -T -c -n %tbname-%version%dirsuffix
rm -rf %_builddir/%tbname-%version%dirsuffix
cd %_builddir
%ifarch aarch64
sh %SOURCE202 -x
%else
sh %SOURCE201 -x
%endif
cd %tbname-%version%dirsuffix
%patch1 -p1

pushd kernel
rm -rf precompiled
popd

%build
%install
mkdir -p %buildroot/%_libdir/
# install fake libraries
ln -s libnvidianull.so %buildroot/%_libdir/libnvidia-ml.so
# install libraries
install -m 0644 %subd/libcuda.so.%version %buildroot/%_libdir/
ln -s libcuda.so.%version %buildroot/%_libdir/libcuda.so
#install -m 0644 %subd/libnvidia-ptxjitcompiler.so.%version %buildroot/%_libdir/
#install -m 0644 %subd/libnvidia-ml.so.%version %buildroot/%_libdir/
#install -m 0644 %subd/libnvcuvid.so.%version %buildroot/%_libdir/
%ifarch %ix86
ln -s libnvidianull.so %buildroot/%_libdir/libnvcuvid.so
%endif
#install -m 0644 %subd/libnvidia-encode.so.%version %buildroot/%_libdir/
%ifarch x86_64
#install -m 0644 %subd/libnvidia-sandboxutils.so.%version %buildroot/%_libdir/
%endif
# all 64-bit
%if "%_lib" != "lib"
install -m 0644 %subd/libnvoptix.so.%version %buildroot/%_libdir/
# install programs
mkdir -p %buildroot/%_bindir/
install -m 0755 nvidia-smi %buildroot/%_bindir/
mkdir -p %buildroot/%_man1dir/
install -m 0644 nvidia-smi.1.gz %buildroot/%_man1dir/
# install nvidia-powerd
install -m 0755 nvidia-powerd %buildroot/%_bindir/
mkdir -p %buildroot/%_unitdir/
install -m 0644 systemd/system/nvidia-powerd.service %buildroot/%_unitdir/
mkdir -p %buildroot/%_datadir/nvidia/nvidia-powerd/
if [ -e dlsnetparams.csv ] ; then
    install -m 0444 dlsnetparams.csv %buildroot/%_datadir/nvidia/nvidia-powerd/
fi
mkdir -p  %buildroot/%_datadir/dbus-1/system.d/
install -m 0644 nvidia-dbus.conf %buildroot/%_datadir/dbus-1/system.d/nvidia-dbus.conf
%endif

%files -n ocl-nvidia
%files -n libnvidia-ptxjitcompiler
#%_libdir/libnvidia-ptxjitcompiler.so.%version
#%_libdir/libnvidia-ptxjitcompiler.so.%nvidia_sover
%files -n libcuda
%_libdir/libcuda.so
%_libdir/libcuda.so.%nvidia_sover
%_libdir/libcuda.so.%version
%files -n libnvidia-ml
%_libdir/libnvidia-ml.so
#%_libdir/libnvidia-ml.so.%version
#%_libdir/libnvidia-ml.so.%nvidia_sover
%files -n libnvcuvid
%ifarch %ix86
%_libdir/libnvcuvid.so
%endif
#%_libdir/libnvcuvid.so.%nvidia_sover
#%_libdir/libnvcuvid.so.%version
#%files -n libnvidia-encode
#%_libdir/libnvidia-encode.so.%nvidia_sover
#%_libdir/libnvidia-encode.so.%version
%ifarch x86_64
%files -n libnvidia-sandboxutils
#%_libdir/libnvidia-sandboxutils.so.%nvidia_sover
#%_libdir/libnvidia-sandboxutils.so.%version
%endif
%if "%_lib" != "lib"
%files -n libnvoptix
%_libdir/libnvoptix.so.%nvidia_sover
%_libdir/libnvoptix.so.%version
%files -n nvidia-smi
%_bindir/nvidia-smi
%_man1dir/nvidia-smi.1.*
%files -n nvidia-powerd
%_datadir/dbus-1/system.d/nvidia-dbus.conf
%_bindir/nvidia-powerd
%_unitdir/nvidia-powerd.service
%_datadir/nvidia/nvidia-powerd/
%endif

%changelog
* Mon Jul 06 2026 Sergey V Turchin <zerg@altlinux.org> 595.84-alt1
- new version

* Tue Jun 02 2026 Sergey V Turchin <zerg@altlinux.org> 595.80-alt1
- new version
- return libcuda.so

* Tue Jun 02 2026 Sergey V Turchin <zerg@altlinux.org> 595.71.05-alt3
- don't package libcuda.so

* Thu May 28 2026 Sergey V Turchin <zerg@altlinux.org> 595.71.05-alt2
- don't package libnvidia-ml.so.*

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 595.71.05-alt1
- new version

* Wed May 06 2026 Sergey V Turchin <zerg@altlinux.org> 595.58.03-alt4
- package libcuda.so

* Fri Apr 24 2026 Sergey V Turchin <zerg@altlinux.org> 595.58.03-alt3
- package empty libnvidia-ptxjitcompiler, libnvcuvid and libnvidia-sandboxutils

* Thu Apr 23 2026 Sergey V Turchin <zerg@altlinux.org> 595.58.03-alt2
- package fake libnvidia-ml.so
- don't package libnvidia-encode

* Wed Apr 08 2026 Sergey V Turchin <zerg@altlinux.org> 595.58.03-alt1
- new version

* Mon Mar 16 2026 Sergey V Turchin <zerg@altlinux.org> 580.142-alt1
- new version

* Mon Feb 02 2026 Sergey V Turchin <zerg@altlinux.org> 580.126.09-alt1
- new version

* Mon Dec 08 2025 Sergey V Turchin <zerg@altlinux.org> 580.95.05-alt2
- don't fail nvidia-powerd service

* Fri Oct 10 2025 Sergey V Turchin <zerg@altlinux.org> 580.95.05-alt1
- new version

* Fri Sep 26 2025 Sergey V Turchin <zerg@altlinux.org> 580.82.09-alt1
- new version

* Mon Sep 08 2025 Sergey V Turchin <zerg@altlinux.org> 580.82.07-alt1
- new version

* Thu Aug 21 2025 Sergey V Turchin <zerg@altlinux.org> 580.76.05-alt1
- new version

* Thu Jul 24 2025 Sergey V Turchin <zerg@altlinux.org> 570.169-alt2
- package libnvidia-sandboxutils (closes: 55287)

* Mon Jun 30 2025 Sergey V Turchin <zerg@altlinux.org> 570.169-alt1
- new version

* Fri May 23 2025 Sergey V Turchin <zerg@altlinux.org> 570.153.02-alt1
- new version

* Thu Apr 03 2025 Sergey V Turchin <zerg@altlinux.org> 570.133.07-alt1
- new version

* Tue Mar 25 2025 Sergey V Turchin <zerg@altlinux.org> 570.124.04-alt2
- package libnvidia-vksc-core

* Tue Mar 04 2025 Sergey V Turchin <zerg@altlinux.org> 570.124.04-alt1
- new version

* Tue Jan 28 2025 Sergey V Turchin <zerg@altlinux.org> 550.144.03-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 550.142-alt1
- new version

* Thu Dec 12 2024 Sergey V Turchin <zerg@altlinux.org> 550.135-alt3
- fix package nvidia-dbus.conf for nvidia-powerd

* Mon Dec 02 2024 Sergey V Turchin <zerg@altlinux.org> 550.135-alt2
- package nvidia-powerd

* Fri Nov 22 2024 Sergey V Turchin <zerg@altlinux.org> 550.135-alt1
- new version

* Sat Nov 02 2024 Sergey V Turchin <zerg@altlinux.org> 550.127.05-alt1
- new version

* Tue Oct 08 2024 Sergey V Turchin <zerg@altlinux.org> 550.120-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 550.107.02-alt1
- new version

* Thu Jun 06 2024 Sergey V Turchin <zerg@altlinux.org> 550.90.07-alt1
- new version

* Sun Apr 28 2024 Sergey V Turchin <zerg@altlinux.org> 550.78-alt1
- new version

* Mon Mar 25 2024 Sergey V Turchin <zerg@altlinux.org> 550.67-alt1
- new version

* Thu Feb 29 2024 Sergey V Turchin <zerg@altlinux.org> 550.54.14-alt1
- new version

* Wed Jan 31 2024 Sergey V Turchin <zerg@altlinux.org> 535.154.05-alt2
- package libnvidia-ml.so against bug#49236

* Tue Jan 23 2024 Sergey V Turchin <zerg@altlinux.org> 535.154.05-alt1
- new version

* Mon Dec 25 2023 Sergey V Turchin <zerg@altlinux.org> 535.146.02-alt1
- new version

* Thu Nov 23 2023 Mikhail Tergoev <fidel@altlinux.org> 535.129.03-alt1.1
- NMU: fixing the work of CUDA rendering in DaVinci Resolve without nvidia-cuda-toolkit

* Fri Nov 03 2023 Sergey V Turchin <zerg@altlinux.org> 535.129.03-alt1
- new version

* Tue Oct 10 2023 Sergey V Turchin <zerg@altlinux.org> 535.113.01-alt1
- new version

* Tue Sep 19 2023 Sergey V Turchin <zerg@altlinux.org> 535.104.05-alt1
- new version

* Wed Jul 19 2023 Sergey V Turchin <zerg@altlinux.org> 535.86.05-alt1
- new version

* Thu Jun 29 2023 Sergey V Turchin <zerg@altlinux.org> 535.54.03-alt1
- new version

* Thu Jun 29 2023 Sergey V Turchin <zerg@altlinux.org> 525.116.04-alt3
- don't package wine dlls

* Mon Jun 05 2023 Sergey V Turchin <zerg@altlinux.org> 525.116.04-alt2
- make nvidia-wine package (closes: 46378)

* Thu May 25 2023 Sergey V Turchin <zerg@altlinux.org> 525.116.04-alt1
- new version

* Wed May 10 2023 Sergey V Turchin <zerg@altlinux.org> 525.105.17-alt2
- package libnvidia-nvvm

* Tue Apr 11 2023 Sergey V Turchin <zerg@altlinux.org> 525.105.17-alt1
- new version
- package libcudadebugger
- package nvidia-smi

* Fri Feb 10 2023 Sergey V Turchin <zerg@altlinux.org> 525.89.02-alt1
- new version

* Wed Jan 25 2023 Sergey V Turchin <zerg@altlinux.org> 525.85.05-alt1
- new version

* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 525.78.01-alt1
- new version

* Fri Nov 25 2022 Sergey V Turchin <zerg@altlinux.org> 515.86.01-alt1
- new version
- package libnvoptix and libnvidia-ngx

* Tue Oct 25 2022 Sergey V Turchin <zerg@altlinux.org> 515.76-alt1
- new version

* Tue Aug 30 2022 Sergey V Turchin <zerg@altlinux.org> 515.65.01-alt1
- new version

* Fri Jul 08 2022 Sergey V Turchin <zerg@altlinux.org> 515.57-alt1
- new version

* Thu May 05 2022 Sergey V Turchin <zerg@altlinux.org> 510.68.02-alt1
- new version

* Fri Apr 15 2022 Sergey V Turchin <zerg@altlinux.org> 510.60.02-alt1
- new version

* Fri Apr 08 2022 Sergey V Turchin <zerg@altlinux.org> 470.103.01-alt2
- dont package libnvidia-compiler

* Wed Feb 09 2022 Sergey V Turchin <zerg@altlinux.org> 470.103.01-alt1
- new version

* Mon Dec 27 2021 Sergey V Turchin <zerg@altlinux.org> 470.94-alt1
- new version

* Mon Nov 15 2021 Sergey V Turchin <zerg@altlinux.org> 470.86-alt1
- new version

* Fri Nov 12 2021 Sergey V Turchin <zerg@altlinux.org> 470.82.00-alt1
- new version

* Mon Sep 27 2021 Sergey V Turchin <zerg@altlinux.org> 470.74-alt1
- new version

* Fri Sep 03 2021 Sergey V Turchin <zerg@altlinux.org> 470.63.01-alt1
- new version

* Tue Aug 24 2021 Sergey V Turchin <zerg@altlinux.org> 470.57.02-alt2
- fix build requires

* Tue Jul 20 2021 Sergey V Turchin <zerg@altlinux.org> 470.57.02-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 460.84-alt1
- new version

* Fri May 14 2021 Sergey V Turchin <zerg@altlinux.org> 460.80-alt1
- new version

* Mon Apr 26 2021 Sergey V Turchin <zerg@altlinux.org> 460.73.01-alt1
- new version

* Wed Mar 03 2021 Sergey V Turchin <zerg@altlinux.org> 460.56-alt1
- new version

* Fri Feb 19 2021 Sergey V Turchin <zerg@altlinux.org> 460.39-alt1
- new version

* Thu Jan 14 2021 Sergey V Turchin <zerg@altlinux.org> 460.32.03-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 450.80.02-alt2
- add aarch64 part

* Thu Oct 01 2020 Sergey V Turchin <zerg@altlinux.org> 450.80.02-alt1
- new version

* Fri Jul 24 2020 Sergey V Turchin <zerg@altlinux.org> 450.57-alt1
- new version

* Fri Jul 17 2020 Sergey V Turchin <zerg@altlinux.org> 440.100-alt1
- new version

* Thu Apr 16 2020 Sergey V Turchin <zerg@altlinux.org> 440.82-alt1
- new version

* Mon Feb 10 2020 Sergey V Turchin <zerg@altlinux.org> 440.59-alt1
- new version

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 440.44-alt1
- new version
- package libnvidia-encode, libnvcuvid

* Tue Nov 26 2019 Sergey V Turchin <zerg@altlinux.org> 440.36-alt1
- new version

* Wed Nov 06 2019 Sergey V Turchin <zerg@altlinux.org> 440.31-alt1
- new version

* Mon Sep 30 2019 Sergey V Turchin <zerg@altlinux.org> 430.50-alt1
- new version

* Fri Jul 12 2019 Sergey V Turchin <zerg@altlinux.org> 430.34-alt1
- new version

* Thu Mar 14 2019 Sergey V Turchin <zerg@altlinux.org> 410.104-alt1
- new version

* Wed Jan 30 2019 Sergey V Turchin <zerg@altlinux.org> 410.93-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 410.78-alt1
- new version

* Wed Dec 05 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt1
- new version

* Thu Sep 20 2018 Sergey V Turchin <zerg@altlinux.org> 390.87-alt1
- new version

* Fri Jun 08 2018 Sergey V Turchin <zerg@altlinux.org> 390.67-alt1
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 390.59-alt1
- new version

* Thu Apr 19 2018 Sergey V Turchin <zerg@altlinux.org> 390.48-alt1
- new version

* Wed Feb 21 2018 Oleg Solovyov <mcpain@altlinux.org> 390.25-alt3
- require libnvidia-ml

* Mon Feb 19 2018 Oleg Solovyov <mcpain@altlinux.org> 390.25-alt2
- added pkgs:
libnvidia-cuda
libnvidia-compiler
libnvidia-ptxjitcompiler
libnvidia-ml

* Fri Feb 16 2018 Oleg Solovyov <mcpain@altlinux.org> 390.25-alt1
- init
