Name: steghide
Version: 0.5.1
Release: alt4

Summary: A steganography hiding tool
License: GPLv2+
Group: File tools

URL: http://steghide.sourceforge.net/
Source: http://downloads.sourceforge.net/steghide/steghide-%version.tar.bz2
Patch0: steghide-0.5.1-gcc34.patch
Patch1: steghide-0.5.1-gcc4.patch
Patch2: steghide-0.5.1-gcc43.patch

# Automatically added by buildreq on Thu Nov 27 2008
BuildRequires: doxygen gcc-c++ libjpeg-devel libmcrypt-devel libmhash-devel zlib-devel

%description
Steghide is a steganography program that is able to hide data in various
kinds of image and audio files. The color-frequencies (for image files) or
sample-frequencies (for audio files) are not changed, thus making the
embedding resistant against first-order statistical tests. Features of
steghide include compression and encryption of embedded data, embedding of
a checksum to verify the integrity of the extracted data, and support for
JPEG, BMP, WAV, and AU files.

%prep
%setup
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
touch NEWS ChangeLog AUTHORS
autoreconf
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot
rm -rf %buildroot%_docdir/%name

%find_lang %name

%files -f %name.lang
%doc BUGS CREDITS HISTORY README
%_bindir/*
%_man1dir/*

%changelog
* Thu Nov 27 2008 Victor Forsyuk <force@altlinux.org> 0.5.1-alt4
- Fix FTBFS with gcc43.

* Sat Dec 29 2007 Victor Forsyuk <force@altlinux.org> 0.5.1-alt3
- Fix FTBFS in current build environment.

* Tue May 16 2006 Victor Forsyuk <force@altlinux.ru> 0.5.1-alt2
- Fix FTBFS with gcc4.

* Mon Jul 18 2005 Victor Forsyuk <force@altlinux.ru> 0.5.1-alt1
- Initial build.
