%define _unpackaged_files_terminate_build 1

%define rz_plugindir %_libdir/rizin/plugins
%define cutter_plugindir_native %_libdir/cutter/plugins/native

Name: rz-ghidra
Version: 0.9.0
Release: alt1

Summary: Deep ghidra decompiler and sleigh disassembler integration for rizin
License: LGPL-3.0-only
Group: Development/Tools
Url: https://github.com/rizinorg/rz-ghidra
VCS: https://github.com/rizinorg/rz-ghidra

Requires: rizin

# Source-url: https://github.com/rizinorg/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: rz-ghidra.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: cutter-re-devel
BuildRequires: libpugixml-devel
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-svg-devel
BuildRequires: rizin-devel
BuildRequires: zlib-devel
%ifarch %qt6_qtwebengine_arches
BuildRequires: qt6-webengine-devel
%endif

%description
This is an integration of the Ghidra decompiler and Sleigh Disassembler
for Rizin. It is solely based on the decompiler part of Ghidra, which
is written entirely in C++, so Ghidra itself is not required at all and
the plugin can be built self-contained.

%package devel
Summary: Development files for the %name package
Group: Development/Tools
Requires: %name = %EVR

%description devel
Development files for the %name package.

%package -n %name-cutter
Summary: Cutter plugin
Group: Development/Tools
Requires: %name = %EVR
Requires: cutter-re

%description -n %name-cutter
%summary

%prep
%setup
%patch1 -p1
tar xvf %SOURCE1 -C ghidra/ghidra

%build
%cmake \
    -DUSE_SYSTEM_PUGIXML=ON \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DRZGHIDRA_VERSION=%version \
    -DBUILD_CUTTER_PLUGIN=ON \
    -DCUTTER_INSTALL_PLUGDIR=%cutter_plugindir_native \
    #
%cmake_build

%install
%cmake_install

# Create symlinks to dynamically loaded plugins
%__install -d %buildroot%_libdir
find %buildroot%rz_plugindir -name '*_ghidra.so' | while read i ; do
	ln -sr $i %buildroot%_libdir/
done

%files
%doc README.md
%dir %rz_plugindir/rz_ghidra_sleigh
%_libdir/*_ghidra.so
%rz_plugindir/*_ghidra.so
%rz_plugindir/rz_ghidra_sleigh/*

%files devel
%_includedir/*.h
%_pkgconfigdir/rz_*.pc

%files -n %name-cutter
%cutter_plugindir_native/*_cutter.so

%changelog
* Tue Jun 23 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.9.0-alt1
- new version

* Wed Jun 11 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux
