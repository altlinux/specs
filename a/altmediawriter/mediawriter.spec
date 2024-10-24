%define sname mediawriter
%define oname ALTMediaWriter

Name:           altmediawriter
Version:        1.0.5
Release:        alt2.1
Summary:        ALT Media Writer
Group:          System/Configuration/Other
Packager:       Maria Alexeeva <alxvmr@altlinux.org>

License:        GPLv2+
URL:            https://github.com/altlinux/ALTMediaWriter
Source:         %oname-%version.tar

BuildRequires:  liblzma-devel
BuildRequires:  libyaml-cpp-devel
BuildRequires:  qt5-declarative-devel
BuildRequires:  qt5-x11extras-devel
BuildRequires:  libappstream-glib

Requires:       qt5-quickcontrols
Requires:       qt5-quickcontrols2
Requires:       polkit
Requires:       udisks2

%description
A tool to write images of ALT media to portable drives
like flash drives or memory cards.

%prep
%setup -n %oname-%version

%build
%qmake_qt5 PREFIX=%_prefix LIBEXECDIR=%_libexecdir/%name MEDIAWRITER_NAME=%name MEDIAWRITER_VERSION=%version-%release
%make_build

%install
make install INSTALL_ROOT=%buildroot
if [ "%name" != "%sname" ]; then
    for i in %buildroot%_datadir/icons/hicolor/*/apps/%sname.png; do
        mv "$i" "$(dirname $i)/%name.png"
    done
    mv %buildroot%_datadir/applications/%sname.desktop %buildroot%_datadir/applications/%name.desktop
    mv %buildroot%_datadir/appdata/%sname.appdata.xml %buildroot%_datadir/appdata/%name.appdata.xml
    sed -i 's/=%sname$/=%name/g' %buildroot%_datadir/applications/%name.desktop
    sed -i 's/%sname\.desktop/%name.desktop/' %buildroot%_datadir/appdata/%name.appdata.xml
fi

%check
appstream-util validate-relax --nonet %buildroot/%_datadir/appdata/%name.appdata.xml

%files
%_bindir/%name
%_libexecdir/%name/
%_datadir/appdata/%name.appdata.xml
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png


%changelog
* Fri Oct 25 2024 Ivan A. Melnikov <iv@altlinux.org> 1.0.5-alt2.1
- NMU: Trimmed build dependencies (thx asheplyakov@).

* Mon Sep 23 2024 Maria Alexeeva <alxvmr@altlinux.org> 1.0.5-alt2
- Fix corruption of the last connected drive (thx a-shavlidze@mail.ru).
- Fix progress bar display.
- Fix disk formatting.
- Fixes #44462, #49205, #47202

* Tue Jun 14 2022 Dmitry Degtyarev <kevl@altlinux.org> 1.0.5-alt1
- Misc: Fix compatibility with ALT Linux P9.

* Wed Jun 01 2022 Dmitry Degtyarev <kevl@altlinux.org> 1.0.4-alt1
- Download dialog: Fix visual problems where text elements
  would sometimes overlap each other.
- Misc: Use software rendering on Windows. Fixes app
  sometimes failing to launch due to hardware rendering.
- Misc: Fix non-English languages in Windows installer.
- Misc: Fix window icon.

* Fri Apr 22 2022 Dmitry Degtyarev <kevl@altlinux.org> 1.0.3-alt1
- Restore dialog: Fixed untranslated text on first page.

* Thu Apr 21 2022 Dmitry Degtyarev <kevl@altlinux.org> 1.0.2-alt1
- Writing: Restored previously removed "MD5 check after
  writing" feature. This feature was originally removed
  in version 0.6.0.
- Writing: Added warnings for cases where "MD5 check
  after writing" is not possible.
- Restore dialog: Fixed a visual bug where if the app was
  launched in Russian, text didn't word wrap correctly
  and leaked into other dialog pages.
- Misc: Fixed a visual bug where notification bar for
  restoration was not sized properly for contents on
  some languages/systems.
- Image details: Fixed links in image description text
  not opening in browser.

* Wed Apr 13 2022 Dmitry Degtyarev <kevl@altlinux.org> 1.0.1-alt1
- 1.0.1 (See CHANGELOG.txt for details)

* Tue Apr 12 2022 Dmitry Degtyarev <kevl@altlinux.org> 1.0.0-alt1
- 1.0.0 (See CHANGELOG.txt for details)

* Mon Jan 10 2022 Dmitry Degtyarev <kevl@altlinux.org> 0.6.5-alt1
- 0.6.5 (See CHANGELOG.txt for details)

* Tue May 11 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.6.4-alt1
- 0.6.4 (closes: 40021)

* Thu Apr 22 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.6.3-alt1
- 0.6.3 (closes: 39932)

* Mon Apr 12 2021 Dmitry Degtyarev <kevl@altlinux.org> 0.6.2-alt1
- 0.6.2

* Thu Nov 05 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.6.1-alt1
- Fix arch and file type translations
- Fix missing header on some Qt versions
- Fix custom image not loading on windows

* Thu Nov 05 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.6.0-alt1
- Implement LIVE variants
- Fix download bugs
- Remove user agent from network requests
- Attempt to recover from connection errors instead of failing
- Don't do MD5 check after writing
- Don't force software renderer
- Remove built-in metadata
  + While metadata is downloading only show Custom release
- Update license

* Tue Oct 20 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.5.0-alt1
- Remove artifacts from all yml strings
- Remove blank rectangle that obscured top of images list
- Put workstation and server releases on the front page
- Reduce row heights and max line counts

* Wed Oct 07 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.8-alt1
- Improve image summary display
- Improve windows build
- Build windows version statically

* Thu Oct 01 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.7-alt1
- Added more filters to file dialog (closes: 39017)
- Add missing image types
- Show image type name instead of description in image details

* Wed Sep 16 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.6-alt1
- Added p9-kworkstation release (closes: 38804).
- Fixed "Delete downloaded image?" button showing for local
  images (closes: 38803).
- Improved asset update process
  + Only need to edit app.qrc now.
  + Match assets dir structure with getalt's.
  + Add assets/UPDATING.md with instructions.
- Fixed "Board is unknown" messages.

* Fri May 22 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.5-alt1
- Fixed searching releases in Russian (closes: 38478)

* Fri May 01 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.4-alt1
- Added qt5-quickcontrols requirement (closes: 38072)
- Updated BuildRequires according to gear-buildreq output
- Changed make to %make_build

* Wed Apr 15 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.3-alt1
- Added missing SSL dll's to windows build

* Wed Apr 15 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.2-alt1
- Removed build instructions from README
- Fixed Unknown architecture text going outside button

* Wed Apr 15 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.1-alt1
- Fixed incorrect encoding of Russian text on Windows
- Improved Windows build.sh so that latest version is displayed
- Fixed MD5 check failing on large files on some 32bit platforms

* Wed Apr 08 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.4.0-alt1
- Changed metadata and image assets to yaml files from getalt.org
- Turned off md5 check for compressed images
- Added Simply variant
- Added Live releases to some variants

* Tue Mar 10 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.3.0-alt1
- Added generate_releases.sh
- Cleaned up releasesmanager.h by removing unused and unneded fields/logic
- Maked local json loading more obvious
- Added Simply variant
- Increased frontpage row height for Russian text that can span 4 lines
- Added info about rootfs'able image types
- Added a check of whether an image type is supported

* Fri Feb 28 2020 Dmitry Degtyarev <kevl@altlinux.org> 0.2.0-alt1
- Fixed Russian translation
- Added translation source files
- Added automatic metadata generation from getalt.org sources
- Improved win builds
- Changed win build to create 32bit executable
- Removed unneeded Raspberry Pi board drop-down menu

* Tue Nov 05 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
