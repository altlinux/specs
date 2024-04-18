%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qmltermwidget

Name: qt5-qmltermwidget
Version: 0.2.0
Release: alt2

Group: System/Libraries
Summary: A port of QTermWidget to QML
Url: http://qt.io/
License: GPL-2.0-or-later

Source: %qt_module-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++ glibc-devel
BuildRequires: qt5-base-devel qt5-declarative-devel qt5-tools

%description
This project is a QML port of QTermWidget. It is written
to be as close as possible to the upstream project in order
to make cooperation possible.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: qt5-base-devel rpm-build-qml
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-qmltermwidget
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common
Requires: libqt5-core = %_qt5_version
%description -n libqt5-qmltermwidget
%summary

%prep
%setup -n %qt_module-%version

%build
%qmake_qt5
%make_build
PATH=%_qt5_bindir:$PATH
for f in lib/translations/*_*.ts ; do
    lrelease $f
done

%install
%installqt5
mkdir -p %buildroot/%_qt5_translationdir
for f in lib/translations/*_*.qm ; do
    install -m 0644 $f %buildroot/%_qt5_translationdir/
done
%find_lang --with-qt --all-name %name

%files -f %name.lang
%_qt5_qmldir/QMLTermWidget/


%changelog
* Thu Apr 18 2024 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt2
- update to git 63228027e1f97c24abb907550b22ee91836929c5 (close: 46603)
- package translations

* Fri Jun 11 2021 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- initial build
