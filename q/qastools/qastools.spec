Name: qastools
Version: 0.21.0
Release: alt1%ubt
Summary: Collection of desktop applications for ALSA
License: GPLv3

Group: Sound
Url: http://xwmw.org/qastools
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-build-ubt
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: qt5-base-devel qt5-svg-devel qt5-tools-devel
#qt5-linguist
BuildRequires: pkgconfig(alsa)
# For libudev.h
BuildRequires: libudev-devel

Requires: qasconfig = %version-%release
Requires: qashctl = %version-%release
Requires: qasmixer = %version-%release

%description
QasTools is a collection of desktop applications for the ALSA sound system.

%package -n qascommon
Summary: Common part of QasTools
Group: Sound

%description -n qascommon
Common part of QasTools.

%package -n qasconfig
Summary: ALSA configuration browser
Group: Sound
Requires: qascommon = %version-%release
Requires: icon-theme-hicolor

%description -n qasconfig
Browser for the ALSA configuration tree.

%package -n qashctl
Summary: ALSA complex mixer
Group: Sound
Requires: qascommon = %version-%release
Requires: icon-theme-hicolor

%description -n qashctl
Mixer for ALSA's more complex "High level Control Interface".

%package -n qasmixer
Summary: ALSA simple mixer
Group: Sound
Requires: qascommon = %version-%release
Requires: icon-theme-hicolor

%description -n qasmixer
Desktop mixer for ALSA's "Simple Mixer Interface" (alsamixer).

%prep
%setup

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
%doc COPYING
%doc CHANGELOG README TODO
%_datadir/%name

%files -n qasconfig
%_bindir/qasconfig
%_desktopdir/qasconfig.desktop
%_iconsdir/hicolor/*/apps/qasconfig.*
%_man1dir/qasconfig.1.*

%files -n qashctl
%_bindir/qashctl
%_desktopdir/qashctl.desktop
%_iconsdir/hicolor/*/apps/qashctl.*
%_man1dir/qashctl.1.*

%files -n qasmixer
%_bindir/qasmixer
%_datadir/%name/icons/
%_desktopdir/qasmixer.desktop
%_iconsdir/hicolor/*/apps/qasmixer.*
%_man1dir/qasmixer.1.*

%changelog
* Thu Dec 21 2017 Anton Midyukov <antohami@altlinux.org> 0.21.0-alt1%ubt
- Initial build for ALT Sisyphus.
