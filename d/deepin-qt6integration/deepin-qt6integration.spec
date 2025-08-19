%define repo qt6integration

%def_without clang

Name: deepin-qt6integration
Version: 6.0.41
Release: alt1

Summary: Qt platform theme integration plugins for DDE

License: LGPL-3.0-or-later
Group: System/Libraries
Url: https://github.com/linuxdeepin/qt6integration
VCS: https://github.com/linuxdeepin/qt6integration

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: cmake dtk6-common-devel libdtk6widget-devel dqt6-base-devel libcups-devel libqt6xdg-devel libmtdev-devel

# Requires: deepin-qt6platform-plugins
Requires: libdqt6-core = %_dqt6_version libdqt6-gui = %_dqt6_version libdqt6-widgets = %_dqt6_version

%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
Multiple Qt plugins to provide better Qt6 integration for DDE is included.

%prep
%setup -n %repo-%version
%patch -p1

%build
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%DQ6build \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DPLUGIN_INSTALL_BASE_DIR=%_dqt6_plugindir \
  -DDTK_VERSION=%version \
#

%install
%DQ6install

%files
%doc README.md
%doc LICENSE
%doc CHANGELOG.md
%_dqt6_plugindir/iconengines/libdicon.so
%_dqt6_plugindir/iconengines/libdsvgicon.so
%_dqt6_plugindir/imageformats/libdci.so
%_dqt6_plugindir/imageformats/libdsvg.so
%_dqt6_plugindir/platformthemes/libqdeepin.so
%_dqt6_plugindir/styles/libchameleon.so

%changelog
* Tue Aug 19 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.41-alt1
- New version 6.0.41.

* Mon Jul 21 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.39-alt1
- New version 6.0.39.

* Fri Jun 20 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.37-alt1
- New version 6.0.37.

* Wed Apr 30 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.34-alt1
- Initial build for ALT Sisyphus.
