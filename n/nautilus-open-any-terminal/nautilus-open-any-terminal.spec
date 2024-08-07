Name: nautilus-open-any-terminal
Version: 0.6.0
Release: alt1

Summary: Extension for nautilus, which adds an context-entry for opening other terminal emulators
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://github.com/Stunkymonkey/nautilus-open-any-terminal

BuildArch: noarch

Source: %name-%version.tar

%filter_from_requires /Caja/d

%add_python3_path %_datadir/nautilus-python/extensions
Requires: nautilus-python typelib(Gtk) = 4.0

Obsoletes: gnome-nautilus-open-any-terminal < %EVR
Provides: gnome-nautilus-open-any-terminal = %EVR

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-dev python3-module-setuptools python3-module-wheel

%description
Is an extension for nautilus, which adds an context-entry for opening other terminal emulators than gnome-terminal.

Right now the plugin is limited to these terminal emulators:
* alacritty
* blackbox
* cool-retro-term
* GNOME Console
* kitty
* konsole
* mate-terminal
And others...

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name

%files -f %name.lang
%doc README.md
%python3_sitelibdir/nautilus_open_any_terminal/
%exclude %python3_sitelibdir/nautilus_open_any_terminal/locale

# FIXME
%python3_sitelibdir/nautilus_open_any_terminal-0.0.0.dist-info/

%_datadir/glib-2.0/schemas/com.github.stunkymonkey.%name.gschema.xml
%_datadir/nautilus-python/extensions/nautilus_open_any_terminal.py
%_datadir/nautilus-python/extensions/__pycache__/*

%exclude %_datadir/caja-python/extensions/nautilus_open_any_terminal.py

%changelog
* Tue Aug 06 2024 Roman Alifanov <ximper@altlinux.org> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Sat Mar 23 2024 Roman Alifanov <ximper@altlinux.org> 0.5.1-alt1
- new version 0.5.1 (with rpmrb script)

* Thu Aug 03 2023 Roman Alifanov <ximper@altlinux.org> 0.4.0-alt2
- renaming to comply with the standart naming of nautilus extensions: nautilus-{sendto,share,image-converter,...}
- exclude unnecessary %python3_sitelibdir/nautilus_open_any_terminal/locale
- added strict typelib(Gtk) req
- added missing rpm-build-gir build dependency (for correct requires)
- switching to pyproject macros

* Tue Aug 01 2023 Roman Alifanov <ximper@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.

