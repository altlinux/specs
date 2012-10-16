Name: sonic-visualiser
Version: 2.0
Release: alt1
Summary: A program for viewing and analysing the contents of music audio files
License: GPLv2
Group: Sound
Url: http://www.sonicvisualiser.org/

Source: %name-%version.tar

BuildRequires: libfftw3-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: bzlib-devel
BuildRequires: libvamp-devel
BuildRequires: librubberband-devel
BuildRequires: liblo-devel
BuildRequires: libportaudio2-devel
BuildRequires: libjack-devel
BuildRequires: libpulseaudio-devel
BuildRequires: liblrdf-devel
BuildRequires: liboggz-devel
BuildRequires: libfishsound-devel
BuildRequires: libmad-devel
BuildRequires: libid3tag-devel
BuildRequires: xorg-xproto-devel
BuildRequires: libqt4-devel
BuildRequires: gcc-c++
BuildRequires: dataquay-devel
BuildRequires: libredland-devel
BuildRequires: libalsa-devel

%description
Sonic Visualiser is a program for viewing and analysing the contents
of music audio files.

%prep
%setup
sed -i -e 's/Icon=sv-icon/Icon=%name/' sonic-visualiser/sonic-visualiser.desktop

%build
cd svcore
%autoreconf
%configure
%make_build

cd ..; cd svgui
%autoreconf
%configure
%make_build

cd ..; cd svapp
%autoreconf
%configure
%make_build

cd ..; cd %name
%autoreconf
%configure
%make_build

%install
install -D -m0755 sonic-visualiser/sonic-visualiser \
		  %buildroot/%_bindir/%name
install -D -m0644 sonic-visualiser/sonic-visualiser.desktop \
		  %buildroot/%_datadir/applications/%name.desktop
for s in 16 22 24 32 48 64 128; do
	install -D -m0644 sonic-visualiser/icons/sv-${s}x${s}.png \
			  %buildroot/%_datadir/icons/hicolor/${s}x${s}/apps/%name.png
done

%files
%_bindir/%name
%_datadir/applications/%name.desktop
%doc sonic-visualiser/README
%doc sonic-visualiser/README.OSC
%_datadir/icons/hicolor/128x128/apps/%name.png
%_datadir/icons/hicolor/64x64/apps/%name.png
%_datadir/icons/hicolor/48x48/apps/%name.png
%_datadir/icons/hicolor/32x32/apps/%name.png
%_datadir/icons/hicolor/24x24/apps/%name.png
%_datadir/icons/hicolor/22x22/apps/%name.png
%_datadir/icons/hicolor/16x16/apps/%name.png

%changelog
* Mon Oct 15 2012 Paul Wolneykien <manowar@altlinux.ru> 2.0-alt1
- Initial release for ALT Linux.
