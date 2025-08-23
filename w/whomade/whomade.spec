%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: whomade
# NOTE: use .gear/tagit.sh HEAD to get a version number
Version: 0.0.0_git20250822.3cb8166
Release: alt1

Summary: Linux daemon that monitors user-specified directories and records which process created each file
License: GPL-3.0
Group: Monitoring
Url: https://github.com/ANGulchenko/whomade

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(sqlite3)

%description
Whomade is a Linux daemon that monitors user-specified directories and
records which process created each file. This makes it easy to later
identify the origin of files with suspicious or unexpected names.

The main idea was to monitor and identify files in the dot directories
in the /home.

%package caja
Summary: Whomade GUI plug-in to the Caja file manager
Group: Graphical desktop/Other
Requires: %name = %version-%release
Requires: python3-module-caja
Requires: /usr/bin/caja

%description caja
Whomade extension for the Caja FM (from MATE DE, fork of Gnome 2) where
you can just right-click on file and ask "Who made this?" from a menu.

%prep
%setup

# correct path to image
sed -i "s|./FM_Extensions/MATE-CAJA/||" README.md

%build
%cmake
%cmake_build

%install
#%%cmake_install

# copy binary
mkdir -p %buildroot/%_bindir
cp -v %_cmake__builddir/whomade %buildroot/%_bindir/

# set SUID to allow regular usage from Caja
chmod u+s %buildroot/%_bindir/whomade

# create database folder
mkdir -p %buildroot/var/lib/whomade

# package Caja plugin
mkdir -p %buildroot%_datadir/caja-python/extensions/
cp -v FM_Extensions/MATE-CAJA/whomade-extension.py %buildroot%_datadir/caja-python/extensions/

%post
echo "NOTE: upon the first start the daemon will create the database and"
echo "      fill the monitor/ignore fields with placeholders."
echo "      You must replace them with your data."
echo "      Use --help for reference how."
echo "      Example:"
echo "           whomade --list # Will show you the current situation"
echo "           whomade --remove \"copy the placeholder here\"" 
echo "           whomade --add \"use the real path you're interested in\""

%files
%doc CHANGELOG.md LICENSE README.md FM_Extensions/MATE-CAJA/whomade_win.png
%_bindir/whomade
%dir /var/lib/whomade

%files caja
%_datadir/caja-python/extensions/whomade-extension.py*

%changelog
* Sat Aug 23 2025 Nikolay Strelkov <snk@altlinux.org> 0.0.0_git20250822.3cb8166-alt1
- Initial build for Sisyphus
