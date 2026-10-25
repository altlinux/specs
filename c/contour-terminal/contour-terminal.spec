%define _unpackaged_files_terminate_build 1

%def_with check

Name: contour-terminal
Version: 0.8.0.9335
Release: alt1

Summary: Modern C++ Terminal Emulator
License: Apache-2.0
Group: Terminals
Url: https://github.com/contour-terminal/contour

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: gcc-c++
BuildRequires: libmicrosoft-gsl-devel
BuildRequires: pkgconfig(yaml-cpp)
BuildRequires: pkgconfig(freetype2)
BuildRequires: libunicode-devel
BuildRequires: libboxed-cpp-devel
BuildRequires: libreflection-cpp-devel
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6ShaderTools)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: /usr/bin/tic
BuildRequires: libutempter-devel
BuildRequires: pkgconfig(libsystemd)

%if_with check
BuildRequires: ctest
BuildRequires: catch-devel
BuildRequires: libqt6-core5compat
%endif

ExcludeArch: %ix86

Requires: libqt6-core5compat
Requires: libqt6-qml
Requires: libqt6-multimediaquick
Requires: libqt6-quicklayouts
Requires: libqt6-quickcontrols2fusion
Requires: libqt6-quickcontrols2basic
Requires: libqt6-quicktemplates2

Requires: terminfo-extra

%description
Contour is a modern and actually fast, modal, virtual terminal emulator,
for everyday use. It is aiming for power users with a modern feature mindset.

%prep
%setup
sed -i "s|docs/screenshots/contour-notcurses-ncneofetch.png|contour-notcurses-ncneofetch.png|" README.md

%build
%cmake \
       -DCONTOUR_USE_CPM=OFF \
       -DCONTOUR_PACKAGE_TERMINFO=OFF \
%if_with check
       -DCONTOUR_TESTING=ON
%else
       -DCONTOUR_TESTING=OFF
%endif
%cmake_build

%install
%cmake_install

%check
%ctest -E "vtpty_test|vtconformance_test|vthost_test|contour_gui_test|contour_e2e_lifecycle|contour_e2e_vt_stream|contour_e2e_custom_config|contour_test"

%files
%doc LICENSE.txt README.md docs/screenshots/contour-notcurses-ncneofetch.png
%_bindir/contour
%_desktopdir/org.contourterminal.Contour.desktop
%exclude %_datadir/contour/LICENSE.txt
%exclude %_datadir/contour/README.md
%dir %_datadir/contour
%dir %_datadir/contour/shell-integration
%_datadir/contour/shell-integration/shell-integration.bash
%_datadir/contour/shell-integration/shell-integration.fish
%_datadir/contour/shell-integration/shell-integration.tcsh
%_datadir/contour/shell-integration/shell-integration.zsh
%_datadir/contour/shell-integration/shell-integration.pwsh
%_iconsdir/hicolor/128x128/apps/org.contourterminal.Contour.png
%_iconsdir/hicolor/256x256/apps/org.contourterminal.Contour.png
%_iconsdir/hicolor/32x32/apps/org.contourterminal.Contour.png
%_iconsdir/hicolor/512x512/apps/org.contourterminal.Contour.png
%_iconsdir/hicolor/64x64/apps/org.contourterminal.Contour.png
%_datadir/kio/servicemenus/org.contourterminal.Contour.OpenHere.desktop
%_datadir/kio/servicemenus/org.contourterminal.Contour.RunIn.desktop
%_datadir/metainfo/org.contourterminal.Contour.metainfo.xml
%_userunitdir/app-glib-org.contourterminal.Contour-.scope.d/50-oom-policy.conf
%_userunitdir/app-gnome-org.contourterminal.Contour-.scope.d/50-oom-policy.conf
%_userunitdir/app-org.contourterminal.Contour-.scope.d/50-oom-policy.conf
%_userunitdir/app-org.contourterminal.Contour@.service.d/50-oom-policy.conf

%changelog
* Sun Oct 25 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.0.9335-alt1
- New version 0.8.0.9335.
- Exclude %%ix86 arch as not buildable.

* Tue Aug 25 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.0.8982-alt2
- Build with libssh2.

* Mon Aug 24 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.0.8982-alt1
- Initial build for Sisyphus

