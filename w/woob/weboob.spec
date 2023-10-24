%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif
%def_with docs

%if_enabled qtwebengine
%add_python3_req_skip PyQt5.QtWebKit PyQt5.QtWebKitWidgets
%else
%add_python3_req_skip PyQt5.QtWebEngineCore PyQt5.QtWebEngineWidgets
%endif

Name:    woob
Version: 3.6
Release: alt1

Summary: woob is a collection of applications able to interact with websites, without requiring the user to open them in a browser
License: AGPL-3.0+
Group:   Networking/WWW
URL:     https://woob.tech/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python3
BuildRequires: python3-module-distribute
BuildRequires: python3-module-PyQt5-devel
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pdm-alt-namespace
BuildRequires: python3-module-pdm-pep517
%if_with docs
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-sphinx-autodoc-typehints
%endif

Source: %name-%version.tar
Patch2: weboob-alt-import-from-urllib3-directly.patch
Patch3: woob-alt-fix-logger.patch
Patch4: woob-alt-modules-path.patch

Provides: weboob = %EVR
Obsoletes: weboob < %EVR
Requires: python3-module-woob = %EVR

%description
woob is a collection of applications able to interact with websites, without
requiring the user to open them in a browser. It also provides well-defined
APIs to talk to websites lacking one.

%package -n python3-module-woob
Summary: Python module for Woob
Group: Development/Python3
Provides: python3-module-weboob = %EVR
Obsoletes: python3-module-weboob < %EVR

%description -n python3-module-woob
Python module for Woob.

%prep
%setup -n %name-%version
%patch2 -p1
%patch3 -p1
%patch4 -p1
# Remove unsupported formatter
rm -rf woob/tools/application/formatters/webkit
# Set correct python3 executable in shebang
subst 's|#!.*python[0-9.]*$|#!%__python3|' $(grep -Rl '#!.*python[0-9.]*$' *)
%if_disabled qtwebengine
rm -rf woob/tools/blinkpdf.py
%endif

%build
%pyproject_build
%if_with docs
make -C docs html
%endif

%install
%pyproject_install
if [ "%python3_sitelibdir" != "%python3_sitelibdir_noarch" ] ; then
    mkdir -p %buildroot/%python3_sitelibdir
    mv %buildroot/%python3_sitelibdir_noarch/* %buildroot/%python3_sitelibdir/
fi
mkdir -p %buildroot%_desktopdir
#cp -a desktop/*.desktop %buildroot%_desktopdir
mkdir -p %buildroot%_iconsdir/hicolor/64x64/apps
cp -a icons/*.png %buildroot%_iconsdir/hicolor/64x64/apps
rm -rf %buildroot%python3_sitelibdir/tests
mkdir %buildroot%_datadir/%name
cp -a modules %buildroot%_datadir/%name

%files
%doc AUTHORS README.rst
%if_with docs
%doc docs/build/html/*
%endif
%_bindir/*
#_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.*
%_datadir/%name

%files -n python3-module-woob
%python3_sitelibdir/%name/
%python3_sitelibdir/weboob/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Wed Jun 14 2023 Andrey Cherepanov <cas@altlinux.org> 3.6-alt1
- New version.

* Sat Apr 22 2023 Andrey Cherepanov <cas@altlinux.org> 3.5-alt1
- New version.

* Sun Apr 02 2023 Andrey Cherepanov <cas@altlinux.org> 3.4-alt1
- New version.

* Thu Feb 02 2023 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- New version.
- Renamed to woob.

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
