Name: krusader
Version: 2.9.0
Release: alt1

Summary: Advanced KDE twin-panel file-manager
License: GPLv3+
Group: File tools

Url: http://%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://download.kde.org/stable/%name/%version/%name-%version.tar.xz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires(pre): rpm-build-kf6

BuildRequires: extra-cmake-modules
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-kstatusnotifieritem-devel
BuildRequires: kf6-ktextwidgets-devel
BuildRequires: kf6-kwallet-devel
BuildRequires: libcups-devel
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-declarative-devel
BuildRequires: zlib-devel

Provides: kde5-%name = %EVR
Obsoletes: kde5-%name <= 2.8.0-alt1

%description
Krusader is an advanced twin panel (commander style) file manager
for KDE and other desktops in the *nix world, silar to Midnight
or Total Commander. It provides all the file management features
you could possibly want.

Plus: extensive archive handling, mounted filesystem support, FTP,
advanced search module, an internal viewer/editor, directory
synchronisation, file content comparisons, powerful batch renaming
and much much more. It supports a wide variety of archive formats
and can handle other KIO slaves such as smb or fish.

It is (almost) completely customizable, very user friendly,
fast and looks great on your desktop! You should give it a try.

This piece of software is developed by the Krusader Krew,
published under the GNU General Public Licence
(http://www.gnu.org/copyleft/gpl.html).

%prep
%setup

%build
%add_optflags -fpermissive
%K6build

%install
%K6install

%find_lang %name --with-kde

%files -f %name.lang
%doc README AUTHORS ChangeLog TODO INSTALL CREDITS
%_K6bin/%name
%_K6xdgapp/*.desktop
%_datadir/%name
%_K6xdgconf/kio_isorc
%_K6icon/*/*/apps/*.png
%_K6plug/kf6/kio/kio_*.so
%_K5xmlgui/%name
%_K6doc/*/%name
%_datadir/metainfo/org.kde.%name.appdata.xml

%changelog
* Sun Mar 23 2025 Nazarov Denis <nenderus@altlinux.org> 2.9.0-alt1
- Version 2.9.0:
  + Port to KDE Frameworks 6 (ALT #51852)

* Sat Sep 16 2023 Nazarov Denis <nenderus@altlinux.org> 2.8.0-alt1
- Version 2.8.0

* Mon Jan 24 2022 Nazarov Denis <nenderus@altlinux.org> 2.7.2-alt3
- update russian translation

* Fri Jan 21 2022 Nazarov Denis <nenderus@altlinux.org> 2.7.2-alt2
- restore translation

* Mon Dec 27 2021 Nazarov Denis <nenderus@altlinux.org> 2.7.2-alt1
- new 2.7.2 version (ALT #40495)

* Mon Apr 15 2019 Pavel Moseev <mars@altlinux.org> 2.7.1-alt3
- update translation

* Wed Jan 23 2019 Konstantin Artyushkin <akv@altlinux.org> 2.7.1-alt2
- new 2.7.1 version

* Tue Jun 19 2018 Konstantin Artyushkin <akv@altlinux.org> 2.7.0-alt2
- add some requires for non-kde5 environtments

* Mon May 14 2018 Konstantin Artyushkin <akv@altlinux.org> 2.7.0-alt1
- new version

* Thu Aug 31 2017 Konstantin Artyushkin <akv@altlinux.org> 2.6.0-alt1
- new version

* Wed Jan 25 2017 Konstantin Artyushkin <akv@altlinux.org> 2.5.0-alt1
- update version 

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt0.1.1
- Fixed build with gcc 4.7

* Wed Jan 18 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.4.0-alt0.1
- Update to 2.4.0-beta1 (ALT#26829)

* Mon Jun 27 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.3.0-alt0.2
- Update to 2.3.0-beta1

* Fri Feb 25 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.3.0-alt0.1
- Update to git a65a9653fdb230fa65a8b6bd230eb04a4b0f33ac
- move to standart place

* Tue Nov 09 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt2.svn20101108
- Update to svn 20101108

* Sat May 08 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt1.beta1
- Update to 2.2.0-beta1

* Mon Feb 08 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt2.beta1
- Update to svn 20100208 (ALT #22223)
- Not show hidden files by default (ALT #22496)

* Mon Nov 02 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 2.1.0-alt1.beta1
- Update to 2.1.0-beta1

* Fri Aug 28 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.0-alt4
- Picked up from orphaned
- Update to svn 20090828

* Sun Apr 12 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt3
- Krusader 2.0.0 "Mars Pathfinder" released!

* Sat Apr 11 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt2.svn6287.1
- new version - 2.0.0-svn6287
- temporary disabled russian docs (docs old ald not compileable)

* Wed Mar 11 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt2.svn6247.2
- delete CVSNEWS from spec

* Wed Mar 11 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt2.svn6247.1
- new version - 2.0.0-svn6247

* Tue Mar 10 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt1.svn6244.1
- new version - 2.0.0-svn6244

* Tue Jan 20 2009 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt0.beta2.1
- new version - 2.0.0-beta2

* Wed Nov 19 2008 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt0.beta1.2
- fix repocop errors - remove update-desktop-database, update_menus macroses

* Fri Oct 24 2008 Konstantin Baev <kipruss@altlinux.org> 2.0.0-alt0.beta1.1
- initial build for Sisyphus (KDE4)
