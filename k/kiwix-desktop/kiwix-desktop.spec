Name:     kiwix-desktop
Version:  2.3.1
Release:  alt1

# no qtwebengine
ExcludeArch: ppc64le

Summary:  Kiwix for Windows and GNU/Linux desktops
License:  GPL-3.0+
Group:    Other
Url:      https://github.com/kiwix/kiwix-desktop

Packager: Andrey Cherepanov <cas@altlinux.org>

# no qtwebengine
ExcludeArch: ppc64le

Source:   %name-%version.tar

BuildRequires(pre): qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-webkit-devel
BuildRequires: qt5-webengine-devel
BuildRequires: qt5-tools
BuildRequires: libkiwix-devel
BuildRequires: aria2

Requires: aria2

%description
%summary

%prep
%setup

%build
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 PREFIX=%_prefix
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc README.md
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*x*/apps/%name.png
%_datadir/metainfo/*.appdata.xml
%_datadir/mime/packages/*.xml

%changelog
* Thu Dec 01 2022 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version.

* Fri Sep 09 2022 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Mon Jun 27 2022 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt2
- Added inheritance for p10.

* Fri Jun 24 2022 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- New version.

* Sun Mar 13 2022 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt1
- New version.

* Sat Mar 05 2022 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.

* Thu Mar 03 2022 Sergey V Turchin <zerg@altlinux.org> 2.0.5-alt2
- exclude ppc64le from build

* Mon Jan 31 2022 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt2
- exclude ppc64le from build

* Sat Jan 22 2022 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Wed Nov 18 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- New version.

* Sat Jul 18 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- New version.

* Thu Jul 02 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1
- New version.

* Wed Jul 01 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version.

* Tue Apr 28 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version.

* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 2.0-alt0.rc4.1
- Initial build for Sisyphus.
