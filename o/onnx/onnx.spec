%define _unpackaged_files_terminate_build 1
%define pypi_name onnx
%define mod_name %pypi_name

%def_with check

%python3_set_limited_api

%define abiversion 1
Name: onnx
Version: 1.22.0
Release: alt1

Summary: Open standard for machine learning interoperability
License: Apache-2.0
Group: Development/Other
Url: https://pypi.org/project/onnx/
Vcs: https://github.com/onnx/onnx

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires(pre): rpm-build-cmake
%add_pyproject_deps_build_filter ninja
%add_pyproject_deps_build_filter protobuf
%pyproject_builddeps_build
BuildRequires: python3-module-nanobind
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: protobuf-compiler
BuildRequires: libprotobuf-devel
BuildRequires: pybind11-devel
%if_with check
%add_pyproject_deps_check_filter lintrunner
%pyproject_builddeps_metadata_extra reference
%pyproject_builddeps_check
BuildRequires: python3-module-numpy-testing
%endif

%description
%summary.

%package -n lib%name%abiversion
Summary: Shared libraries for %name
Group: System/Libraries

%description -n lib%name%abiversion
%summary.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel
%summary.

%package -n python3-module-%pypi_name
Summary: Python module for %name
Group: Development/Python3
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata

%description -n python3-module-%pypi_name
%summary.

%prep
%setup
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
export nanobind_DIR=%python3_sitelibdir_noarch/nanobind/cmake
%cmake \
    -DBUILD_SHARED_LIBS=1 \
    -DONNX_USE_PROTOBUF_SHARED_LIBS=1 \
    -DONNX_HARDENING=1
%cmake_build
%pyproject_build

%install
%cmake_install
%pyproject_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
cd %buildroot%python3_sitelibdir
python3 -m pytest -vra -p no:cacheprovider -o=addopts=-Wignore

%files -n lib%name%abiversion
%_libdir/libonnx.so.%abiversion
%_libdir/libonnx.so.%abiversion.*
%_libdir/libonnx_proto.so.%abiversion
%_libdir/libonnx_proto.so.%abiversion.*

%files -n lib%name-devel
%_libdir/libonnx.so
%_libdir/libonnx_proto.so
%_cmakedir/ONNX/
%_includedir/onnx/

%files -n python3-module-%pypi_name
%_bindir/backend-test-tools
%_bindir/check-*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 06 2026 Anton Zhukharev <ancieg@altlinux.org> 1.22.0-alt1
- Updated to 1.22.0.

* Mon Mar 30 2026 Anton Zhukharev <ancieg@altlinux.org> 1.21.0-alt1
- Updated to 1.21.0 (fixes GHSA-hqmj-h5c6-369m).

* Thu Mar 19 2026 Anton Zhukharev <ancieg@altlinux.org> 1.20.1-alt1
- Updated to 1.20.1.

* Thu Nov 13 2025 Anton Zhukharev <ancieg@altlinux.org> 1.18.0-alt4
- Cleaned up packaging scheme after 1.18.0-alt3.

* Thu Nov 13 2025 Nikita Shmatko <nash@altlinux.org> 1.18.0-alt3
- NMU: Disabled symbol visibility hiding (Closes: #55423).

* Mon Jul 21 2025 Anton Zhukharev <ancieg@altlinux.org> 1.18.0-alt2
- Fixed RPM-packages summaries and descriptions.

* Fri Jul 18 2025 Anton Zhukharev <ancieg@altlinux.org> 1.18.0-alt1
- Packaged for ALT Sisyphus.
