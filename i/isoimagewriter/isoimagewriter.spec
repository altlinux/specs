%define rname isoimagewriter
%define nameL org.kde.isoimagewriter

Name: isoimagewriter
Version: 26.04.2
Release: alt1

Group: Archiving/Cd burning
Summary: Program to write hybrid ISO files onto USB disks
License: GPL-3.0-or-later
Url: https://apps.kde.org/ru/isoimagewriter
Vcs: https://invent.kde.org/utilities/isoimagewriter

Provides: rosa-imagewriter = %version
Obsoletes: rosa-imagewriter < 3

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: kf6-ki18n-devel kf6-kcoreaddons-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kiconthemes-devel kf6-karchive-devel kf6-kcrash-devel
BuildRequires: kf6-solid-devel

%description
%summary

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
for n in RosaImageWriter rosa-imagewriter ; do
    ln -sr %buildroot/%_K6bin/%rname %buildroot/%_K6bin/$n
done

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc *.md LICENSES
%_K6bin/*mage*riter
%_K6xdgapp/*%{rname}*.desktop
%_K6icon/hicolor/*/apps/*%{rname}*.svg
%_K6data/%rname/
%_datadir/metainfo/*%{rname}*.xml

%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Tue Mar 24 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt2
- provide rosa-imagewriter binaries

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Wed Oct 01 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt2
- obsolete rosa-imagewriter

* Fri Sep 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.08.1-alt1
- 25.08.0 -> 25.08.1

* Fri Aug 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.08.0-alt1
- 25.04.3 -> 25.08.0

* Fri Jul 04 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.04.3-alt1
- 25.04.2 -> 25.04.3

* Fri Jun 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.04.2-alt1
- 25.04.1 -> 25.04.2

* Thu May 29 2025 Aleksandr Shamaraev <shad@altlinux.org> 25.04.1-alt1
- Initial build for ALT Linux.
