Name: surguch
Version: 0.4.1
Release: alt1
License: GPL-3.0-or-later

Summary: Verification and creation of digitally signed pdf documents.

Source:  %name-%version.tar

Group: Office

BuildRequires: gcc-c++ cmake ninja-build
BuildRequires: libaltcsp-devel libcsppdf-devel >= 0.4.0-alt1
BuildRequires: libmupdf-devel
BuildRequires:  qt6-base-devel qt6-declarative-devel rpm-macros-qt6 qt6-declarative qt6-svg-devel qt6-svg qt6-tools

Requires: qt6-svg qt6-declarative fonts-ttf-google-noto-sans qt6-wayland qt6-translations
Requires: libcsppdf >= 0.4.0-alt1

%description
A gui application for verification and creation of digitally signed pdf documents.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -G Ninja
%cmake_build

%install
%cmake_install

%files
%_bindir/surguch
%_datadir/applications/surguch.desktop
%_datadir/icons/hicolor/scalable/apps/SealWax-1_32.svg
%_datadir/pixmaps/SealWax-1_32.png


%changelog
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

