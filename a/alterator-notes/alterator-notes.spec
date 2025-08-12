%define _unpackaged_files_terminate_build 1
%def_with noarch

Name: alterator-notes
Version: 1.6.0
Release: alt1

Summary: alterator module for view license and release notes
License: GPL-2.0+
Group: System/Configuration/Other

%if_with noarch
BuildArch: noarch
%endif

Provides: alterator-license = %version
Obsoletes: alterator-license
Requires: alterator-notes-base

Source:%name-%version.tar

BuildPreReq: alterator >= 3.1
BuildRequires: alterator
BuildRequires(pre): rpm-macros-alterator
BuildRequires: desktop-file-utils

%description
alterator module for view license and release notes.

%package base
Group: System/Configuration/Other
Summary: alterator module for view license and release notes
Requires: alterator >= 3.1-alt4, alterator-sh-functions
Requires: distro-licenses
Requires: alterator-notes-utils
Conflicts: alterator-browser-qt < 2.9.70
Conflicts: alterator-lookout    < 0.3
Conflicts: alterator-notes < 1.5.1-alt7
%description base
alterator module for view license and release notes.

%prep
%setup -q

%build
%make_build

%install
%makeinstall
%if_with noarch
rm -rf %buildroot%_alterator_libdir/ui/notes/*.go
%endif

mkdir -p %buildroot/%_bindir
install alterator-notes-show %buildroot/%_bindir/
mkdir -p %buildroot/%_desktopdir
#for n in license release-notes ; do
for n in license ; do
    install -m 0644 \
	%buildroot/%_datadir/alterator/applications/$n.desktop \
	%buildroot/%_desktopdir/%name-$n.desktop
    desktop-file-install --mode=0644 --dir %buildroot/%_desktopdir \
	--add-category=System \
	--add-category=Documentation \
	--set-icon=alt-distro-logo \
	--set-key=Exec \
	--set-value="alterator-notes-show $n" \
	--set-key=NotShowIn \
	--set-value="GNOME;" \
	%buildroot/%_desktopdir/%name-$n.desktop
done
mkdir -p %buildroot/%_datadir/kio_desktop/DesktopLinks/
install -m 0755 %buildroot/%_desktopdir/%name-license.desktop %buildroot/%_datadir/kio_desktop/DesktopLinks/

%files
%_bindir/alterator-notes-show
%_desktopdir/%name-*.desktop
%_datadir/kio_desktop/DesktopLinks/%name-*.desktop

%files base
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%if_without noarch
%_alterator_libdir/ui/notes/*.go
%endif
%_alterator_backend3dir/*

%changelog
* Sun Aug 10 2025 Kirill Sharov <sheriffkorov@altlinux.org> 1.6.0-alt1
- Add support for notes of edition
- Move search of notes to other common package

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt7
- move desktops to separate package

* Tue May 20 2025 Anton Midyukov <antohami@altlinux.org> 1.5.1-alt6
- license.desktop: correct Name (License -> License agreement) (Closes: 54379)

* Mon Apr 28 2025 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt5
- correct dekstop-file category

* Fri Apr 25 2025 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt4
- don't package release notes menu entry

* Fri Apr 25 2025 Semen Fomchenkov <armatik@altlinux.org> 1.5.1-alt3
- Not show license and release notes icons in GNOME apps menu

* Tue Apr 22 2025 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt2
- put license to KDE desktop

* Tue Apr 22 2025 Sergey V Turchin <zerg@altlinux.org> 1.5.1-alt1
- allow user to view license and release notes

* Fri Apr 18 2025 Evgeny Sinelnikov <sin@altlinux.org> 1.5-alt1
- final-notes: remove header with module name in ui

* Tue Apr 15 2025 Evgeny Sinelnikov <sin@altlinux.org> 1.4-alt1
- Add final-notes hidden module for installation process

* Mon Mar 17 2025 Evgeny Sinelnikov <sin@altlinux.org> 1.3-alt1
- Add support of license calculation from edition entry

* Fri Dec 13 2024 Evgeny Sinelnikov <sin@altlinux.org> 1.2-alt1
- add support license search in distro-licenses by /etc/os-release

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt9
- move translations to alterator-l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt8
- use help from new l10n

* Tue Dec 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt7
- update help (by azol@)

* Mon Sep 22 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt6
- rebuild with new alterator-l10n

* Tue Sep 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt5
- rebuild with new alterator-l10n

* Thu Jul 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt4
- remove translations from desktop file

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt3
- remove (document:insert "/std/functions") from qt ui

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt2
- backend: use alterator_api_version=1

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- remove po/*
- use module.mak

* Mon Jun 16 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt7
- fix desktop file (fix #15957)

* Thu May 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt6
- rebuild with new alterator-l10n

* Thu May 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt5
- use alterator-l10n

* Fri Mar 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt4
- << and >> quotes in po-file

* Fri Mar 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt3
- use "url" attribute of textarea
- if accesed from the next page then "agree" checked 

* Wed Mar 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt2
- add <head> section in help-files

* Fri Feb 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- rename from alterator-license 

* Tue Jan 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add help
- backend: add support for diffent licenses

* Wed Oct 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- fix again

* Fri Oct 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- fix translation

* Tue Sep 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- convert license to html format

* Thu Aug 16 2007 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- Initial release
