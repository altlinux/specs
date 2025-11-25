%define _unpackaged_files_terminate_build 1
%global __find_debuginfo_files %nil

%define oname nvidia-cuda-toolkit
%define nsight_compute_ver 2025.2.1
%define nsight_sys_ver 2025.1.3
%define min_driver_ver 575.57.08
%define cuda_release 12
%define cuda_major 9
%define cuda_minor 1

%if "%cuda_minor" != "%nil"
%define cuda_version_full %cuda_release.%cuda_major.%cuda_minor
%else
%define cuda_version_full %cuda_release.%cuda_major
%endif

%add_verify_elf_skiplist %_datadir/nvidia-cuda-toolkit/*
%add_verify_elf_skiplist %_libdir/nsight-systems-%nsight_sys_ver/*
%add_verify_elf_skiplist %_libdir/nsight-compute-%nsight_compute_ver/*

%add_findreq_skiplist %_libdir/nsight-systems-%nsight_sys_ver/*
%add_findprov_skiplist %_libdir/nsight-systems-%nsight_sys_ver/*
%add_findreq_skiplist %_libdir/nsight-compute-%nsight_compute_ver/*
%add_findprov_skiplist %_libdir/nsight-compute-%nsight_compute_ver/*

%ifarch aarch64
%define name_arch aarch64
%add_findreq_skiplist %_libdir/gds/tools/gds*
%add_findreq_skiplist %_bindir/cuda-gdb*
%else
%define name_arch x86_64
%add_findreq_skiplist %_libdir/nvvp/*
%add_findprov_skiplist %_libdir/nvvp/*
%endif

Name: nvidia_cuda_toolkit_%{cuda_version_full}_%name_arch
Version: %cuda_version_full
Release: alt1

Summary: NVIDIA CUDA Toolkit libraries
Summary(ru_RU.UTF-8): Библиотеки NVIDIA CUDA Toolkit

License: NVIDIA
Group: System/Libraries
Url: http://www.nvidia.com


Source1: %{name}.tar.xz
Source2: pkgconfig.tar.xz

Source10: nvidia-nsight-compute.desktop
Source11: nvidia-nsight-systems.desktop
Source12: nvidia-visual-profiler.desktop

Source20: ncu-ui.png
Source21: nsys-ui.png
Source22: nvvp.png

BuildRequires(pre): rpm-build-python3

BuildRequires: libcuda >= %min_driver_ver
BuildRequires: libibverbs librdmacm libGL libGLU libfreeglut libibumad ocl-icd-devel libnuma
BuildRequires: libglvnd-devel gcc-c++ libvdpau-devel tbb-devel
BuildRequires: /usr/bin/convert chrpath
BuildRequires: python3-dev

ExclusiveArch: x86_64

%description
NVIDIA CUDA is a general purpose parallel computing architecture
that leverages the parallel compute engine in NVIDIA graphics
processing units (GPUs) to solve many complex computational problems
in a fraction of the time required on a CPU. It includes the CUDA
Instruction Set Architecture (ISA) and the parallel compute engine in
the GPU. To program to the CUDA architecture, developers can, today,
use C++, one of the most widely used high-level programming languages,
which can then be run at great performance on a CUDA enabled
processor. Support for other languages, like FORTRAN, Python or Java,
is available from third parties.

This package contains the libraries and attendant files needed to run
programs that make use of CUDA.

%package -n nvidia-cuda-toolkit
Group: System/Libraries
Summary: nvidia library
Requires: libcuda >= %min_driver_ver
Requires: libglut libGLU nvidia-modprobe
Requires: libibverbs librdmacm libnuma
%description -n nvidia-cuda-toolkit
NVIDIA CUDA Toolkit base files.

%package -n nvidia-cuda-devel
Group: Development/Other
Summary: NVIDIA CUDA development files
Requires: nvidia-cuda-toolkit = %EVR
Requires: libglvnd-devel ocl-icd-devel gcc-c++ libvdpau-devel tbb-devel
%description -n nvidia-cuda-devel
NVIDIA CUDA development files.

%package -n nvidia-cuda-devel-static
Group: Development/Other
Summary: NVIDIA CUDA static library
Requires: nvidia-cuda-devel = %EVR
%description -n nvidia-cuda-devel-static
NVIDIA CUDA static library.

%package -n nvidia-cuda-gdb
Group: System/Libraries
Summary: NVIDIA CUDA Debugger (GDB)
%description -n nvidia-cuda-gdb
NVIDIA CUDA Debugger (GDB)

%package -n libcublaslt
Group: System/Libraries
Summary: NVIDIA cuBLASLt Library
Provides: libcublasLt.so.12(libcublasLt.so.12)(64bit)
%description -n libcublaslt
NVIDIA cuBLASLt Library.

%package -n libcublas
Group: System/Libraries
Summary: NVIDIA cuBLAS Library
Provides: libcublas.so.12(libcublas.so.12)(64bit)
%description -n libcublas
NVIDIA cuBLAS Library.

%package -n libcudart
Group: System/Libraries
Summary: NVIDIA CUDA Runtime Library
Provides: libcudart.so.12(libcudart.so.12)(64bit)
%description -n libcudart
NVIDIA CUDA Runtime Library.

%package -n libcufft
Group: System/Libraries
Summary: NVIDIA cuFFT Library
Provides: libcufft.so.11(libcufft.so.11)(64bit)
%description -n libcufft
NVIDIA cuFFT Library.

%package -n libcufftw
Group: System/Libraries
Summary: NVIDIA cuFFTW Library
Provides: libcufftw.so.11(libcufftw.so.11)(64bit)
%description -n libcufftw
NVIDIA cuFFTW Library.

%package -n libcufile-rdma
Group: System/Libraries
Summary: GPUDirect Storage cuFile RDMA runtime library
%description -n libcufile-rdma
GPUDirect Storage cuFile RDMA runtime library.

%package -n libcufile
Group: System/Libraries
Summary: GPUDirect Storage cuFile runtime library
%description -n libcufile
GPUDirect Storage cuFile runtime library.

%package -n libcufile-devel
Group: Development/Other
Summary: GPUDirect Storage - development files
%description -n libcufile-devel
GPUDirect Storage - development files

%package -n libcupti
Group: System/Libraries
Summary: NVIDIA CUDA Profiler Tools Interface runtime library
Provides: libcupti.so.12(libcupti.so.12)(64bit)
%description -n libcupti
NVIDIA CUDA Profiler Tools Interface runtime library.

%package -n libcupti-devel
Group: Development/Other
Summary: NVIDIA CUDA Profiler Tools Interface development files
%description -n libcupti-devel
NVIDIA CUDA Profiler Tools Interface development files

%package -n libcurand
Group: System/Libraries
Summary: NVIDIA cuRAND Library
Provides: libcurand.so.10(libcurand.so.10)(64bit)
%description -n libcurand
NVIDIA cuRAND Library.

%package -n libcusolvermg
Group: System/Libraries
Summary: NVIDIA cuSOLVERmg Library
Provides: libcusolverMg.so.11(libcusolverMg.so.11)(64bit)
%description -n libcusolvermg
NVIDIA cuSOLVERmg Library.

%package -n libcusolver
Group: System/Libraries
Summary: NVIDIA cuSOLVER Library
Provides: libcusolver.so.11(libcurand.so.11)(64bit)
%description -n libcusolver
NVIDIA cuSOLVER Library.

%package -n libcusparse
Group: System/Libraries
Summary: NVIDIA cuSPARSE Library
Provides: libcusparse.so.12(libcusparse.so.12)(64bit)
%description -n libcusparse
NVIDIA cuSPARSE Library.

%package -n libnppc
Group: System/Libraries
Summary: NVIDIA Performance Primitives core runtime library
Provides: libnppc.so.12(libnppc.so.12)(64bit)
%description -n libnppc
NVIDIA Performance Primitives core runtime library.

%package -n libnppial
Group: System/Libraries
Summary: NVIDIA Performance Primitives lib for Image Arithmetic and Logic
Provides: libnppial.so.12(libnppial.so.12)(64bit)
%description -n libnppial
NVIDIA Performance Primitives lib for Image Arithmetic and Logic.

%package -n libnppicc
Group: System/Libraries
Summary: NVIDIA Performance Primitives lib for Image Color Conversion
Provides: libnppicc.so.12(libnppicc.so.12)(64bit)
%description -n libnppicc
NVIDIA Performance Primitives lib for Image Color Conversion.

%package -n libnppidei
Group: System/Libraries
Summary: NVIDIA Performance Primitives lib for Image Data Exchange and Initialization
Provides: libnppidei.so.12(libnppidei.so.12)(64bit)
%description -n libnppidei
NVIDIA Performance Primitives lib for Image Data Exchange and Initialization.

%package -n libnppif
Group: System/Libraries
Summary: NVIDIA Performance Primitives lib for Image Filters
Provides: libnppif.so.12(libnppif.so.12)(64bit)
%description -n libnppif
NVIDIA Performance Primitives lib for Image Filters.

%package -n libnppig
Group: System/Libraries
Summary: NVIDIA Performance Primitives lib for Image Geometry transforms
Provides: libnppig.so.12(libnppig.so.12)(64bit)
%description -n libnppig
NVIDIA Performance Primitives lib for Image Geometry transforms.

%package -n libnppim
Group: System/Libraries
Summary: NVIDIA Performance Primitives lib for Image Morphological operations
Provides: libnppim.so.12(libnppim.so.12)(64bit)
%description -n libnppim
NVIDIA Performance Primitives lib for Image Morphological operations.

%package -n libnppist
Group: System/Libraries
Summary: NVIDIA Performance Primitives lib for Image Statistics
Provides: libnppist.so.12(libnppist.so.12)(64bit)
%description -n libnppist
NVIDIA Performance Primitives lib for Image Statistics.

%package -n libnppisu
Group: System/Libraries
Summary: NVIDIA Performance Primitives lib for Image Support
Provides: libnppisu.so.12(libnppisu.so.12)(64bit)
%description -n libnppisu
NVIDIA Performance Primitives lib for Image Support.

%package -n libnppitc
Group: System/Libraries
Summary: NVIDIA Performance Primitives lib for Image Threshold and Compare
Provides: libnppitc.so.12(libnppitc.so.12)(64bit)
%description -n libnppitc
NVIDIA Performance Primitives lib for Image Threshold and Compare.

%package -n libnpps
Group: System/Libraries
Summary: NVIDIA Performance Primitives for signal processing runtime library
Provides: libnpps.so.12(libnpps.so.12)(64bit)

%description -n libnpps
NVIDIA Performance Primitives for signal processing runtime library.

%package -n libnvblas
Group: System/Libraries
Summary: NVBLAS runtime library
Provides: libnvblas.so.12(libnvblas.so.12)(64bit)
%description -n libnvblas
NVBLAS runtime library.

%package -n libnvjitlink
Group: System/Libraries
Summary: NVIDIA Compiler JIT LTO Library
Provides: libnvJitLink.so.12(libnvJitLink.so.12)(64bit)
%description -n libnvjitlink
NVIDIA Compiler JIT LTO Library.

%package -n libnvjpeg
Group: System/Libraries
Summary: NVIDIA JPEG library (nvJPEG)
Provides: libnvjpeg.so.12(libnvjpeg.so.12)(64bit)
%description -n libnvjpeg
NVIDIA JPEG library (nvJPEG).

%package -n libnvrtc-builtins
Group: System/Libraries
Summary: CUDA Runtime Compilation (NVIDIA NVRTC Builtins Library)
%description -n libnvrtc-builtins
CUDA Runtime Compilation (NVIDIA NVRTC Builtins Library).

%package -n libnvrtc
Group: System/Libraries
Summary: CUDA Runtime Compilation (NVIDIA NVRTC Library)
Provides: libnvrtc.so.12(libnvrtc.so.12)(64bit)
%description -n libnvrtc
CUDA Runtime Compilation (NVIDIA NVRTC Library).

%package -n libnvvm
Group: System/Libraries
Summary: NVIDIA NVVM Library
%description -n libnvvm
NVIDIA NVVM Library.

%package -n libnvfatbin
Group: System/Libraries
Summary: NVIDIA FatBin Library.
Provides: libnvfatbin.so.12(libnvfatbin.so.12)(64bit)
%description -n libnvfatbin
NVIDIA FatBin Library.

%package -n libnvtx
Group: System/Libraries
Summary: NVIDIA Tools Extension (NVTX) library.
%description -n libnvtx
NVIDIA Tools Extension (NVTX) library.

%package -n libaccinj64
Group: System/Libraries
Summary: NVIDIA ACCINJ Library (64-bit)
%description -n libaccinj64
NVIDIA ACCINJ Library (64-bit).

%package -n gds-tools
Group: System/Libraries
Summary: GPUDirect Storage - tools
Requires: nvidia-cuda-devel = %EVR
%description -n gds-tools
GPUDirect Storage - tools.

%package -n libcuinj64
Group: System/Libraries
Summary: NVIDIA CUINJ Library (64-bit)
%description -n libcuinj64
NVIDIA CUINJ Library (64-bit).

%ifarch x86_64
%package -n nvidia-profiler
Group: System/Libraries
Summary: NVIDIA Profiler for CUDA and OpenCL
Requires: nvidia-cuda-devel = %EVR
Requires: libpython3
%description -n nvidia-profiler
NVIDIA Profiler for CUDA and OpenCL.

%package -n nvidia-visual-profiler
Group: System/Libraries
Summary: NVIDIA Visual Profiler for CUDA and OpenCL
Requires: nvidia-cuda-toolkit = %EVR
Requires: nvidia-profiler = %EVR
Requires: ant java-1.8.0-openjdk
%description -n nvidia-visual-profiler
The NVIDIA Visual Profiler is a cross-platform performance profiling tool
that delivers developers vital feedback for optimizing CUDA C/C++ applications.
%endif

%package -n nvidia-nsight-compute
Group: Development/Other
Summary: NVIDIA Nsight Compute
Requires: nvidia-cuda-toolkit = %EVR
Requires: java
%description -n nvidia-nsight-compute
NVIDIA Nsight Compute is an interactive profiler for CUDA and NVIDIA OptiX
that provides detailed performance metrics and API debugging via a user
interface and command-line tool. Users can run guided analysis and compare
esults with a customizable and data-driven user interface, as well as
post-process and analyze results in their own workflows.

%package -n nvidia-nsight-systems
Group: Development/Other
Summary: NVIDIA Nsight Systems
Requires: nvidia-cuda-toolkit = %EVR
Requires: java
%description -n nvidia-nsight-systems
NVIDIA Nsight Systems is a system-wide performance analysis tool designed
to visualize an applications algorithms, identify the largest opportunities
to optimize, and tune to scale efficiently across any quantity or size of
CPUs and GPUs, from large servers to our smallest system on a chip (SoC).

%prep
%setup -T -D -a1 -a2 -c -n %name

%build
# nothing to build

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_docdir,%_includedir,%_desktopdir,%_pkgconfigdir}

pushd builds

cp -vr cuda_cccl/lib64/* %buildroot%_libdir/
cp -vr cuda_cccl/include/* %buildroot%_includedir/

cp -vr cuda_cudart/lib64/* %buildroot%_libdir/
cp -vr cuda_cudart/include/* %buildroot%_includedir/

cp -v cuda_cuobjdump/bin/* %buildroot%_bindir/

mkdir -p %buildroot%_datadir/%oname/extras
cp -vr cuda_cupti/extras/* %buildroot%_datadir/%oname/extras/
mv -v %buildroot%_datadir/%oname/extras/CUPTI/lib64/* %buildroot%_libdir/
rm -rv %buildroot%_datadir/%oname/extras/CUPTI/lib64

cp -v cuda_cuxxfilt/bin/* %buildroot%_bindir/
cp -vr cuda_cuxxfilt/lib64/* %buildroot%_libdir/
cp -vr cuda_cuxxfilt/include/* %buildroot%_includedir/

mkdir -p %buildroot%_docdir/%oname/
cp -vr cuda_documentation/* %buildroot%_docdir/%oname/

for i in "3.8" "3.9" "3.10" "3.11" "3.12" ; do
    if [[ -f cuda_gdb/bin/cuda-gdb-python${i}-tui ]]
    then rm -v cuda_gdb/bin/cuda-gdb-python${i}-tui
    fi
done
cp -vr cuda_gdb/bin/* %buildroot%_bindir/
cp -vr cuda_gdb/extras/Debugger %buildroot%_datadir/%oname/extras/

cp -v cuda_nvcc/nvvm/bin/* %buildroot%_bindir/
cp -vr cuda_nvcc/nvvm/lib64/* %buildroot%_libdir/
cp -vr cuda_nvcc/nvvm/include/* %buildroot%_includedir/

mkdir -p %buildroot%_libdir/nvvm
cp -vr cuda_nvcc/nvvm/libdevice %buildroot%_libdir/nvvm/

mkdir -p %buildroot%_libdir/nvcc
cp -vr cuda_nvcc/bin %buildroot%_libdir/nvcc/

cp -vr cuda_nvcc/include/* %buildroot%_includedir/

for i in bin2c cudafe++ fatbinary nvcc __nvcc_device_query nvlink ptxas ; do
cat > %buildroot%_bindir/$i <<EOF
#!/usr/bin/env bash
exec %_libdir/nvcc/bin/$i "\$@"
EOF
chmod 755 %buildroot%_bindir/$i
done

cat > %buildroot%_libdir/nvcc/bin/nvcc.profile <<EOF
NVVMIR_LIBRARY_DIR = %_libdir/nvvm/libdevice
PATH += %_libdir/nvcc:
LIBRARIES =+ \$(_SPACE_) -L/usr/lib64/stubs -L/usr/lib64
EOF
chmod 644 %buildroot%_libdir/nvcc/bin/nvcc.profile

cp -v cuda_nvdisasm/bin/* %buildroot%_bindir/

cp -vr cuda_nvml_dev/lib64/* %buildroot%_libdir/
cp -vr cuda_nvml_dev/include/* %buildroot%_includedir/
cp -vr cuda_nvml_dev/nvml %buildroot%_datadir/%oname/

cp -v cuda_nvprune/bin/* %buildroot%_bindir/

cp -vr cuda_nvrtc/lib64/* %buildroot%_libdir/
cp -vr cuda_nvrtc/include/* %buildroot%_includedir/

cp -vr cuda_nvtx/lib64/* %buildroot%_libdir/
cp -vr cuda_nvtx/include/* %buildroot%_includedir/

cp -vr cuda_profiler_api/include/* %buildroot%_includedir/

cp -v cuda_sanitizer_api/compute-sanitizer/compute-sanitizer %buildroot%_bindir/
cp -v cuda_sanitizer_api/compute-sanitizer/TreeLauncherSubreaper %buildroot%_bindir/
cp -v cuda_sanitizer_api/compute-sanitizer/TreeLauncherTargetLdPreloadHelper %buildroot%_bindir/
cp -v cuda_sanitizer_api/compute-sanitizer/*.so %buildroot%_libdir/
cp -vr cuda_sanitizer_api/compute-sanitizer/include/* %buildroot%_includedir/
mkdir -p %buildroot%_docdir/compute-sanitizer
cp -vr cuda_sanitizer_api/compute-sanitizer/docs* %buildroot%_docdir/compute-sanitizer

cp -vr libcublas/lib64/* %buildroot%_libdir/
cp -vr libcublas/include/* %buildroot%_includedir/
%ifarch x86_64
cp -vr libcublas/src %buildroot%_datadir/%oname/
%endif

cp -vr libcufft/lib64/* %buildroot%_libdir/
cp -vr libcufft/include/* %buildroot%_includedir/

# remove error link
rm -v libcufile/lib64/lib64
cp -vr libcufile/lib64/* %buildroot%_libdir/
cp -vr libcufile/include/* %buildroot%_includedir/

cp -vr libcufile/gds %buildroot%_libdir/
cp -vr libcufile/gds-*.* %buildroot%_docdir/

cp -vr libcurand/lib64/* %buildroot%_libdir/
cp -vr libcurand/include/* %buildroot%_includedir/

cp -vr libnvfatbin/lib64/* %buildroot%_libdir/
cp -vr libnvfatbin/include/* %buildroot%_includedir/

cp -vr libcusolver/lib64/* %buildroot%_libdir/
cp -vr libcusolver/include/* %buildroot%_includedir/

cp -vr libcusparse/lib64/* %buildroot%_libdir/
cp -vr libcusparse/include/* %buildroot%_includedir/
%ifarch x86_64
cp -vr libcusparse/src/* %buildroot%_datadir/%oname/src/
%endif

cp -vr libnpp/lib64/* %buildroot%_libdir/
cp -vr libnpp/include/* %buildroot%_includedir/

cp -vr libnvjitlink/lib64/* %buildroot%_libdir/
cp -vr libnvjitlink/include/* %buildroot%_includedir/

cp -vr libnvjpeg/lib64/* %buildroot%_libdir/
cp -vr libnvjpeg/include/* %buildroot%_includedir/

%ifarch x86_64
cp -v cuda_nvprof/bin/* %buildroot%_bindir/
cp -vr cuda_nvprof/lib64/* %buildroot%_libdir/

cp -v cuda_nvvp/bin/* %buildroot%_bindir/
cp -vr cuda_nvvp/libnvvp %buildroot%_libdir/nvvp

cat > %buildroot%_bindir/nvvp <<EOF
#!/usr/bin/env bash
UBUNTU_MENUPROXY=0 LIBOVERLAY_SCROLLBAR=0 %_libdir/nvvp/nvvp \$@
EOF
chmod 755 %buildroot%_bindir/nvvp

# explicit python shebang
find %buildroot%_libdir/nvvp/plugins/ -name "*.py" -exec sed -i "s|#!%_bindir/python|#!%__python3|" {} \;

# nvvp only works with java 8
cat >> %buildroot%_libdir/nvvp/nvvp.ini <<EOF
-vm
/usr/lib/jvm/jre-1.8.0/bin/java
EOF
%endif

mkdir -p %buildroot%_libdir/nsight-compute-%nsight_compute_ver
cp -vr nsight_compute/* %buildroot%_libdir/nsight-compute-%nsight_compute_ver/
cp -v integration/nsight-compute/* %buildroot%_bindir/
# fix path nsight-compute
sed -i 's|"$CUDA_TOOLKIT_BIN_DIR"/../nsight-compute-*|%_libdir/nsight-compute-*|' %buildroot%_bindir/ncu*

mkdir -p %buildroot%_libdir/nsight-systems-%nsight_sys_ver
cp -vr nsight_systems/* %buildroot%_libdir/nsight-systems-%nsight_sys_ver/
cp -v integration/nsight-systems/* %buildroot%_bindir/
# fix path nsight-systems
sed -i 's|"$CUDA_INSTALL_DIR"/|%_libdir/|' %buildroot%_bindir/nsys*




# Remove bundled python _sqlite3 library compiled with python3.10 and rm bad_elf_symbols detected
%ifarch aarch64
rm -rv %buildroot%_libdir/nsight-systems-%nsight_sys_ver/target-linux-sbsa-armv8/python/packages/nsys_recipe/third_party/
rm -vr %buildroot%_libdir/nsight-systems-%nsight_sys_ver/target-linux-sbsa-armv8/CollectX
rm -vr %buildroot%_libdir/nsight-systems-%nsight_sys_ver/host-linux-armv8/Mesa
rm -vr %buildroot%_libdir/nsight-compute-%nsight_compute_ver/host/linux-desktop-t210-a64/Mesa
%else
rm -rv %buildroot%_libdir/nsight-systems-%nsight_sys_ver/target-linux-x64/python/packages/nsys_recipe/third_party
rm -vr %buildroot%_libdir/nsight-systems-%nsight_sys_ver/target-linux-x64/CollectX
rm -vr %buildroot%_libdir/nsight-compute-%nsight_compute_ver/host/target-linux-x64/python/packages/nsys_recipe/third_party
rm -vr %buildroot%_libdir/nsight-compute-%nsight_compute_ver/target/linux-desktop-glibc_2_11_3-x86
%endif

# install desktop files and build icons
install -m644 %SOURCE10 %buildroot%_desktopdir/
install -m644 %SOURCE11 %buildroot%_desktopdir/
for S in 16 24 32 48 64 128 192 256 ; do
    mkdir -p %buildroot%_iconsdir/hicolor/$S\x$S/apps
    magick %SOURCE20 -resize $S\x$S %buildroot%_iconsdir/hicolor/$S\x$S/apps/ncu-ui.png
    magick %SOURCE21 -resize $S\x$S %buildroot%_iconsdir/hicolor/$S\x$S/apps/nsys-ui.png
done

%ifarch x86_64
install -m644 %SOURCE12 %buildroot%_desktopdir/
for S in 16 24 32 48 64 128 192 256 ; do
    magick %SOURCE22 -resize $S\x$S %buildroot%_iconsdir/hicolor/$S\x$S/apps/nvvp.png
done
%endif

# remove error link
rm -v %buildroot%_includedir/include

# fix rpath
chrpath -d %buildroot%_libdir/*.so.*
chrpath -d %buildroot%_libdir/libTreeLauncherTargetInjection.so
%ifarch x86_64
chrpath -d %buildroot%_bindir/cuda-gdb-minimal
chrpath -d %buildroot%_bindir/nvprof
%endif

# Allow newer compilers to work. This is not officially supported.
# See https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#system-requirements
# for official requirements
sed -i "/.*unsupported GNU version.*/d" %buildroot%_includedir/crt/host_config.h
sed -i "/.*unsupported clang version.*/d" %buildroot%_includedir/crt/host_config.h

# update version in pkgconfig files
sed -i "s/Version: XX.X/Version: %{cuda_release}.%{cuda_major}/g" ../pkgconfig/*.pc

# copy pkgconfig files
cp -v ../pkgconfig/*.pc %buildroot%_pkgconfigdir/

%files -n nvidia-cuda-toolkit
%_bindir/bin2c
%_bindir/cudafe++
%_bindir/fatbinary
%_bindir/nvcc
%_bindir/__nvcc_device_query
%_bindir/nvlink
%_bindir/ptxas
%_libdir/nvcc/
%_docdir/%oname

%files -n nvidia-cuda-devel
%_bindir/cicc
%_bindir/nvprune
%_bindir/cu++filt
%_bindir/nvdisasm
%_bindir/cuobjdump
%_bindir/TreeLauncherSubreaper
%_bindir/TreeLauncherTargetLdPreloadHelper
%_bindir/compute-sanitizer
%_includedir/*
%_libdir/*.so
%exclude %_libdir/libcheckpoint.so
%exclude %_libdir/libnvperf_host.so
%exclude %_libdir/libnvperf_target.so
%exclude %_libdir/libpcsamplingutil.so
%exclude %_libdir/libcufile.so
%exclude %_libdir/libcufile_rdma.so
%exclude %_libdir/libcupti.so
%_libdir/stubs/
%_libdir/cmake/
%_libdir/nvvm/
%_datadir/%oname
%exclude %_datadir/%oname/extras/Debugger
%exclude %_datadir/%oname/extras/CUPTI
%_docdir/compute-sanitizer
%_pkgconfigdir/*.pc

%files -n nvidia-cuda-devel-static
%_libdir/*.a

%files -n nvidia-cuda-gdb
%ifarch x86_64
%_bindir/cuda-gdb-*
%endif
%_bindir/cuda-gdb
%_bindir/cuda-gdbserver
%_datadir/%oname/extras/Debugger

%files -n gds-tools
%_libdir/gds/
%_docdir/gds-*.*/

%ifarch x86_64
%files -n libaccinj64
%_libdir/libaccinj64.so.*

%files -n libcuinj64
%_libdir/libcuinj64.so.*
%endif

%files -n libcublaslt
%_libdir/libcublasLt.so.*

%files -n libcublas
%_libdir/libcublas.so.*

%files -n libcudart
%_libdir/libcudart.so.*

%files -n libcufft
%_libdir/libcufft.so.*

%files -n libcufftw
%_libdir/libcufftw.so.*

%files -n libcufile-rdma
%_libdir/libcufile_rdma.so.*

%files -n libcufile
%_libdir/libcufile.so.*

%files -n libcufile-devel
%_libdir/libcufile.so
%_libdir/libcufile_rdma.so

%files -n libcupti
%_libdir/libcupti.so.*
%_libdir/libcheckpoint.so
%_libdir/libnvperf_host.so
%_libdir/libnvperf_target.so
%_libdir/libpcsamplingutil.so

%files -n libcupti-devel
%_datadir/%oname/extras/CUPTI
%_libdir/libcupti.so

%files -n libcurand
%_libdir/libcurand.so.*

%files -n libcusolvermg
%_libdir/libcusolverMg.so.*

%files -n libcusolver
%_libdir/libcusolver.so.*

%files -n libcusparse
%_libdir/libcusparse.so.*

%files -n libnppc
%_libdir/libnppc.so.*

%files -n libnppial
%_libdir/libnppial.so.*

%files -n libnppicc
%_libdir/libnppicc.so.*

%files -n libnppidei
%_libdir/libnppidei.so.*

%files -n libnppif
%_libdir/libnppif.so.*

%files -n libnppig
%_libdir/libnppig.so.*

%files -n libnppim
%_libdir/libnppim.so.*

%files -n libnppist
%_libdir/libnppist.so.*

%files -n libnppisu
%_libdir/libnppisu.so.*

%files -n libnppitc
%_libdir/libnppitc.so.*

%files -n libnpps
%_libdir/libnpps.so.*

%files -n libnvblas
%_libdir/libnvblas.so.*

%files -n libnvjitlink
%_libdir/libnvJitLink.so.*

%files -n libnvjpeg
%_libdir/libnvjpeg.so.*

%files -n libnvrtc-builtins
%_libdir/libnvrtc-builtins.so.*
%ifarch x86_64
%_libdir/libnvrtc-builtins.alt.so.*
%endif

%files -n libnvrtc
%_libdir/libnvrtc.so.*
%ifarch x86_64
%_libdir/libnvrtc.alt.so.*
%endif

%files -n libnvvm
%_libdir/libnvvm.so.*

%files -n libnvfatbin
%_libdir/libnvfatbin.so.*

%files -n libnvtx
%_libdir/libnvtx3interop.so.*

%ifarch x86_64
%files -n nvidia-profiler
%_bindir/nvprof

%files -n nvidia-visual-profiler
%_bindir/computeprof
%_bindir/nvvp
%_libdir/nvvp/
%_iconsdir/hicolor/*/apps/nvvp.png
%_desktopdir/nvidia-visual-profiler.desktop
%endif

%files -n nvidia-nsight-compute
%_bindir/ncu
%_bindir/ncu-ui
%_libdir/nsight-compute-%nsight_compute_ver/
%_iconsdir/hicolor/*/apps/ncu-ui.png
%_desktopdir/nvidia-nsight-compute.desktop

%files -n nvidia-nsight-systems
%_bindir/nsys
%_bindir/nsys-ui
%_bindir/nsight-sys
%_libdir/nsight-systems-%nsight_sys_ver/
%_iconsdir/hicolor/*/apps/nsys-ui.png
%_desktopdir/nvidia-nsight-systems.desktop

%changelog
* Fri Nov 21 2025 Mikhail Tergoev <fidel@altlinux.org> 12.9.1-alt1
- updated to 12.9.1
- splitting the repository for each new version

* Sat Sep 13 2025 Grigory Ustinov <grenka@altlinux.org> 12.8.1-alt1.1
- Fixed building with python3.13.

* Thu May 01 2025 Mikhail Tergoev <fidel@altlinux.org> 12.8.1-alt1
- updated to 12.8.1 (ALT bug: 53832 54080)
- removed version from name *.pc files

* Mon Feb 03 2025 Mikhail Tergoev <fidel@altlinux.org> 12.4.1-alt1
- updated to 12.4.1

* Mon Jan 29 2024 Mikhail Tergoev <fidel@altlinux.org> 12.3.2-alt1
- updated to 12.3.2 (ALT bug: 49154)
- returned requires nvidia-cuda-toolkit to nvidia-cuda-devel

* Mon Jan 22 2024 Mikhail Tergoev <fidel@altlinux.org> 12.3.1-alt3
- drop requires nvidia-cuda-toolkit from nvidia-cuda-devel (ALT bug: 48761)
- separation of nvidia-cuda-gdb packages from nvidia-cuda-devel (ALT bug: 48762)
- separation of libcufile-devel packages from nvidia-cuda-devel
- separation of libcupti-devel packages from nvidia-cuda-devel

* Mon Jan 15 2024 Grigory Ustinov <grenka@altlinux.org> 12.3.1-alt2
- Fixed working with python3.12.

* Fri Dec 01 2023 Mikhail Tergoev <fidel@altlinux.org> 12.3.1-alt1
- Initial build for ALT Sisyphus
