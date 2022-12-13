%def_disable clang

%define repo dde-app-services

Name: deepin-app-services
Version: 0.0.20
Release: alt1
Summary: Service collection of DDE applications
License: LGPL-3.0+
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dde-app-services

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake dtk5-widget-devel dtk5-common libgtest-devel

%description
%summary.

%prep
%setup -n %repo-%version

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DDVERSION=%version \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
chmod +x %buildroot%_datadir/bash-completion/completions/dde-dconfig

%files
%doc LICENSE README.md
%_bindir/dde-dconfig*
%_datadir/dbus-1/interfaces/org.desktopspec.ConfigManager*.xml
%_datadir/dbus-1/system.d/org.desktopspec.ConfigManager.conf
%_datadir/dbus-1/system-services/org.desktopspec.ConfigManager.service
%_datadir/bash-completion/completions/dde-dconfig
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/dconfig-example/
%dir %_datadir/dsg/configs/dconfig-example/a/
%dir %_datadir/dsg/configs/overrides/
%dir %_datadir/dsg/configs/overrides/dconfig-example/
%dir %_datadir/dsg/configs/overrides/dconfig-example/example/
%dir %_datadir/dsg/configs/overrides/dconfig-example/example/a/
%_datadir/dsg/configs/dconfig-example/example.json
%_datadir/dsg/configs/dconfig-example/a/example.json
%_datadir/dsg/configs/example.json
%_datadir/dsg/configs/overrides/dconfig-example/example/dconf-example.override.json
%_datadir/dsg/configs/overrides/dconfig-example/example/dconf-example.override.a.json
%_datadir/dsg/configs/overrides/dconfig-example/example/a/dconf-example.override.a.json

%changelog
* Tue Dec 13 2022 Leontiy Volodin <lvol@altlinux.org> 0.0.20-alt1
- Initial build for ALT Sisyphus.
