%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
# due weak requires to libnvidia-ml
%set_verify_elf_method unresolved=relaxed

Name: nvidia-container-toolkit
Version: 1.17.8
Release: alt1

Summary: NVIDIA Container Toolkit
Group: System/Configuration/Hardware
Url: https://github.com/NVIDIA/nvidia-container-toolkit
Vcs: https://github.com/NVIDIA/nvidia-container-toolkit.git
License: Apache-2.0
Source: %name-%version.tar
Patch: go-no-strip.patch
Patch1: discover-alt.patch
Patch2: aarch64-stub.patch

BuildRequires: golang /proc

# x86 is not supported
# internal/dxcore/dxcore.go:55:2: type [1073741824]_Ctype_struct_dxcore_adapter too large
ExclusiveArch: x86_64 aarch64

Obsoletes: nvidia-container-runtime <= 3.5.0-1, nvidia-container-runtime-hook <= 1.4.0-2
Provides: nvidia-container-runtime
Provides: nvidia-container-runtime-hook
Requires: libnvidia-container-tools >= %version, libnvidia-container-tools < 2.0.0
Requires: nvidia-container-toolkit-base = %EVR

%description
Provides tools and utilities to enable GPU support in containers.

# The BASE package consists of the NVIDIA Container Runtime and the NVIDIA Container Toolkit CLI.
# This allows the package to be installed on systems where no NVIDIA Container CLI is available.
%package base
Summary: NVIDIA Container Toolkit Base
Group: System/Configuration/Hardware
Obsoletes: nvidia-container-runtime <= 3.5.0-1, nvidia-container-runtime-hook <= 1.4.0-2
Provides: nvidia-container-runtime
# Since this package allows certain components of the NVIDIA Container Toolkit to be installed separately
# it conflicts with older versions of the nvidia-container-toolkit package that also provide these files.
Conflicts: nvidia-container-toolkit <= 1.10.0-1
Requires: libnvidia-ml libcuda
%ifarch x86_64
Requires: libnvidia-sandboxutils
%endif

%description base
Provides tools such as the NVIDIA Container Runtime and NVIDIA Container Toolkit CLI to enable GPU support in containers.

# The OPERATOR EXTENSIONS package consists of components that are required to enable GPU support in Kubernetes.
# This package is not distributed as part of the NVIDIA Container Toolkit RPMs.
%package operator-extensions
Summary: NVIDIA Container Toolkit Operator Extensions
Group: System/Configuration/Hardware
Requires: nvidia-container-toolkit-base = %EVR

%description operator-extensions
Provides tools for using the NVIDIA Container Toolkit with the GPU Operator

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1

%build
CGO_CFLAGS='%optflags' %__make binaries

%install
mkdir -p %buildroot{%_bindir,%_sysconfdir/nvidia-container-runtime}
install -m 755 -t %buildroot%_bindir nvidia-container-runtime-hook
install -m 755 -t %buildroot%_bindir nvidia-container-runtime
install -m 755 -t %buildroot%_bindir nvidia-container-runtime.cdi
install -m 755 -t %buildroot%_bindir nvidia-container-runtime.legacy
install -m 755 -t %buildroot%_bindir nvidia-ctk
install -m 755 -t %buildroot%_bindir nvidia-cdi-hook

touch %buildroot%_sysconfdir/nvidia-container-runtime/config.toml
ln -svf %_bindir/nvidia-container-runtime-hook %buildroot%_bindir/nvidia-container-toolkit

%post
# Generate the default config; If this file already exists no changes are made.
if [ ! -s %_sysconfdir/nvidia-container-runtime/config.toml ]; then
	rm -f %_sysconfdir/nvidia-container-runtime/config.toml ||:
	%_bindir/nvidia-ctk --quiet config --config-file=%_sysconfdir/nvidia-container-runtime/config.toml --in-place
fi

%files
%_bindir/nvidia-container-runtime-hook
%_bindir/nvidia-container-toolkit

%files base
%doc LICENSE
%dir %_sysconfdir/nvidia-container-runtime
%ghost %attr(644,root,root) %config(missingok) %verify(not md5 mtime size) %_sysconfdir/nvidia-container-runtime/config.toml
%_bindir/nvidia-container-runtime
%_bindir/nvidia-ctk
%_bindir/nvidia-cdi-hook

%files operator-extensions
%_bindir/nvidia-container-runtime.cdi
%_bindir/nvidia-container-runtime.legacy

%changelog
* Fri Jul 18 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.17.8-alt1
- Build to Sisyphus (closes: #52483).

* Mon Jun 23 2025 L.A. Kostis <lakostis@altlinux.ru> 1.17.8-alt0.1
- Initial build for ALTLinux.

