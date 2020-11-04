# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
# build errors
%def_without external_json

Name: sqlitebrowser
Version: 3.12.0
Release: alt1

Summary: Official home of the DB Browser for SQLite (DB4S) project
License: GPLv3+ or MPLv2.0
Group: Other
Url: https://github.com/sqlitebrowser/sqlitebrowser

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: desktop-file-utils

BuildRequires: libappstream-glib
BuildRequires: qcustomplot-qt5-devel
BuildRequires: qhexedit2-qt5-devel
BuildRequires: libsqlite3-devel
BuildRequires: libqscintilla2-qt5-devel
%if_with external_json
BuildRequires: nlohmann-json-devel
%endif
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel

BuildRequires: ctest

%description
DB Browser for SQLite (DB4S) is a high quality, visual, open source tool to
create, design, and edit database files compatible with SQLite.

It is for users and developers wanting to create databases, search, and edit
data. It uses a familiar spreadsheet-like interface, and you don't need to
learn complicated SQL commands.

Controls and wizards are available for users to:
- Create and compact database files
- Create, define, modify and delete tables
- Create, define and delete indexes
- Browse, edit, add and delete records
- Search records
- Import and export records as text
- Import and export tables from/to CSV files
- Import and export databases from/to SQL dump files
- Issue SQL queries and inspect the results
- Examine a log of all SQL commands issued by the application
- Plot simple graphs based on table or query data

%prep
%setup

# Unbundle
rm -rfv libs/{qcustomplot-source,qhexedit,qscintilla}/
%if_with external_json
rm -rfv libs/json/
%endif

# replace internal cmake/* with pkgconfig files
%__subst "1ifind_package(PkgConfig)" CMakeLists.txt
%__subst 's|find_package(QCustomPlot)|pkg_check_modules(QCUSTOMPLOT qcustomplot-qt5)|' CMakeLists.txt
%__subst 's|find_package(QHexEdit)|pkg_check_modules(QHEXEDIT qhexedit2-qt5)|' CMakeLists.txt
# pkg_check_modules don't set _FOUND
%__subst 's|([A-Z]*_FOUND)|(TRUE)|' CMakeLists.txt
%__subst 's|INCLUDE_DIR|INCLUDE_DIRS|' CMakeLists.txt

%if_with external_json
%__subst 's|add_subdirectory(${JSON_DIR})|set(JSON_DIR /usr/include/nlohmann)|' CMakeLists.txt
%endif

%build
%cmake -DUSE_QT5=1 -DENABLE_TESTING=1 \
       -DFORCE_INTERNAL_QSCINTILLA=OFF \
       -DFORCE_INTERNAL_QCUSTOMPLOT=OFF \
       -DFORCE_INTERNAL_QHEXEDIT=OFF

%cmake_build

%install
%cmakeinstall_std

%_bindir/appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%name.desktop.appdata.xml
desktop-file-validate %buildroot%_datadir/applications/%name.desktop

%check
%cmake_build test

%files
%doc README.md LICENSE
%_bindir/%name
%_datadir/metainfo/%name.desktop.appdata.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/256x256/apps/%name.png

%changelog
* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 3.12.0-alt1
- NMU: new version (3.12.0) with rpmgs script via gear-uupdate (ALT bug 38707)

* Tue Sep 18 2018 Anton Midyukov <antohami@altlinux.org> 3.10.1-alt1
- Initial build for Sisyphus (Closes: 35277)
