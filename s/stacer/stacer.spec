Name:     stacer
Version:  1.1.0
Release:  alt1.1

Summary:  Linux System Optimizer and Monitoring - https://oguzhaninan.github.io/Stacer-Web
License:  GPL-3.0
Group:    System/Configuration/Hardware
Url:      https://github.com/oguzhaninan/Stacer

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

#set_gcc_version 11

Source:   %name-%version.tar
Patch1: stacer-1.1.0-translation.patch

BuildRequires(pre): cmake rpm-macros-cmake  rpm-macros-qt5 gcc-c++ 

# Automatically added by buildreq on Thu Jun 02 2022
# optimized out: cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libgpg-error libqt5-charts libqt5-concurrent libqt5-core libqt5-gui libqt5-network libqt5-svg libqt5-widgets libsasl2-3 libssl-devel libstdc++-devel python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel sh4
BuildRequires: cmake python3-module-zope qt5-charts-devel qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-sensors-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel

%ifnarch ppc64le
BuildRequires: qt5-webengine-devel
%endif

BuildRequires: qt5-base-devel qt5-svg-devel qt5-charts-devel qt5-tools-devel 

# BuildRequires: bzlib-devel libblkid-devel libe2fs-devel libgcrypt-devel liblz4-devel liblzma-devel liblzo2-devel libuuid-devel python3-module-zope qt5-connectivity-devel qt5-multimedia-devel qt5-phonon-devel qt5-sensors-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel zlib-devel


%description
%summary



%prep
%setup
%patch1 -p1

%build
export PATH=$PATH:%_qt5_bindir
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

#-DCMAKE_BUILD_TYPE=Release
# translations
lupdate-qt5 stacer/stacer.pro -no-obsolete
lrelease-qt5 stacer/stacer.pro
install -d  stacer/translations
mv translations/*.qm stacer/translations



%install
export PATH=$PATH:%_qt5_bindir
%cmake_install

mkdir -p %buildroot%_datadir/%name/translations
cp stacer/translations/%{name}*.qm %buildroot%_datadir/%name/translations


%find_lang %name


%files
%_bindir/*
%doc *.md
%_iconsdir/*
%_desktopdir/*
%exclude %_target_libdir_noarch
%dir %_datadir/%name/
%_datadir/%name/*


%changelog
* Wed Jun 01 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.0-alt1.1
- Correct BuildRequires

* Tue May 31 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.0-alt1
- Initial build for Sisyphus

