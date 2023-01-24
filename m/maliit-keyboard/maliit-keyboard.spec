
Name: maliit-keyboard
Version: 2.1.0
Release: alt2
%K5init no_altplace

Group: System/Libraries
Summary: Virtual Keyboard
License: LGPL-3.0-only and BSD
Url: http://www.maliit.org

Provides: maliit-plugins = %version
Obsoletes: maliit-plugins < %version
#Requires: maliit-inputcontext-qt5
Requires: maliit-framework

Source: %name-%version.tar

# Automatically added by buildreq on Fri Jun 04 2021 (-bi)
# optimized out: cmake-modules debugedit elfutils gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libgio-devel libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libsasl2-3 libssl-devel libstdc++-devel libwayland-client pkg-config python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel qt5-declarative-devel rpm-build-gir rpm-build-python3 rpm-build-qml sh4
#BuildRequires: cmake libhunspell-devel libpinyin-data libpinyin-devel maliit-framework-devel python-modules-encodings python3-dev python3-module-mpl_toolkits qt5-multimedia-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: maliit-framework-devel
#BuildRequires: libpinyin-devel
BuildRequires: qt5-multimedia-devel qt5-svg-devel qt5-wayland-devel qt5-feedback-devel
BuildRequires: cmake libhunspell-devel doxygen

%description
Maliit Plugins provide reference input method plugins for use with Maliit Framework.
Currently it provides a single QML based keyboard plugin.

%prep
%setup -n %name-%version

sed -i '/find_package.*Pinyin/d' CMakeLists.txt

%build
%K5build \
    -Denable-presage:BOOL=OFF \
    -Denable-hunspell:BOOL=ON \
    -Denable-tests:BOOL=OFF \
    #

%install
make -C BUILD DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/maliit/plugins/org/

# clean docs
rm -rf %buildroot/%_defaultdocdir/maliit-plugins/html


%files
%doc COPYING*
%_libdir/maliit/plugins/*
%_libdir/maliit/keyboard2/
%_bindir/maliit-keyboard*
%_desktopdir/com.github.maliit.keyboard.desktop
%dir %_datadir/maliit/
%_datadir/maliit/plugins/
%_datadir/maliit/keyboard2/
%_datadir/glib-2.0/schemas/org.maliit.keyboard.maliit.gschema.xml

%changelog
* Tue Jan 24 2023 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt2
- obsolete maliit-plugins
- fix build requires

* Wed Jan 12 2022 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- new version

* Fri Jun 04 2021 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- initial build
