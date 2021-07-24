%define descr \
Arronax is GUI program to create and edit starter files (.desktop files) for \
applications locations or URLs. It can be used as a standalone application \
or as plugins for the file managers Nautilus, Nemo and Caja. \
\
The plugins add a menu item "Create starter for this file" or \
"Create a starter for this program" to the context menu (that's the menu you get \
when you right-click a file) in the file manager. If the file is an \
application starter you get an item "Modify this starter" instead. \
\
On some desktop environments the plugins add a menu item "Create starter" \
to your desktop's context menu. \
\
Arronax supports most of the keys specified by the Desktop Entry Specification \
including quicklists.

Name: arronax
Version: 0.8
Release: alt2

Summary: Create and modify application, file and URI starters

Group: Development/Tools
License: GPLv3
Url: https://www.florian-diesch.de/software/arronax/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

Requires: libwnck3-gir

BuildArch:  noarch

%description
%descr

%package -n python3-module-%name
Summary: Python3 library for creation and modifying of application starters
Group: Development/Python3
License: GPLv3

%description -n python3-module-%name
%descr

%package -n nautilus-%name
Summary: Python3 library for creation and modifying of application starters
Group: Development/Python3
License: GPLv3

%description -n nautilus-%name
%descr

%package -n nemo-%name
Summary: Python3 library for creation and modifying of application starters
Group: Development/Python3
License: GPLv3

%description -n nemo-%name
%descr

%package -n mate-file-manager-%name
Summary: Python3 library for creation and modifying of application starters
Group: Development/Python3
License: GPLv3

%description -n mate-file-manager-%name
%descr

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%_datadir/%name
%_man1dir/%name.*
%_iconsdir/hicolor/*/*.png
%_iconsdir/hicolor/scalable/apps/arronax.svg

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/*.egg-info

%files -n nautilus-%name
%_datadir/nautilus-python/extensions/nautilus-arronax.py

%files -n nemo-%name
%_datadir/nemo-python/extensions/nemo-arronax.py

%files -n mate-file-manager-%name
%_datadir/caja-python/extensions/caja-arronax.py

%changelog
* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.8-alt2
- Add icons package (thx to mike@).

* Wed Jul 07 2021 Grigory Ustinov <grenka@altlinux.org> 0.8-alt1
- Initial build for Sisyphus (Closes: #39066).
