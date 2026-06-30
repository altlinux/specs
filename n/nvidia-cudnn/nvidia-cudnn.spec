%define         cuda_version 12
%define 	soversion 9
%define 	major_version %soversion.20.0

Name:           nvidia-cudnn
Version:        %major_version.48
Release:        alt1
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

%package -n libcudnn%soversion
Group: System/Libraries
Summary: NVIDIA CUDA Deep Neural Network library (cuDNN)
Provides: libcudnn.so.%soversion(libcudnn.so.%soversion)(64bit) 

%description -n libcudnn%soversion
The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated
library of primitives for deep neural networks. cuDNN provides highly tuned
implementations for standard routines such as forward and backward convolution,
pooling, normalization, and activation layers. cuDNN is part of the NVIDIA Deep
Learning SDK.

%package -n libcudnn%soversion-adv
Summary: cuDNN Advanced API shared libraries
Group: System/Libraries

%description -n libcudnn%soversion-adv
Shared libraries providing advanced cuDNN API routines (libcudnn_adv*),
used for high-level neural network operations.


%package -n libcudnn%soversion-cnn
Summary: cuDNN Convolutional Neural Network API shared libraries
Group: System/Libraries

%description -n libcudnn%soversion-cnn
Shared libraries implementing cuDNN CNN (convolutional) primitives,
including forward/backward convolutions, pooling and normalization.

%package -n libcudnn%soversion-ops
Summary: cuDNN Operations API shared libraries
Group: System/Libraries
Provides: libcudnn_ops.so.%soversion(libcudnn_ops.so.%soversion)(64bit)

%description -n libcudnn%soversion-ops
Shared libraries for core cuDNN operation graph execution (libcudnn_ops*),
providing tensor operations, fusion, and activation layers.

%package -n libcudnn%soversion-heuristic
Summary: cuDNN Heuristic API shared libraries
Group: System/Libraries

%description -n libcudnn%soversion-heuristic
Heuristic-based optimizer libraries for selecting optimal kernels
and execution plans for cuDNN operations.

%package -n libcudnn%soversion-engines
Summary: cuDNN Execution Engine API shared libraries
Group: System/Libraries

%description -n libcudnn%soversion-engines
Shared libraries implementing the cuDNN engine runtime and precompiled engines,
providing backend-agnostic execution of neural network graphs.

%package -n libcudnn%soversion-graph
Summary: cuDNN Graph API shared libraries
Group: System/Libraries
Provides: libcudnn_graph.so.%soversion(libcudnn_graph.so.%soversion)(64bit)

%description -n libcudnn%soversion-graph
cuDNN Graph API shared libraries enabling graph-based computation,
static graph optimizations, and reusable graph descriptors.

%package -n libcudnn-devel
Group:  	Development/Other 
Summary:        Development files for libcudnn
Requires:       libcudnn%soversion = %EVR

%description -n libcudnn-devel
The libcudnn-devel package contains libraries and header files for developing
applications that use libcudnn.

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

install -d %buildroot%_includedir
install -m 644 include/* %buildroot%_includedir/

pushd %buildroot%_libdir
for f in libcudnn*.so.%major_version; do
    base=${f%%.so.%{major_version}}
    ln -sf $(basename $f) ${base}.so.%soversion
    ln -sf ${base}.so.%soversion ${base}.so
done
popd

%files -n libcudnn%soversion
%doc LICENSE
%_libdir/libcudnn.so.%{soversion}*

%files -n libcudnn%soversion-adv
%_libdir/libcudnn_adv.so.%{soversion}*
 
%files -n libcudnn%soversion-cnn
%_libdir/libcudnn_cnn.so.%{soversion}*
 
%files -n libcudnn%soversion-ops
%_libdir/libcudnn_ops.so.%{soversion}*
 
%files -n libcudnn%soversion-heuristic
%_libdir/libcudnn_heuristic.so.%{soversion}*
 
%files -n libcudnn%soversion-engines
%_libdir/libcudnn_engines_*.so.%{soversion}*
 
%files -n libcudnn%soversion-graph
%_libdir/libcudnn_graph.so.%{soversion}*

%files -n libcudnn-devel
%_includedir/cudnn*
%_libdir/libcudnn*.so

%changelog
* Fri Jun 26 2026 Nikita Shmatko <nash@altlinux.org> 9.20.0.48-alt1
- New version 9.20.0.48.
- Dropped the unused static library subpackage.

* Wed Mar 11 2026 Nikita Shmatko <nash@altlinux.org> 9.13.1.26-alt2
- Minor specfile fixes.

* Wed Nov 26 2025 Nikita Shmatko <nash@altlinux.org> 9.13.1.26-alt1
- Initial build for Sisyphus.
