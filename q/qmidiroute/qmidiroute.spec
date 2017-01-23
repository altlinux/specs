Name: qmidiroute
Version: 0.4.0
Release: alt1
Summary: MIDI event router and filter
License: GPL2
Group: Sound
Url: http://alsamodular.sourceforge.net/

Source: https://sourceforge.net/projects/alsamodular/files/QMidiRoute/%version/%name-%version.tar.bz2

# Automatically added by buildreq on Fri Jan 20 2017
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libstdc++-devel pkg-config python-base
BuildRequires: gcc-c++ libalsa-devel libqt4-devel

%description
QMidiRoute is a MIDI event router and filter. MIDI note, control change,
program change and pitch bend events are logged, and can be filtered,
redirected and transformed into other events according to MIDI maps
defined as tabs in the main control surface.
To start, click the 'Add MIDI map' button. You can copy midi MAPS into new
tabs using the 'Clone MIDI map' button. All MIDI maps can be saved in
a .qma text file.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man1dir/*
%_mandir/*/man1/%name.1.xz
%_datadir/%name

%changelog
* Fri Jan 20 2017 Ildar Mulyukov <ildar@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

