%def_without check

Name:    ulauncher
Version: 5.15.3
Release: alt1

Summary: Feature rich application Launcher for Linux
License: GPL-3.0+
Group:   Other
URL:     https://github.com/Ulauncher/Ulauncher

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-distutils-extra
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-dbus
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-pyxdg
BuildRequires: python3-module-Levenshtein
BuildRequires: python3-module-pyinotify
BuildRequires: python3-module-websocket-client
BuildRequires: intltool

%add_typelib_req_skiplist typelib(AppIndicator3)

Requires: typelib(Gtk) = 3.0 typelib(WebKit2) = 4.0

%description
Ulauncher is a fast application launcher for Linux. It is written in Python,
using GTK+, and features: App Search (fuzzy matching), Calculator, Extensions,
Shortcuts, File browser mode and Custom Color Themes.

%prep
%setup -n %name-%version
subst 's|%%VERSION%%|%version|' setup.py

%build
%pyproject_build

%install
%pyproject_install
rm -f %buildroot%_defaultdocdir/%name/README.md
mkdir -p %buildroot%_desktopdir
mv %buildroot%python3_sitelibdir/%_desktopdir/*.desktop %buildroot%_desktopdir
subst 's|^TryExec=.*$|TryExec=%name|;s|^Exec=.*%name|Exec=%name|' %buildroot%_desktopdir/extras-%name.desktop
subst 's|ulauncher-%version.data/data|usr|' %buildroot%python3_sitelibdir/%name/config.py

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc AUTHORS README.md
%_bindir/*
%_datadir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_desktopdir/*.desktop
%_iconsdir/*/*/apps/*.svg
%_iconsdir/breeze/apps/48/ulauncher-indicator.svg
%_libexecdir/systemd/user/%name.service

%changelog
* Thu Sep 07 2023 Andrey Cherepanov <cas@altlinux.org> 5.15.3-alt1
- Initial build for Sisyphus.
