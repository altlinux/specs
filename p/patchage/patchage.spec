Name: patchage
Version: 0.4.2
Release: alt3

Summary: A modular patch bay for JACK and LASH audio systems
License: %gpl2plus
Group: Sound
Url: http://www.altlinux.org/SampleSpecs/program

Packager: Timur Batyrshin <erthad@altlinux.org>
Source0: %name-%version.tar.bz2

BuildPreReq: rpm-build-licenses
BuildRequires: gcc-c++ libraul-devel libflowcanvas-devel boost-devel libglademm-devel libalsa-devel libjack-devel
BuildRequires: desktop-file-utils

%description
Patchage is a modular patch bay for audio and MIDI systems based on Jack, Lash,
and Alsa.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Midi \
	%buildroot%_desktopdir/patchage.desktop

%files -f %name.lang
%doc AUTHORS ChangeLog README 
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

