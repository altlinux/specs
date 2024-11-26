Name:    fwbackups
Version: 1.43.8
Release: alt3
Summary: A feature-rich user backup program
Group:   Archiving/Backup
License: GPL-2.0-only
Url:     https://diffingo.com/oss/fwbackups
Source0: fwbackups-%version.tar
Patch:   alt-fix-config-read.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: meson
BuildRequires: libappstream-glib-devel python3-module-pygobject3-devel gtk4-update-icon-cache icon-theme-hicolor

Requires: python3-module-paramiko
Requires: python3-module-notify2
Requires: python3-module-pycryptodome

%description
fwbackups is a feature-rich user backup program that allows users (including
but not limited to root) to backup their files on demand or periodically via
backup sets. Each set may have different settings meaning users can backup
groups of files and folders to different destinations at different times.
Restores can be performed at any time using an existing backup from fwbackups
or from the contents of an external folder or archive.

%prep
%setup
%patch -p1

%build
%meson -Dpython.install_env=auto -Dforce_system_python=true
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING README.md
%_bindir/%{name}*
%_datadir/icons/hicolor/*/apps/*%{name}*
%_datadir/applications/*%{name}*.desktop
%_datadir/metainfo/*
%python3_sitelibdir/%name/

%changelog
* Tue Nov 26 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 1.43.8-alt3
- correct patch

* Fri Oct 04 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 1.43.8-alt2
- add metainfo data into package

* Fri Nov 03 2023 Ratkin Daniil-Vitkor <krf10@altlinux.org> 1.43.8-alt1
- Initial build for ALT Linux (closes: 44702)
- 1.43.8~rc2
