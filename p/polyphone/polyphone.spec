
%define _unpackaged_files_terminate_build 1

Name:     polyphone
Version:  2.3.0
Release:  alt1

Summary:  A soundfont editor for quickly designing musical instruments
License:  GPL-3.0
Group:    Sound
URL:      https://www.polyphone-soundfonts.com

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildRequires: rpm-build-xdg
BuildRequires: qt5-base-devel qt5-tools qt5-svg-devel
BuildRequires: qcustomplot-qt5-devel
BuildRequires: libstk-devel

# git grep PKGCONFIG
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(rtmidi)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(vorbisenc)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(zlib)


%description
Polyphone is an open-source soundfont editor for creating musical
instruments, featuring:
  * editing of sf2, sf3, sfz and sfArk file formats;
  * compatible with jack and asio audio servers;
  * built-in synthesizer, controlled by a virtual keyboard
    or midi signals;
  * automatic recognition of root keys;
  * automatic loop of samples;
  * simultaneous editing of parameters;
  * specific tools for musical instrument creation;
  * recorder to keep a trace of what is played in a .wav file;
  * soundfont browser connected to the online repository.

%prep
%setup
%autopatch -p1

%build
pushd sources
%qmake_qt5 PREFIX=%prefix \
    QMAKE_LFLAGS+="%optflags" \
    QMAKE_STRIP=echo

%make_build
popd

%install
%make_install -C sources install INSTALL_ROOT=%buildroot
rm -rf %buildroot%_mandir/fr

%files
%_bindir/*
%_man1dir/*
%_mandir/ru/man1/*
%_desktopdir/*.desktop
%_xdgmimedir/packages/*.xml
%_datadir/metainfo/*%{name}*.xml
%_iconsdir/*/*/apps/polyphone.*
%_iconsdir/*/*/mimetypes/audio-x-soundfont.*
%doc %_docdir/%name

%changelog
* Mon Mar 14 2022 Ivan A. Melnikov <iv@altlinux.org> 2.3.0-alt1
- 2.3.0
- add Rissian translation

* Thu May 20 2021 Ivan A. Melnikov <iv@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
