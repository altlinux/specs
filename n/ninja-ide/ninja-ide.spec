Name:       ninja-ide
Version:    2.4
Release:    alt2
Summary:    Ninja IDE for Python development

Group:	    Development/Python
License:    GPL-3.0+
URL:        http://www.ninja-ide.org/
Source0:    https://github.com/downloads/%name/%name/%name-%version.zip
# VCS:      https://github.com/ninja-ide/ninja-ide
Source1:    %name.1
Patch0:     %name-install-to-purelib-dir.patch
Patch1:     %name-fix-desktop-file.patch
Patch2:     %name-fix-python3-syntax.patch
Patch3:     %name-fix-missing-build.patch
Patch4:     %name-python3.8.patch
Patch5:     %name-fix-missing-CONSTANT.patch
Patch6:     %name-replace-distutils.patch

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-pyinotify
BuildRequires:  python3-module-PyQt5-devel
BuildRequires:  unzip

BuildArch:      noarch

%add_python3_req_skip pywintypes win32con win32event win32file

%description
NINJA-IDE is a cross-platform integrated development environment (IDE).
It currently features:

* code editor: NINJA-IDE provides a complete code editor with
  highlighting for several languages, code completion, code assistant
  for imports, navigation, etc.

* project management: NINJA-IDE allows one to manage Python projects
  automatically, saving descriptive information about them and letting
  the user perform file-management-related tasks in the IDE itself.

* high extensibility: you can create plugins for several purposes, and
  they can be completely integrated within the IDE, increasing the
  available features.


%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
rm -f build_files/installer/windows/setup.py

%build
%python3_build

%install
%python3_install
install -Dm 644 icon.png %buildroot/%_pixmapsdir/%name.png
install -Dm 644 %SOURCE1 %buildroot%_man1dir/%name.1

%files
%doc README.md
%_bindir/%name
%python3_sitelibdir/ninja*
%python3_sitelibdir/NINJA_IDE-*.egg-info/
%_pixmapsdir/%name.png
%_desktopdir/*.desktop
%_man1dir/%name.1*

%changelog
* Sat Nov 04 2023 Andrey Cherepanov <cas@altlinux.org> 2.4-alt2
- Replaced deprecated distutils.

* Fri Mar 27 2020 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1
- New version built with Python3 and Qt5.
- Fix License tag according SPDX.

* Mon Dec 21 2015 Andrey Cherepanov <cas@altlinux.org> 2.3-alt2
- Do not use strict extension for man pages

* Thu Apr 17 2014 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- Initial build for ALT Linux (based on Fedora spec)
