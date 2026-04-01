%define oname pyqt6_webengine

# Note: check QtWebEngine subst below
%define webenginever %(rpm -q --qf '%%{VERSION}' libqt6-webenginecore | sed -e 's|\\.|_|g')

Name: python3-module-PyQt6-WebEngine
Version: 6.10.0
Release: alt1

Summary: Python bindings for Qt6 WebEngine

License: GPLv3
Url: http://www.riverbankcomputing.co.uk/software/pyqtwebengine
Group: Development/Python3

# Source0-url: %__pypi_url %oname
Source0: %name-%version.tar

ExclusiveArch: %qt6_qtwebengine_arches

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-macros-qt6-webengine

BuildRequires: python3-module-sip6 >= 5
BuildRequires: python3-module-PyQt-builder
BuildRequires: python3-module-PyQt6-devel >= %version

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ python3-devel

BuildRequires: python3(PyQt6.QtWebChannel)
BuildRequires: pkgconfig(Qt6WebEngineCore)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)

Provides: python3-module-%{pep503_name %oname}

%description
Python bindings for the Qt6 WebEngine C++ class library.

%package devel
Summary: Sip files for %name
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-PyQt6-devel >= %version
Requires: %name = %EVR

%description devel
Python bindings for the Qt6 WebEngine C++ class library.

%prep
%setup
%build
export PATH="$PATH":%_qt6_bindir
sip-build --no-make --debug \
    --api-dir=%_qt6_datadir/qsci/
%make_build -C build

%install
%makeinstall_std -C build INSTALL_ROOT=%buildroot

%files
%python3_sitelibdir/PyQt6/bindings/QtWebEngineCore/
%python3_sitelibdir/PyQt6/bindings/QtWebEngineQuick/
%python3_sitelibdir/PyQt6/bindings/QtWebEngineWidgets/
%python3_sitelibdir/PyQt6/QtWebEngineCore.*
%python3_sitelibdir/PyQt6/QtWebEngineQuick.*
%python3_sitelibdir/PyQt6/QtWebEngineWidgets.*
%python3_sitelibdir/*.dist-info

%_qt6_datadir/qsci/PyQt6-WebEngine.api

%changelog
* Wed Apr 01 2026 Vitaly Lipatov <lav@altlinux.ru> 6.10.0-alt1
- new version 6.10.0 (with rpmrb script)
- fix Source-url: use lowercase oname for PyPI

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt2
- NMU: fix package with Qt-6.9

* Sat Mar 02 2024 Vitaly Lipatov <lav@altlinux.ru> 6.6.0-alt1
- initial build for ALT Sisyphus
