%define _unpackaged_files_terminate_build 1

Name:      appstream-data
Summary:   ALT Linux AppStream metadata
Version:   20230111
Release:   alt1
Group:     System/Configuration/Packaging
BuildArch: noarch
License:   CC0 and CC-BY and CC-BY-SA and GFDL
URL:       http://www.altlinux.org/SoftwareCenter/Applications
Source:    %name-%version.tar

BuildRequires: appstream-data-generator

%description
This package provides the distribution specific AppStream metadata
required for GNOME Software Center or KDE Discover.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/app-info/xmls
mkdir -p %buildroot%_datadir/app-info/icons

cp -r icons/* %buildroot%_datadir/app-info/icons/
cp -r xmls/* %buildroot%_datadir/app-info/xmls/
#cp -r manual-%version/* %buildroot%_datadir/app-info/xmls/

%files
%_datadir/app-info/xmls/*
%_datadir/app-info/icons/altlinux

%changelog
* Wed Jan 11 2023 Kirill Izmestev <felixz@altlinux.org> 20230111-alt1
- Updated database.

* Wed Dec 21 2022 Kirill Izmestev <felixz@altlinux.org> 20221221-alt1
- Updated database.

* Mon Nov 28 2022 Kirill Izmestev <felixz@altlinux.org> 20221128-alt1
- Updated database.

* Fri Nov 04 2022 Andrey Cherepanov <cas@altlinux.org> 20221104-alt1
- Updated database.
- Appended applications from desktop files.

* Sun Oct 02 2022 Andrey Cherepanov <cas@altlinux.org> 20221002-alt1
- Update database.
- Used additionalpackages for icons in another packages.

* Wed Aug 31 2022 Andrey Cherepanov <cas@altlinux.org> 20220831-alt1
- Updated database.

* Wed Jul 27 2022 Andrey Cherepanov <cas@altlinux.org> 20220727-alt1
- Updated database.

* Sun May 15 2022 Andrey Cherepanov <cas@altlinux.org> 20220515-alt1
- Update database.

* Mon Mar 28 2022 Andrey Cherepanov <cas@altlinux.org> 20220328-alt1
- Update database.

* Sat Mar 05 2022 Andrey Cherepanov <cas@altlinux.org> 20220305-alt1
- Update database.

* Sun Feb 20 2022 Andrey Cherepanov <cas@altlinux.org> 20220220-alt1
- Update database.

* Fri Feb 04 2022 Andrey Cherepanov <cas@altlinux.org> 20220204-alt1
- Update database.

* Wed Jan 19 2022 Andrey Cherepanov <cas@altlinux.org> 20220119-alt1
- Update appstream database without refactoring (ALT #41738).

* Thu Sep 19 2019 Andrey Cherepanov <cas@altlinux.org> 20190919-alt1
- Append package with Russian localization for LibreOffice and Firefox.

* Sun Sep 01 2019 Andrey Cherepanov <cas@altlinux.org> 20190901-alt1
- Fix for manual id of conflicted packages (firefox/firefox-esr, LibreOffice/LibreOffice-still) by <launchable> tag
- Add missing project_license tags
- Add apply plugin for screenshot fix
- Move screenshot text to <image> subtag (ALT #37143)
- Fix project license information (ALT #37038)

* Thu Jul 18 2019 Andrey Cherepanov <cas@altlinux.org> 20190718-alt2
- Remove MIME type desktop files.
- appstream-db: add -i parameter for use id instead of pkgname to search.

* Thu Jul 18 2019 Andrey Cherepanov <cas@altlinux.org> 20190718-alt1
- Add LibreOffice and LibreOffice-still.
- Fix gnome-games-aisleriot item.

* Mon Jul 15 2019 Andrey Cherepanov <cas@altlinux.org> 20190715-alt1
- Add applications and popular fonts.

* Sun Jul 14 2019 Andrey Cherepanov <cas@altlinux.org> 20190714-alt1
- Add missing project_license to packages.
- appstream-db: add apply command for mass modification.

* Fri Jul 12 2019 Andrey Cherepanov <cas@altlinux.org> 20190712-alt1
- Mass add applications from its desktop files.
- Fix update-list script.
- Remove old statistic files.

* Wed Jul 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20190702-alt1
- Updated appstream-data for Sisyphus.

* Wed Dec 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 20181212-alt1
- Generated appstream-data for Sisyphus.

* Sun Mar 08 2015 Andrey Cherepanov <cas@altlinux.org> 20150308-alt1
- Initial build in Sisyphus
