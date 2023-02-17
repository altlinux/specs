Name:    mate-menu
Version: 22.04.2
Release: alt3

Summary: An Advanced Menu for the MATE Desktop
# MIT is needed for keybinding.py
License: GPL-2.0 and MIT
Group:   Other
URL:     https://github.com/ubuntu-mate/mate-menu

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-distutils-extra
BuildRequires: intltool

%add_python3_path %_libexecdir/%name

Requires: menu-icons-default
Requires: mate-menu-editor
Requires: altlinux-mime-defaults > 0.17
Requires: typelib(Gtk) = 3.0
Requires: python3(cairo)

BuildArch: noarch

Source:  %name-%version.tar
Patch1: alt-applet-name-l10n.patch
Patch2: alt-menubutton-label-l10n.patch
Patch3: alt-use-themed-app-list.patch
Patch4: alt-set-start-button-gsettings.patch
Patch5: alt-desktop-place-fix.patch
Patch6: fix-version.patch

%description
This is MATE Menu, a fork of MintMenu. An advanced menu for MATE.
Supports filtering, favorites, autosession, and many other features.

%prep
%setup -n %name-%version
%autopatch -p1

%build
%python3_build

%install
%python3_install
%find_lang %name --with-gnome

%files -f %name.lang
%doc *.md
%_bindir/%name
%_libexecdir/%name
%_datadir/%name
%python3_sitelibdir/mate_menu/
%python3_sitelibdir/*.egg-info
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/*.xml
%_datadir/mate-panel/applets/org.mate.panel.MateMenuApplet.mate-panel-applet
%_man1dir/%name.1*

%changelog
* Fri Feb 17 2023 Leontiy Volodin <lvol@altlinux.org> 22.04.2-alt3
- Set start button using gsettings (ALT #45135).

* Thu Jan 12 2023 Andrey Cherepanov <cas@altlinux.org> 22.04.2-alt2
- Fix application version (ALT #44896).

* Fri Mar 25 2022 Andrey Cherepanov <cas@altlinux.org> 22.04.2-alt1
- New version.

* Fri Feb 25 2022 Andrey Cherepanov <cas@altlinux.org> 22.04.1-alt1
- New version.

* Thu Jan 27 2022 Andrey Cherepanov <cas@altlinux.org> 22.04.0-alt1
- New version.

* Sun Aug 15 2021 Anton Midyukov <antohami@altlinux.org> 20.04.3-alt2
- Fix requires (ALT #39754)

* Mon Apr 06 2020 Pavel Vasenkov <pav@altlinux.org> 20.04.3-alt1
- new version 20.04.3

* Tue Mar 24 2020 Pavel Vasenkov <pav@altlinux.org> 20.04.2-alt1
- new version 20.04.2

* Mon Mar 23 2020 Pavel Vasenkov <pav@altlinux.org> 20.04.1-alt2
- Fix open link to Desktop (ALT #37850)
- Fix edit properties (ALT #37851)

* Thu Mar 12 2020 Andrey Cherepanov <cas@altlinux.org> 20.04.1-alt1
- New version.

* Tue Oct 01 2019 Andrey Cherepanov <cas@altlinux.org> 19.10.2-alt1
- New version.

* Thu Aug 15 2019 Andrey Cherepanov <cas@altlinux.org> 19.10.1-alt1
- Initial build for Sisyphus
