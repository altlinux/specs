%define _unpackaged_files_terminate_build 1

Name: hexagonrpcd
Version: 0.4.0
Release: alt1
Summary: Qualcomm HexagonFS firmware loader
License: GPLv3
Group: System/Kernel and hardware
Url: https://github.com/linux-msm/hexagonrpc
VCS: https://github.com/linux-msm/hexagonrpc.git

ExclusiveArch: aarch64

Source: %name-%version.tar
Patch0: 0.4.0-build-fix-missing-headers-on-ALT.patch
Patch1: 0.4.0-add-systemd-units.patch
Patch2: 0.4.0-use-static-linkage.patch
Patch3: 0.4.0-remove-tools-compilation.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: glibc-kernheaders-generic

%description
HexagonRPCD is used to communicate with the Context Hub Runtime Environment, a
program on the DSP that manage sensors, and to serve files to remote processors.

%prep
%setup
%autopatch -p 1

%build
%meson -Dhexagonrpcd_verbose=true \
    -Dunitdir=%_unitdir \
    -Dkernel_headers_dir=%_includedir/linux-default/include \
    -Ddefault_library=static
%meson_build -v

%install
%meson_install

%files
%_bindir/hexagonrpcd
%_unitdir/hexagonrpcd*.service
%_man1dir/*

%changelog
* Mon Jul 06 2026 Vasiliy Doylov <neko@altlinux.org> 0.4.0-alt1
- Initial build for ALT.
