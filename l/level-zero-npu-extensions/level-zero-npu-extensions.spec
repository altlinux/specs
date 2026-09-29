%define _unpackaged_files_terminate_build 1

Name: level-zero-npu-extensions
Version: 1.19
Release: alt1

Summary: oneAPI Level Zero extensions for Intel NPU
License: MIT
Group: Development/C
Url: https://github.com/intel/level-zero-npu-extensions
Vcs: https://github.com/intel/level-zero-npu-extensions

ExclusiveArch: x86_64

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: gcc-c++
BuildRequires: libze-devel

%description
Level Zero extension API headers for Intel NPU (graph, profiling, command
queue, context and driver extensions).

%package devel
Summary: oneAPI Level Zero extension headers for Intel NPU
Group: Development/C
Requires: libze-devel

%description devel
This package contains Level Zero extension API headers for Intel NPU (graph,
profiling, command queue, context and driver extensions) used by the NPU
driver and the OpenVINO NPU plugin.

%prep
%setup
%autopatch -p1

%install
mkdir -p %buildroot%_includedir/level_zero
install -pm644 ze_*.h %buildroot%_includedir/level_zero/

%files devel
%doc LICENSE.txt README.md CHANGELOG.md
%_includedir/level_zero/ze_command_queue_npu_ext.h
%_includedir/level_zero/ze_context_npu_ext.h
%_includedir/level_zero/ze_driver_npu_ext.h
%_includedir/level_zero/ze_graph_ext.h
%_includedir/level_zero/ze_graph_profiling_ext.h
%_includedir/level_zero/ze_intel_npu_uuid.h

%changelog
* Wed Sep 23 2026 Artem Krasovskiy <aibure@altlinux.org> 1.19-alt1
- Initial build for Sisyphus.
