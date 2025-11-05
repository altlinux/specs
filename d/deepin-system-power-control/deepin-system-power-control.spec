Name: deepin-system-power-control
Version: 1.7.0.1.deepin3
Release: alt1

Summary: TLP settings for DDE

License: GPL-2.0-or-later
Group: Graphical desktop/Other
URL: https://github.com/deepin-community/tlp
VCS: https://github.com/deepin-community/tlp

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
%summary.

%prep
%setup
%patch -p1
patch -p1 < debian/patches/uniontech-deepin-system-power-control.patch

%install
%make_install install-dspc DESTDIR=%buildroot

%files
%doc LICENSE README.rst debian/changelog
%_sbindir/%name
%_datadir/tlp/%name/

%changelog
* Wed Nov 05 2025 Leontiy Volodin <lvol@altlinux.org> 1.7.0.1.deepin3-alt1
- New version 1.7.0.1.deepin3.
- Moved the configs to default place.

* Wed Nov 05 2025 Leontiy Volodin <lvol@altlinux.org> 1.7.0.1.deepin2-alt1
- Initial build for ALT Sisyphus (for deepin-daemon).

