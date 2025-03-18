%define nameL io.github.ebonjaeger.bluejay

Name: bluejay
Version: 1.0.2
Release: alt1

Summary: Bluetooth manager written in Qt

License: MPL-2.0
Group: System/Configuration/Hardware

Url: https://github.com/EbonJaeger/bluejay
Vcs: https://github.com/EbonJaeger/bluejay

Source0: %name-%version.tar

BuildRequires(Pre): rpm-macros-cmake rpm-build-cmake
BuildRequires: cmake qt6-base-devel kf6-kirigami-devel qt6-tools-devel
BuildRequires: kf6-kirigami-addons-devel kf6-kcoreaddons-devel
BuildRequires: extra-cmake-modules llvm-devel kf6-bluez-qt-devel
BuildRequires: kf6-ki18n-devel clang libstdc++-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kconfig-devel pkgconfig(Qt6Qml) libgomp-devel
BuildRequires: qt6-declarative-devel kf6-qqc2-desktop-style-devel

%description
A Bluetooth manager and Bluez front-end. With it, you can 
pair devices, connect to and remove devices, turn Bluetooth 
on and off, and more. Bluejay is powered by the Qt6 graphical 
toolkit and KDE Frameworks.

%prep
%setup

%build
mkdir -p %_cmake__builddir; 
cmake  \
        -DCMAKE_C_FLAGS:STRING='-pipe -frecord-gcc-switches -Wall -g -O2 -flto=auto' \
        -DCMAKE_CXX_FLAGS:STRING='-pipe -frecord-gcc-switches -Wall -g -O2 -flto=auto' \
        -DSHARE_INSTALL_PREFIX:PATH=/usr/share \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DINCLUDE_INSTALL_DIR:PATH=/usr/include \
        -DLIB_INSTALL_DIR:PATH=/usr/lib64 \
        -DSYSCONF_INSTALL_DIR:PATH=/etc \
        -DSHARE_INSTALL_PREFIX:PATH=/usr/share \
        -DLIB_DESTINATION=lib64 \
    -S . -B "%_arch-alt-linux"

%cmake_build

%install
%cmake_install

%files
%_bindir/*
%_datadir/applications/%nameL.desktop
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_datadir/metainfo/%nameL.metainfo.xml
%doc *.md LICENSE

%changelog
* Tue Mar 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Mar 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.0.1-alt1
- Initial build for ALT Linux.
