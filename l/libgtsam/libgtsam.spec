Name:    libgtsam
Version: 4.2.2
Release: alt2

Summary: GTSAM: C++ library for SAM in robotics/vision via factor graphs & Bayes nets
License: BSD-3-Clause
Group:   System/Libraries
URL:     https://borglab.github.io/gtsam/
VCS:     https://github.com/borglab/gtsam

Source: gtsam-%version.tar
Patch0: eigen5-compat.patch
Patch1: cmake-libdir.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel
BuildRequires: eigen3-devel tbb-devel python3-dev python3-module-pyparsing
BuildRequires: libmetis-devel chrpath

%description
GTSAM is a C++ library that implements smoothing and mapping (SAM) in robotics
and vision, using Factor Graphs and Bayes Networks as the underlying computing
paradigm rather than sparse matrices.

This is a metapackage/source package; the runtime shared libraries are in
libgtsam4 and libgtsam-unstable4.

%package -n libgtsam-devel
Summary: Development files for GTSAM
Group:   Development/C++
Requires: libgtsam = %EVR
Requires: eigen3-devel

%description -n libgtsam-devel
Development headers, CMake config files and the static helper library for
GTSAM.

%package -n libgtsam-unstable
Summary: Unstable/experimental GTSAM library
Group:   System/Libraries

%description -n libgtsam-unstable
Experimental extensions for GTSAM.

%package -n libgtsam-unstable-devel
Summary: Development files for GTSAM unstable
Group:   Development/C++
Requires: libgtsam-devel = %EVR
Requires: libgtsam-unstable = %EVR

%description -n libgtsam-unstable-devel
Development headers and CMake config files for GTSAM unstable.

%package -n python3-module-gtsam
Summary: Python 3 bindings for GTSAM
Group:   Development/Python
Requires: libgtsam = %EVR
Requires: python3
Requires: python3-module-numpy

%description -n python3-module-gtsam
Python 3 bindings for the GTSAM library.

%prep
%setup
%patch0 -p1
%patch1 -p1

# Several Python modules exposed from the compiled gtsam extension
# (gtsam.gtsam.gtsfm, gtsam.gtsam.imuBias, etc.) are not visible to RPM's
# Python dependency scanner, and the examples import PreintegrationExample
# by its bare name.  Suppress the bogus auto-generated Requires.
%add_python3_req_skip gtsam.gtsam.gtsfm gtsam.gtsam.imuBias gtsam.gtsam.noiseModel gtsam.gtsam.symbol_shorthand PreintegrationExample

%build
%cmake \
    -DGTSAM_WITH_TBB=ON \
    -DGTSAM_INSTALL_GEOGRAPHICLIB=OFF \
    -DGTSAM_USE_SYSTEM_METIS=ON \
    -DGTSAM_USE_SYSTEM_EIGEN=ON \
    -DMETIS_INCLUDE_DIR=%_includedir/metis \
    -DGTSAM_BUILD_PYTHON=ON \
    -DGTSAM_BUILD_TESTS=OFF \
    -DGTSAM_BUILD_EXAMPLES_ALWAYS=OFF \
    -DGTSAM_BUILD_TIMING_ALWAYS=OFF \
    -Wno-dev

%cmake_build

%install
%cmake_install

# CppUnitLite is built as a static LTO-only library; brp-alt rejects it.
# It is only needed to build unit tests, so drop it from the install tree.
rm -f %buildroot%_libdir/libCppUnitLite.a

# GTSAM's installed CMake exports still reference the deleted libCppUnitLite.a
# via the imported target "CppUnitLite", which makes find_package(GTSAM) fail
# with "references the file ... but this file does not exist". The target is
# an internal test helper, not part of the public API, so strip it from the
# installed export files.
sed -i '/foreach(_cmake_expected_target IN ITEMS metis-gtsam-if CppUnitLite gtsam)/s/ CppUnitLite//' \
    %buildroot%_libdir/cmake/GTSAM/GTSAM-exports.cmake
sed -i '/^# Create imported target CppUnitLite/,/^# Create imported target gtsam$/{/^# Create imported target gtsam$/!d}' \
    %buildroot%_libdir/cmake/GTSAM/GTSAM-exports.cmake
sed -i '/# Import target "CppUnitLite"/,/^$/d' \
    %buildroot%_libdir/cmake/GTSAM/GTSAM-exports-release.cmake
sed -i '/_cmake_import_check_targets CppUnitLite/d; /_cmake_import_check_files_for_CppUnitLite/d' \
    %buildroot%_libdir/cmake/GTSAM/GTSAM-exports-release.cmake

# gtwrap/pybind11 are only needed to generate the Python wrappers during the
# build; they should not be shipped as installed files.
rm -rf %buildroot/usr/bin/gtwrap
rm -rf %buildroot/usr/include/gtwrap
rm -rf %buildroot/usr/lib/cmake/gtwrap
rm -rf %buildroot/usr/lib/gtwrap

# Upstream does not install the Python modules via `cmake --install`.
# Copy the prebuilt extension packages from the build directory.
builddir=$(find . -maxdepth 1 -type d -name '*-alt-linux*' | head -1)
mkdir -p %buildroot%python3_sitelibdir
cp -a "$builddir/python/gtsam" %buildroot%python3_sitelibdir/
if [ -d "$builddir/python/gtsam_unstable" ]; then
    cp -a "$builddir/python/gtsam_unstable" %buildroot%python3_sitelibdir/
fi

# Python extension modules carry build-directory RPATH; remove it before
# verify-elf checks the installed files.
for so in %buildroot%python3_sitelibdir/gtsam/*.so \
          %buildroot%python3_sitelibdir/gtsam_unstable/*.so; do
    [ -f "$so" ] && chrpath -d "$so"
done

# Upstream copies gtsam_unstable tests using the full path instead of the
# basename, creating bogus /usr/src/RPM/BUILD/... directories under tests.
rm -rf %buildroot%python3_sitelibdir/gtsam_unstable/tests/usr

%files
%doc LICENSE README.md
%_libdir/libgtsam.so.*

%files -n libgtsam-devel
%_includedir/gtsam/
%_includedir/CppUnitLite/
%_libdir/libgtsam.so
%_libdir/cmake/GTSAM/
%_libdir/cmake/GTSAMCMakeTools/

%files -n libgtsam-unstable
%_libdir/libgtsam_unstable.so.*

%files -n libgtsam-unstable-devel
%_includedir/gtsam_unstable/
%_libdir/libgtsam_unstable.so
%_libdir/cmake/GTSAM_UNSTABLE/

%files -n python3-module-gtsam
%python3_sitelibdir/gtsam/
%python3_sitelibdir/gtsam_unstable/

%changelog
* Thu Aug 13 2026 Sergey Palcheh <minergenon@altlinux.org> 4.2.2-alt2
- Strip stale CppUnitLite target from installed CMake exports so that
  find_package(GTSAM) does not fail on the missing libCppUnitLite.a

* Sun Jul 12 2026 Sergey Palcheh <minergenon@altlinux.org> 4.2.2-alt1
- Initial build for Sisyphus
