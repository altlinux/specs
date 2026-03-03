%global import_path github.com/NVIDIA/nvidia-container-toolkit

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# due weak requires to libnvidia-ml
%set_verify_elf_method unresolved=relaxed

%define git_commit 4ffedd8fc0f5fbb9c7b6c8015199cdc8bab47c89

Name: nvidia-container-toolkit
Version: 1.18.2
Release: alt1

Summary: NVIDIA Container Toolkit
Group: System/Configuration/Hardware
Url: https://github.com/NVIDIA/nvidia-container-toolkit
Vcs: https://github.com/NVIDIA/nvidia-container-toolkit.git
License: Apache-2.0

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

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
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="\
	-X %import_path/internal/info.version=%version \
	-X %import_path/internal/info.gitCommit=%git_commit \
"

%golang_prepare

%golang_build \
	cmd/nvidia-cdi-hook \
	cmd/nvidia-container-runtime-hook \
	cmd/nvidia-container-runtime.cdi \
	cmd/nvidia-container-runtime.legacy \
	cmd/nvidia-container-runtime \
	cmd/nvidia-ctk

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_sysconfdir/{nvidia-container-toolkit,nvidia-container-runtime}

touch %buildroot%_sysconfdir/nvidia-container-runtime/config.toml

ln -svf %_bindir/nvidia-container-runtime-hook %buildroot%_bindir/nvidia-container-toolkit

install -m 0644 deployments/systemd/nvidia-cdi-refresh.service %buildroot%_unitdir
install -m 0644 deployments/systemd/nvidia-cdi-refresh.path    %buildroot%_unitdir
install -m 0644 deployments/systemd/nvidia-cdi-refresh.env     %buildroot%_sysconfdir/nvidia-container-toolkit

%post
# Generate the default config; If this file already exists no changes are made.
if [ ! -s %_sysconfdir/nvidia-container-runtime/config.toml ]; then
	rm -f %_sysconfdir/nvidia-container-runtime/config.toml ||:
	%_bindir/nvidia-ctk --quiet config --config-file=%_sysconfdir/nvidia-container-runtime/config.toml --in-place
fi

%post base
%post_systemd nvidia-cdi-refresh.service

%preun base
%preun_systemd nvidia-cdi-refresh.service

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
%_unitdir/nvidia-cdi-refresh.service
%_unitdir/nvidia-cdi-refresh.path
%config(noreplace) %_sysconfdir/nvidia-container-toolkit/nvidia-cdi-refresh.env

%files operator-extensions
%_bindir/nvidia-container-runtime.cdi
%_bindir/nvidia-container-runtime.legacy

%changelog
* Mon Mar 02 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.18.2-alt1
- New version 1.18.2.
- Added systemd service (closes: #58034).

* Fri Jul 18 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.17.8-alt1
- Build to Sisyphus (closes: #52483).

* Mon Jun 23 2025 L.A. Kostis <lakostis@altlinux.ru> 1.17.8-alt0.1
- Initial build for ALTLinux.

