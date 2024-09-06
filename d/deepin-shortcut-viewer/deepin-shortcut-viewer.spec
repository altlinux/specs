Name: deepin-shortcut-viewer
Version: 5.0.9
Release: alt2
Summary: Deepin Shortcut Viewer
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-shortcut-viewer
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: dqt5-base-devel dtk5-widget-devel

%description
The program displays a shortcut key window when a JSON data is passed.

%prep
%setup

%build
%qmake_dqt5 \
  CONFIG+=nostrip \
  PREFIX=%prefix \
  QMAKE_RPATHDIR=%_dqt5_libdir
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README.md
%doc LICENSE
%_bindir/%name

%changelog
* Mon May 27 2024 Leontiy Volodin <lvol@altlinux.org> 5.0.9-alt2
- Built via separate qt5 instead system (ALT #48138).

* Tue Apr 09 2024 Leontiy Volodin <lvol@altlinux.org> 5.0.9-alt1
- New version 5.0.9.

* Thu Dec 15 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.7-alt1
- New version (5.0.7).
- Upstream:
  + fix: Display problem of shortcut-viewer.

* Wed Jul 13 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.6-alt1
- New version (5.0.6).
- Upstream:
  + Title: fix Wayland Environmental Calendar-New Schedule Window
  Title/Control Center-Cloud Account Logging Window Title/Open an application,
  the fast key window headings popped are not Hanized.
  + fix: The fast key window will not automatically close and affect
  other applications.
  + chore: Code optimization.

* Wed Apr 28 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.3-alt1
- New version (5.0.3) with rpmgs script.

* Fri Jul 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
