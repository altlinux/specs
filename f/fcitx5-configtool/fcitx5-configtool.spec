Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat rpm-build-kf5
BuildRequires: /usr/bin/desktop-file-install /usr/bin/gettext pkgconfig(bzip2) pkgconfig(expat) pkgconfig(libbrotlidec) pkgconfig(libpcre2-8) pkgconfig(libpng) pkgconfig(uuid) pkgconfig(xkbcommon) pkgconfig(zlib) qt5-base-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

%global translation_domain org.fcitx.fcitx5.kcm

Name:           fcitx5-configtool
Version:        5.1.1
Release:        alt2_%autorelease
Summary:        Configuration tools used by fcitx5
License:        GPLv2+
URL:            https://github.com/fcitx/fcitx5-configtool
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gettext-tools libasprintf-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kirigami-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Utils)
BuildRequires:  kf5-plasma-framework-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  qt5-quickcontrols2-devel
BuildRequires:  qt5-svg-devel
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  /usr/bin/appstream-util

# to display scalable icons
Requires:       libqt5-svg
# explicit requires on fcitx5-qt
Requires:       fcitx5-qt
Source44: import.info

%description
Configuration tools used by fcitx5.

%package -n kcm-fcitx5
Group: Graphical desktop/Other
Summary:        Config tools to be used on KDE based environment.
Requires:       kf5-filesystem
Requires:       libkf5kcmutils libkf5kcmutilscore
Requires:       %{name} = %{version}-%{release}

%description -n kcm-fcitx5
Config tools to be used on KDE based environment. Can be installed seperately.

%package -n fcitx5-migrator
Group: Graphical desktop/Other
Summary:        Migration tools for fcitx5
Requires:       %{name} = %{version}-%{release}

%description -n fcitx5-migrator
Migration tools for fcitx5, containing fcitx5-migrator

%package -n fcitx5-migrator-devel
Group: Graphical desktop/Other
Summary:        Devel files for fcitx5-migrator
Requires:       fcitx5-migrator = %{version}-%{release}

%description -n fcitx5-migrator-devel
Development files for fcitx5-migrator

%prep
%setup -q


#fix typos
sed -i 's/Catogories/Categories/g' src/configtool/org.fcitx.fcitx5-config-qt.desktop.in
sed -i 's/Catogories/Categories/g' src/migrator/app/org.fcitx.fcitx5-migrator.desktop.in

%build
%cmake_kf5 -GNinja
%fedora_v2_cmake_build 

%install
%fedora_v2_cmake_install
# kservices5/*.desktop desktop file dont't need to use desktop-file-install
# only for applications/*.desktop
for desktop_file_name in kbd-layout-viewer5 org.fcitx.fcitx5-config-qt org.fcitx.fcitx5-migrator
do
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/${desktop_file_name}.desktop
done
sed "/icon/d" -i %{buildroot}%{_metainfodir}/%{translation_domain}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang %{name}
%find_lang %{translation_domain}


%files -f %{name}.lang 
%doc --no-dereference LICENSES/GPL-2.0-or-later.txt
%doc README
%{_bindir}/fcitx5-config-qt
%{_datadir}/applications/org.fcitx.fcitx5-config-qt.desktop
%{_bindir}/kbd-layout-viewer5
%{_datadir}/applications/kbd-layout-viewer5.desktop

%files -n kcm-fcitx5 -f %{translation_domain}.lang 
%doc --no-dereference LICENSES/GPL-2.0-or-later.txt
%{_kf5_qtplugindir}/kcms/kcm_fcitx5.so
%{_datadir}/kpackage/kcms/%{translation_domain}
%{_datadir}/kservices5/kcm_fcitx5.desktop
%{_metainfodir}/%{translation_domain}.appdata.xml
%{_bindir}/fcitx5-plasma-theme-generator

%files -n fcitx5-migrator
%{_bindir}/fcitx5-migrator
%{_libdir}/libFcitx5Migrator.so.5*
%{_libdir}/libFcitx5Migrator.so.1
%{_datadir}/applications/org.fcitx.fcitx5-migrator.desktop

%files -n fcitx5-migrator-devel
%{_libdir}/libFcitx5Migrator.so

%changelog
* Mon Oct 30 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt2_1
- fixed build

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_1
- update

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.15-alt1_1
- new version

