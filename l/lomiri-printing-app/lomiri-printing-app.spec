%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: lomiri-printing-app
Version: 0.4.2
Release: alt1

Summary: Printing app which consumes a PDF from content hub
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-printing-app

Source: %name-%version.tar

# sync with version 0.4.2-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ayatana-cmake-modules
BuildRequires: pkgconfig(poppler-qt5)
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: intltool

%if_with check
BuildRequires: ctest
BuildRequires: /usr/bin/xvfb-run
BuildRequires: qt5-declarative-devel
BuildRequires: qml(Lomiri.Test)
BuildRequires: qml(Lomiri.Components.Extras)
%endif

Requires: libqt5-qml
Requires: libqt5-quick
Requires: qml(Lomiri.Components)
Requires: qml(Lomiri.Components.Extras)
Requires: qml(Lomiri.Content)

%description
This app is an add-on app for Ubuntu Touch's shell Lomiri. Ubuntu Touch
is a mobile OS developed by the UBports Foundation. Lomiri is its
operating environment optimized for touch based human-machine
interaction, but also supports convergence (i.e. switching between
tablet/phone and desktop mode).

This package provides Lomiri's Printing App. The printing app consumes a
PDF document from Lomiri's content-hub, allows for basic configuration
and then sends the to-be-printed document to a CUPS print queue.

%prep
%setup
%patch -p1

%build
export PATH=$PATH:/usr/share/qt5/bin
%cmake \
       -DCLICK_MODE=OFF \
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %name

%check
export PATH=$PATH:/usr/share/qt5/bin
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%_bindir/lomiri-printing-app
%_bindir/lomiri-printqueue-dialog
%dir %_qt5_qmldir/LomiriPrintingApp
%_qt5_qmldir/LomiriPrintingApp/libLomiriPrintingAppBackend.so
%_qt5_qmldir/LomiriPrintingApp/qmldir
%_desktopdir/lomiri-printing-app.desktop
%_desktopdir/lomiri-printqueue-dialog.desktop
%dir %_datadir/lomiri-printing-app
%_datadir/lomiri-printing-app/*
%_datadir/lomiri-content-hub/peers/lomiri-printing-app
%_datadir/lomiri-url-dispatcher/urls/lomiri-printqueue-dialog.url-dispatcher

%exclude %_datadir/locale/zh_Hans/LC_MESSAGES/lomiri-printing-app.mo
%exclude %_datadir/locale/zh_Hant/LC_MESSAGES/lomiri-printing-app.mo
%exclude %_datadir/locale/zh_Hant_HK/LC_MESSAGES/lomiri-printing-app.mo

%changelog
* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus
