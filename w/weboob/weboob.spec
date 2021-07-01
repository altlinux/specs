Name:    weboob
Version: 2.0
Release: alt2

Summary: Weboob is a collection of applications able to interact with websites, without requiring the user to open them in a browser
License: AGPL-3.0+
Group:   Networking/WWW
URL:     http://weboob.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python3
BuildRequires: python3-module-distribute
BuildRequires: python3-module-PyQt5-devel

BuildArch: noarch

Source: %name-%version.tar
Patch1: weboob-alt-disable-webkit-formatter.patch
Patch2: weboob-alt-import-from-urllib3-directly.patch

%description
Weboob is a collection of applications able to interact with websites,
without requiring the user to open them in a browser.

%package -n python3-module-weboob
Summary: Python module for Weboob
Group: Development/Python3

%description -n python3-module-weboob
Python module for Weboob.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
# Remove unsupported formatter
rm -rf weboob/tools/application/formatters/webkit
# Set correct python3 executable in shebang
subst 's|#!.*python[0-9.]*$|#!%__python3|' $(grep -Rl '#!.*python[0-9.]*$' *)

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot%_desktopdir
cp -a desktop/*.desktop %buildroot%_desktopdir
mkdir -p %buildroot%_iconsdir/hicolor/64x64/apps
cp -a icons/*.png %buildroot%_iconsdir/hicolor/64x64/apps

%files
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/64x64/apps/*.png
%_man1dir/*

%files -n python3-module-weboob
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Jun 28 2021 Grigory Ustinov <grenka@altlinux.org> 2.0-alt2
- Drop python2 support.

* Fri Feb 14 2020 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- New version.
- Build both modules for Python2 and Python3.

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- New version.

* Sun Feb 17 2019 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- New version.

* Wed Mar 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- Initial build in Sisyphus
