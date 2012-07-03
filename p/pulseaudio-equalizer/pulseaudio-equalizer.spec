Name: pulseaudio-equalizer
Version: 2.7
Release: alt1
Summary: A 15 Bands Equalizer for PulseAudio
Group: Sound
License: GPLv3+
URL: https://code.launchpad.net/~psyke83/+junk/%name

Requires: ladspa-swh-plugins

Source0: %name-%version.tar.bz2
Source1: %name.1
Source2: %name-gtk.1
Patch0: %name-%version-force-default-persistence-value.patch
Patch1: %name-%version-remove-preamp.patch
Patch2: %name-%version-window-icon.patch
Patch3: %name-%version-do-not-crash-on-missing-preset.patch

BuildArch:      noarch

%description
PulseAudio Equalizer is a 15 bands system wide equalizer, that means
any application that is using PulseAudio, will benefit from the sound
improvement

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

%install
mkdir -p %buildroot%_prefix
cp -rf usr/* %buildroot/%_prefix/
install -Dpm 644 %SOURCE1 %buildroot%_man1dir/%name.1
install -Dpm 644 %SOURCE2 %buildroot%_man1dir/%name-gtk.1

%files
%_bindir/%name
%_bindir/%name-gtk
%_desktopdir/%name.desktop
%_datadir/%name
%_man1dir/*.1.*

%changelog
* Mon Jan 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.7-alt1
- initial release

