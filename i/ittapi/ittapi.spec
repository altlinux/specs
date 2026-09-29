%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define _unpackaged_files_terminate_build 1

Name: ittapi
Version: 3.28.4
Release: alt1

Summary: Intel Instrumentation and Tracing Technology (ITT) and Just-In-Time (JIT) API
License: BSD-3-Clause OR GPL-2.0-only
Group: Development/C
Url: https://github.com/intel/ittapi
Vcs: https://github.com/intel/ittapi

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
The Instrumentation and Tracing Technology (ITT) API enables applications
to generate and control the collection of trace data during their execution
across different Intel tools (e.g. Intel VTune Profiler).
The Just-In-Time (JIT) Profiling API provides functionality to report
information about just-in-time generated code.

%package devel
Summary: Header files for Intel ITT and JIT API
Group: Development/C
BuildArch: noarch

%description devel
The Instrumentation and Tracing Technology (ITT) API enables applications
to generate and control the collection of trace data during their execution
across different Intel tools (e.g. Intel VTune Profiler).

This package contains header files for the ITT and JIT profiling API.

%package devel-static
Summary: Static libraries for Intel ITT and JIT API
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
The Instrumentation and Tracing Technology (ITT) API enables applications
to generate and control the collection of trace data during their execution
across different Intel tools (e.g. Intel VTune Profiler).

This package contains static libraries (built as PIC) and CMake
configuration files for the ITT and JIT profiling API.

%prep
%setup
%autopatch -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_POSITION_INDEPENDENT_CODE=ON \
	-DITT_API_FORTRAN_SUPPORT=OFF \
	-DITT_API_IPT_SUPPORT=OFF \
	%nil
%cmake_build

%install
%cmake_install
install -pm644 %_cmake__builddir/bin/libjitprofiling.a %buildroot%_libdir/
# C# annotation file is not needed
rm -f %buildroot%_includedir/AdvisorAnnotate.cs

%files devel
%doc README.md LICENSES
%_includedir/advisor-annotate.h
%_includedir/ittnotify.h
%_includedir/ittnotify-zca.h
%_includedir/jitprofiling.h
%_includedir/libittnotify.h
%_includedir/legacy

%files devel-static
%_libdir/libittnotify.a
%_libdir/libjitprofiling.a
%_libdir/cmake/ittapi

%changelog
* Wed Sep 23 2026 Artem Krasovskiy <aibure@altlinux.org> 3.28.4-alt1
- Initial build for Sisyphus.
