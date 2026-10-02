%define _unpackaged_files_terminate_build 1
%global translation_domain kcm_fcitx5

Name: fcitx5-configtool
Version: 5.1.16
Release: alt1

Summary: Configuration tools used by fcitx5
License: GPLv2+
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-configtool
Vcs: https://github.com/fcitx/fcitx5-configtool

Source: %name-%version.tar.xz

# to display scalable icons
Requires: libqt6-svg
# explicit requires on fcitx5-qt
Requires: fcitx5-qt

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat rpm-build-kf6
BuildRequires: /usr/bin/desktop-file-install
BuildRequires: /usr/bin/gettext
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(zlib)
BuildRequires: qt6-base-devel
BuildRequires: gnupg2
BuildRequires: ctest cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: fcitx5-qt-devel
BuildRequires: gettext-tools libasprintf-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: cmake(Fcitx5Core)
BuildRequires: cmake(Fcitx5Utils)
#BuildRequires: kf5-plasma-framework-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-svg-devel
BuildRequires: pkgconfig(iso-codes)
#BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(xkbfile)
#BuildRequires: /usr/bin/appstream-util
BuildRequires: plasma6-lib-devel
BuildRequires: kf6-ksvg-devel
BuildRequires: kf6-kcmutils-devel

%description
Configuration tools used by fcitx5.

%package -n kcm-fcitx5
Group: Graphical desktop/Other
Summary: Config tools to be used on KDE based environment
Requires: kf6-filesystem
Requires: libkf6kcmutils libkf6kcmutilscore
Requires: %name = %EVR

%description -n kcm-fcitx5
Config tools to be used on KDE based environment. Can be installed seperately.

%package -n fcitx5-migrator
Group: Graphical desktop/Other
Summary: Migration tools for fcitx5
Requires: %name = %EVR

%description -n fcitx5-migrator
Migration tools for fcitx5, containing fcitx5-migrator

%package -n fcitx5-migrator-devel
Group: Graphical desktop/Other
Summary: Devel files for fcitx5-migrator
Requires: fcitx5-migrator = %EVR

%description -n fcitx5-migrator-devel
Development files for fcitx5-migrator

%prep
%setup

#fix typos
sed -i 's/Catogories/Categories/g' src/configtool/org.fcitx.fcitx5-config-qt.desktop.in
sed -i 's/Catogories/Categories/g' src/migrator/app/org.fcitx.fcitx5-migrator.desktop.in

%build
%fedora_v2_cmake -GNinja
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install
# kservices5/*.desktop desktop file dont't need to use desktop-file-install
# only for applications/*.desktop
for desktop_file_name in kbd-layout-viewer5 org.fcitx.fcitx5-config-qt org.fcitx.fcitx5-migrator
do
desktop-file-install --delete-original \
  --dir %buildroot%_datadir/applications \
  %buildroot%_datadir/applications/${desktop_file_name}.desktop
done
#appdata fileREADME is missing
#sed "/icon/d" -i %buildroot%_metainfodir/%translation_domain.appdata.xml
#appstream-util validate-relax --nonet %buildroot%_metainfodir/*.appdata.xml
%find_lang %name
%find_lang %translation_domain

%files -f %name.lang
%doc --no-dereference LICENSES/GPL-2.0-or-later.txt
%doc README.md
%_K6bin/fcitx5-config-qt
%_K6bin/kbd-layout-viewer5
%_datadir/applications/org.fcitx.fcitx5-config-qt.desktop
%_datadir/applications/kbd-layout-viewer5.desktop

%files -n kcm-fcitx5 -f %translation_domain.lang
%doc --no-dereference LICENSES/GPL-2.0-or-later.txt
%_K6plug/plasma/kcms/systemsettings/kcm_fcitx5.so
%_K6bin/fcitx5-plasma-theme-generator
%_desktopdir/kcm_fcitx5.desktop

%files -n fcitx5-migrator
%_K6bin/fcitx5-migrator
%_libdir/libFcitx5Migrator.so.5*
%_libdir/libFcitx5Migrator.so.1
%_datadir/applications/org.fcitx.fcitx5-migrator.desktop

%files -n fcitx5-migrator-devel
%_libdir/libFcitx5Migrator.so

%changelog
* Thu Oct 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.1.16-alt1
- 5.1.1 -> 5.1.16 (ALT #52992)

* Thu Dec 14 2023 Kirill Izmestev <felixz@altlinux.org> 5.1.1-alt3_1
- fixed build for p10 (ALT #48268)

* Mon Oct 30 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt2_1
- fixed build

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_1
- update

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.15-alt1_1
- new version

