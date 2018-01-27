Name:     fastonosql
Version:  1.15.0
Release:  alt2

Summary:  FastoNoSQL is a crossplatform Redis, Memcached, SSDB, LevelDB, RocksDB, UnQLite, LMDB, UpscaleDB, ForestDB GUI management tool.

License:  GPLv3
Group:    Other
Url:      https://github.com/fastogt/fastonosql

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/fastogt/fastonosql/archive/v%version.tar.gz
Source:   %name-%version.tar

# submodule
# Source1-url: https://github.com/fastogt/cmake/archive/master.zip
Source1: %name-cmake-%version.tar

# used common uncommon static libs
# update with separate script update_common.sh
Source2: %name-common-%version.tar

#BuildRequires:

# Automatically added by buildreq on Sun Jan 28 2018
# optimized out: cmake cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libEGL-devel libGL-devel libjson-c libqscintilla2-13-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-printsupport libqt5-widgets libqt5-xcbqpa libqt5-xml libstdc++-devel pkg-config python-base python-modules python3 python3-base qt5-base-common qt5-base-devel qt5-tools sssd-client zlib-devel
BuildRequires: bzlib-devel cmake libev-devel libjson-c-devel libleveldb-devel liblmdb-devel libqscintilla2-qt5-devel libsnappy-devel libssh2-devel libssl-devel qt5-imageformats qt5-tools-devel zlib-devel libssh2-devel

Requires: qt5-imageformats

%description
%summary

%prep
%setup -a1 -a2

# hack to search compiled common (and CMAKE_CXX_FLAGS later)
%__subst "s|/usr /usr/local /opt|$(pwd)/DEST/usr/lib $(pwd)/DEST/usr|" cmake/FindCommon.cmake

%__subst "s|qscintilla2|qscintilla2_qt5|" src/CMakeLists.txt

# use pkg-config instead cmake module for libssh2
%__subst "s|FIND_PACKAGE(Libssh2 REQUIRED CONFIG)|pkg_check_modules(SSH2 libssh2)|" src/CMakeLists.txt
%__subst "s|Libssh2::libssh2|\${SSH2_LIBRARIES}|" src/CMakeLists.txt

# disable "A new version is available"
%__subst "s|is_need_update =.*|is_need_update = false;|" src/gui/main_window.cpp

%__subst 's|app_dir +|app_dir + "/../share/fastonosql" +|' common/src/qt/translations/translations.cpp

# TODO: check for resources using (CONNECT_GIF_PATH_RELATIVE)

%build
pushd common
%cmake -DQT_ENABLED=ON
%cmake_build
%cmakeinstall_std DESTDIR=$(pwd)/../DEST
popd

# redis due libssh2 cmake missed
%cmake \
        -DBUILD_WITH_ROCKSDB=OFF -DBUILD_WITH_UNQLITE=OFF \
        -DBUILD_WITH_FORESTDB=OFF -DBUILD_WITH_UPSCALEDB=OFF \
        -DBUILD_WITH_MEMCACHED=OFF \
        -DCMAKE_CXX_FLAGS=-I$(pwd)/DEST/usr/include
%cmake_build

%install
%cmakeinstall_std
install -m0644 -D BUILD/FastoNoSQL/fastonosql.desktop %buildroot%_desktopdir/%name.desktop
rm -rf %buildroot%_prefix/{CHANGELOG,COPYRIGHT,LICENSE}
rm -rf %buildroot%_prefix/lib/
mkdir %buildroot%_datadir/%name/
mv %buildroot%_datadir/resources/ %buildroot%_datadir/%name/
mv %buildroot%_bindir/translations/ %buildroot%_datadir/%name/
rm -f %buildroot%_bindir/%name
mv %buildroot%_bindir/FastoNoSQL %buildroot%_bindir/%name

%files
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/%name.png
%doc CHANGELOG COPYRIGHT README.md

%changelog
* Sun Jan 28 2018 Vitaly Lipatov <lav@altlinux.ru> 1.15.0-alt2
- fix build on i686
- build with redis support

* Wed Jan 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.15.0-alt1
- Initial build for Sisyphus
