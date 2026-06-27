%define _unpackaged_files_terminate_build 1

Name: qqc2-suru-style
Version: 0.20260619
Release: alt1

Summary: Suru style for QtQuick Controls 2
License: GPL-2.0-or-later
Group: System/Libraries
Url: https://gitlab.com/ubports/development/core/qqc2-suru-style

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5

BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: qt5-quickcontrols2-devel

%description
This is a style for QtQuickControls 2 providing a uniform look'n'feel
for apps targetting the Lomiri Operatoring / Ubuntu Touch.

This QQC2 style explicitly uses the Suru icon theme for drawing its
elements.

%prep
%setup

%build
%qmake_qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc AUTHORS ChangeLog LICENSE.GPL-2 LICENSE.LGPL-3 README.md
%dir %_qt5_qmldir/QtQuick/Controls.2/Suru
%_qt5_qmldir/QtQuick/Controls.2/Suru/*

%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 0.20260619-alt1
- New version 0.20260619.

* Sun Jul 20 2025 Nikolay Strelkov <snk@altlinux.org> 0.20230630-alt1
- Initial build for Sisyphus
