
%define _unpackaged_files_terminate_build 1

Name:     polyphone
Version:  2.5.1
Release:  alt2

Summary:  A soundfont editor for quickly designing musical instruments
License:  GPL-3.0
Group:    Sound
URL:      https://www.polyphone-soundfonts.com

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildRequires: rpm-build-xdg
BuildRequires: qt6-base-devel qt6-tools qt6-svg-devel
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
BuildRequires: pkgconfig(sndfile)
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
%qmake_qt6 PREFIX=%prefix \
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
%_desktopdir/*.desktop
%_xdgmimedir/packages/*.xml
%_datadir/metainfo/*%{name}*.xml
%_iconsdir/*/*/apps/polyphone.*
%doc %_docdir/%name

%changelog
* Wed Aug 27 2025 Ivan A. Melnikov <iv@altlinux.org> 2.5.1-alt2
- Switch to Qt6.

* Wed Aug 27 2025 Ivan A. Melnikov <iv@altlinux.org> 2.5.1-alt1
- 2.5.1

* Wed Aug 09 2023 Ivan A. Melnikov <iv@altlinux.org> 2.3.1-alt1
- 2.3.1

* Mon Mar 14 2022 Ivan A. Melnikov <iv@altlinux.org> 2.3.0-alt1
- 2.3.0
- add Rissian translation

* Thu May 20 2021 Ivan A. Melnikov <iv@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus
