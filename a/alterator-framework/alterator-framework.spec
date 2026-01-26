%define _unpackaged_files_terminate_build 1

Name: alterator-framework
Version: 0.1.0
Release: alt1

Summary: Qt 6-based host application for Alterator QML modules
License: %gpl3only
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-framework

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-build-licenses

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools

Requires: qt6-translations
Requires: qt6-svg
Requires: alterator-application-framework
Requires: alterator-interface-framework
Requires: alterator-module-backend3 >= 0.2.0-alt1

%description
Qt 6-based host application for Alterator modules.

It loads UI modules written in QML and connects them to backend3 over D-Bus.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DALTERATOR_FRAMEWORK_VERSION=%version
%cmake_build

%install
%cmakeinstall_std

install -d %buildroot%_datadir/alterator-framework/modules


%files
%_bindir/alterator-framework
%dir %_datadir/alterator-framework
%dir %_datadir/alterator-framework/modules
%dir %_datadir/alterator-framework/qml
%dir %_datadir/alterator-framework/qml/AlteratorFramework
%dir %_datadir/alterator-framework/ts
%_datadir/alterator-framework/qml/AlteratorFramework/*
%_datadir/alterator-framework/ts/*.qm
%_datadir/applications/alterator-framework.desktop
%_datadir/icons/hicolor/scalable/apps/alterator-framework.svg
%doc README.md LICENSE


%changelog
* Mon Jan 19 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.0-alt1
- Init build for Sisyphus (thx Oleg Chagaev).

