Name: deepin-clone
Version: 5.0.15.0.4.bc86
Release: alt2

Summary: Disk and partition backup/restore tool

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-clone

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

ExcludeArch: armh

Requires: icon-theme-hicolor partclone

BuildRequires(pre): desktop-file-utils cmake rpm-build-ninja
BuildRequires: gcc-c++ deepin-gettext-tools dtkcore libdtkwidget-devel dtk6-common-devel dqt5-linguist libpolkitqt5-qt5-devel dqt5-base-devel

%description
%summary.

%prep
%setup
%patch -p1
sed -i 's|Version=0.1|Version=%version|' app/%name.desktop

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DDISABLE_DFM_PLUGIN=YES \
    -DDISABLE_DFM_PLUGIN=YES \
    -DENABLE_GUI=YES \
    -DVERSION=%version \
    -DAPP_VERSION=%version \
    %nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
chmod +x %buildroot%_bindir/deepin-clone-pkexec
chmod +x %buildroot%_sbindir/deepin-clone-ionice
%find_lang --with-qt %name

%files -f %name.lang
%doc README.md LICENSE
%_bindir/%{name}*
%_sbindir/%{name}*
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/%name.qm
%_datadir/%name/translations/%{name}_es_419.qm
%_datadir/%name/translations/policy.qm
%_datadir/%name/translations/policy_es_419.qm
%_iconsdir/hicolor/scalable/mimetypes/*.svg
%_datadir/mime/packages/%name.xml
%_datadir/polkit-1/actions/com.deepin.pkexec.%name.policy

%changelog
* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 5.0.15.0.4.bc86-alt2
- Built via separate qt5 instead system (ALT #48138).

* Sat Dec 30 2023 Leontiy Volodin <lvol@altlinux.org> 5.0.15.0.4.bc86-alt1
- New version 5.0.15-4-gbc86458.

* Tue Apr 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.11-alt1
- New version (5.0.11).

* Mon May 31 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.10-alt1.1
- NMU: spec: adapted to new cmake macros (altlinux.org/CMakeMigration2021).

* Mon Apr 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.10-alt1
- New version (5.0.10) with rpmgs script.
- Built with cmake and ninja instead qmake and make.

* Tue Aug 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.3-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
