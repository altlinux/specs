Name: folder-color-switcher
Version: 1.7.1
Release: alt3

Summary: Folder Color Switcher extensions

License: GPL-3.0
Group: Graphical desktop/MATE
URL: https://github.com/linuxmint/folder-color-switcher
VCS: https://github.com/linuxmint/folder-color-switcher.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python3

%description
Folder Color Switcher extensions for Caja and Nemo.

%package common
Summary: Folder Color Switcher extensions common files
Group: Graphical desktop/MATE

%description common
%summary.

%package -n caja-%name
Summary: Folder Color Switcher extension for Caja
Group: Graphical desktop/MATE

Requires: %name-common = %EVR
Requires: python3-module-caja
Requires: %_bindir/caja

%description -n caja-%name
Allows you to change folder colors from the context menu under supported icon themes.

%package -n nemo-%name
Summary: Folder Color Switcher extension for Nemo
Group: Graphical desktop/Other

Requires: %name-common = %EVR
Requires: nemo-python

%description -n nemo-%name
Allows you to change folder colors from the context menu under supported icon themes.

%prep
%setup

%build
chmod -x COPYING.GPL3
%make_build

%install
mkdir -p %buildroot%prefix
cp -a usr/* %buildroot%prefix
%find_lang %name

%files common -f %name.lang
%doc COPYING.GPL3
%_datadir/%name/color.svg

%files -n caja-%name
%_datadir/caja-python/extensions/caja-%name.py

%files -n nemo-%name
%_datadir/nemo-python/extensions/nemo-%name.py

%changelog
* Sun May 24 2026 Alexander Kovalev <alexvk@altlinux.org> 1.7.1-alt3
- Fixed spec.

* Wed Apr 22 2026 Alexander Kovalev <alexvk@altlinux.org> 1.7.1-alt2
- Added requires for Caja extension.

* Sat Jan 17 2026 Alexander Kovalev <alexvk@altlinux.org> 1.7.1-alt1
- New version 1.7.1.

* Sun Aug 10 2025 Alexander Kovalev <alexvk@altlinux.org> 1.6.8-alt1
- New version 1.6.8.

* Mon Apr 14 2025 Alexander Kovalev <alexvk@altlinux.org> 1.6.7-alt1
- Initial build for ALT.
