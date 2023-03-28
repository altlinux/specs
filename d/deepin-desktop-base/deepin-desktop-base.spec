Name: deepin-desktop-base
Version: 2022.11.15
Release: alt1
Summary: Base component for Deepin
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-desktop-base
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Source1: distribution.info
Patch: deepin-desktop-base-2022.07.26-alt-fix-multiarch-build.patch
Patch1: deepin-desktop-base-2022.11.15-upstream-chore-208-release.patch

BuildArch: noarch
#Recommends:     deepin-wallpapers
#Recommends:     deepin-screensaver
#Recommends:     plymouth-theme-deepin

%description
This package provides some components for Deepin desktop environment.

- deepin logo
- deepin desktop version
- login screen background image
- language information

%prep
%setup
%autopatch -p1

%build
%make_build

%install
%makeinstall_std

install -Dm644 %SOURCE1 -t %buildroot/usr/share/deepin/
# Remove Deepin distro's lsb-release
rm %buildroot/etc/lsb-release
# Don't override systemd timeouts
rm -r %buildroot/etc/systemd
# Make a symlink for deepin-version
mkdir -p %buildroot%_sysconfdir/
ln -sfv ../usr/lib/deepin/desktop-version %buildroot%_sysconfdir/deepin-version
# Remove apt-specific templates
rm -r %buildroot/usr/share/python-apt

%files
%doc LICENSE
%exclude %_sysconfdir/appstore.json
%dir %_datadir/deepin/
%_datadir/deepin/distribution.info
%_datadir/i18n/i18n_dependent.json
%_datadir/i18n/language_info.json
%_libexecdir/deepin/desktop-version
%_sysconfdir/deepin-version
%exclude %_datadir/plymouth/deepin-logo.png

%changelog
* Tue Mar 28 2023 Leontiy Volodin <lvol@altlinux.org> 2022.11.15-alt1
- New version 2022.11.15.

* Mon Aug 08 2022 Leontiy Volodin <lvol@altlinux.org> 2022.07.26-alt1
- New version (2022.07.26).
- Used distribution logo.

* Wed Mar 16 2022 Leontiy Volodin <lvol@altlinux.org> 2021.11.08-alt1
- New version (2021.11.08).

* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 2021.06.16-alt1
- New version (2021.06.16).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 2021.5.07-alt1
- New version (2021.5.07) with rpmgs script.

* Tue Apr 20 2021 Leontiy Volodin <lvol@altlinux.org> 2021.3.10-alt1
- New version (2021.3.10) with rpmgs script.

* Wed Mar 03 2021 Leontiy Volodin <lvol@altlinux.org> 2021.2.20-alt1
- New version (2021.2.20) with rpmgs script.

* Mon Feb 08 2021 Leontiy Volodin <lvol@altlinux.org> 2021.1.25-alt1
- New version (2021.1.25) with rpmgs script.
- Removed subpackage deepin-manual-directory.

* Wed Feb 03 2021 Leontiy Volodin <lvol@altlinux.org> 2021.1.12-alt1
- New version (2021.1.12) with rpmgs script.

* Wed Dec 30 2020 Leontiy Volodin <lvol@altlinux.org> 2020.12.09-alt1
- New version (2020.12.09) with rpmgs script.

* Wed Dec 02 2020 Leontiy Volodin <lvol@altlinux.org> 2020.11.04-alt1
- New version (2020.11.04) with rpmgs script.

* Tue Aug 04 2020 Leontiy Volodin <lvol@altlinux.org> 2020.07.31-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
