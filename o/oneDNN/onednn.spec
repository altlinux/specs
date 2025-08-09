%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: oneDNN
Version: 3.8.1
Release: alt1

Summary: oneAPI Deep Neural Network Library

License: Apache-2.0
Group: Sciences/Computer science
URL: https://github.com/uxlfoundation/oneDNN

Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gcc gcc-c++
BuildRequires: libgomp-devel
BuildRequires: libblas-devel

%description
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.
oneDNN project is part of the UXL Foundation and is an implementation of the
oneAPI specification for oneDNN component.

The oneAPI specification is available at:
https://oneapi-spec.uxlfoundation.org/specifications/oneapi/latest/elements/onednn/source/

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on CPUs and GPUs.

%prep
%setup

%build
%cmake -GNinja \
    -Wno-dev
%cmake_build

%install
%cmake_install

%files
%doc %_docdir/dnnl

%package -n libdnnl
Summary: oneDNN shared library
Group: Sciences/Computer science

%description -n libdnnl
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.
oneDNN project is part of the UXL Foundation and is an implementation of the
oneAPI specification for oneDNN component.

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on CPUs and GPUs.

This package contains the dnnl shared library.

%files -n libdnnl
%_libdir/libdnnl.so.3
%_libdir/libdnnl.so.3.8

%package -n libdnnl-devel
Summary: development files for the oneDNN shared library
Group: Development/C

%description -n libdnnl-devel
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.
oneDNN project is part of the UXL Foundation and is an implementation of the
oneAPI specification for oneDNN component.

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on CPUs and GPUs.

This package contains development files and headers for the dnnl shared library.

%files -n libdnnl-devel
%_libdir/libdnnl.so
%_libdir/cmake/dnnl
%_includedir/oneapi/dnnl
%_includedir/dnnl*.h
%_includedir/dnnl*.hpp

%changelog
* Wed Aug 06 2025 Arseny Maslennikov <arseny@altlinux.org> 3.8.1-alt1
- Initial build for ALT Sisyphus.
