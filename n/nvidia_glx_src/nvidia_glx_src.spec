
%define tbname         NVIDIA-Linux-x86
%define dirsuffix %nil
%ifarch x86_64
%define tbname         NVIDIA-Linux-x86_64
%define dirsuffix -no-compat32
%endif

%define nvidia_opencl_sover 1
%define nvidia_egl_wayland_sover 1
%define nvidia_egl_wayland_libver 1.0.2
%define libnvidia_egl_wayland libnvidia-egl-wayland%nvidia_egl_wayland_sover

# version-release
%define nv_version 390
%define nv_release 25
%define pkg_rel alt1%ubt

%define tbver %{nv_version}.%{nv_release}

Name: nvidia_glx_src
Version: 390.25
Release: alt1%ubt

Source0: null
Source201: ftp://download.nvidia.com/XFree86/Linux-x86/%tbver/NVIDIA-Linux-x86-%tbver.run
Source202: ftp://download.nvidia.com/XFree86/Linux-x86_64/%tbver/NVIDIA-Linux-x86_64-%tbver-no-compat32.run

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

%package -n ocl-nvidia
Group: System/Libraries
Summary: nvidia library
Requires: libnvidia-opencl
%description -n ocl-nvidia
nvidia OpenCL library

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
%setup -T -c -n %tbname-%tbver%dirsuffix
rm -rf %_builddir/%tbname-%tbver%dirsuffix
cd %_builddir
%ifarch x86_64
sh %SOURCE202 -x
%else
sh %SOURCE201 -x
%endif
cd %tbname-%tbver%dirsuffix

pushd kernel
#%patch1 -p1
%patch2 -p1
rm -rf precompiled
popd

%build


%install
%set_verify_elf_method textrel=relaxed

# install libraries
%__mkdir -p %buildroot/%_libdir/
%__install -m 0644 libnvidia-fatbinaryloader.so.%tbver %buildroot/%_libdir/
%__install -m 0644 libnvidia-opencl.so.%tbver %buildroot/%_libdir/
%__mkdir -p %buildroot/%_sysconfdir/OpenCL/vendors/
%__install -m 0644 nvidia.icd %buildroot/%_sysconfdir/OpenCL/vendors/

%files -n ocl-nvidia

%files -n libnvidia-fatbinaryloader
%_libdir/libnvidia-fatbinaryloader.so.%version

%files -n libnvidia-opencl
%_libdir/libnvidia-opencl.so.%{nvidia_opencl_sover}
%_libdir/libnvidia-opencl.so.%version
%_sysconfdir/OpenCL/vendors/nvidia.icd

%changelog
* Fri Feb 16 2018 Oleg Solovyov <mcpain@altlinux.org> 390.25-alt1%ubt
- init
