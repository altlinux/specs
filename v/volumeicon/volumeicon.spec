Name: volumeicon
Version: 0.4.5
Release: alt1.1

Summary: Systray volume control
License: GPLv3
Group: Graphical desktop/Other
Url: http://softwarebakery.com/maato/volumeicon.html

Source: %name-%version.tar
Patch: %name-0.4.5-alt-glib2-2.32.3.patch

BuildRequires: libgtk+2-devel libalsa-devel

%description
Volume Icon aims to be a lightweight volume control that sits in your systray
(ALSA)

Features:
 * Change volume by scrolling on the systray icon
 * Ability to choose which channel to control
 * Several icon themes (with gtk theme as default)
 * Configurable external mixer
 * Volume Slider
 * Hotkey support

%prep
%setup
%patch -p2

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING NEWS README*
%_bindir/*
%_datadir/*

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.1
- Fixed build

* Tue Dec 27 2011 Timur Aitov <timonbl4@altlinux.org> 0.4.5-alt1
- New version (0.4.5)

* Thu Aug 11 2011 Timur Aitov <timonbl4@altlinux.org> 0.4.3-alt1
- New version (0.4.3)

* Tue Jan 11 2011 Timur Aitov <timonbl4@altlinux.org> 0.3.0-alt1
- New version

* Fri Oct 15 2010 Timur Aitov <timonbl4@altlinux.org> 0.2.1-alt1
- initial build for ALT

