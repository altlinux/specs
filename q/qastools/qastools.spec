# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qastools
Version: 1.4.0
Release: alt1

Summary: Collection of desktop applications for ALSA
License: MIT
Group: Sound

Url: https://gitlab.com/sebholt/qastools
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: qt6-base-devel qt6-svg-devel qt6-tools-devel
BuildRequires: pkgconfig(alsa)
# For libudev.h
BuildRequires: libudev-devel

Requires: qasconfig = %EVR
Requires: qashctl = %EVR
Requires: qasmixer = %EVR

%description
QasTools is a collection of desktop applications for the ALSA sound system.

%package -n qascommon
Summary: Common part of QasTools
Group: Sound
BuildArch: noarch

%description -n qascommon
Common part of QasTools.

%package -n qasconfig
Summary: ALSA configuration browser
Group: Sound
Requires: qascommon = %version-%release
Requires: icon-theme-hicolor
# https://bugzilla.altlinux.org/47318
Requires: qt6-svg

%description -n qasconfig
Browser for the ALSA configuration tree.

%package -n qashctl
Summary: ALSA complex mixer
Group: Sound
Requires: qascommon = %version-%release
Requires: icon-theme-hicolor
# https://bugzilla.altlinux.org/47318
Requires: qt6-svg

%description -n qashctl
Mixer for ALSA's more complex "High level Control Interface".

%package -n qasmixer
Summary: ALSA simple mixer
Group: Sound
Requires: qascommon = %version-%release
Requires: icon-theme-hicolor
# https://bugzilla.altlinux.org/47318
Requires: qt6-svg

%description -n qasmixer
Desktop mixer for ALSA's "Simple Mixer Interface" (alsamixer).

%prep
%setup
%patch -p1

%build
%cmake -DSKIP_LICENSE_INSTALL:BOOL=ON
%cmake_build

%install
%cmakeinstall_std
for file in %buildroot/%_desktopdir/*.desktop; do
    desktop-file-validate $file
done

%files
# meta package

%files -n qascommon
%doc COPYING CHANGELOG README.md TODO
%_datadir/%name

%files -n qasconfig
%_bindir/qasconfig
%_desktopdir/qasconfig.desktop
%_iconsdir/hicolor/*/apps/qasconfig.*
%_man1dir/qasconfig.1.*
%_datadir/metainfo/qasconfig.appdata.xml

%files -n qashctl
%_bindir/qashctl
%_desktopdir/qashctl.desktop
%_iconsdir/hicolor/*/apps/qashctl.*
%_man1dir/qashctl.1.*
%_datadir/metainfo/qashctl.appdata.xml

%files -n qasmixer
%_bindir/qasmixer
%_desktopdir/qasmixer.desktop
%_iconsdir/hicolor/*/apps/qasmixer.*
%_man1dir/qasmixer.1.*
%_datadir/metainfo/qasmixer.appdata.xml

%changelog
* Thu Feb 15 2024 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- nev version 1.4.0

* Sat Feb 10 2024 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- nev version 1.3.0
- fix License
- update URL

* Mon Dec 18 2023 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Tue Dec 12 2023 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Wed Dec 06 2023 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt2
- Requires: qt6-svg for qasconfig, qashctl, qasmixer

* Tue Dec 05 2023 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- New version 1.0.0
- build with qt6
- Requires: qt6-svg

* Fri Aug 07 2020 Anton Midyukov <antohami@altlinux.org> 0.23.0-alt1
- new version 0.23.0

* Tue Nov 19 2019 Anton Midyukov <antohami@altlinux.org> 0.22.0-alt1
- new version 0.22.0

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.21.0-alt5
- NMU: remove rpm-build-ubt from BR:

* Fri May 31 2019 Michael Shigorin <mike@altlinux.org> 0.21.0-alt4
- Dropped %%ubt
- Minor spec cleanup

* Sat Jun 16 2018 Anton Midyukov <antohami@altlinux.org> 0.21.0-alt3%ubt
- Rebuilt for aarch64

* Sun Jan 14 2018 Anton Midyukov <antohami@altlinux.org> 0.21.0-alt2%ubt
- Disabled tray icon at startup

* Thu Dec 21 2017 Anton Midyukov <antohami@altlinux.org> 0.21.0-alt1%ubt
- Initial build for ALT Sisyphus.
