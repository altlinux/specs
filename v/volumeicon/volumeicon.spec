%define _unpackaged_files_terminate_build 1

Name: volumeicon
Version: 0.5.1
Release: alt1

Summary: Systray volume control
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/Maato/volumeicon

Source: %name-%version.tar

BuildRequires: libalsa-devel
BuildRequires: glib2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libnotify-devel
BuildRequires: intltool

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

%build
./autogen.sh
%configure --enable-notify
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING README
%_bindir/*
%_datadir/volumeicon
%_datadir/locale/*/*/volumeicon.mo

%changelog
* Tue Jun 07 2022 Egor Ignatov <egori@altlinux.org> 0.5.1-alt1
- new version 0.5.1
- remove volumeicon-0.4.5-alt-glib2-2.32.3 patch

* Fri Oct 12 2012 Alexander Plehanov <tonik@altlinux.org> 0.4.6-alt1
- New version (0.4.6)

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

