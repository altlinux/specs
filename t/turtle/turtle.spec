%define _unpackaged_files_terminate_build 1
%define mod_name turtlevcs
%def_with check

## Define directories
%define glib_apiver 2.0
%define glib_schemasdir %_datadir/glib-%glib_apiver/schemas

%define nautilus_extdir %_datadir/nautilus-python/extensions
%define caja_extdir %_datadir/caja-python/extensions
%define nemo_extdir %_datadir/nemo-python/extensions
%define thunar_extdir %_datadir/thunarx-python/extensions

%define _scliconsdir %_iconsdir/hicolor/scalable/apps
%define _symiconsdir %_iconsdir/hicolor/symbolic/apps

%define _bshcompldir %_datadir/bash-completion/completions
%define _dbussrvsdir %_datadir/dbus-1/services


## Define turtle files
%define turtle_svg de.philippun1.turtle.svg
%define turtle_symbolic_svg de.philippun1.turtle-symbolic.svg

%define turtle_schema de.philippun1.turtle.gschema.xml

%define turtle_cli turtle_cli
%define turtle_service turtle_service

%define turtle_desktop de.philippun1.turtle.desktop
%define turtle_dbus_service de.philippun1.turtle.service
%define turtle_completion turtle_cli

%define turtle_nautilus_plg turtle_nautilus.py
%define turtle_nautilus_cmpr_plg turtle_nautilus_compare.py
%define turtle_caja_plg turtle_caja.py
%define turtle_nemo_plg turtle_nemo.py
%define turtle_thunar_plg turtle_thunar.py

Name: turtle
Version: 0.10
Release: alt1

Summary: Turtle is a graphical interface for version control intended to run on gnome and nautilus
License: GPLv3
Group: Development/Other
Url: https://gitlab.gnome.org/philippun1/turtle
Vcs: https://gitlab.gnome.org/philippun1/turtle

BuildArch: noarch

Source: %name-%version.tar

Requires: meld
Requires: libcryptui

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pygobject3
BuildRequires: libgio

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pygit2
BuildRequires: python3-module-dbus
BuildRequires: libgtk4
BuildRequires: libadwaita-gir
%endif

%description
Manage your git repositories with easy-to-use dialogs in Nautilus.
Currently these dialogs are implemented:
* commit, add, stage, unstage, revert, resolve
* sync (pull+push), pull, push
* checkout, create branch, merge
* init, clone
* remotes, submodules
* log, diff
* settings and about

There is also the possibility to perform operations from context menu
of table entries in the log and commit window:
* pull, checkout, create branch, merge from log entries
* revert, (un)stage from commit entries

Staging hunks directly is also possible, both from the nautilus plugin
and the commit window.
Currently only ssh login is possible for remote operations.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# install icons
icons_source="data/icons/hicolor"
sclicons="$icons_source/scalable/apps"
symicons="$icons_source/symbolic/apps"
install -pDm 644 $sclicons/%turtle_svg %buildroot%_scliconsdir/%turtle_svg
install -pDm 644 $symicons/%turtle_symbolic_svg %buildroot%_symiconsdir/%turtle_symbolic_svg

# install glib schema
install -pDm 644 data/%turtle_schema %buildroot%glib_schemasdir/%turtle_schema

# install binary files
install -pDm 755 %turtle_cli %buildroot%_bindir/%turtle_cli
install -pDm 755 %turtle_service %buildroot%_bindir/%turtle_service

# install desktop file
install -pDm 644 data/%turtle_desktop %buildroot%_desktopdir/%turtle_desktop

# install bash copletion
install -pDm 644 data/completions/%turtle_completion %buildroot%_bshcompldir/%turtle_completion

# install dbus service
install -pDm 644 data/%turtle_dbus_service %buildroot%_dbussrvsdir/%turtle_dbus_service

# install filemanager plugins
install -pDm 644 plugins/%turtle_nautilus_plg %buildroot%nautilus_extdir/%turtle_nautilus_plg
python3 -m compileall %buildroot%nautilus_extdir/%turtle_nautilus_plg
install -pDm 644 plugins/%turtle_nautilus_cmpr_plg %buildroot%nautilus_extdir/%turtle_nautilus_cmpr_plg
python3 -m compileall %buildroot%nautilus_extdir/%turtle_nautilus_cmpr_plg
install -pDm 644 plugins/%turtle_caja_plg %buildroot%caja_extdir/%turtle_caja_plg
python3 -m compileall %buildroot%caja_extdir/%turtle_caja_plg
install -pDm 644 plugins/%turtle_nemo_plg %buildroot%nemo_extdir/%turtle_nemo_plg
python3 -m compileall %buildroot%nemo_extdir/%turtle_nemo_plg
install -pDm 644 plugins/%turtle_thunar_plg %buildroot%thunar_extdir/%turtle_thunar_plg
python3 -m compileall %buildroot%thunar_extdir/%turtle_thunar_plg

%check
%pyproject_run_pytest -Wignore

%files
%doc README.md
%_bindir/%turtle_cli
%_bindir/%turtle_service
%_scliconsdir/%turtle_svg
%_symiconsdir/%turtle_symbolic_svg
%glib_schemasdir/%turtle_schema
%_desktopdir/%turtle_desktop
%_bshcompldir/%turtle_completion
%_dbussrvsdir/%turtle_dbus_service
%nautilus_extdir/%turtle_nautilus_plg
%nautilus_extdir/%turtle_nautilus_cmpr_plg
%nautilus_extdir/__pycache__/turtle_*
%caja_extdir/%turtle_caja_plg
%caja_extdir/__pycache__/turtle_*
%nemo_extdir/%turtle_nemo_plg
%nemo_extdir/__pycache__/turtle_*
%thunar_extdir/%turtle_thunar_plg
%thunar_extdir/__pycache__/turtle_*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Thu Oct 10 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.10-alt1
- Initial build for ALT Sisyphus.

