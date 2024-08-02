Name: alt-csp-cryptopro
Version: 0.3.0
Release: alt4

Group: File tools
Summary: CryptoPRO GUI tool
License: GPL-2.0-or-later

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: quazip-qt5-devel
BuildRequires: qt5-tools-devel

Provides: alt-csp-cryptopro-mate = %EVR
Obsoletes: alt-csp-cryptopro-mate < %EVR
Provides: alt-csp-cryptopro-kde = %EVR
Obsoletes: alt-csp-cryptopro-kde < %EVR

%description
CryptoPRO GUI tool

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %buildroot/%_qt5_translationdir/
install -m 0644 %_cmake__builddir/*.qm %buildroot/%_qt5_translationdir/
%find_lang --with-qt --all-name %name

%files -f %name.lang
%_bindir/alt-csp-cryptopro
%_desktopdir/alt-csp-cryptopro.desktop
%_K5srv/ServiceMenus/alt-csp-cryptopro.desktop
%_datadir/file-manager/actions/alt-csp-cryptopro.desktop

%changelog
* Fri Aug 02 2024 Oleg Solovyov <mcpain@altlinux.org> 0.3.0-alt4
- fix controls (Closes: #50922)

* Mon Jul 29 2024 Oleg Solovyov <mcpain@altlinux.org> 0.3.0-alt3
- fix regression (Closes: #50997)

* Fri Jul 19 2024 Oleg Solovyov <mcpain@altlinux.org> 0.3.0-alt2
- disable unsupported bulk operations
- enable checking signature for multiple files

* Thu Jun 20 2024 Oleg Solovyov <mcpain@altlinux.org> 0.3.0-alt1
- enable signing group of files

* Thu Nov 16 2023 Oleg Solovyov <mcpain@altlinux.org> 0.2.11-alt1
- add .p7s extension

* Wed Oct 18 2023 Oleg Solovyov <mcpain@altlinux.org> 0.2.10-alt1
- drop procps dependency

* Mon Jul 10 2023 Oleg Solovyov <mcpain@altlinux.org> 0.2.9-alt1
- change categories

* Fri Apr 21 2023 Oleg Solovyov <mcpain@altlinux.org> 0.2.8-alt1
- use current dir (Closes: #45162)
- use .sig as default (Closes: #45930)

* Thu Nov 24 2022 Oleg Solovyov <mcpain@altlinux.org> 0.2.7-alt1
- support aarch64

* Fri Sep 03 2021 Oleg Solovyov <mcpain@altlinux.org> 0.2.6-alt1
- minor fixes and improvements:
  + automatically select file and signature when archive is selected
  + fix: select signature after compressing
  + fix: don't insert ".0" into signature name if only one signature is requested
  + fix: after creating archive controls were disabled
  + UI: show error if containers are missing
  + fix: after creating archive no result given
  + UI: give user a clue that archive can be selected

* Wed Aug 18 2021 Oleg Solovyov <mcpain@altlinux.org> 0.2.5-alt1
- support newer version of cryptopro (Closes: #40749)

* Fri Jul 23 2021 Oleg Solovyov <mcpain@altlinux.org> 0.2.4-alt1
- sign using multiple certificates at once

* Wed Jul 21 2021 Oleg Solovyov <mcpain@altlinux.org> 0.2.3-alt1
- use QListView
- fix errors caused by implementing attached signatures creation
- fix behavior of View button
- don't alter environment in child processes

* Thu Jul 15 2021 Oleg Solovyov <mcpain@altlinux.org> 0.2.2-alt1
- fix build with Qt 5.12

* Thu Jul 15 2021 Oleg Solovyov <mcpain@altlinux.org> 0.2.1-alt1
- clean up code
- fix error code detection (Closes: #40493)
- allow creating attached signatures
- update translation

* Wed Jul 14 2021 Oleg Solovyov <mcpain@altlinux.org> 0.2.0-alt1
- refactor source code, simplify UI
- use QTableView for certificates
- show progress bar at long signing/verification operations
- remove dead/rarely used code

* Mon Jul 12 2021 Oleg Solovyov <mcpain@altlinux.org> 0.1.9-alt1
- use system alterator style
- fix ui

* Mon Jul 12 2021 Oleg Solovyov <mcpain@altlinux.org> 0.1.8-alt1
- fix null pointer dereference

* Fri Jul 09 2021 Oleg Solovyov <mcpain@altlinux.org> 0.1.7-alt1
- fix cleaning up result window right after completing task
- refactor source code
- update translation
- remove dead timestamp checking code

* Thu Jul 08 2021 Oleg Solovyov <mcpain@altlinux.org> 0.1.6-alt1
- new version

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.1.5-alt2
- NMU: spec: adapted to new cmake macros.

* Tue Apr 13 2021 Oleg Solovyov <mcpain@altlinux.org> 0.1.5-alt1
- fail if there are untrusted certs

* Tue Apr 13 2021 Oleg Solovyov <mcpain@altlinux.org> 0.1.4-alt1
- new version (Closes: #39547)

* Fri Apr 09 2021 Oleg Solovyov <mcpain@altlinux.org> 0.1.3-alt1
- quit without pop-ups in case of errors in headless mode

* Wed Apr 07 2021 Oleg Solovyov <mcpain@altlinux.org> 0.1.2-alt1
- implement headless signature verifying
- ignore cprocsp-rdr-gui-gtk-64 package (Closes: #39547)

* Mon Apr 05 2021 Oleg Solovyov <mcpain@altlinux.org> 0.1.1-alt1
- fix regression
- report no errors

* Sun Apr 04 2021 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- improve UI

* Sun Apr 04 2021 Oleg Solovyov <mcpain@altlinux.org> 0.0.6-alt1
- new version

* Mon Feb 01 2021 Oleg Solovyov <mcpain@altlinux.org> 0.0.5-alt1
- new version (Closes: 39484, 39547, 39548, 39557)

* Fri Jan 15 2021 Oleg Solovyov <mcpain@altlinux.org> 0.0.4-alt1
- new version

* Tue Jan 12 2021 Sergey V Turchin <zerg at altlinux dot org> 0.0.3-alt1
- rearrange UI

* Sat Dec 26 2020 Oleg Solovyov <mcpain@altlinux.org> 0.0.2-alt1
- new version

* Fri Dec 04 2020 Oleg Solovyov <mcpain@altlinux.org> 0.0.1-alt1
- Initial build

