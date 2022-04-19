Name: deepin-clone
Version: 5.0.11
Release: alt1
Summary: Disk and partition backup/restore tool
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-clone
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

ExcludeArch: armh

BuildRequires(pre): desktop-file-utils cmake rpm-build-ninja
BuildRequires: gcc-c++ deepin-gettext-tools dtk5-core-devel dtk5-widget-devel dtk5-common qt5-linguist libpolkitqt5-qt5-devel qt5-base-devel
# Checking for dfm-plugin... no
Requires: icon-theme-hicolor partclone
# Check app/src/fixboot/bootdoctor.cpp
# RHBZ#1687369
# ExclusiveArch: x86_64 %%ix86 aarch64

%description
%summary.

%prep
%setup
sed -i 's|Version=0.1|Version=%version|' app/%name.desktop
# sed -i 's|/usr/sbin|/usr/bin|' \
#     app/com.deepin.pkexec.deepin-clone.policy.tmp \
#     app/deepin-clone-ionice \
#     app/deepin-clone-pkexec \
#     app/src/corelib/helper.cpp

%build
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
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

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files
%doc README.md
%doc LICENSE
%_bindir/%{name}*
%_sbindir/%{name}*
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/mimetypes/*.svg
%_datadir/mime/packages/%name.xml
%_datadir/polkit-1/actions/com.deepin.pkexec.%name.policy

%changelog
* Tue Apr 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.0.11-alt1
- New version (5.0.11).

* Mon May 31 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.10-alt1.1
- NMU: spec: adapted to new cmake macros (altlinux.org/CMakeMigration2021).

* Mon Apr 26 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.10-alt1
- New version (5.0.10) with rpmgs script.
- Built with cmake and ninja instead qmake and make.

* Tue Aug 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.3-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
