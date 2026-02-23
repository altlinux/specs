%define _unpackaged_files_terminate_build 1

# TODO - make binfmt-bypass library at 
#        %%_libdir/appimagelauncher/libbinfmt-bypass-preload.so
#        debuggable
%global __find_debuginfo_files %nil

Name: appimagelauncher
Version: 2.2.0
Release: alt1

Summary: Integration of AppImages into the Linux desktop
License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/TheAssassin/AppImageLauncher

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: gcc-c++
BuildRequires: qt5-tools
BuildRequires: /usr/bin/wget
BuildRequires: /usr/bin/xxd
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(libappimage)
BuildRequires: libappimage-devel-static
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(libcurl)

%description
Integrate AppImages to your application launcher with one click, and
manage, update and remove them from there. Double-click AppImages to
open them, without having to make them executable first. 

AppImageLauncher plays well with other applications managing AppImages, 
for example app stores. However, it doesn't depend on any of those, and 
can run completely standalone.

%prep
%setup
%patch -p1
echo "tag v{%version}" > cmake/GIT_COMMIT

sed -i "s|https://github.com/TheAssassin/AppImageLauncher/raw/master/resources/doc/||" README.md
sed -i "s|https://github.com/TheAssassin/AppImageLauncher/raw/master/resources/icons|%_iconsdir|" README.md

sed -i "s|Categories=.*|Categories=Qt;Settings;PackageManager;|" resources/appimagelaunchersettings.desktop

%build
%cmake \
       -DBUILD_SHARED_LIBS:BOOL=OFF \
       -DCMAKE_BUILD_TYPE=Release \
       -DUSE_SYSTEM_LIBARCHIVE=ON \
       -DUSE_SYSTEM_LIBCURL=ON \
       -DUSE_SYSTEM_SQUASHFUSE=ON \
       -DUSE_SYSTEM_BOOST=ON \
       -DUSE_SYSTEM_CURL=ON \
       -DUSE_SYSTEM_XDGUTILS=ON \
       -DUSE_SYSTEM_LIBAPPIMAGE=ON \
       -DENABLE_UPDATE_HELPER=OFF \
       -DINSTALL_MAINTAINER_SCRIPTS=ON
%cmake_build

%install
%cmake_install

chmod +x %buildroot%_datadir/appimagelauncher/maintainer-scripts/post-install
chmod +x %buildroot%_datadir/appimagelauncher/maintainer-scripts/post-uninstall

%files
%doc LICENSE.txt README.md resources/doc/screenshot.png
%_bindir/AppImageLauncher
%_bindir/AppImageLauncherSettings
%_bindir/ail-cli
%_bindir/appimagelauncherd
%_usr/lib/binfmt.d/appimage.conf
%_userunitdir/appimagelauncherd.service
%dir %_libdir/appimagelauncher
%_libdir/appimagelauncher/binfmt-bypass
%_libdir/appimagelauncher/libbinfmt-bypass-preload.so
%_libdir/appimagelauncher/remove
%dir %_datadir/appimagelauncher
%dir %_datadir/appimagelauncher/fallback-icons
%_datadir/appimagelauncher/fallback-icons/*.svg
%dir %_datadir/appimagelauncher/l10n
%_datadir/appimagelauncher/l10n/desktopfiles.*.json
%_datadir/appimagelauncher/l10n/ui.*.qm
%dir %_datadir/appimagelauncher/maintainer-scripts
%_datadir/appimagelauncher/maintainer-scripts/post-install
%_datadir/appimagelauncher/maintainer-scripts/post-uninstall
%_desktopdir/appimagelauncher.desktop
%_desktopdir/appimagelaunchersettings.desktop
%_iconsdir/hicolor/*/apps/AppImageLauncher.png
%_iconsdir/hicolor/scalable/apps/AppImageLauncher.svg
%_man1dir/AppImageLauncher.1.*
%_datadir/mime/packages/appimage.xml

%changelog
* Mon Feb 23 2026 Nikolay Strelkov <snk@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
