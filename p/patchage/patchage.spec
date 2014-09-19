Name: patchage
Version: 1.0.0
Release: alt1

Summary: A modular patch bay for JACK and LASH audio systems
License: %gpl2plus
Group: Sound
Url: http://www.altlinux.org/SampleSpecs/program

Source0: %name-%version.tar.bz2

BuildPreReq: rpm-build-licenses doxygen graphviz libganv-devel
BuildRequires: gcc-c++ libraul-devel libflowcanvas-devel boost-devel
BuildRequires: libglademm-devel libalsa-devel libjack-devel
BuildRequires: desktop-file-utils libdbus-devel libdbus-glib-devel

%description
Patchage is a modular patch bay for audio and MIDI systems based on
Jack, Lash, and Alsa.

%prep
%setup

%build
./waf configure \
	--prefix=%prefix \
	--configdir=%_sysconfdir \
	--libdir=%_libdir \
	--docs \
	--lv2-user \
	--lv2-system \
	--debug
./waf build -j %__nprocs

%install
./waf install --destdir=%buildroot

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Midi \
	%buildroot%_desktopdir/patchage.desktop

%files -f %name.lang
%doc AUTHORS NEWS README 
%_bindir/*
%_desktopdir/*
%_liconsdir/*
%_niconsdir/*
%_miconsdir/*
%_iconsdir/hicolor/22x22/apps/*
%_iconsdir/hicolor/24x24/apps/*
%_iconsdir/hicolor/scalable/apps/*
%_datadir/%name/*

%changelog
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

