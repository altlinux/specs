%define _unpackaged_files_terminate_build 1
%def_with check

Name: openfreebuds
Version: 0.15.1
Release: alt1
Summary: Open source app for HUAWEI FreeBuds
License: GPL-3.0
Group: Sound
Url: https://mmk.pw/openfreebuds
VCS: https://github.com/melianmiko/OpenFreebuds

Source: %name-%version.tar
Patch1: alt-fix-desktop-comment.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry
BuildRequires: python3-module-PyQt6-devel
BuildRequires: qt6-tools

%if_with check
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-dbus-next
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
%endif

%description
Desktop application to manage wireless headphones from HUAWEI/Honor.

%package -n python3-module-openfreebuds
Summary: Open source app for HUAWEI FreeBuds
Group: Sound
BuildArch: noarch

%description -n python3-module-openfreebuds
Common python3 module and backend for openfreebuds.

%package cmd
Summary: Open source app for HUAWEI FreeBuds
Group: Sound
BuildArch: noarch
Requires: python3-module-openfreebuds = %EVR

%description cmd
CLI interaface for openfreebuds.

%package qt
Summary: Open source app for HUAWEI FreeBuds
Group: Sound
BuildArch: noarch
Requires: python3-module-openfreebuds = %EVR

%description qt
QT interaface for openfreebuds.

%prep
%setup
%patch1 -p1

%build
%pyproject_build
find openfreebuds_qt/designer \
    -type f \
    -name "*.ui" \
    -exec sh -c 'poetry run pyuic6 "$1" -o "${1%.ui}.py"' _ {} \;
lrelease-qt6 openfreebuds_qt/assets/i18n/*.ts

%install
%pyproject_install
cp openfreebuds_qt/designer/*.py %buildroot%python3_sitelibdir/openfreebuds_qt/designer
cp openfreebuds_qt/assets/i18n/*.qm  %buildroot%python3_sitelibdir/openfreebuds_qt/assets/i18n
mkdir -p %buildroot%_desktopdir %buildroot%_pixmapsdir
install -m 0644 openfreebuds_qt/assets/pw.mmk.OpenFreebuds.desktop %buildroot%_desktopdir
install -m 0644 openfreebuds_qt/assets/pw.mmk.OpenFreebuds.png %buildroot%_pixmapsdir

%check
%pyproject_run_pytest

%files -n python3-module-openfreebuds
%python3_sitelibdir/openfreebuds
%python3_sitelibdir/openfreebuds_backend
%python3_sitelibdir/%{pyproject_distinfo openfreebuds}
%exclude %python3_sitelibdir/openfreebuds_backend/windows

%files cmd
%_bindir/openfreebuds_cmd
%python3_sitelibdir/openfreebuds_cmd

%files qt
%_bindir/openfreebuds_qt
%_pixmapsdir/pw.mmk.OpenFreebuds.png
%_desktopdir/pw.mmk.OpenFreebuds.desktop
%python3_sitelibdir/openfreebuds_qt
%exclude %python3_sitelibdir/openfreebuds_qt/designer/*.ui

%changelog
* Tue Dec 03 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.1-alt1
- Initial build for ALT.
