%define _unpackaged_files_terminate_build 1

Name: ebook-speaker
Version: 6.2.0
Release: alt1

Summary: eBook reader that reads aloud in a synthetic voice
License: GPL-2.0-or-later AND LGPL-3.0-or-later
Group: Office
Url: https://github.com/book-readers/ebook-speaker

Source: %name-%version.tar

ExcludeArch: i586

# sync with version 6.2.0-7 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(sox)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libmagic)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(sndfile)
BuildRequires: /usr/bin/txt2man

Requires: /usr/bin/pandoc
Requires: /usr/bin/iconv
Requires: /usr/bin/tesseract
Requires: /usr/bin/cuneiform
Requires: /usr/bin/wget

Requires: /usr/bin/ebook-convert
Requires: /usr/bin/calibre

Requires: /usr/bin/lowriter
Requires: /usr/bin/espeak
Requires: /usr/bin/flite
Requires: /usr/bin/text2wave
Requires: /usr/bin/mbrola
Requires: /usr/bin/pico2wave
Requires: /usr/bin/scanimage
Requires: /usr/bin/pnmflip
Requires: /usr/bin/unar
Requires: /usr/bin/unrtf
Requires: /usr/bin/pulseaudio
Requires: /usr/bin/pactl
Requires: /usr/bin/amixer
Requires: /usr/bin/alsamixer

# Missed:
# Requires: /usr/bin/gif2png
# Requires: /usr/bin/man2html
## different purpose
# Requires: /usr/bin/swift

%description
This package provides a command-line e-reader that reads out
electronic text using speech synthesis. It has a simple user
interface appropriate for Braille terminals.

Currently the following formats are supported (some formats need
installation of additional packages):

* AportisDoc
* ASCII mail text
* ASCII text
* Broadband eBooks (BBeB)
* Composite Document File (Microsoft Office Word)
* DAISY3 DTBook
* EPUB ebook data
* GIF image data
* GutenPalm zTXT
* GNU gettext message catalogue
* HTML document
* ISO-8859 text
* JPEG image data
* Microsoft Reader eBook Data
* Microsoft Windows HtmlHelp Data
* Microsoft Word 2007+
* Mobipocket E-book
* MS Windows HtmlHelp Data
* Netpbm PPM data
* OpenDocument Text
* PDF document
* PeanutPress PalmOS
* PNG image data
* POSIX shell script text
* PostScript document
* Rich Text Format
* troff or preprocessor text (e.g. Linux man-pages)
* UTF-8 Unicode mail text
* UTF-8 Unicode text
* WordPerfect
* XML document text

%prep
%setup
%patch -p1
sed -i "/^Comment=Speaking e-reader/d" doc/ebook-speaker.desktop
sed -i "s/Categories=.*/Categories=Accessibility;Utility;ConsoleOnly;/" doc/ebook-speaker.desktop

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

mkdir -pv %buildroot%_desktopdir
cp -pv doc/ebook-speaker.desktop %buildroot%_desktopdir/

mkdir -pv %buildroot%_datadir/doc/%name-%version
mv -v  %buildroot%_datadir/doc/%name/* %buildroot%_datadir/doc/%name-%version/

mkdir -pv %buildroot%_iconsdir/hicolor/scalable/apps
cp -pv doc/ebook-speaker.svg %buildroot%_iconsdir/hicolor/scalable/apps/

%check
%make_build check

%files -f %{name}.lang
%doc doc
%_bindir/*
%_man1dir/*
%_desktopdir/ebook-speaker.desktop
%_iconsdir/hicolor/scalable/apps/ebook-speaker.svg

%changelog
* Sun Nov 30 2025 Nikolay Strelkov <snk@altlinux.org> 6.2.0-alt1
- Initial build for Sisyphus
