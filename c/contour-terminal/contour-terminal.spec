%define _unpackaged_files_terminate_build 1

%def_with check

Name: contour-terminal
Version: 0.7.0.8982
Release: alt2

Summary: Modern C++ Terminal Emulator
License: Apache-2.0
Group: Terminals
Url: https://github.com/contour-terminal/contour

Source: %name-%version.tar

BuildRequires(pre): cmake

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

%if_with check
BuildRequires: ctest
BuildRequires: catch-devel
%endif

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
%ctest -E "vtconformance_test|contour_gui_test|contour_e2e_lifecycle|contour_e2e_vt_stream|contour_e2e_custom_config"

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
%_iconsdir/hicolor/128x128/apps/org.contourterminal.Contour.png
%_iconsdir/hicolor/256x256/apps/org.contourterminal.Contour.png
%_iconsdir/hicolor/32x32/apps/org.contourterminal.Contour.png
%_iconsdir/hicolor/512x512/apps/org.contourterminal.Contour.png
%_iconsdir/hicolor/64x64/apps/org.contourterminal.Contour.png
%_datadir/kio/servicemenus/org.contourterminal.Contour.OpenHere.desktop
%_datadir/kio/servicemenus/org.contourterminal.Contour.RunIn.desktop
%_datadir/metainfo/org.contourterminal.Contour.metainfo.xml

%changelog
* Tue Aug 25 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.0.8982-alt2
- Build with libssh2.

* Mon Aug 24 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.0.8982-alt1
- Initial build for Sisyphus

