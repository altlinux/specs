%def_disable clang
# TODO:
# libplugin-ipwatchd.so:
# undefined symbol: sd_bus_read_dict
%def_without ipwatchd

%define repo dde-services

Name: deepin-services
Version: 1.0.8
Release: alt1

Summary: Manage DBus service on DDE

License: LGPL-3.0-or-later
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dde-services
VCS: https://github.com/linuxdeepin/dde-services.git

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-dqt6
BuildRequires: cmake dqt6-base-devel dtk6-common-devel libdtk6gui-devel
%if_with ipwatchd
BuildRequires: libsystemd-devel glib2-devel libpcap-devel libnet2-devel
%endif
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.


%prep
%setup -n %repo-%version
%autopatch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
%DQ6build \
%if_without ipwatchd
  -DENABLE_PLUGIN_IPWATCHD=OFF \
%endif
#

%install
%DQ6install

%files
%doc LICENSE README.md
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libplugin-qt-thememanager.so
%_libdir/deepin-service-manager/libplugin-qt-wallpaperslideshow.so
%dir %_datadir/deepin-service-manager/
%if_with ipwatchd
%_libdir/deepin-service-manager/libplugin-ipwatchd.so
%_datadir/dbus-1/system.d/org.deepin.ipwatchd.conf
%dir %_datadir/deepin-service-manager/system/
%_datadir/deepin-service-manager/system/plugin-ipwatchd.json
%endif
%dir %_datadir/deepin-service-manager/user/
%_datadir/deepin-service-manager/user/plugin-qt-thememanager.json
%_datadir/deepin-service-manager/user/plugin-qt-wallpaperslideshow.json

%changelog
* Thu Jul 31 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.8-alt1
- Initial build for ALT Sisyphus.
