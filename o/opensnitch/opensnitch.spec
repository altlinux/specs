%define _unpackaged_files_terminate_build 1

%define import_path github.com/evilsocket/opensnitch

# Required to build the ebpf module
%define kver %(cat %_usrsrc/linux-*/include/config/kernel.release 2>/dev/null | cut -d'.' -f1,2)
%define kbuild_dir %(ls -d %_usrsrc/linux-* 2>/dev/null | head -n 1)
%ifarch %ix86 x86_64
%define arch_dir x86
%else
%define arch_dir %base_arch
%endif

# Pseudouser
%define _pseudouser_user _%name
%define _pseudouser_group _%name
%define _pseudouser_home %_localstatedir/%{name}d

Name: opensnitch
Version: 1.8.0
Release: alt1.gitf2ce074

Summary: OpenSnitch is a GNU/Linux port of the Little Snitch application firewall
License: GPL-3.0-or-later
Group: Networking/Other
Url: https://github.com/evilsocket/opensnitch
Vcs: https://github.com/evilsocket/opensnitch.git

Source0: %name-%version.tar
Source1: vendor.tar
Source2: protoc-gen-go-grpc.tar

ExclusiveArch: %go_arches

# opensnitch-daemon
BuildRequires(pre): rpm-build-golang
BuildRequires: libnetfilter_queue-devel
BuildRequires: protobuf-compiler
BuildRequires: protobuf-go
# opensnitch-daemon-ebpf
BuildRequires(pre): rpm-build-kernel
BuildRequires: bc
BuildRequires: clang
BuildRequires: kernel-headers-modules-%kernel_latest
BuildRequires: libelf-devel
BuildRequires: llvm

# opensnitch-ui
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python3
BuildRequires: python3-module-configargparse
BuildRequires: python3-module-grpcio
BuildRequires: python3-module-grpcio-tools
BuildRequires: python3-module-notify2
BuildRequires: python3-module-pyside6
BuildRequires: python3-module-PyQt6-devel
BuildRequires: python3-module-unicode_slugify
BuildRequires: qt6-tools

%description
%summary.

%package daemon
Summary: %summary
Group: Networking/Other

%description daemon
%summary.
This package contains opensnitch daemon.

%package ui
Summary: %summary
Group: Networking/Other
BuildArch: noarch
Requires: %name-daemon = %EVR
# The automation incorrectly identified provides
%filter_from_provides /tests/d
%filter_from_provides /opensnitch/d
# The automation incorrectly identified dependencies
Requires: python3-module-notify2

%add_python3_self_prov_path %buildroot%python3_sitelibdir_noarch

%description ui
%summary.
This package contains opensnitch ui.

%prep
%setup -a1 -a2

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

# Opensnitch requires a very specific version of protoc-gen-go-grpc
# See https://github.com/evilsocket/opensnitch/issues/1142
# Build the protoc-gen-go-grpc
pushd protoc-gen-go-grpc.d/grpc-go-8ba23be9613c672d40ae261d2a1335d639bdd59b/cmd/protoc-gen-go-grpc
%golang_build .
popd
# Add the compiled version of the protoc-gen-go-grpc to PATH
export PATH=$PATH:$PWD/.build/bin

%golang_prepare

# Build the opensnitch-daemon
pushd .build/src/%import_path/proto
%make clean
%make
popd
pushd .build/src/%import_path/daemon
go build -o opensnitchd .
popd
# Build the opensnitch-daemon-ebpf
pushd ebpf_prog
%make ARCH="%arch_dir" \
	KERNEL_VER="%kver" \
	KERNEL_DIR="%kbuild_dir" \
	KERNEL_HEADERS="%kbuild_dir" \
	EXTRA_FLAGS="-Wno-microsoft-anon-tag -fms-extensions"
popd

# Build the opensnitch-ui
pushd ui/i18n
%make
popd
pushd ui
pyside6-rcc opensnitch/res/resources.qrc | sed '0,/PySide6/s//PyQt6/' > opensnitch/resources_rc.py
find %name/proto -name 'ui_pb2_grpc.py' -exec sed -i 's/^import ui_pb2/from . import ui_pb2/' {} \;
%pyproject_build
popd

%install
# Path for installing opensnitch binaries
mkdir -p %buildroot%_bindir

# Path for installing ebpf modules
mkdir -p %buildroot%_libexecdir/%{name}d/ebpf

# Path for installing opensnitchd.service
mkdir -p %buildroot%_unitdir

# Path for installing opensnitch configuration files
mkdir -p %buildroot%_sysconfdir/%{name}d/rules

mkdir -p %buildroot%_pseudouser_home

# Install the opensnitch-daemon
install -Dpm 0644 utils/packaging/daemon/deb/debian/%{name}.service %buildroot%_unitdir/%{name}d.service
install -Dpm 0755 .build/src/%import_path/daemon/%{name}d %buildroot/%_bindir
pushd daemon/data
install -Dpm 0644 network_aliases.json %buildroot%_sysconfdir/%{name}d/network_aliases.json
install -Dpm 0644 system-fw.json %buildroot%_sysconfdir/%{name}d/system-fw.json
install -Dpm 0644 default-config.json %buildroot%_sysconfdir/%{name}d/default-config.json
popd
# Install the opensnitch-daemon-ebpf
install -Dpm 0644 ebpf_prog/%{name}*.o %buildroot/%_libexecdir/%{name}d/ebpf
# See https://www.altlinux.org/RPM/debuginfo
%brp_strip_none %_libexecdir/%{name}d/ebpf/%{name}*

# Install the opensnitch-ui
pushd ui
%pyproject_install
install -Dpm 0644 resources/opensnitch_ui.desktop %buildroot%_desktopdir/%{name}_ui.desktop
install -Dpm 0644 resources/icons/48x48/opensnitch-ui.png %buildroot%_liconsdir/%name-ui.png
install -Dpm 0644 resources/io.github.evilsocket.opensnitch.appdata.xml \
       %buildroot%_metainfodir/io.github.evilsocket.%name.appdata.xml
popd

# Incorrect installation of additional files
# The required files were installed manually above
rm -rv %buildroot%python3_sitelibdir_noarch/usr
rm -rv %buildroot%python3_sitelibdir_noarch/tests

%pre daemon
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'The %name daemon' \
	-d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%preun daemon
%preun_service %{name}d

%post daemon
%post_service %{name}d

%files daemon
%doc LICENSE README.md
%dir %attr(0770,root,%_pseudouser_group) %_pseudouser_home
%dir %_sysconfdir/%{name}d
%dir %_sysconfdir/%{name}d/rules
%_bindir/%{name}d
%dir %_libexecdir/%{name}d
%dir %_libexecdir/%{name}d/ebpf
%_libexecdir/%{name}d/ebpf/%{name}*
%_sysconfdir/%{name}d/*.json
%_unitdir/%{name}d.service

%files ui
%_bindir/%name-ui
%_desktopdir/%{name}_ui.desktop
%_liconsdir/%name-ui.png
%_metainfodir/io.github.evilsocket.%name.appdata.xml
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%{name}_ui-%version.dist-info

%changelog
* Wed Apr 01 2026 Ulysses Apokin <ulysses@altlinux.org> 1.8.0-alt1.gitf2ce074
- new version
- removed installation of unnecessary files (ALT #57612)
- added installation of metainfo file
- fixed FTBFS

* Wed Aug 13 2025 Ulysses Apokin <ulysses@altlinux.org> 1.7.2-alt1
- new version
- fixed post-install unowned files

* Fri Jun 27 2025 Ulysses Apokin <ulysses@altlinux.org> 1.7.0.0-alt1
- new version

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.0.0-alt5.b.git.5c8f710.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Jul 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt5.b.git.5c8f710
- fix BR: python3-module-PyQt5-devel

* Mon Sep 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt4.b.git.5c8f710
- Fixed build.

* Sun May 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt3.b.git5c8f710
- fixed build

* Fri Mar 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2.b.git5c8f710
- Updated to current upstream version (Closes: #36208)

* Fri May 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1.b.gitf71d8ce
- Initial build for ALT.
