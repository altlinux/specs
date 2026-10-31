Name: keepassxc
Version:  2.8.0
Release:  alt1

Summary: KeePassXC Password Safe - light-weight cross-platform password manager
License: GPLv2+
Group: File tools

Url: http://www.keepassxc.org/
#Source: https://github.com/keepassxreboot/keepassxc/releases/download/%version/%name-%version-src.tar.xz
Source: %name-%version.tar
# to update the translation (may require creating an account on transifex and joining the project):
# - either go to https://www.transifex.com/keepassxc/keepassxc/language/ru/ and "download for use", category "master"
# - or use transifex client `tx pull` accordingly
Source1: keepassxc_ru.ts

Patch1: alt-add-chromium-gost-support-for-browser-integrations.patch

# requires asciidoctor
%def_enable docs
%def_without asan

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ctest gcc-c++
%if_with asan
BuildRequires: liblsan-devel-static
%endif
BuildRequires: qt6-base-devel >= 6.2.4 qt6-svg-devel qt6-tools-devel
BuildRequires: libbotan-devel >= 3.11.1
BuildRequires: zlib-devel >= 1.2.0
BuildRequires: libreadline-devel
BuildRequires: libminizip-devel
BuildRequires: libusb-devel
BuildRequires: libpcsclite-devel
BuildRequires: libkeyutils-devel
BuildRequires: libXi-devel, libXtst-devel
BuildRequires: libqrencode4-devel
%if_enabled docs
BuildRequires: asciidoctor
%endif

%description
KeePassXC is a community fork of KeePassX, a native cross-platform port of
KeePass Password Safe, with the goal to extend and improve it with new features
and bugfixes to provide a feature-rich, fully cross-platform and modern
open-source password manager.

%prep
%setup
%patch1 -p1
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif
# install fresh translation
cp -v %SOURCE1 share/translations/keepassxc_ru.ts

%build
# LTO is not supported yet, see https://github.com/keepassxreboot/keepassxc/issues/5801
#%define optflags_lto %{nil}

%cmake \
  -DWITH_TESTS=ON \
%if_with asan
  -DWITH_ASAN=ON \
%endif
  -DWITH_APP_BUNDLE=OFF \
  -DWITH_BUILD_X11=ON \
  -DWITH_BUILD_QT=OFF \
  -DKPXC_FEATURE_BROWSER=ON \
  -DKPXC_FEATURE_SSHAGENT=ON \
  -DKPXC_FEATURE_FDOSECRETS=ON \
  -DKPXC_FEATURE_NETWORK=ON \
  -DKPXC_FEATURE_UPDATES=OFF \
%if_enabled docs
  -DKPXC_FEATURE_DOCS=ON \
%else
  -DKPXC_FEATURE_DOCS=OFF \
%endif

%cmake_build

%check
export LANG=en_US.UTF-8; \
  %ctest --exclude-regex "testcli"

%install
%cmake_install

%files
%_bindir/*
%_datadir/%name
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/*/*/*
%_desktopdir/org.%name.KeePassXC.desktop
%_datadir/polkit-1/actions/org.%name.KeePassXC.policy
%_datadir/metainfo/org.%name.KeePassXC.appdata.xml
%if_enabled docs
%_mandir/man?/*
%endif

%changelog
* Sat Oct 31 2026 Pavel Nakonechnyi <zorg@altlinux.org> 2.8.0-alt1
- updated to v2.8.0

* Sat Mar 28 2026 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.12-alt1
- updated to v2.7.12

* Sat Dec 06 2025 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.11-alt1
- updated to v2.7.11
- update Russian translation to its current state (as of 24.11.2025)

* Tue Aug 12 2025 Alexander Danilov <admsasha@altlinux.org> 2.7.10-alt3
- fix russian translation.

* Mon Jun 16 2025 Nikolai Kostrigin <nickel@altlinux.org> 2.7.10-alt2
- NMU: fix optional build with yubikey support and switch it on (closes: #54817)
- change ykpers-devel to libykpers-1-devel build dependency
- add libpcsclite-devel and libusb-devel to build dependencies

* Sat Mar 08 2025 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.10-alt1
- updated to v2.7.9
- update Russian translation to its current state (as of 02.03.2025)
- enable passkeys without tests (may need botan3)

* Sat Mar 01 2025 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.9-alt3
- update Russian translation to its current state (as of 24.02.2025)
  closes: #52823

* Sat Nov 23 2024 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.9-alt2
- add Chromium-Gost support for browser integration (closes: #52159)

* Sat Jul 13 2024 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.9-alt1
- updated to v2.7.9

* Thu May 09 2024 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.8-alt1
- updated to v2.7.8

* Sat Mar 16 2024 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.7-alt1
- updated to v2.7.7

* Sun Aug 20 2023 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.6-alt1
- updated to v2.7.6

* Sun May 21 2023 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.5-alt1
- updated to v2.7.5

* Sun Oct 30 2022 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.4-alt1
- updated to v2.7.4

* Mon Oct 24 2022 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.3-alt1
- updated to v2.7.3

* Sun Apr 10 2022 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.1-alt1
- updated to v2.7.1

* Thu Mar 24 2022 Pavel Nakonechnyi <zorg@altlinux.org> 2.7.0-alt1
- updated to v2.7.0
- updated Russian translation from https://www.transifex.com/keepassxc/keepassxc/language/ru/
- added libbotan-devel build dependency, quazip-qt5-devel removed
- added libreadline-devel and libminizip-devel build dependencies

- tests were enabled
- minor cleanup of cmake build flags

* Thu Nov 11 2021 Sergey V Turchin <zerg@altlinux.org> 2.6.6-alt4
- update build requires

* Sat Aug 28 2021 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.6-alt3
- LTO explicitly disabled as it is not supported yet
- disable building tests: we don't run them anyway

* Mon Jul 19 2021 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.6-alt2
- Updated Russian translation from https://www.transifex.com/keepassxc/keepassxc/language/ru/
  last updated: May 30th 2021, fixes #40503

* Mon Jun 14 2021 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.6-alt1
- Updated to v2.6.6.

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 2.6.4-alt1.1
- NMU: spec: adapted to new cmake macros.

* Mon Feb 01 2021 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.4-alt1
- Updated to v2.6.4.

* Sun Jan 17 2021 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.3-alt1
- Updated to v2.6.3.

* Thu Oct 22 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.2-alt1
- Updated to v2.6.2.

* Thu Aug 20 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.1-alt1
- Updated to v2.6.1.

* Tue Jul 07 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.6.0-alt1
- Updated to v2.6.0.
- add asciidoctor as a build requirement to build documentation

* Fri Apr 10 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.5.4-alt1
- Updated to v2.5.4.

* Sun Feb 09 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.5.3-alt1
- Updated to v2.5.3.

* Mon Jan 13 2020 Pavel Nakonechnyi <zorg@altlinux.org> 2.5.2-alt1
- Updated to v2.5.2.

* Tue Nov 12 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.5.1-alt1
- Updated to v2.5.1.

* Sat Oct 27 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.5.0-alt1
- Updated to v2.5.0.
- enable support for Freedesktop.org secret storage DBus protocol

* Wed Jun 12 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.4.3-alt1
- Updated to v2.4.3.

* Mon Jun 03 2019 Michael Shigorin <mike@altlinux.org> 2.4.2-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24
- minor spec cleanup

* Sat Jun 01 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.4.2-alt1
- Updated to v2.4.2.

* Sun Apr 14 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.4.1-alt1
- Updated to v2.4.1.
- Check for updates disabled.

* Wed Mar 20 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.4.0-alt1
- Updated to v2.4.0.
- KeeShare support enabled
- new dependencies: libqrencode, qt5svg, libquazip-qt5

* Thu Aug 23 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.3.4-alt1
- Updated to v2.3.4.

* Sat Jun 16 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.3.3-alt1
- Updated to v2.3.3.

* Mon Oct 23 2017 Pavel Vyazovoy <paulelms@altlinux.org> 2.2.2-alt1
- Updated to v2.2.2.

* Sun Oct 15 2017 Pavel Vyazovoy <paulelms@altlinux.org> 2.2.1-alt1
- Initial build v2.2.1.
