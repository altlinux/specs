%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%if_enabled qtwebengine
%add_python3_req_skip PyQt5.QtWebKit PyQt5.QtWebKitWidgets
%else
%add_python3_req_skip PyQt5.QtWebEngineCore PyQt5.QtWebEngineWidgets
%endif

Name:    weboob
Version: 2.0
Release: alt5

Summary: Weboob is a collection of applications able to interact with websites, without requiring the user to open them in a browser
License: AGPL-3.0+
Group:   Networking/WWW
URL:     http://weboob.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python3
BuildRequires: python3-module-distribute
BuildRequires: python3-module-PyQt5-devel

Source: %name-%version.tar
Patch1: weboob-alt-disable-webkit-formatter.patch
Patch2: weboob-alt-import-from-urllib3-directly.patch

Requires: python3-module-weboob = %EVR

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
%if_disabled qtwebengine
rm -rf weboob/tools/blinkpdf.py
%endif

%build
%python3_build

%install
%python3_install
if [ "%python3_sitelibdir" != "%python3_sitelibdir_noarch" ] ; then
    mkdir -p %buildroot/%python3_sitelibdir
    mv %buildroot/%python3_sitelibdir_noarch/* %buildroot/%python3_sitelibdir/
fi
mkdir -p %buildroot%_desktopdir
cp -a desktop/*.desktop %buildroot%_desktopdir
mkdir -p %buildroot%_iconsdir/hicolor/64x64/apps
cp -a icons/*.png %buildroot%_iconsdir/hicolor/64x64/apps

%files
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.*
%_man1dir/*

%files -n python3-module-weboob
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Feb 03 2022 Sergey V Turchin <zerg@altlinux.org> 2.0-alt5
- fix previous ugly packaging

* Wed Feb 02 2022 Sergey V Turchin <zerg@altlinux.org> 2.0-alt4
- disable using of qtwebengine on e2k and ppc64le

* Wed Jul 14 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt3
- add require python module weboob (ALT bug 40486)

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
