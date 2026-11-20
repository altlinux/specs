%define _unpackaged_files_terminate_build 1
%define libname cura-formulae-engine
%define sover 1

%{?optflags_lto:%global optflags_lto %nil}
%ifarch %ix86
%global optflags %optflags -mfpmath=sse -msse2
%endif

%def_with check

Name: CuraFormulaeEngine
Version: 1.2.1
Release: alt1.gc1257dd6.1

Summary: Formulae parser and evaluator engine used in Ultimaker Cura
License: AGPL-3.0-or-later
Group: Engineering
URL: https://github.com/Ultimaker/CuraFormulaeEngine
VCS: https://github.com/Ultimaker/CuraFormulaeEngine

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: lexy-devel
BuildRequires: libspdlog-devel
BuildRequires: libexpected-devel
BuildRequires: librange-v3-devel
%if_with check
BuildRequires: ctest
BuildRequires: catch-devel
%endif

%description
Cura Formulae Engine is a library designed to parse and evaluate
Cura setting-expressions. These (python-like) expressions can
be written to express complex logic for 3D printing settings
and internal dependencies between settings.

%package -n lib%libname%sover
Summary: Cura Formulae Engine shared library
Group: System/Libraries

%description -n lib%libname%sover
%summary.

%package -n %libname-devel
Summary: Development files for lib%libname
Group: Development/C++
Requires: lib%libname%sover = %EVR

%description -n %libname-devel
%summary.

%prep
%setup
%autopatch -p1

%build
%cmake \
    -DCURA_FORMULA_VERSION_VERSION=%version \
    -DENABLE_TESTS=%{?_with_check:ON}%{!?_with_check:OFF} \
    -DENABLE_APPS=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n lib%libname%sover
%_libdir/lib%libname.so.%sover
%_libdir/lib%libname.so.%version

%files -n %libname-devel
%doc LICENSE README.md formula.md
%_includedir/%libname
%_libdir/lib%libname.so
%_cmakedir/%libname

%changelog
* Wed Nov 04 2026 Valery Zabrovsky <brow@altlinux.org> 1.2.1-alt1.gc1257dd6.1
- Initial build for ALT Sisyphus.
