%define oname PyQtWebEngine

# Note: check QtWebEngine subst below
%define webenginever %(rpm -q --qf '%%{VERSION}' libqt5-webengine | sed -e 's|\\.|_|g')

Name: python3-module-%oname
Version: 5.15.6
Release: alt2

Summary: Python bindings for Qt WebEngine 5

License: GPL
Url: http://www.riverbankcomputing.co.uk/software/pyqtwebengine
Group: Development/Python3

# Source0-url: %__pypi_url %oname
Source0: %name-%version.tar

ExclusiveArch: %qt5_qtwebengine_arches

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-macros-qt5-webengine

BuildRequires: python3-module-sip6 >= 5
BuildRequires: python3-module-PyQt-builder
BuildRequires: python3-module-PyQt5-devel >= %version

BuildRequires(pre): rpm-build-python3 >= 0.1.9.2-alt1
BuildRequires: gcc-c++ python3-devel

BuildRequires: pkgconfig(Qt5WebEngineCore)
BuildRequires: pkgconfig(Qt5WebEngineWidgets)

# makes python3(QtWebEngineCore) only
#add_python3_path %python3_sitelibdir/PyQt5
# but we need
Provides: python3(PyQt5.QtWebEngine)
Provides: python3(PyQt5.QtWebEngineCore)
Provides: python3(PyQt5.QtWebEngineWidgets)

Provides: python3-module-%{pep503_name %oname}

%description
Python bindings for the Qt WebEngine C++ class library.

%package devel
Summary: Sip files for %name
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-PyQt5-devel >= %version
Requires: %name = %EVR

%description devel
Python bindings for the Qt WebEngine C++ class library.

%prep
%setup
#__subst "s|QtWebEngine_5_12_4|QtWebEngine_5_12_4 QtWebEngine_%webenginever|" sip/*/*.sip
#grep -q "QtWebEngine_%webenginever" sip/*/*.sip || { echo "Unsupported QtWebEngine version, see spec file" ; exit 1 ; }

%build
export PATH="$PATH":%_qt5_bindir
sip-build --no-make --debug \
    --api-dir=%_qt5_datadir/qsci/
%make_build -C build

%install
%makeinstall_std -C build INSTALL_ROOT=%buildroot

%files
%python3_sitelibdir/PyQt5/bindings/QtWebEngine/
%python3_sitelibdir/PyQt5/bindings/QtWebEngineCore/
%python3_sitelibdir/PyQt5/bindings/QtWebEngineWidgets/
%python3_sitelibdir/PyQt5/QtWebEngine.*
%python3_sitelibdir/PyQt5/QtWebEngineCore.*
%python3_sitelibdir/PyQt5/QtWebEngineWidgets.*
%python3_sitelibdir/PyQtWebEngine-*

#files devel
#%_datadir/sip3/PyQt5/QtWebEngine*
%_qt5_datadir/qsci/PyQtWebEngine.api

%changelog
* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 5.15.6-alt2
- (NMU) Provided PEP503-normalized project name.

* Thu Aug 04 2022 Vitaly Lipatov <lav@altlinux.ru> 5.15.6-alt1
- new version 5.15.6 (with rpmrb script)

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 5.15.5-alt1
- new version 5.15.5 (with rpmrb script)

* Thu Jul 15 2021 Vitaly Lipatov <lav@altlinux.ru> 5.15.4-alt2
- add BR: python3-module-PyQt5-devel

* Mon Jul 12 2021 Vitaly Lipatov <lav@altlinux.ru> 5.15.4-alt1
- new version 5.15.4 (with rpmrb script)

* Sat Sep 05 2020 Vitaly Lipatov <lav@altlinux.ru> 5.15.0-alt1
- new version 5.15.0 (with rpmrb script)
- download sources from PyPi

* Thu Jan 23 2020 Vitaly Lipatov <lav@altlinux.ru> 5.13.1-alt2
- rebuild with QtWebEngine 5.12.6 (ALT bug 37911)

* Mon Oct 07 2019 Vitaly Lipatov <lav@altlinux.ru> 5.13.1-alt1
- Initial build for ALT Sisyphus

