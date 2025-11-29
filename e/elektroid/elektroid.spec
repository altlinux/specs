%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_without check

Name: elektroid
Version: 3.2.3
Release: alt1

Summary: Sample and MIDI device manager
License: GPL-3.0
Group: Sound
Url: https://github.com/dagargo/elektroid

Source: %name-%version.tar

BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libzip)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(cunit)

%description
Elektroid is a sample and MIDI device manager.

With Elektroid you can easily upload and download audio files and manage
different types of data on different MIDI devices, such as presets,
projects or tunings.

It can also be used to send and receive SysEx MIDI files.

This package provides both the GUI and CLI application of Elektroid.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%check
%make_build check

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README README.md THANKS
%_bindir/elektroid
%_bindir/elektroid-cli
%_desktopdir/io.github.dagargo.Elektroid.desktop
%exclude %_datadir/elektroid/THANKS
%dir %_datadir/elektroid
%dir %_datadir/elektroid/elektron
%_datadir/elektroid/elektron/devices.json
%_datadir/elektroid/gui.css
%_datadir/elektroid/gui.glade
%dir %_datadir/elektroid/microbrute
%_datadir/elektroid/microbrute/gui.glade
%_iconsdir/hicolor/scalable/apps/*.svg
%_man1dir/elektroid-cli.1.*
%_man1dir/elektroid.1.*
%_datadir/metainfo/io.github.dagargo.Elektroid.appdata.xml

%changelog
* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 3.2.3-alt1
- Initial build for Sisyphus
