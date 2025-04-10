%define repo dde-appearance

%def_disable clang

Name: deepin-appearance
Version: 1.1.58
Release: alt1

Summary: Set the theme and appearance of DDE

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-appearance
Vcs: https://github.com/linuxdeepin/dde-appearance.git

Provides: %repo = %EVR

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: cmake dqt6-tools-devel dqt6-declarative-devel dtk6-common-devel libdtk6gui-devel kf6-kconfig-devel kf6-kwindowsystem-devel kf6-kglobalaccel-devel libgio-devel libXcursor-devel libXfixes-devel libgtk+3-devel libxcbutil-cursor-devel libsystemd-devel
%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif

%description
%summary.

%prep
%setup -n %repo-%version

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%DQ6build

%install
%DQ6install
%find_lang --with-qt plugin-dde-appearance

%files -f plugin-dde-appearance.lang
%doc README.md
%_bindir/dde-fakewm
%_userunitdir/dde-fakewm.service
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libplugin-dde-appearance.so
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/user/
%_datadir/deepin-service-manager/user/plugin-dde-appearance.json
%dir %_datadir/%repo/
%_datadir/%repo/custom.png
# package outside find_lang
%dir %_datadir/plugin-dde-appearance/
%dir %_datadir/plugin-dde-appearance/translations/
%_datadir/plugin-dde-appearance/translations/dde-appearance_ky@Arab.qm
# ---
%_datadir/dbus-1/services/com.deepin.wm.service
%_datadir/dbus-1/services/org.deepin.dde.Appearance1.service
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.appearance/
%_datadir/dsg/configs/org.deepin.dde.appearance/org.deepin.dde.appearance.json

%changelog
* Thu Apr 10 2025 Leontiy Volodin <lvol@altlinux.org> 1.1.58-alt1
- New version 1.1.58.
- Added vcs tag.
- Switched to dqt6.

* Wed Oct 16 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.34-alt1
- New version 1.1.34.

* Mon May 27 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.28-alt1
- New version 1.1.28.
- Built via separate qt5 instead system (ALT #48138).

* Tue Mar 26 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.26-alt1
- New version 1.1.26.

* Tue Jan 30 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.25-alt1
- New version 1.1.25.

* Fri Dec 08 2023 Leontiy Volodin <lvol@altlinux.org> 1.1.7-alt1.git9f81088
- Initial build for ALT Sisyphus.
