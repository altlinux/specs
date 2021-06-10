
Name: maliit-plugins
Version: 0.99.1
Release: alt1
%K5init no_altplace

Group: System/Libraries
Summary: Maliit Input Method Plugins
License: BSD
Url: http://www.maliit.org

Requires: maliit-framework

Source: %name-%version.tar

# Automatically added by buildreq on Fri Jun 04 2021 (-bi)
# optimized out: cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libsasl2-3 libssl-devel libstdc++-devel libwayland-client python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel qt5-declarative-devel rpm-build-python3 rpm-build-qml sh4
#BuildRequires: cmake maliit-framework-devel python-modules-encodings python3-dev python3-module-mpl_toolkits qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake doxygen
BuildRequires: qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires: maliit-framework-devel

%description
Maliit Plugins provide reference input method plugins for use with Maliit Framework.
Currently it provides a single QML based keyboard plugin.

%prep
%setup -qn %name-%version

%build
%K5build \
    -Denable-maliit-keyboard:BOOL=ON \
    -Denable-nemo-keyboard:BOOL=OFF \
    -Denable-presage:BOOL=OFF \
    -Denable-hunspell:BOOL=OFF \
    -Denable-preedit:BOOL=OFF \
    -Denable-tests:BOOL=OFF \
    -Denable-docs:BOOL=OFF \
    -DMALIIT_DEFAULT_PROFILE=olpc-xo \
    #

%install
%make -C BUILD DESTDIR=%buildroot install

#mkdir -p %buildroot%_datadir/maliit/plugins/org/

# clean docs
#rm -rf %buildroot/%_defaultdocdir/maliit-plugins/html


%files
%doc LICENSE NEWS README
%_bindir/maliit-keyboard*
%_libdir/maliit/plugins/*
%dir %_datadir/maliit/
%_datadir/maliit/plugins/

%changelog
* Fri Jun 04 2021 Sergey V Turchin <zerg@altlinux.org> 0.99.1-alt1
- new version

* Thu Mar 14 2013 Sergey V Turchin <zerg@altlinux.org> 0.94.2-alt1
- new version

* Thu Jan 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.94.0-alt1
- new version

* Thu Oct 18 2012 Sergey V Turchin <zerg@altlinux.org> 0.92.5-alt1
- initial build

