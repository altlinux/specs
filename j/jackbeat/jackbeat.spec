Name: jackbeat
Version: 0.7.6
Release: alt1.1
Summary: Jackbeat is an audio sequencer
License: GPLv2+
Group: Sound
Url: http://jackbeat.samalyse.org/
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar
Patch0: jackbeat-0.7.6-alt-DSO.patch

BuildRequires: libalsa-devel libgtk+2-devel libjack-devel liblo-devel
BuildRequires: libportaudio2-devel libpulseaudio-devel libsamplerate-devel
BuildRequires: libsndfile-devel libxml2-devel

%description
Jackbeat is an audio sequencer running on Linux and Mac OS X, for musicians 
and sound artists:

* Drummachine interface with animations for easy and playful editing
* Built for both composition and live setups with high interactivity needs
* Extremely easy to use but yet powerful by connecting with other 
  applications and plugins using JACK and OSC
* Loads and saves .jab files, Jackbeat's xml+tar open file format
* Supports native audio devices, PulseAudio and JACK

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

rm -rf -- %buildroot%_datadir/%name/help

mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48,scalable}/apps
for size in 16x16 32x32 48x48
do
    install -p -m 644 -T pkgdata/icons/%name-$size.png \
        %buildroot%_iconsdir/hicolor/$size/apps/%name.png
done
install -p -m 644 pkgdata/icons/%name.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Jackbeat
Version=%version
GenericName=Jackbeat
Comment=Jackbeat is an audio sequencer
Exec=%_bindir/%name
Icon=%name
Categories=Audio;Midi;Sequencer;X-Alsa;X-Jack;Gtk;
Terminal=false
Type=Application
EOF

%files
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/16x16/apps/%name.png
%_iconsdir/hicolor/32x32/apps/%name.png
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1.1
- Fixed build

* Mon May 30 2011 Egor Glukhov <kaman@altlinux.org> 0.7.6-alt1
- 0.7.6

* Sun Aug 08 2010 Egor Glukhov <kaman@altlinux.org> 0.7.5-alt1
- Initial build for Sisyphus
