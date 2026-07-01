Name: deepin-desktop-base
Version: 2026.06.30
Release: alt1

Summary: Base component for Deepin

License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-desktop-base
Vcs: https://github.com/linuxdeepin/deepin-desktop-base

Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
#Recommends:     deepin-wallpapers
#Recommends:     deepin-screensaver
#Recommends:     plymouth-theme-deepin
Requires: menu-icons-default

%description
This package provides some components for Deepin desktop environment.

- deepin logo
- deepin desktop version
- login screen background image
- language information

%prep
%setup
%patch -p1

%build
%make_build

%install
%makeinstall_std

install -Dm644 distribution.info -t %buildroot%_datadir/deepin/
# Remove Deepin distro's lsb-release
rm %buildroot/etc/lsb-release
# Don't override systemd timeouts
rm -r %buildroot/etc/systemd
# Make a symlink for deepin-version
mkdir -p %buildroot%_sysconfdir/
ln -s %_libexecdir/deepin/desktop-version %buildroot%_sysconfdir/deepin-version
# Install os-version and rename to uos-version
install -Dm644 files/os-version %buildroot%_sysconfdir/uos-version
# Remove apt-specific templates
rm -r %buildroot/usr/share/python-apt
# Remove empty distro info directory
rm -r %buildroot%_datadir/distro-info

%files
%doc LICENSE debian/changelog
%exclude %_sysconfdir/appstore.json
%dir %_datadir/deepin/
%_datadir/deepin/distribution.info
%_datadir/i18n/i18n_dependent.json
%_datadir/i18n/language_info.json
%dir %_libexecdir/deepin/
%_libexecdir/deepin/desktop-version
%_sysconfdir/deepin-version
%_sysconfdir/uos-version
%exclude %_datadir/plymouth/deepin-logo.png

%changelog
* Wed Jul 01 2026 Leontiy Volodin <lvol@altlinux.org> 2026.06.30-alt1
- New version 2026.06.30.

* Wed Jun 03 2026 Leontiy Volodin <lvol@altlinux.org> 2026.05.25-alt1
- New version 2026.05.25.

* Fri Apr 10 2026 Leontiy Volodin <lvol@altlinux.org> 2026.03.25-alt1
- New version 2026.03.25.

* Tue Mar 10 2026 Leontiy Volodin <lvol@altlinux.org> 2026.01.27-alt1
- New version 2026.01.27.

* Wed Jan 28 2026 Leontiy Volodin <lvol@altlinux.org> 2025.12.22-alt1
- New version 2025.12.22.

* Wed Nov 26 2025 Leontiy Volodin <lvol@altlinux.org> 2025.11.25-alt1
- New version 2025.11.25.

* Wed Sep 24 2025 Leontiy Volodin <lvol@altlinux.org> 2025.09.22-alt1
- New version 2025.09.22.

* Thu Sep 11 2025 Leontiy Volodin <lvol@altlinux.org> 2025.08.22-alt1
- New version 2025.08.22.

* Fri Jul 18 2025 Leontiy Volodin <lvol@altlinux.org> 2025.06.23-alt1
- New version 2025.06.23.

* Tue Apr 29 2025 Leontiy Volodin <lvol@altlinux.org> 2025.03.06-alt1
- New version 2025.03.06.

* Thu Apr 17 2025 Leontiy Volodin <lvol@altlinux.org> 2024.07.26-alt1
- New version 2024.07.26.
- Added vcs tag.
- Used distribution.info for ALT.

* Tue Feb 06 2024 Leontiy Volodin <lvol@altlinux.org> 2024.01.03-alt1
- New version 2024.01.03.

* Thu Nov 30 2023 Leontiy Volodin <lvol@altlinux.org> 2023.09.05-alt1
- New version 2023.09.05.

* Fri Oct 20 2023 Ivan A. Melnikov <iv@altlinux.org> 2023.03.31-alt1.1
- NMU: loongarch64 support

* Thu Apr 13 2023 Leontiy Volodin <lvol@altlinux.org> 2023.03.31-alt1
- New version 2023.03.31.

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
