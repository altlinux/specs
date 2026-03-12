Name: surguch
Version: 0.4.6
Release: alt1
Summary: Verification and creation of digitally signed pdf documents

Source:  %name-%version.tar

License: GPL-3.0-or-later
Url: https://gitlab.basealt.space/proskurinov/surguch
VCS: https://gitlab.basealt.space/proskurinov/surguch.git


Group: Office

BuildRequires(pre): rpm-macros-qt6 
BuildRequires: gcc-c++ cmake ninja-build
BuildRequires: libaltcsp-devel libcsppdf-devel >= 0.4.0-alt1
BuildRequires: libmupdf-devel
BuildRequires: qt6-base-devel qt6-declarative-devel 
BuildRequires: qt6-declarative qt6-svg-devel qt6-svg qt6-tools

Requires: qt6-svg qt6-declarative fonts-ttf-google-noto-sans 
Requires: qt6-wayland qt6-translations
Requires: libcsppdf >= 0.4.0-alt1

Obsoletes: alt-csp-cryptopro

%description
A gui application for verification and creation 
of digitally signed pdf documents.

%package gnome-extension
Summary: Nautilus extension for surguch
Group: Other
Requires: surguch
Requires: nautilus-python

%description gnome-extension
An extension that allows you to add files for signing from file manager.

%package mate-extension
Summary: Mate file manager extension for surguch
Group: Other
Requires: surguch
Requires: mate-file-manager-actions

%description mate-extension
An extension that allows you to add files for signing from file manager.


%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DDESKTOP_DIR=%_desktopdir \
       -DAPP_ICON_DIR=%_iconsdir/hicolor/scalable/apps/ \
       -DAPP_ICON_PNG_DIR=%_pixmapsdir \
       -G Ninja
%cmake_build

%install
%cmake_install
%find_lang --with-gnome %name-gnome-extension

%files
%_bindir/surguch
%_desktopdir/surguch.desktop
%_iconsdir/hicolor/scalable/apps/SealWax-1_32.svg
%_pixmapsdir/SealWax-1_32.png
%_datadir/metainfo/surguch.metainfo.xml
%_datadir/kio/servicemenus/surguch.desktop
%_datadir/file-manager/actions/surguch.desktop

%files gnome-extension -f %name-gnome-extension.lang
%_datadir/nautilus-python/extensions/surguch-gnome-extension.py

%files mate-extension

%changelog
* Thu Mar 12 2026 Oleg Proskurin <proskur@altlinux.org> 0.4.6-alt1
- Minor fixes (closes #58139, #58129):
    * Custom error message dialog.
    * Handle filenames containing quote marks.
    * Animate the unchosen user certificate validation
      error when creating a profile.

* Mon Mar 02 2026 Daniil-Viktor Ratkin <krf10@altlinux.org> 0.4.5-alt2
- add subpackage with requires for mate file actions (closes #58061).

* Fri Feb 26 2026 Daniil-Viktor Ratkin <krf10@altlinux.org> 0.4.5-alt1
- add new launch options, add file manager actions.

* Tue Feb 10 2026 Daniil-Viktor Ratkin <krf10@altlinux.org> 0.4.4-alt1
- update icons.

* Tue Dec 30 2025 Oleg Proskurin <proskur@altlinux.org> 0.4.3-alt2
- Fix major mistakes in the .spec file (closes #57232).

* Fri Nov 14 2025 Oleg Proskurin <proskur@altlinux.org> 0.4.3-alt1
- Update application metadata (thanks to @sirius)

* Wed Nov 12 2025 Oleg Proskurin <proskur@altlinux.org> 0.4.2-alt1
- Minor fixes (Closes #56761, #56749):
  * Add meta info XML file.
  * Fix the error message typo.

* Wed Oct 29 2025 Daniil-Viktor Ratkin <krf10@altlinux.org> 0.4.1-alt1
- Fix scroll and save in PDF mode (Closes: #56649, #56655)

* Tue Oct 14 2025 Oleg Proskurin <proskur@altlinux.org> 0.4.0-alt1
- New features:
    + Add machine-readable power of attorney (MRPA) support.
    + Work with document packages.
    + Sign files in bulk with detached/attached signature.

* Thu Sep 04 2025 Oleg Proskurin <proskur@altlinux.org> 0.3.3-alt1
- Fix undefined Aim behaviour when launched without any default profile

* Thu Sep 04 2025 Oleg Proskurin <proskur@altlinux.org> 0.3.2-alt2
- Additional hotfixes for the GUI

* Fri Aug 29 2025 Oleg Proskurin <proskur@altlinux.org> 0.3.2-alt1
- New features:
  + Open URLs by ctrl+click.
Fixes (Closes: #54387, #54370, #55451):
  + SearchDialog and RubberStamp list positioning.
  + Aim-rectangle size for custom stamps.
  + The scroll bar that overlaps the buttons.
  + The flattening distortion of the rubber stamp preview.
  * The flattening distortion of the signature stamp.
  + The position of the rubber stamp preview image.
  + The position of the signature stamp preview image.
  + Tranlations update.
  + Multiple UI fixes for different desktop environments.

* Thu Jul 24 2025 Oleg Proskurin <proskur@altlinux.org> 0.3.1-alt1
- Fix saving file to itself.

* Fri Jun 27 2025 Oleg Proskurin <proskur@altlinux.org> 0.3-alt1
- New features (Closes:#53303):
  + Dark themes support
  + Text search
  + Custom signature stamps
  + Custom annotation stamps
  + Transparent stamps support

* Wed Feb 12 2025 Oleg Proskurin <proskur@altlinux.org> 0.2.2-alt1
- Fix zoom behavior (Closes: #52860, #52859)

* Tue Jan 28 2025 Oleg Proskurin <proskur@altlinux.org> 0.2.1-alt1
- Fix e2k build

* Mon Jan 20 2025 Oleg Proskurin <proskur@altlinux.org> 0.2-alt2
- Bugfixing:
  + Forbid signing of damaged documents
  + Translate the error messagebox title

* Thu Dec 26 2024 Oleg Proskurin <proskur@altlinux.org> 0.2-alt1
- zoom with mouse wheel

* Thu Dec 19 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt2
- License info was added

* Thu Nov 21 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build

