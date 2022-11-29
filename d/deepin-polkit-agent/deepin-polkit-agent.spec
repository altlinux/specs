%define repo dde-polkit-agent

%def_disable clang

Name: deepin-polkit-agent
Version: 5.5.21
Release: alt1
Summary: Deepin Polkit Agent
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-polkit-agent
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake dtk5-core-devel dtk5-widget-devel dtk5-common deepin-qt-dbus-factory-devel libpolkitqt5-qt5-devel qt5-tools-devel

%description
DDE Polkit Agent is the polkit agent used in Deepin Desktop Environment.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other
BuildArch: noarch

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%cmake \
	-GNinja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	%nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files
%doc README.md
%doc LICENSE
%dir %_libexecdir/polkit-1-dde
%_libexecdir/polkit-1-dde/%repo
%_datadir/%repo/

%files devel
%dir %_includedir/dpa/
%_includedir/dpa/agent-extension-proxy.h
%_includedir/dpa/agent-extension.h

%changelog
* Tue Nov 29 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.21-alt1
- New version (5.5.21).

* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.12-alt1
- New version (5.4.12).

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.7-alt1
- New version (5.4.7).

* Tue Apr 27 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.3-alt2
- Changed location of the libraries.

* Wed Nov 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.3-alt1
- New version (5.3.0.3) with rpmgs script.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.2-alt1
- New version (5.3.0.2) with rpmgs script.

* Mon Aug 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.7-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

