Name: macrofusion
Version: 0.7.6
Release: alt1

Summary: GUI to combine photos to get deeper DOF or HDR

License: GPLv3+
Group: Graphics
URL: http://sourceforge.net/projects/macrofusion/
VCS: https://github.com/da-phil/macrofusion

Source: %name-%version.tar
Patch1: macrofusion-0.7.2-desktop.patch

Requires: enblend hugin

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Pillow rpm-build-gir

BuildArch: noarch

%description
MacroFusion is a neat little GUI for great tool Enfuse (command line).
It makes easy fusion few photos to one with great DOF (Deep of Field) or
DR (Dynamic Range). It can be useful for every macro lovers or
landscapers.

%prep
%setup
%patch1 -p1

%build

%install
install -pDm755 macrofusion.py %buildroot%_bindir/macrofusion
install -d %buildroot%_datadir/mfusion
cp -a ui %buildroot%_datadir/mfusion
install -pDm644 images/macrofusion.png %buildroot%_datadir/pixmaps/macrofusion.png
install -pDm644 images/logoSplash.png %buildroot%_datadir/mfusion/images/logoSplash.png
install -pDm644 macrofusion.desktop %buildroot%_desktopdir/macrofusion.desktop

%files
%_bindir/%name
%_datadir/mfusion
%_pixmapsdir/*
%_desktopdir/*

%changelog
* Tue Mar 25 2025 Grigory Ustinov <grenka@altlinux.org> 0.7.6-alt1
- Build new version.

* Wed May 12 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.4-alt2
- Fixed FTBFS.

* Mon Jun 04 2018 Grigory Ustinov <grenka@altlinux.org> 0.7.4-alt1
- Build new version (Closes: #27298).

* Sat Feb 25 2012 Victor Forsiuk <force@altlinux.org> 0.7.3-alt1
- 0.7.3

* Sun Jan 01 2012 Victor Forsiuk <force@altlinux.org> 0.7.2-alt1
- Initial build.
