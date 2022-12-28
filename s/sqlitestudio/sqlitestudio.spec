Name:		sqlitestudio
Version:	3.4.1
Release:	alt1

Summary:	Database manager for SQLite
Summary(ru_RU.UTF-8): Менеджер баз данных типа SQLite
License:	GPL-3.0+
Group:          Development/Databases
URL:		https://github.com/pawelsalawa/sqlitestudio

# Source-url: https://github.com/pawelsalawa/%name/archive/refs/tags/%version.tar.gz
Source:         %name-%version.tar

Source1:	%name.svg

%set_verify_elf_method skip
%global __find_debuginfo_files %nil

BuildRequires:  qt5-base-devel
BuildRequires:  qt5-declarative-devel
BuildRequires:  libsqlite3-devel
BuildRequires:  libreadline-devel
BuildRequires:  libncurses-devel
BuildRequires:  qt5-svg-devel
BuildRequires:  qt5-tools-devel 
BuildRequires:  qt5-script-devel
BuildRequires:  python3-dev
BuildRequires:  patchelf

AutoReq: no

ExclusiveArch: %ix86 x86_64

%description
SQLiteStudio is a free, open source, multi-platform SQLite database manager written in C++,
with use of Qt framework.
It is a SQLite database manager with the following features:

* Single executable file
* Intuitive interface
* All SQLite3 and SQLite2 features wrapped within simple GUI
* Cross-platform
* Localizations
* Exporting to various formats
* Importing data from various formats
* Numerous small additions
* UTF-8 support
* Skinnable
* Configurable colors, fonts and shortcuts

%description -l ru_RU.UTF-8
SQLiteStudio - это свободный многоплатформенный менеджер баз данных SQLite, с открытым исходным кодом,
написанный на C++, с использованием фреймворка Qt.
Это менеджер баз данных SQLite со следующими возможностями:

* Единый исполняемый файл
* Интуитивно понятный интерфейс
* Все возможности SQLite3 и SQLite2 заключены в простой графический интерфейс.
* Кросс-платформенность
* Локализации
* Экспорт в различные форматы
* Импорт данных из различных форматов
* Многочисленные мелкие дополнения
* Поддержка UTF-8
* Возможность смены стиля
* Настраиваемые цвета, шрифты и ярлыки.

%prep
%setup -q -n %name-%version

sed -i "/ScriptingTcl/d" Plugins/Plugins.pro

# ld: cannot find -lpython3.9: No such file or directory
if [ "$(pkg-config --modversion python3 | cut -d. -f2)" -ge 10 ]; then
    sed -i -e 's/lpython3.9/lpython3/g' Plugins/ScriptingPython/ScriptingPython.pro
fi

%build
%qmake_qt5 SQLiteStudio3/SQLiteStudio3.pro
%make_build


if [ "$(pkg-config --modversion python3 | cut -d. -f2)" -ge 10 ] ; then
    PKG_CONFIG_PYTHON="`pkg-config --cflags --libs python-3.10`"
else
    PKG_CONFIG_PYTHON="`pkg-config --cflags --libs python3`"
fi

%qmake_qt5 Plugins/Plugins.pro \
                               INCLUDEPATH+=%_builddir/%name-%version/SQLiteStudio3/coreSQLiteStudio \
                               QMAKE_CXXFLAGS+=$PKG_CONFIG_PYTHON
%make_build -j1

%install
install -m644 -D %SOURCE1 %buildroot%_pixmapsdir/%name.svg

install -d -m 755 %buildroot%_datadir/applications
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Sqlitestudio
Comment=Database manager for SQLite
Exec=%name
Icon=%name
Terminal=false
StartupNotify=false
Categories=Application;Development
EOF

mkdir -p %buildroot%_libdir/%name/
cp -r %_builddir/%name-%version/output/SQLiteStudio/*.so.* %buildroot%_libdir/%name/
cp -r %_builddir/%name-%version/output/SQLiteStudio/*.so %buildroot%_libdir/%name/
cp -r %_builddir/%name-%version/output/SQLiteStudio/plugins %buildroot%_libdir/%name/
cp -r %_builddir/%name-%version/output/SQLiteStudio/%name %buildroot%_libdir/%name/

#run.sh (set env to avoid some possible issues)
cat > %buildroot%_libdir/%name/run.sh <<EOF
#!/bin/bash
# start SQLiteStudio with plugins
env SQLITESTUDIO_PLUGINS=%_libdir/%name/plugins %_libdir/%name/%name
EOF

chmod 0755 %buildroot%_libdir/%name/run.sh

mkdir -p %buildroot%_bindir/
cp -r %_builddir/%name-%version/output/SQLiteStudio/%{name}cli %buildroot%_bindir/
ln -s -T %_libdir/%name/run.sh %buildroot/%_bindir/sqlitestudio

patchelf --set-rpath '$ORIGIN/../%_lib/%name' %buildroot%_bindir/%{name}cli
patchelf --set-rpath '$ORIGIN' %buildroot%_libdir/%name/%name
patchelf --set-rpath '$ORIGIN' %buildroot%_libdir/%name/libguiSQLiteStudio.so

%files
%_bindir/%name
%_bindir/%{name}cli
%_libdir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.svg

%changelog
* Wed Dec 28 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 3.4.1-alt1
- Initial build
