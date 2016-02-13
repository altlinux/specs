Name: seafile-client
Version: 5.0.4
Release: alt1

Summary: Seafile gui client on QT bassed

Group: Networking/File transfer
License: GPLv3
Url: https://github.com/haiwen/seafile-client

Packager: Denis Baranov <baraka@altlinux.ru>

# Source-url: https://github.com/haiwen/seafile-client/archive/v%version.tar.gz
Source: %name-%version.tar

Requires: seafile >= %version

# Automatically added by buildreq on Sun Nov 10 2013
# optimized out: cmake cmake-modules fontconfig glib2-devel libevent-devel libgio-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libsearpc-devel libssl-devel libstdc++-devel mariadb-client mariadb-common pkg-config
BuildRequires: ccmake gcc-c++ libjansson-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libsqlite3-devel phonon-devel

BuildRequires(pre): rpm-macros-cmake

BuildRequires: libccnet-devel >= %version
BuildRequires: libseafile-devel >= %version

Conflicts: libseafile <= 2.0.4

%description
Seafile desktop gui client.
Seafile is a full-fledged document collaboration platform.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/seafile-applet
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*

%changelog
* Sat Feb 13 2016 Vitaly Lipatov <lav@altlinux.ru> 5.0.4-alt1
- new version 5.0.4 (with rpmrb script)

* Fri Nov 21 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.11-alt1
- new version 3.1.11 (with rpmrb script)

* Sun Aug 31 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt2
- rebuild with rebuilt libseafile

* Thu Aug 28 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt1
- new version 3.1.5 (with rpmrb script)

* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt1
- new version 3.1.4 (with rpmrb script)

* Mon Jan 20 2014 Denis Baranov <baraka@altlinux.ru> 2.1.1-alt1
- Update to version 2.1.1

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 2.0.6-alt1
- Initial build gui client for ALTLinux
