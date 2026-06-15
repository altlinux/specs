%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict
%def_disable doc

%ifarch x86_64 aarch64
%def_with cuda
%filter_from_requires /libcudart\.so\.12/d
# cuda (12.x) is not ready for gcc15
%define gcc_ver 14
%else
%def_without cuda
%endif

%define soname 3.7.0

Name: opensubdiv
Version: %soname
Release: alt4
Summary: An Open-Source subdivision surface library
Group: Development/Other
License: TOST
URL: https://graphics.pixar.com/opensubdiv/

# https://github.com/PixarAnimationStudios/OpenSubdiv.git
Source: %name-%version.tar

Patch1: opensubdiv-alt-no-static-libraries.patch
Patch2: opensubdiv-alt-tutorials-install.patch
Patch3: opensubdiv-alt-link-glx.patch

BuildRequires(pre): cmake rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: tbb-devel
BuildRequires: libgomp-devel
BuildRequires: ocl-icd-devel
# documentation
%if_enabled doc
BuildRequires: python3-module-docutils doxygen graphviz
%endif
# examples
BuildRequires: libglfw3-devel libXrandr-devel libXxf86vm-devel libXcursor-devel libXinerama-devel libXi-devel libPtex-devel
BuildRequires: gcc-c++ libgomp-devel
%if_with cuda
BuildRequires: nvidia-cuda-devel
BuildRequires: gcc%{gcc_ver}-c++
# build runs under gcc%{gcc_ver}: -fopenmp needs the matching libgomp.so,
# otherwise FindOpenMP fails and the Osd OMP evaluator is dropped
BuildRequires: libgomp%{gcc_ver}-devel
%endif

%description
OpenSubdiv is a set of open source libraries that implement
high performance subdivision surface (subdiv) evaluation
on massively parallel CPU and GPU architectures.
This codepath is optimized for drawing deforming subdivs
with static topology at interactive framerates.
The resulting limit surface matches Pixar's Renderman to numerical precision.

OpenSubdiv is covered by the Apache license,
and is free to use for commercial or non-commercial use.
This is the same code that Pixar uses internally for animated film production.
Our intent is to encourage high performance accurate subdiv drawing
by giving away the "good stuff".

Feel free to use it and let us know what you think.

%package -n lib%name%soname
Summary: An Open-Source subdivision surface library
Group: System/Libraries
%if_with cuda
Requires: libcudart
%endif
Provides: lib%name = %EVR

%description -n lib%name%soname
OpenSubdiv is a set of open source libraries that implement
high performance subdivision surface (subdiv) evaluation
on massively parallel CPU and GPU architectures.
This codepath is optimized for drawing deforming subdivs
with static topology at interactive framerates.
The resulting limit surface matches Pixar's Renderman to numerical precision.

OpenSubdiv is covered by the Apache license,
and is free to use for commercial or non-commercial use.
This is the same code that Pixar uses internally for animated film production.
Our intent is to encourage high performance accurate subdiv drawing
by giving away the "good stuff".

Feel free to use it and let us know what you think.

%package devel
Summary: An Open-Source subdivision surface library
Group: Development/C++
Requires: lib%name = %EVR
# ugly workaround until cpp.req support cmake
Requires: ocl-icd-devel libgomp-devel
# due /usr/lib64/libcudart.so
%if_with cuda
Requires: nvidia-cuda-devel
%endif

%description devel
OpenSubdiv is a set of open source libraries that implement
high performance subdivision surface (subdiv) evaluation
on massively parallel CPU and GPU architectures.
This codepath is optimized for drawing deforming subdivs
with static topology at interactive framerates.
The resulting limit surface matches Pixar's Renderman to numerical precision.

OpenSubdiv is covered by the Apache license,
and is free to use for commercial or non-commercial use.
This is the same code that Pixar uses internally for animated film production.
Our intent is to encourage high performance accurate subdiv drawing
by giving away the "good stuff".

Feel free to use it and let us know what you think.

This package contains development files for OpenSubdiv.

%if_enabled doc
%package doc
Summary: An Open-Source subdivision surface library documentation
Group: Documentation
Requires: %name-devel = %EVR
BuildArch: noarch

%description doc
An Open-Source subdivision surface library documentation
%endif

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%if_with cuda
export GCC_VERSION=%{gcc_ver}
%endif
%cmake \
	-DCMAKE_CXX_STANDARD=17 \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DPYTHON_EXECUTABLE=%_bindir/python3 \
	-DCMAKE_LIBDIR_BASE=%_lib \
	-DCMAKE_TUTORIAL_BASE=%_lib/%name \
	%nil

%cmake_build

%install
%cmake_install
rm -rf %buildroot%_libdir/*.a

%files
%_bindir/*
%dir %_libdir/%name
%_libdir/%name/tutorials

%files -n lib%name%soname
%doc LICENSE.txt
%doc NOTICE.txt README.md
%_libdir/*.so.%{soname}

%files devel
%_libdir/*.so
%_libdir/cmake/OpenSubdiv
%_includedir/*

%if_enabled doc
%files doc
%_defaultdocdir/%name
%endif

%changelog
* Sun Jun 14 2026 Anton Farygin <rider@altlinux.org> 3.7.0-alt4
- fix FTBFS: compile cuda with gcc14 (nvcc 12.x rejects gcc15 headers)

* Wed Feb 18 2026 L.A. Kostis <lakostis@altlinux.ru> 3.7.0-alt3
- Fix FTBFS with new Ptex (std::clamp is C++17 feature).

* Tue Nov 25 2025 L.A. Kostis <lakostis@altlinux.ru> 3.7.0-alt2
- aarch64: enable CUDA.
- devel: add cuda deps.

* Sat Nov 15 2025 L.A. Kostis <lakostis@altlinux.ru> 3.7.0-alt1
- 3.7.0.
- Change license from Apache 2.0 to TOST
  (https://disneystreaming.github.io/TOST-1.0.txt).

* Sun Jul 20 2025 L.A. Kostis <lakostis@altlinux.ru> 3.6.1-alt1
- 3.6.1.
- spec: remove cuda gcc hacks.

* Mon Apr 28 2025 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt4.1
- Fix OMP compilation for CUDA case.

* Thu Apr 24 2025 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt4
- Improve -no-static patch.
- devel: update requires.

* Tue Nov 12 2024 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt3.1
- Fix FTBFS with gcc14 (compile with gcc13 for cuda).

* Sun Dec 10 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt3
- x86_64: Enable CUDA support.

* Thu Nov 16 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt2
- Don't build documentation by default.
- BR: remove clew deps (as we don't care about portability).

* Wed Nov 15 2023 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt1
- 3.6.0.
- BR: added OpenCL and Ptex.
- Added documentation subpackage.

* Thu Jan 27 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.4-alt2
- Rebuilt with new TBB.

* Fri Jun 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.4-alt1
- Initial build for ALT.
