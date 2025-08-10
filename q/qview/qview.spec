%define _unpackaged_files_terminate_build 1

Name: qview
Version: 7.1
Release: alt1
Summary: Practical and minimal image viewer
License: GPL-3.0
Group: Graphics
Url: https://interversehq.com/qview
VCS: https://github.com/jurplel/qView

Source: %name-%version.tar

BuildRequires: qt6-base-devel
BuildRequires: qt6-tools

Requires: qt6-imageformats

%description
qView is an image viewer designed with minimalism and usability in mind.

%prep
%setup
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.h' -print0 |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
export PREFIX=/usr
qmake-qt6
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot
# NB: it's not %%_licensedir
rm -rf %buildroot%_datadir/licenses/%name

%files
%_bindir/%name
%_desktopdir/com.interversehq.qView.desktop
%_datadir/metainfo/com.interversehq.qView.appdata.xml
%_iconsdir/hicolor/*x*/apps/com.interversehq.qView.png
%_iconsdir/hicolor/scalable/apps/com.interversehq.qView.svg
%_iconsdir/hicolor/symbolic/apps/com.interversehq.qView-symbolic.svg
%doc LICENSE

%changelog
* Sun Aug 10 2025 Alexander Makeenkov <amakeenk@altlinux.org> 7.1-alt1
- Updated to version 7.1.

* Tue Jul 15 2025 Alexander Makeenkov <amakeenk@altlinux.org> 7.0-alt2
- Added qt6-imageformats to requires.

* Mon Jun 30 2025 Alexander Makeenkov <amakeenk@altlinux.org> 7.0-alt1
- Updated to version 7.0.
- Built with Qt6.

* Mon Aug 21 2023 Alexander Makeenkov <amakeenk@altlinux.org> 6.1-alt1
- Updated to version 6.1.

* Fri Aug 11 2023 Alexander Makeenkov <amakeenk@altlinux.org> 6.0-alt1
- Updated to version 6.0.

* Sun Jan 23 2022 Alexander Makeenkov <amakeenk@altlinux.org> 5.0-alt1
- Updated to version 5.0

* Wed Jan 06 2021 Alexander Makeenkov <amakeenk@altlinux.org> 4.0-alt1
- Updated to version 4.0

* Thu Jan 23 2020 Alexander Makeenkov <amakeenk@altlinux.org> 3.0-alt1
- New version

* Thu Jun 20 2019 Michael Shigorin <mike@altlinux.org> 2.0-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24
- minor spec cleanup

* Mon May 27 2019 Alexander Makeenkov <amakeenk@altlinux.org> 2.0-alt1
- Initial build for ALT
