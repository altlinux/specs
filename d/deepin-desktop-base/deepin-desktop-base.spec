Name: deepin-desktop-base
Version: 2021.11.08
Release: alt1
Summary: Base component for Deepin
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-desktop-base
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-desktop-base_2021.3.10_alt_fix-multiarch-build.patch

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
%patch -p2

# Remove Deepin distro's lsb-release
# Don't override systemd timeouts
# Remove apt-specific templates
sed -E '/lsb-release|systemd|apt|back/d' Makefile

# Fix data path
sed -i 's|/usr/lib|%_datadir|' Makefile

# Set deepin type to Desktop
sed -i 's|Type=.*|Type=Desktop|; /Type\[/d; s|Version=.*|Version=20.3|' files/desktop-version*.in

sed -i 's|/etc/systemd/|/lib/systemd/|' Makefile

%build
%make_build

%install
%makeinstall_std

# Make a symlink for deepin-version
mkdir -p %buildroot/etc/
ln -sfv ..%_datadir/deepin/desktop-version %buildroot/etc/deepin-version

%files
%doc LICENSE
%exclude %_sysconfdir/appstore.json
%dir %_datadir/deepin/
%_datadir/i18n/i18n_dependent.json
%_datadir/i18n/language_info.json
%_datadir/deepin/desktop-version
%_sysconfdir/deepin-version
%exclude %_datadir/plymouth/deepin-logo.png
%exclude %_sysconfdir/lsb-release
/lib/systemd/system.conf.d/deepin-base.conf
/lib/systemd/logind.conf.d/deepin-base.conf
%exclude %_datadir/python-apt/templates/Deepin.info
%exclude %_datadir/python-apt/templates/Deepin.mirrors

%changelog
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
