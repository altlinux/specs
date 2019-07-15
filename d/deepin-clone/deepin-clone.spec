Name: deepin-clone
Version: 5.0.3
Release: alt1
Summary: Disk and partition backup/restore tool
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-clone
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-clone_5.0.3_archlinux_dtk5.patch
Patch1: deepin-clone_5.0.3_alt_qt5.15.patch

ExcludeArch: armh

BuildRequires(pre): desktop-file-utils
BuildRequires: gcc-c++ deepin-gettext-tools dtk5-core-devel dtk5-widget-devel qt5-linguist libpolkitqt5-qt5-devel qt5-base-devel
# Checking for dfm-plugin... no
Requires: icon-theme-hicolor partclone
# Check app/src/fixboot/bootdoctor.cpp
# RHBZ#1687369
# ExclusiveArch: x86_64 %%ix86 aarch64

%description
%summary.

%prep
%setup
%patch -p1
%patch1 -p2
%__subst 's|/usr/sbin|/usr/bin|' app/{%name-app.pro,%name-ionice,%name-pkexec,com.deepin.pkexec.%name.policy.tmp}
%__subst 's|lrelease|lrelease-qt5|' app/translate_generation.sh
%__subst 's|Version=0.1|Version=%version|' app/%name.desktop

%build
%qmake_qt5 PREFIX=%_prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files
%doc README.md
%doc LICENSE
%_bindir/%{name}*
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/scalable/mimetypes/*.svg
%_datadir/mime/packages/%name.xml
%_datadir/polkit-1/actions/com.deepin.pkexec.%name.policy

%changelog
* Tue Aug 04 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.3-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
