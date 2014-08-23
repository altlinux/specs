Name: seafile-client
Version: 3.1.4
Release: alt1
Summary: Seafile gui client on QT bassed

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/seafile-client

Packager: Denis Baranov <baraka@altlinux.ru>

# Source-url: https://github.com/haiwen/seafile-client/archive/v%version.tar.gz
Source: %name-%version.tar

Requires: libseafile

# Automatically added by buildreq on Sun Nov 10 2013
# optimized out: cmake cmake-modules fontconfig glib2-devel libevent-devel libgio-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libsearpc-devel libssl-devel libstdc++-devel mariadb-client mariadb-common pkg-config
BuildRequires: ccmake gcc-c++ libccnet-devel libjansson-devel libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libsqlite3-devel phonon-devel

BuildRequires: libseafile-devel >= 3.1.0

%description
Seafile is a full-fledged document collaboration platform
Seafile desktop gui client

%prep
%setup
#%__subst /\(DESTDIR\)/d libseafile.pc.in
# add missed qm from ts
%__subst "s|.*QDebug.*||g" src/main.cpp
cd i18n
lrelease-qt4 *.ts

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*

%changelog
* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt1
- new version 3.1.4 (with rpmrb script)

* Mon Jan 20 2014 Denis Baranov <baraka@altlinux.ru> 2.1.1-alt1
- Update to version 2.1.1

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.6-alt1
- Initial build gui client for ALTLinux
