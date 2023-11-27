
%define _unpackaged_files_terminate_build 1

Name:     geonkick
Version:  3.0.0
Release:  alt1

Summary:  A free software percussion synthesizer
License:  GPL-3.0
Group:    Sound
Url:      https://geonkick.org/
# Vcs:    https://github.com/Geonkick-Synthesizer/geonkick.git

Source:   %name-%version.tar
Patch1:   geonkick-alt-linking-fixes.patch
Patch2:   geonkick-alt-fix-build-with-unsigned-char.patch

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(RapidJSON)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(libssl)

Requires: %name-common

%description
Geonkick is a synthesizer that can synthesize elements of percussion.
The most basic examples are: kicks, snares, hit-hats, shakers, claps.

This package contains a standalone (jack) version on Geonkick.

%package  common
Group:    Sound
Summary:  Common files for Geonkick -- A free software percussion synthesizer

%description common
Geonkick is a synthesizer that can synthesize elements of percussion.
The most basic examples are: kicks, snares, hit-hats, shakers, claps.

This package contains common files that are used by all builds
of Geonkick.

%package -n lv2-geonkick-plugins
Group:    Sound
Summary:  A free software percussion synthesizer -- lv2
Requires: %name-common

%description -n lv2-geonkick-plugins
Geonkick is a synthesizer that can synthesize elements of percussion.
The most basic examples are: kicks, snares, hit-hats, shakers, claps.

This package contains Geonkick build as LV2 plugins.

%prep
%setup
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_man1dir/%name.*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/mime/*

%files common
%_datadir/%name

%files -n lv2-geonkick-plugins
%_libdir/lv2/*.lv2


%changelog
* Sun Nov 26 2023 Ivan A. Melnikov <iv@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sun Oct 29 2023 Ivan A. Melnikov <iv@altlinux.org> 2.10.2-alt1
- switch to new upstream
- 2.10.2

* Fri Sep 08 2023 Ivan A. Melnikov <iv@altlinux.org> 2.10.0-alt1
- 2.10.0

* Thu Sep 07 2023 Ivan A. Melnikov <iv@altlinux.org> 2.9.2-alt2
- Fix build with pipwire-provided Jack.

* Sun Aug 20 2023 Ivan A. Melnikov <iv@altlinux.org> 2.9.2-alt1
- 2.9.2

* Thu Aug 04 2022 Ivan A. Melnikov <iv@altlinux.org> 2.9.1-alt1
- Initial build for Sisyphus
