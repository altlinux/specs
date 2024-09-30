%define _unpackaged_files_terminate_build 1

Name:      appstream-data-desktop
Summary:   ALT Linux AppStream metadata
Version:   20240830
Release:   alt1
Group:     System/Configuration/Packaging
BuildArch: noarch
License:   CC0 and CC-BY and CC-BY-SA and GFDL
URL:       http://www.altlinux.org/SoftwareCenter/Applications
Source:    %name-%version.tar

Provides:  appstream-data = %EVR
Obsoletes: appstream-data < 20240211

BuildRequires: appstream-data-generator

%description
This package provides the distribution specific AppStream metadata
required for GNOME Software Center or KDE Discover.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/swcatalog/xml
mkdir -p %buildroot%_datadir/swcatalog/icons

cp -r icons/* %buildroot%_datadir/swcatalog/icons/
cp -r xmls/* %buildroot%_datadir/swcatalog/xml/
#cp -r manual-%version/* %buildroot%_datadir/app-info/xmls/

%files
%_datadir/swcatalog/xml/*
%_datadir/swcatalog/icons/altlinux

%changelog
* Fri Aug 30 2024 Kirill Izmestev <felixz@altlinux.org> 20240830-alt1
- Updated database. 

* Fri Aug 02 2024 Kirill Izmestev <felixz@altlinux.org> 20240802-alt1
- Updated database.
- Add gnome-shell-data in skiplist (duplicated gnome-extensions-app).

* Sat Jun 29 2024 Kirill Izmestev <felixz@altlinux.org> 20240705-alt1
- Updated database.

* Sat Jun 29 2024 Kirill Izmestev <felixz@altlinux.org> 20240629-alt1
- Added i586 architecture for generating ProtonPlus package.
- Updated database.

* Fri Jun 14 2024 Kirill Izmestev <felixz@altlinux.org> 20240614-alt1
- Updated database.

* Fri May 31 2024 Kirill Izmestev <felixz@altlinux.org> 20240531-alt1
- Updated database.

* Fri May 17 2024 Kirill Izmestev <felixz@altlinux.org> 20240517-alt1
- Updated database.

* Thu May 16 2024 Ajrat Makhmutov <rauty@altlinux.org> 20240405-alt2
- NMU: Rename the installation directories (ALT #50312).

* Fri Apr 05 2024 Kirill Izmestev <felixz@altlinux.org> 20240405-alt1
- Updated database.

* Fri Mar 22 2024 Kirill Izmestev <felixz@altlinux.org> 20240322-alt1
- Updated database.

* Wed Mar 06 2024 Kirill Izmestev <felixz@altlinux.org> 20240306-alt1
- Updated database.

* Mon Feb 26 2024 Kirill Izmestev <felixz@altlinux.org> 20240226-alt1
- Changed package name to appstream-data-desktop.
- Added provides, obsoletes for appstream-data (thanks antohami@).

* Thu Feb 08 2024 Kirill Izmestev <felixz@altlinux.org> 20240208-alt1
- Updated database.

* Fri Jan 26 2024 Kirill Izmestev <felixz@altlinux.org> 20240126-alt1
- Updated database.

* Tue Jan 09 2024 Kirill Izmestev <felixz@altlinux.org> 20240109-alt1
- Updated database.

* Fri Dec 22 2023 Kirill Izmestev <felixz@altlinux.org> 20231222-alt1
- Updated database.

* Fri Dec 08 2023 Kirill Izmestev <felixz@altlinux.org> 20231208-alt1
- Updated database.

* Fri Nov 24 2023 Kirill Izmestev <felixz@altlinux.org> 20231124-alt1
- Updated database.

* Tue Oct 31 2023 Kirill Izmestev <felixz@altlinux.org> 20231031-alt1
- Updated database.
- Added applications experiencing problems due to data packets (ALT #48240).

* Tue Oct 17 2023 Kirill Izmestev <felixz@altlinux.org> 20231017-alt1
- Updated database.
- Add package name substitution (ALT #47276, ALT #47260).

* Mon Oct 09 2023 Kirill Izmestev <felixz@altlinux.org> 20231009-alt1
- Updated database.

* Tue Sep 19 2023 Kirill Izmestev <felixz@altlinux.org> 20230919-alt1
- Updated database.

* Tue Sep 05 2023 Kirill Izmestev <felixz@altlinux.org> 20230905-alt1
- Updated database.

* Sat Aug 12 2023 Kirill Izmestev <felixz@altlinux.org> 20230812-alt1
- Updated database.
- Add imhex in skiplist.

* Thu Jul 13 2023 Kirill Izmestev <felixz@altlinux.org> 20230713-alt1
- Updated database.

* Thu Jun 29 2023 Kirill Izmestev <felixz@altlinux.org> 20230629-alt1
- Updated database.

* Thu Jun 15 2023 Kirill Izmestev <felixz@altlinux.org> 20230615-alt1
- Updated database.

* Thu Jun 01 2023 Kirill Izmestev <felixz@altlinux.org> 20230601-alt1
- Updated database.

* Thu May 18 2023 Kirill Izmestev <felixz@altlinux.org> 20230518-alt1
- Updated database.

* Fri May 05 2023 Kirill Izmestev <felixz@altlinux.org> 20230505-alt1
- Updated database.

* Wed Apr 19 2023 Kirill Izmestev <felixz@altlinux.org> 20230419-alt1
- Updated database.

* Thu Mar 30 2023 Kirill Izmestev <felixz@altlinux.org> 20230330-alt1
- Updated database.

* Thu Mar 16 2023 Kirill Izmestev <felixz@altlinux.org> 20230316-alt1
- Updated database.

* Wed Mar 1 2023 Kirill Izmestev <felixz@altlinux.org> 20230301-alt1
- Updated database.

* Mon Feb 13 2023 Kirill Izmestev <felixz@altlinux.org> 20230213-alt1
- Updated database.

* Wed Jan 25 2023 Kirill Izmestev <felixz@altlinux.org> 20230125-alt1
- Updated database.

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
