%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtdoc

Name: qt6-doc
Version: 6.6.1
Release: alt1

Group: Development/KDE and QT
Summary: Main Qt6 Reference Documentation
Url: http://qt.io/
License: FDL

#BuildArch: noarch

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake qt6-base-devel
BuildRequires: qt6-svg-devel qt6-declarative-devel qt6-tools-devel

%description
QtDoc contains the main Qt Reference Documentation, which includes
overviews, Qt topics, and examples not specific to any Qt module.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: qt6-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: %name-devel
%description devel-static
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-doc
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
%description -n libqt6-doc
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
#syncqt.pl-qt6 -version %version

%build
%Q6build
%if %qdoc_found
%make -C BUILD docs
%endif

%install
%Q6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif

%files
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*
%_qt6_archdatadir/mkspecs/*doc*

%changelog
* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- initial build
