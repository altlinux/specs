%define _unpackaged_files_terminate_build 1

Name: kiwix-desktop
Version: 2.4.1
Release: alt1

Summary: Offline reader for works with the highly compressed ZIM file format
License: GPL-3.0-or-later
Group: Other
Url: https://kiwix.org
VCS: https://github.com/kiwix/kiwix-desktop.git
ExclusiveArch: %qt6_qtwebengine_arches

Source: %name-%version.tar

Requires: aria2

BuildRequires(pre): qt6-base-devel
BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: aria2
BuildRequires: libkiwix-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools
BuildRequires: qt6-webengine-devel

%description
Kiwix is an offline reader and manager for online content
like Wikipedia, Project Gutenberg, or TED Talks.
Kiwix allows you to read and search through offline content
as they were online. Similar to a browser, Kiwix works with
the highly compressed ZIM file format.

%prep
%setup

%build
export PATH=%_qt6_bindir:$PATH
%qmake_qt6 PREFIX=%_prefix
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc README.md
%_bindir/*
%_datadir/metainfo/*.appdata.xml
%_datadir/mime/packages/*.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/kiwix-desktop.svg
%_iconsdir/hicolor/*x*/apps/%name.png

%changelog
* Sat Dec 21 2024 Constantin Sunzow <protvin@altlinux.org> 2.4.1-alt1
- Enable check for unpackaged files.
- Regroup spec tags and trim unnecessary spaces.
- Changelog correction.
- New version.

* Mon Dec 16 2024 Constantin Sunzow <protvin@altlinux.org> 2.4.0-alt1
- Merge source code to main directory.
- Build against Qt 6.
- Use ExclusiveArch instead ExcludeArch.
- New version.

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
