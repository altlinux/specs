
%define tbname         NVIDIA-Linux-x86
%define dirsuffix %nil
%ifarch x86_64
%define tbname         NVIDIA-Linux-x86_64
%define dirsuffix -no-compat32
%endif

%define nvidia_ml_sover 1
%define nvidia_ptxjitcompiler_sover 1
%define nvidia_cuda_sover 1
%define nvidia_opencl_sover 1
%define nvidia_egl_wayland_sover 1
%define nvidia_egl_wayland_libver 1.0.2
%define libnvidia_egl_wayland libnvidia-egl-wayland%nvidia_egl_wayland_sover

Name: nvidia_glx_src
Version: 390.25
Release: alt2%ubt

Source0: null
Source201: ftp://download.nvidia.com/XFree86/Linux-x86/%version/NVIDIA-Linux-x86-%version.run
Source202: ftp://download.nvidia.com/XFree86/Linux-x86_64/%version/NVIDIA-Linux-x86_64-%version-no-compat32.run

Source2: nvidia.xinf
Source100: nvidia_create_xinf

Patch1: alt-fix-build-kernel.patch
Patch2: alt-ignore-dma-remap.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: kernel-build-tools rpm-macros-alternatives
BuildRequires: libXext-devel libEGL-devel
BuildRequires: libwayland-client-devel libwayland-server-devel
#BuildRequires: libGLdispatch libGLX
ExclusiveArch: %ix86 x86_64
#ExcludeArch: ppc64 x86_64 ppc s390 s390x ia64



Group: System/Kernel and hardware
Summary: NVIDIA drivers and OpenGL libraries for XOrg X-server
Summary(ru_RU.UTF-8): Драйверы NVIDIA и библиотеки OpenGL для Х-сервера XOrg
Url: http://www.nvidia.com
License: NVIDIA
%description
Sources for nvidia_glx package

#TODO libnvidia-ptxjitcompiler.so
#TODO libnvidia-compiler.so
#TODO libnvidia-ml.so (?)

%package -n ocl-nvidia
Group: System/Libraries
Summary: nvidia library
Requires: libnvidia-opencl libnvidia-compiler
Requires: libnvidia-ptxjitcompiler
#Requires: libnvidia-ml
%description -n ocl-nvidia
nvidia OpenCL library

%package -n libnvidia-ptxjitcompiler
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-ptxjitcompiler = %version-%release
%description -n libnvidia-ptxjitcompiler
nvidia library

%package -n libnvidia-ml
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-ml = %version-%release
%description -n libnvidia-ml
nvidia library

%package -n libnvidia-compiler
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-compiler = %version-%release
%description -n libnvidia-compiler
nvidia library

%package -n libnvidia-cuda
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-cuda = %version-%release
%description -n libnvidia-cuda
nvidia CUDA library

%package -n libnvidia-opencl
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-opencl = %version-%release
Requires: ocl-icd
%description -n libnvidia-opencl
nvidia OpenCL library

%package -n libnvidia-fatbinaryloader
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-fatbinaryloader = %version-%release
%description -n libnvidia-fatbinaryloader
nvidia library

%prep
%setup -T -c -n %tbname-%version%dirsuffix
rm -rf %_builddir/%tbname-%version%dirsuffix
cd %_builddir
%ifarch x86_64
sh %SOURCE202 -x
%else
sh %SOURCE201 -x
%endif
cd %tbname-%version%dirsuffix

pushd kernel
#%patch1 -p1
%patch2 -p1
rm -rf precompiled
popd

%build


%install
%set_verify_elf_method textrel=relaxed

# install libraries
mkdir -p %buildroot/%_libdir/
install -m 0644 libnvidia-fatbinaryloader.so.%version %buildroot/%_libdir/
install -m 0644 libnvidia-opencl.so.%version %buildroot/%_libdir/
install -m 0644 libcuda.so.%version %buildroot/%_libdir/
install -m 0644 libnvidia-compiler.so.%version %buildroot/%_libdir/
install -m 0644 libnvidia-ptxjitcompiler.so.%version %buildroot/%_libdir/
install -m 0644 libnvidia-ml.so.%version %buildroot/%_libdir/
mkdir -p %buildroot/%_sysconfdir/OpenCL/vendors/
install -m 0644 nvidia.icd %buildroot/%_sysconfdir/OpenCL/vendors/

%files -n ocl-nvidia

%files -n libnvidia-compiler
%_libdir/libnvidia-compiler.so.%version

%files -n libnvidia-ptxjitcompiler
%_libdir/libnvidia-ptxjitcompiler.so.%version
%_libdir/libnvidia-ptxjitcompiler.so.%{nvidia_ptxjitcompiler_sover}

%files -n libnvidia-ml
%_libdir/libnvidia-ml.so.%version
%_libdir/libnvidia-ml.so.%{nvidia_ml_sover}

%files -n libnvidia-fatbinaryloader
%_libdir/libnvidia-fatbinaryloader.so.%version

%files -n libnvidia-cuda
%_libdir/libcuda.so.%{nvidia_cuda_sover}
%_libdir/libcuda.so.%version

%files -n libnvidia-opencl
%_libdir/libnvidia-opencl.so.%{nvidia_opencl_sover}
%_libdir/libnvidia-opencl.so.%version
%_sysconfdir/OpenCL/vendors/nvidia.icd

%changelog
* Mon Feb 19 2018 Oleg Solovyov <mcpain@altlinux.org> 390.25-alt2%ubt
- added pkgs:
libnvidia-cuda
libnvidia-compiler
libnvidia-ptxjitcompiler
libnvidia-ml

* Fri Feb 16 2018 Oleg Solovyov <mcpain@altlinux.org> 390.25-alt1%ubt
- init
