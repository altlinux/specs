# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: OpenBoard
Version: 1.7.7
Release: alt1
Summary: Interactive whiteboard for schools and universities
Summary(ru_RU.UTF-8): Интерактивная доска для школ и университетов
License: GPL-3.0-or-later
Group: Education
URL: https://openboard.ch/index.en.html
VCS: https://github.com/OpenBoard-org/OpenBoard

ExcludeArch: %not_qt6_qtwebengine_arches

Source: %name-%version.tar

Source1: %name.svg

# GeoInfo widget with a version with modified borders of Ukraine and Russia from ThomasLucky13
Source2: GeoInfo.wgt.tar.gz

Source3: openboard.xml

# https://github.com/OpenBoard-org/OpenBoard/pull/648
Patch1: 0001-OpenBoard-1.7.7-update-russian-translations.patch
Patch2: 0002-dark-background-color-set-ability-feature.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/635
Patch3: 0003-new-icon-images.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/714
Patch4: 0004-toolbar_elements_changed.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/714
Patch6: 0006-polygon_line_styles.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/712
Patch8: 0008-background-grid-size-save.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/714
Patch9: 0009-vector_tool.patch
Patch10: 0010-alt-Fix-disappiearing-components-of-dashed-and-dotte.patch
Patch11: 0011-fix-videoSize-saving.patch
Patch13: 0013-Changes-for-dark-mode.patch
Patch14: 0014-widgets-names-ru_translate.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/809
Patch16: 0016-UBCompassTool-upgrade.patch
# Patch changes:
# - Added help buttons to the toolbar
Patch18: 0018-Add-help-buttons.patch
Patch19: 0019-add-ru-translate-for-startupHints.patch
Patch20: 0020-showMaximized-when-open.patch
Patch21: 0021-set-web-search-engine-to-yandex.patch
Patch22: 0022-fix-documents-view.patch
Patch23: 0023-improvement-tool-change.patch
Patch24: 0024-fix-problem-with-multiscreen.patch
Patch25: 0025-multi-touch.patch
Patch26: 0026-remove-swipe-pages.patch
# Build with C++20 for Poppler v24.04 and newer
# https://github.com/OpenBoard-org/OpenBoard/issues/958
Patch28: 0028-add-Oblique-Seyes-Ruled-Background.patch
Patch100: build-with-c++20.patch
# disable update check and startup hints
Patch101: 0100-alt-settings.patch

BuildRequires(pre): rpm-macros-qt6 rpm-macros-qt6-webengine
BuildRequires: gcc-c++ libgomp-devel
BuildRequires: desktop-file-utils
BuildRequires: libpaper-devel
BuildRequires: libssl-devel
BuildRequires: quazip-qt6-devel
BuildRequires: t1lib-devel
BuildRequires: libavcodec-devel libavformat-devel libswscale-devel libswresample-devel
BuildRequires: libalsa-devel libvpx-devel libvorbis-devel libtheora-devel libogg-devel
BuildRequires: libopus-devel liblame-devel libass-devel
BuildRequires: liblzma-devel bzlib-devel
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Help)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6MultimediaWidgets)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6PrintSupport)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6UiTools)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)
BuildRequires: pkgconfig(Qt6Xml)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(poppler)
BuildRequires: pkgconfig(poppler-cpp)
BuildRequires: pkgconfig(sdl)

Requires: onboard
Requires: /sbin/pidof

%description
Interactive whiteboard for schools and universities.

%description -l ru_RU.UTF-8
Интерактивная доска для школ и университетов

%prep
%setup -a2
%autopatch -p1

# remove unwanted and nonfree libraries
sed -i -e 's|-lfdk-aac ||' src/podcast/podcast.pri
sed -i -e 's|-lx264 ||' src/podcast/podcast.pri

# drop quazip LIBS INCLUDEPATH
sed -i  -e '/LIBS += -lquazip6/d' \
	OpenBoard.pro

# Removed some map widgets because of incorrect display of borders of Ukraine and Russia
rm -vr resources/library/applications/GoogleMaps.wgt
rm -vr resources/library/applications/OpenStreetMap.wgt

# Replacement of the GeoInfo widget with a version with modified borders of Ukraine and Russia
rm -vr resources/library/applications/GeoInfo.wgt
mv GeoInfo.wgt resources/library/applications/GeoInfo.wgt

rm -v resources/etc/OpenBoard.css

%build
%qmake_qt6 \
    LIBS+="`pkg-config --libs quazip1-qt6`" \
    INCLUDEPATH+="`pkg-config --cflags-only-I quazip1-qt6 |
      sed 's/-I//g'`" \
    INCLUDEPATH+=%_includedir/poppler \
    %name.pro
%make_build

%install
%makeinstall_std
install -D -m 0644 %SOURCE1 %buildroot%_iconsdir/hicolor/scalable/apps/OpenBoard.svg

# missing desktop file, creating one
mkdir -p %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
GenericName=%name
Comment=Interactive whiteboard for schools and universities
Comment[ru]=Интерактивная доска для школ и университетов
Exec=%_bindir/openboard "%f"
Icon=%name
StartupNotify=true
Terminal=false
Type=Application
MimeType=application/x-%name;
Categories=Education;Engineering;
EOF

install -D -m 0755 build/linux/release/product/OpenBoard %buildroot%_libdir/%name/OpenBoard
cp -r build/linux/release/product/* %buildroot%_libdir/%name/

#run.sh (set env to avoid some possible issues)
cat > %buildroot%_libdir/%name/run.sh <<EOF
#!/bin/bash
# --------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------------------------------------------

if pid="\$(/sbin/pidof OpenBoard)"; then
    echo "OpenBoard is already running, PID \${pid}."
    exit 0
fi

env QT_PLUGIN_PATH=\$QT_PLUGIN_PATH:%_libdir/%name/plugins LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:%_libdir/%name/plugins/cffadaptor %_libdir/%name/OpenBoard "\$@"
EOF

chmod 0755 %buildroot%_libdir/%name/run.sh
mkdir -p %buildroot/%_bindir/
ln -s -T %_libdir/%name/run.sh %buildroot/%_bindir/openboard

mkdir -p %buildroot%_datadir/mime/packages/
install -m644 %SOURCE3 %buildroot%_datadir/mime/packages/
# make sure that MIME xml and desktop file are in sync
grep -q '^MimeType=application/x-OpenBoard;'  %buildroot%_datadir/applications/%name.desktop

# clean some exe bits
find %buildroot -executable -type f -name *.js -exec chmod -x '{}' \+
find %buildroot -executable -type f -name *.svg -exec chmod -x '{}' \+
find %buildroot -executable -type f -name *.css -exec chmod -x '{}' \+
find %buildroot -executable -type f -name *.xml -exec chmod -x '{}' \+
find %buildroot -executable -type f -name *.html -exec chmod -x '{}' \+

# internalization
lrelease-qt6 -removeidentical %name.pro
mkdir -p %buildroot%_libdir/%name/i18n/
cp -R resources/i18n/%{name}*.qm %buildroot%_libdir/%name/i18n/

# customizations
cp -R resources/customizations %buildroot%_libdir/%name/

# remove broken search widgets
rm -r %buildroot%_libdir/%name/library/search

%files
%doc COPYRIGHT LICENSE
%_bindir/openboard
%_libdir/%name
%_desktopdir/%name.desktop
%_datadir/mime/packages/openboard.xml
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Wed Apr 08 2026 Valery Zabrovsky <brow@altlinux.org> 1.7.7-alt1
- New version 1.7.7.

* Tue Nov 25 2025 Ivan A. Melnikov <iv@altlinux.org> 1.7.3-alt7
- Fix the fix for erasing of dashed and dotted lines (ALT#56884).

* Sat Nov 08 2025 Anton Midyukov <antohami@altlinux.org> 1.7.3-alt6
- Do not use xwayland always.
- Remove broken search widgets.

* Wed Aug 27 2025 Ivan A. Melnikov <iv@altlinux.org> 1.7.3-alt5
- Build with Qt6
- Don't build on architectures that don't have qt6-webengine
- Rewrite workaround for disappearing dotted and dashed line
  components

* Sat Aug 02 2025 Anton Midyukov <antohami@altlinux.org> 1.7.3-alt4
- add Oblique Seyes Ruled Background

* Sat Aug 02 2025 Anton Midyukov <antohami@altlinux.org> 1.7.3-alt3
- Disable check update and startup hints by default.

* Wed Jun 18 2025 Anton Midyukov <antohami@altlinux.org> 1.7.3-alt2
- Run with QT_QPA_PLATFORM=xcb on wayland

* Wed Jun 18 2025 Anton Midyukov <antohami@altlinux.org> 1.7.3-alt1
- New version 1.7.3
- Open *.ubz mime type via OpenBoard

* Fri Dec 13 2024 Anton Midyukov <antohami@altlinux.org> 1.7.1-alt3
- fix build with ffmpeg 7.1

* Wed Oct 09 2024 Anton Midyukov <antohami@altlinux.org> 1.7.1-alt2
- Remove Google Maps widget

* Sat Jun 29 2024 Anton Midyukov <antohami@altlinux.org> 1.7.1-alt1
- New version 1.7.1.
- ExcludeArch: ppc64le

* Sat Sep 09 2023 Anton Midyukov <antohami@altlinux.org> 1.6.4-alt4
- add upstream patches for fix build with ffmpeg-6.0

* Mon Dec 26 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.4-alt3
- Added the patch for restore video size when it loading from a document:
  (https://github.com/OpenBoard-org/OpenBoard/issues/715)
- Removed some map widgets because of incorrect display of borders of Ukraine and Russia.
  Will return after fixing the inaccuracy.
- Added GeoInfo widget with the correct borders of Ukraine and Russia (thanx for ThomasLucky13)

* Tue Nov 29 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.4-alt2
- Several patches replaced and one removed
- css file removed

* Mon Oct 10 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.4-alt1
- new version 1.6.4
- Patches adapted and assembled into a patchset. Unnecessary patches removed

* Fri Sep 30 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.3-alt6
- Adding the patch with a new drawing element - vector and the patch with russian translation of it

* Mon Sep 26 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.3-alt5
- Adding the patch for increasing the gaps in the dotted line style
- Adding the patch with ability for changing line selection using StrokesGroup item
- Adding the patch with ability for saving background grid size when it has been changed

* Mon Aug 29 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.3-alt4
- Adding the patch with new icon images
- Adding the patch with ability for draw dashed and dotted lines
- Adding the patch with ability for running in a window
- Removed widget GeoInfo because of incorrect display of borders of Ukraine and Russia. Will return after fixing the inaccuracy.

* Fri Jul 08 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.3-alt3
- Fixed the program version in the text from the copyrightTextBrowser widget (Closes: 43124)

* Thu Jun 23 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.3-alt2
- Fix of patch with russian translation for 1.6.3

* Wed Jun 22 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.3-alt1
- new version 1.6.3
- Update russian translation for 1.6.3
- Remove patches merged to upstream
- Cleaned up spec

* Tue Apr 19 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.1-alt8
- Adding the patch for russian translation of GraphMe widget

* Tue Apr 12 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.1-alt7
- Adding a license to the icon
- Adding the patch for increasing the call area of the submenu
- Adding the patch for ability to set the color of the dark background in the configuration
- Adding the patch for stylus palette icons replacing from png to svg

* Wed Mar 23 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.1-alt6
- Update russian translation for 1.6.1
- Multiple app instances run ability disabling
- Replacing the icon from png to svg

* Fri Mar 18 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.1-alt5
- adapted for build with libpoppler-devel-21.11.0 and libpoppler-devel-22.03.0

* Thu Mar 17 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.1-alt4
- fix build with poppler-22

* Sat Jan 01 2022 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt3
- realy fix build with libquazip1-qt5

* Sat Jan 01 2022 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt2
- fix build with libquazip1-qt5

* Fri Oct 22 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.6.1-alt1
- new version 1.6.1
- Removing patches merged to upstream

* Wed Mar 24 2021 Anton Midyukov <antohami@altlinux.org> 1.5.4-alt3
- Update Russian translation

* Mon Oct 26 2020 Anton Midyukov <antohami@altlinux.org> 1.5.4-alt2
- Requires onboard (Closes: 39119)

* Sat Mar 28 2020 Anton Midyukov <antohami@altlinux.org> 1.5.4-alt1
- new version 1.5.4

* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 1.5.3-alt1
- new version 1.5.3

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt3
- NMU: remove rpm-build-ubt from BR:

* Sun Mar 31 2019 Anton Midyukov <antohami@altlinux.org> 1.5.2-alt2
- Update patchs (Fix FTBFS) (Thanks Mageia Team)

* Thu Feb 14 2019 Anton Midyukov <antohami@altlinux.org> 1.5.2-alt1
- new version 1.5.2

* Sat Nov 17 2018 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- new version 1.4.1

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt3.1%ubt
- NMU: Rebuild with new openssl 1.1.0.

* Fri Jul 27 2018 Anton Midyukov <antohami@altlinux.org> 1.3.6-alt3%ubt
- Fix build with libpoppler >= 0.64

* Sun Jul 08 2018 Anton Midyukov <antohami@altlinux.org> 1.3.6-alt2%ubt.1
- Rebuilt for aarch64

* Wed Jan 31 2018 Anton Midyukov <antohami@altlinux.org> 1.3.6-alt2%ubt
- Fix build for ALT Sisyphus.

* Mon Nov 13 2017 Anton Midyukov <antohami@altlinux.org> 1.3.6-alt1%ubt
- Initial build for ALT Sisyphus.
