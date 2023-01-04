Name: patchage
Version: 1.0.10
Release: alt1

Summary: A modular patch bay for JACK and LASH audio systems
License: GPL-2.0+
Group: Sound
Url: https://drobilla.net/software/patchage

Source0: %name-%version.tar

BuildRequires(pre): meson ninja-build
BuildRequires: doxygen graphviz libganv-devel
BuildRequires: gcc-c++ libflowcanvas-devel boost-devel
BuildRequires: libglademm-devel libalsa-devel libjack-devel
BuildRequires: desktop-file-utils libdbus-devel libdbus-glib-devel

%description
Patchage is a modular patch bay for audio and MIDI systems based on
Jack, Lash, and Alsa.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Midi \
	%buildroot%_desktopdir/patchage.desktop

%files -f %name.lang
%doc AUTHORS NEWS README.md
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/%name/*
%_man1dir/%name.1*

%changelog
* Wed Jan 04 2023 Andrey Cherepanov <cas@altlinux.org> 1.0.10-alt1
- New version.

* Fri May 27 2022 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- New version.

* Fri Jan 08 2021 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version.

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New version.

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Thu Aug 07 2014 Michael Shigorin <mike@altlinux.org> 0.4.2-alt3.qa2
- NMU: rebuilt against current libflowcanvam

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.2-alt3.qa1
- NMU: rebuilt for updated dependencies.

* Wed Nov 23 2011 Lenar Shakirov <snejok@altlinux.ru> 0.4.2-alt3
- Build with libjack fixed (ALT #26592)

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.2-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for patchage

* Mon Aug 03 2009 Timur Batyrshin <erthad@altlinux.org> 0.4.2-alt2
- RPM package group fixed

* Mon Aug 03 2009 Timur Batyrshin <erthad@altlinux.org> 0.4.2-alt1
- Initial build for sisyphus

