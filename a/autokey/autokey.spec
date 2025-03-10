%define _unpackaged_files_terminate_build 1

Name: autokey
Version: 0.96.0
Release: alt2

Summary: AutoKey, a desktop automation utility for Linux and X11
License: GPL-3.0
Group: Graphical desktop/Other
URL: https://github.com/autokey/autokey

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
AutoKey is a desktop automation utility for Linux and X11. It allows the
automation of virtually any task by responding to typed abbreviations and
hotkeys. It offers a full-featured GUI that makes it highly accessible for
novices, as well as a scripting interface offering the full flexibility and
power of the Python language.

## Common

%package common
Summary: Desktop automation utility - common data
Group: Graphical desktop/Other
Requires: typelib(Notify)
%filter_from_requires /python3(distutils.spawn)/d
# needed for autokey-shell
Requires: python3(setuptools)

%description common
AutoKey is a desktop automation utility for Linux and X11. It allows the
automation of virtually any task by responding to typed abbreviations and
hotkeys. It offers a full-featured GUI that makes it highly accessible for
novices, as well as a scripting interface offering the full flexibility and
power of the Python language.

This package contains the common data shared between the various frontends.

%package gtk
Summary: Desktop automation utility - GTK+ version
Group: Graphical desktop/Other
Requires: %name-common = %version-%release
Requires: typelib(AyatanaAppIndicator3)
Requires: libgtksourceview3-gir
Requires: wmctrl
Requires: zenity
Requires: xautomation

%description gtk
AutoKey is a desktop automation utility for Linux and X11. It allows the
automation of virtually any task by responding to typed abbreviations and
hotkeys. It offers a full-featured GUI that makes it highly accessible for
novices, as well as a scripting interface offering the full flexibility and
power of the Python language.

This package contains the GTK+ frontend.

%package qt
Summary: Desktop automation utility - Qt version
Group: Graphical desktop/Other
Requires: %name-common = %version-%release
Requires: python3-module-qscintilla2-qt5
Requires: xautomation
Requires: wmctrl
Requires: kdialog

%description qt
AutoKey is a desktop automation utility for Linux and X11. It allows the
automation of virtually any task by responding to typed abbreviations and
hotkeys. It offers a full-featured GUI that makes it highly accessible for
novices, as well as a scripting interface offering the full flexibility and
power of the Python language.

This package contains the Qt frontend.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files common
%doc ACKNOWLEDGMENTS README.rst CHANGELOG.rst CONTRIBUTORS.rst LICENSE
%_bindir/autokey-run
%_bindir/autokey-shell
%_man1dir/autokey-run.1*
%_datadir/icons/hicolor/scalable/apps/autokey-status*.svg
%_datadir/icons/hicolor/*/apps/autokey.png
%_datadir/icons/hicolor/scalable/apps/autokey.svg
%_datadir/icons/ubuntu-mono-dark/apps/*
%_datadir/icons/ubuntu-mono-light/apps/*
%_datadir/icons/Humanity/scalable/apps/*.svg
%python3_sitelibdir/%{name}-*.egg-info
%dir %python3_sitelibdir/%name
%python3_sitelibdir/%name/UI_common_functions.py
%python3_sitelibdir/%name/__init__.py
%python3_sitelibdir/%name/argument_parser.py
%python3_sitelibdir/%name/common.py
%python3_sitelibdir/%name/dbus_service.py
%python3_sitelibdir/%name/interface.py
%python3_sitelibdir/%name/logger.py
%python3_sitelibdir/%name/macro.py
%python3_sitelibdir/%name/monitor.py
%python3_sitelibdir/%name/service.py
%python3_sitelibdir/%name/__pycache__/
%python3_sitelibdir/%name/configmanager/
%python3_sitelibdir/%name/iomediator/
%python3_sitelibdir/%name/model/
%python3_sitelibdir/%name/scripting/

%files gtk
%_bindir/autokey-gtk
%_man1dir/autokey-gtk.1*
%_datadir/applications/autokey-gtk.desktop
%python3_sitelibdir/%name/gtkapp.py*
%dir %python3_sitelibdir/%name/gtkui
%python3_sitelibdir/%name/gtkui/*

%files qt
%_bindir/autokey-qt
%_man1dir/autokey-qt.1*
%_datadir/applications/autokey-qt.desktop
%python3_sitelibdir/%name/qtapp.py*
%dir %python3_sitelibdir/%name/qtui
%python3_sitelibdir/%name/qtui/*

%changelog
* Mon Mar 10 2025 Nikolay Strelkov <snk@altlinux.org> 0.96.0-alt2
- bump release to override autoimports package

* Sun Mar 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.96.0-alt1
- Initial build for Sisyphus
