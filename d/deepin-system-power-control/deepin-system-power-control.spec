Name: deepin-system-power-control
Version: 1.7.0.1.deepin2
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

%install
install -d %buildroot%_datadir/tlp/%name
install -D -t %buildroot%_sbindir debian/%name/%name
install -D -t %buildroot%_sysconfdir/tlp.d debian/%name/*.conf

%files
%doc LICENSE README.rst debian/changelog
%_sbindir/%name
%config(noreplace) %_sysconfdir/tlp.d/*.conf
%dir %_datadir/tlp/%name

%changelog
* Wed Nov 05 2025 Leontiy Volodin <lvol@altlinux.org> 1.7.0.1.deepin2-alt1
- Initial build for ALT Sisyphus (for deepin-daemon).

