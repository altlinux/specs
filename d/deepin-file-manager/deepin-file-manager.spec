%define repo dde-file-manager

%def_disable clang

Name: deepin-file-manager
Version: 5.8.1
Release: alt1
Summary: Deepin File Manager
License: GPL-3.0+
Group: File tools
Url: https://github.com/linuxdeepin/dde-file-manager
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch1: deepin-file-manager-5.5.1-desktop.patch
Patch3: deepin-file-manager-5.2.0.87-alt-qterminal-instead-xterm.patch
Patch4: deepin-file-manager-5.5.1-hide-lockscreen-checkbox.patch
Patch5: deepin-file-manager-5.5.1-gcc11-fix-segfault.patch
Patch6: deepin-file-manager-5.5.1-alt-aarch64.patch

ExcludeArch: armh ppc64le

Requires: libdde-file-manager5 libdfm-extension5

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif

BuildRequires(pre): rpm-build-kf5
BuildRequires: git-core
BuildRequires: desktop-file-utils
BuildRequires: deepin-gettext-tools
BuildRequires: deepin-dock-devel
BuildRequires: libmagic-devel
BuildRequires: libjemalloc-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: libatk-devel
BuildRequires: dtk5-widget-devel
BuildRequires: dtk5-gui-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: libgtk+2-devel
BuildRequires: libsecret-devel
BuildRequires: libpoppler-cpp-devel
BuildRequires: libpolkit-devel
BuildRequires: libpolkitqt5-qt5-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libtag-devel
BuildRequires: libuchardet-devel
BuildRequires: libxcbutil-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: qt5-linguist
BuildRequires: udisks2-qt5-devel
BuildRequires: disomaster-devel
BuildRequires: qt5-tools
BuildRequires: libgio-qt-devel
BuildRequires: libssl-devel
BuildRequires: libqtxdg-devel
BuildRequires: libmediainfo-devel
BuildRequires: libpcre-devel
BuildRequires: libffmpegthumbnailer-devel
BuildRequires: libdmr-devel
BuildRequires: deepin-anything-devel
BuildRequires: liblucene++-devel
BuildRequires: libxml2-devel
BuildRequires: libhtmlcxx-devel
BuildRequires: libgsf-devel
BuildRequires: libmimetic-devel
BuildRequires: libdocparser-devel
BuildRequires: libcryptsetup-devel

# run command by QProcess
# Requires: deepin-shortcut-viewer deepin-terminal deepin-desktop file-roller gvfs samba xdg-user-dirs gst-plugins-good1.0-qt5
#Recommends:     deepin-manual
# dde-file-manager-lib/configure/global-setting-template-{fedora,pro,js}.js:2:13: error: Expected token `,'

%description
File manager front end of Deepin OS.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
Development files for %name.

%package -n lib%{repo}5
Summary: Library for %name
Group: System/Libraries

%description -n lib%{repo}5
Library for %name.

%package -n lib%repo-devel
Summary: Development files for lib%repo
Group: Development/Other

%description -n lib%repo-devel
Development files for lib%repo.

%package -n libdfm-extension5
Summary: Library for %name extensions
Group: System/Libraries

%description -n libdfm-extension5
Library for %name extensions.

%package -n libdfm-extension-devel
Summary: Development files for %name extensions
Group: Development/Other

%description -n libdfm-extension-devel
Development files for %name extensions.

%package -n deepin-desktop
Summary: Deepin desktop environment - desktop module
Group: Graphical desktop/Other
# Requires: deepin-dock deepin-launcher deepin-session-shell

%description -n deepin-desktop
Deepin desktop environment - desktop module.

%prep
%setup -n %repo-%version
# %%patch1 -p1
# %%patch3 -p1
%patch4 -p1
%patch5 -p1
# %%patch6 -p1

# sed -i 's|"groups":|"groups"\ :|' dde-file-manager-lib/configure/global-setting-template*.js

# fix file permissions
find -type f -perm 775 -exec chmod 644 {} \;
sed -i 's|/usr/lib/gvfs|/usr/libexec/gvfs|' \
    src/%repo-lib/gvfs/networkmanager.cpp
sed -i 's|/lib/dde-dock/plugins|/%_lib/dde-dock/plugins|' \
    src/dde-dock-plugins/disk-mount/disk-mount.pro

sed -i '/systembusconf.path/s|/etc/dbus-1/system.d|%_datadir/dbus-1/system.d|' \
    src/dde-file-manager-daemon/dde-file-manager-daemon.pro \
    tests/dde-file-manager-daemon/test-dde-file-manager-daemon.pro
sed -i 's|/usr/lib/systemd/system|%_unitdir|' \
   tests/dde-file-manager-daemon/test-dde-file-manager-daemon.pro
sed -i 's|$$PREFIX/lib/systemd/system|%_unitdir|' \
    src/dde-file-manager-daemon/dde-file-manager-daemon.pro
sed -i 's|/usr/lib32/libc.so.6|/%_lib/libc.so.6|' \
   tests/dde-file-manager-lib/io/ut_dfilestatisticsjob.cpp
sed -i 's|/usr/lib|%_libdir|' \
    src/dde-file-manager-lib/plugins/schemepluginmanager.cpp \
    tests/dde-file-manager-lib/views/ut_dfileview.cpp \
    tests/dde-desktop/src/grandsearchdaemon/ut_daemonplugin.cpp
#     dde-file-manager-lib/3rdParty/wv2/wv2.pri \
#     dde-file-manager-lib/3rdParty/charsetdetect/charsetdetect.pri
sed -i 's|#include <pcre.h>|#include <pcre/pcre.h>|' \
    3rdparty/fsearch/database_search.c

sed -i 's|/usr/bin/file-manager.sh|/usr/bin/dde-file-manager|' \
    src/dde-file-manager/mips/dde-file-manager.desktop

%if_enabled clang
# Fix build on aarch64
sed -i 's/| isEqual(ARCH, aarch64)//' \
    src/common/common.pri \
    src/dde-file-manager-lib/dde-file-manager-lib.pro
%endif

#%%ifarch aarch64
#sed -i 's|$$system($$PKG_CONFIG --variable libdir deepin-anything-server-lib)|%%_libdir|' \
#    deepin-anything-server-plugins/dde-anythingmonitor/dde-anythingmonitor.pro \
#    deepin-anything-server-plugins/test-deepin-anything-server-plugins.pro
#%%endif

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%define optflags_lto %nil
%endif

export PATH=%_qt5_bindir:$PATH
%qmake_qt5 \
           CONFIG+=nostrip \
%ifarch aarch64
           CONFIG+=DISABLE_ANYTHING \
%endif
           DEFINES+="VERSION=%version" \
           unix:LIBS+="-L%_libdir -lgio-2.0 -licui18n -lX11" \
           unix:LIBS+="-L%_K5link -lKF5Codecs" \
           QT.KCodecs.libs=%_K5link \
           PREFIX=%prefix \
           DTK_VERSION=%version \
           LIB_INSTALL_DIR=%_libdir \
           VERSION=%version \
%if_enabled clang
           QMAKE_STRIP= -spec linux-clang \
%endif
           filemanager.pro

%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

# %%check
# desktop-file-validate %%buildroot%%_desktopdir/%%repo.desktop
# desktop-file-validate %%buildroot%%_desktopdir/dde-computer.desktop ||:
# desktop-file-validate %%buildroot%%_desktopdir/dde-trash.desktop ||:

%files
%doc README.md LICENSE.txt
%_bindir/%repo
%_bindir/%repo-daemon
%_bindir/%repo-pkexec
%_bindir/dde-property-dialog
%_bindir/dde-select-dialog-x11
%_bindir/dde-select-dialog-wayland
%dir %_libdir/%repo/
%dir %_libdir/%repo/tools/
%dir %_libdir/%repo/tools/thumbnail/
%_libdir/%repo/tools/thumbnail/video*
%_datadir/%repo/
%_iconsdir/hicolor/scalable/apps/*.svg
%_desktopdir/%repo.desktop
%_datadir/dbus-1/interfaces/com.deepin.filemanager.filedialog.xml
%_datadir/dbus-1/interfaces/com.deepin.filemanager.filedialogmanager.xml
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.disk-mount.gschema.xml
%_datadir/glib-2.0/schemas/com.deepin.dde.filemanager.gschema.xml
%_datadir/dbus-1/services/com.deepin.filemanager.filedialog.service
%_datadir/dbus-1/services/org.freedesktop.FileManager.service
%_datadir/dbus-1/system-services/com.deepin.filemanager.daemon.service
%_datadir/dbus-1/system.d/com.deepin.filemanager.daemon.conf
%_unitdir/dde-filemanager-daemon.service
%_datadir/dbus-1/services/com.deepin.filemanager.filedialog_x11.service
%_datadir/dbus-1/services/com.deepin.filemanager.filedialog_wayland.service
%dir %_datadir/deepin/
%_datadir/deepin/%repo/
%_datadir/polkit-1/actions/com.deepin.filemanager.daemon.policy
%_datadir/polkit-1/actions/com.deepin.pkexec.dde-file-manager.policy
%_datadir/applications/context-menus/.readme
%_datadir/dsg/configs/org.deepin.dde.file-manager/org.deepin.dde.file-manager.json
# %%ifnarch aarch64
%dir %_libdir/deepin-anything-server-lib/
%dir %_libdir/deepin-anything-server-lib/plugins/
%dir %_libdir/deepin-anything-server-lib/plugins/handlers/
%_libdir/deepin-anything-server-lib/plugins/handlers/libdde-anythingmonitor.so
# %%endif
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%dir %_libdir/dde-dock/plugins/system-trays/
%_libdir/dde-dock/plugins/system-trays/libdde-disk-mount-plugin.so
%dir %_libdir/%repo/plugins/
%dir %_libdir/%repo/plugins/previews/
%_libdir/%repo/plugins/previews/*.so
%dir %_libdir/%repo/plugins/extensions/
%_libdir/%repo/plugins/extensions/.readme
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%repo/
%_datadir/deepin-manual/manual-assets/application/%repo/file-manager/

%files devel
%dir %_includedir/%repo/
%dir %_includedir/%repo/%repo-plugins/
%_includedir/%repo/%repo-plugins/*.h
# %%dir %%_includedir/%%repo/gvfs/
# %%_includedir/%%repo/gvfs/*.h
# %%dir %%_includedir/%%repo/private/
# %%_includedir/%%repo/private/*.h

%files -n lib%{repo}5
%_libdir/lib%repo.so.5*

%files -n lib%repo-devel
%dir %_includedir/%repo/
%_includedir/%repo/*.h
%_pkgconfigdir/%repo.pc
%_libdir/lib%repo.so

%files -n libdfm-extension5
%_libdir/libdfm-extension.so.5*

%files -n libdfm-extension-devel
%dir %_includedir/dfm-extension/
%_includedir/dfm-extension/*.h
%dir %_includedir/dfm-extension/emblemicon/
%_includedir/dfm-extension/emblemicon/*.h
%dir %_includedir/dfm-extension/menu/
%_includedir/dfm-extension/menu/*.h
%_libdir/libdfm-extension.so
%_pkgconfigdir/dfm-extension.pc

%files -n deepin-desktop
%_bindir/dde-desktop
%_desktopdir/dde-computer.desktop
%_desktopdir/dde-trash.desktop
%_desktopdir/dde-home.desktop
%_desktopdir/dde-open.desktop
%dir %_datadir/dde-desktop
%_datadir/dde-desktop/translations/
%dir %_datadir/dde-disk-mount-plugin
%_datadir/dde-disk-mount-plugin/translations/
%_datadir/dbus-1/services/com.deepin.dde.desktop.service

%changelog
* Tue Dec 06 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.1-alt1
- New version (5.8.1).

* Wed Nov 09 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.0-alt1
- New version (5.8.0).

* Mon Oct 03 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt2
- Fixed build with pcre.

* Tue Aug 16 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt1
- New version (5.6.4).

* Thu Jun 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.10-alt2
- Fixed gcc12 build.
- Returned desktop icons.

* Thu Apr 07 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.10-alt1
- New version (5.5.10).
- Changed group tag.

* Tue Mar 22 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.1-alt1
- New version (5.5.1).

* Thu Sep 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt5
- Fixed dde-disk-mount-plugin for i586.

* Fri Jun 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt4
- Hidden lockscreen checkbox more correctly.

* Thu Jun 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt3
- Fixed startup on aarch64 architecture.

* Sat Jun 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt2
- Hidden lockscreen checkbox.
- Fixed version tag.

* Mon Feb 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt1.1
- Rebuilt with Qt 5.15.2.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt1
- New version (5.2.0.87) with rpmgs script.

* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.85-alt1
- New version (5.2.0.85) with rpmgs script.

* Sat Dec 26 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.82-alt3
- Built with gcc10.

* Tue Dec 22 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.82-alt2
- Removed non-working shortcuts from the desktop.

* Mon Dec 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.82-alt1
- New version (5.2.0.82) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.76-alt2.git7ccae23
- Built from git.

* Tue Nov 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.76-alt1
- New version (5.2.0.76) with rpmgs script.

* Mon Nov 02 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.69-alt1
- New version (5.2.0.69) with rpmgs script.

* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.61-alt1
- New version (5.2.0.61) with rpmgs script.
- Removed requires.

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.59-alt1
- New version (5.2.0.59) with rpmgs script.

* Mon Sep 14 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.45-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
