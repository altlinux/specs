%define         cuda_version 12
%define 	soversion 9
%define 	major_version %soversion.13.1

%define oname cudnn

Name:           nvidia-cudnn
Version:        %major_version.26
Release:        alt2
Group:  	System/Libraries
Summary:        NVIDIA CUDA Deep Neural Network library (cuDNN)
License:        NVIDIA
URL:            https://developer.nvidia.com/cudnn

Source0:        cudnn-linux-x86_64-%{version}_cuda%cuda_version-archive.tar.xz
Source1:        cudnn-linux-aarch64-%{version}_cuda%cuda_version-archive.tar.xz


ExclusiveArch:  x86_64 aarch64

Requires: nvidia-cuda-devel

%description
The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated
library of primitives for deep neural networks. cuDNN provides highly tuned
implementations for standard routines such as forward and backward convolution,
pooling, normalization, and activation layers. cuDNN is part of the NVIDIA Deep
Learning SDK.

%package -n lib%oname%soversion
Group: System/Libraries
Summary: NVIDIA CUDA Deep Neural Network library (cuDNN)
Provides:       libcudnn.so.9(libcudnn.so.9)(64bit) 

%description -n lib%oname%soversion
The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated
library of primitives for deep neural networks. cuDNN provides highly tuned
implementations for standard routines such as forward and backward convolution,
pooling, normalization, and activation layers. cuDNN is part of the NVIDIA Deep
Learning SDK.

%package -n lib%oname%soversion-adv
Summary: cuDNN Advanced API shared libraries
Group: System/Libraries

%description -n lib%oname%soversion-adv
Shared libraries providing advanced cuDNN API routines (libcudnn_adv*),
used for high-level neural network operations.


%package -n lib%oname%soversion-cnn
Summary: cuDNN Convolutional Neural Network API shared libraries
Group: System/Libraries

%description -n lib%oname%soversion-cnn
Shared libraries implementing cuDNN CNN (convolutional) primitives,
including forward/backward convolutions, pooling and normalization.

%package -n lib%oname%soversion-ops
Summary: cuDNN Operations API shared libraries
Group: System/Libraries
Provides: libcudnn_ops.so.9(libcudnn_ops.so.9)(64bit)

%description -n lib%oname%soversion-ops
Shared libraries for core cuDNN operation graph execution (libcudnn_ops*),
providing tensor operations, fusion, and activation layers.


%package -n lib%oname%soversion-heuristic
Summary: cuDNN Heuristic API shared libraries
Group: System/Libraries

%description -n lib%oname%soversion-heuristic
Heuristic-based optimizer libraries for selecting optimal kernels
and execution plans for cuDNN operations.


%package -n lib%oname%soversion-engines
Summary: cuDNN Execution Engine API shared libraries
Group: System/Libraries

%description -n lib%oname%soversion-engines
Shared libraries implementing the cuDNN engine runtime and precompiled engines,
providing backend-agnostic execution of neural network graphs.


%package -n lib%oname%soversion-graph
Summary: cuDNN Graph API shared libraries
Group: System/Libraries
Provides: libcudnn_graph.so.9(libcudnn_graph.so.9)(64bit)

%description -n lib%oname%soversion-graph
cuDNN Graph API shared libraries enabling graph-based computation,
static graph optimizations, and reusable graph descriptors.

%package -n lib%oname-devel
Group:  	Development/Other 
Summary:        Development files for lib%name
Requires:       lib%oname%soversion = %EVR

%description -n lib%oname-devel
The lib%oname-devel package contains libraries and header files for developing
applications that use lib%name.

%package -n lib%oname-static
Group: 		Development/Other
Summary:        Static libraries for lib%name

%description -n lib%oname-static
Static library files for lib%name.

%prep
%ifarch x86_64
%setup -n cudnn-linux-x86_64-%{version}_cuda%cuda_version-archive
%endif

%ifarch aarch64
%setup -T -b 1 -n cudnn-linux-aarch64-%{version}_cuda%cuda_version-archive
%endif

%build
# Nothing to build

%install
install -d %buildroot%_libdir
install -m 755 lib/*.so.%major_version %buildroot%_libdir/
install -m 644 lib/*.a %buildroot%_libdir/

install -d %buildroot%_includedir
install -m 644 include/* %buildroot%_includedir/

pushd %buildroot%_libdir
for f in lib%{oname}*.so.%major_version; do
    base=${f%%.so.%{major_version}}
    ln -sf $(basename $f) ${base}.so.%soversion
    ln -sf ${base}.so.%soversion ${base}.so
done
popd

%files -n lib%oname%soversion
%doc LICENSE
%_libdir/lib%oname.so.%{soversion}*

%files -n lib%oname%soversion-adv
%_libdir/libcudnn_adv.so.%{soversion}*
 
%files -n lib%oname%soversion-cnn
%_libdir/libcudnn_cnn.so.%{soversion}*
 
%files -n lib%oname%soversion-ops
%_libdir/libcudnn_ops.so.%{soversion}*
 
%files -n lib%oname%soversion-heuristic
%_libdir/libcudnn_heuristic.so.%{soversion}*
 
%files -n lib%oname%soversion-engines
%_libdir/libcudnn_engines_*.so.%{soversion}*
 
%files -n lib%oname%soversion-graph
%_libdir/libcudnn_graph.so.%{soversion}*

%files -n lib%oname-devel
%_includedir/%{oname}*
%_libdir/lib%{oname}*.so

%files -n lib%oname-static
%_libdir/lib%{oname}*.a

%changelog
* Wed Mar 11 2026 Nikita Shmatko <nash@altlinux.org> 9.13.1.26-alt2
- Minor specfile fixes.

* Wed Nov 26 2025 Nikita Shmatko <nash@altlinux.org> 9.13.1.26-alt1
- Initial build for Sisyphus.
