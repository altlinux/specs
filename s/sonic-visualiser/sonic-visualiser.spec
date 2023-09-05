Name: sonic-visualiser
Version: 4.5.2
Release: alt1

Summary: Application for viewing and analysing the contents of music audio files

License: GPLv2+
Group: Sound
Url: http://sonicvisualiser.org/

Packager: Grigory Ustinov <grenka@altlinux.org>

Source0: %name-%version.tar
Source1: %name.xml

Patch0: sonic-visualiser-system-dataquay.patch

BuildRequires: bzlib-devel capnproto-devel dataquay-minefeld-devel
BuildRequires: libfftw3-devel libfishsound-devel libid3tag-devel
BuildRequires: libjack-devel liblo-devel liblrdf-devel libmad-devel
BuildRequires: liboggz-devel libportaudio2-devel libpulseaudio-devel
BuildRequires: librubberband-devel libsamplerate-devel libsndfile-devel
BuildRequires: libsord-devel qt5-svg-devel libopusfile-devel
BuildRequires: meson

%description
Sonic Visualiser is an application for viewing and analysing the
contents of music audio files.

The aim of Sonic Visualiser is to be the first program you reach for
when want to study a musical recording rather than simply listen to it.

We hope Sonic Visualiser will be of particular interest to
musicologists, archivists, signal-processing researchers and anyone else
looking for a friendly way to take a look at what lies inside the audio
file.

%prep
%setup
# Make sure, that we use system dataquay
rm -rfv dataquay
%patch0 -p2

%build
%add_optflags %(pkg-config --libs dataquay)
%meson
%meson_build

%install
%meson_install

# plugin dir
install -dm 755 %buildroot%_libdir/vamp

# icons
for size in 16 22 24 32 48 64 128 ; do
install -Dm 644 icons/sv-${size}x${size}.png %buildroot/%_datadir/icons/hicolor/${size}x${size}/apps/%name.png
done

install -Dm 644 icons/sv-icon.svg %buildroot/%_datadir/icons/hicolor/scalable/apps/%name.svg
ln -s sonic-visualiser.svg %buildroot/%_datadir/icons/hicolor/scalable/apps/sv-icon.svg

# mime types
install -Dm 644 %SOURCE1 %buildroot%_datadir/mime/packages/%name.xml

install -Dm 644 x-sonicvisualiser.desktop %buildroot/%_datadir/mimelnk/application/x-sonicvisualiser.desktop
install -Dm 644 x-sonicvisualiser-layer.desktop %buildroot/%_datadir/mimelnk/application/x-sonicvisualiser-layer.desktop

%files
%doc CHANGELOG README.md COPYING
%_bindir/%name
%_bindir/piper-convert
%_bindir/piper-vamp-simple-server
%_bindir/vamp-plugin-load-checker
%dir %_libdir/vamp
%_datadir/icons/hicolor/*/apps/%name.*
%_datadir/icons/hicolor/scalable/apps/sv-icon.svg
%_datadir/applications/%name.desktop
%_datadir/mime/packages/%name.xml
%dir %_datadir/mimelnk
%dir %_datadir/mimelnk/application
%_datadir/mimelnk/application/x-sonicvisualiser*

%changelog
* Tue Sep 05 2023 Grigory Ustinov <grenka@altlinux.org> 4.5.2-alt1
- Build new version.

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 4.5-alt1
- Build new version.

* Mon May 17 2021 Grigory Ustinov <grenka@altlinux.org> 4.3-alt1
- Build new version.

* Wed Sep 09 2020 Sergey V Turchin <zerg@altlinux.org> 4.2-alt1
- New version.

* Wed May 22 2019 Grigory Ustinov <grenka@altlinux.org> 3.3-alt1
- Build new version.

* Thu Jan 10 2019 Grigory Ustinov <grenka@altlinux.org> 3.2.1-alt1
- Build new version.

* Tue Dec 18 2018 Grigory Ustinov <grenka@altlinux.org> 3.2-alt1
- Build new version.

* Fri Oct 26 2018 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Build new version.

* Thu Jun 11 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4-alt2.hg20140912.1
- Rebuilt for gcc5 C++11 ABI.

* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt2.hg20140912
- Built with dataquay-minefeld instead of dataquay

* Sun Sep 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.hg20140912
- Initial build for Sisyphus

