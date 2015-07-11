Name: mp3unicode
Version: 1.2.1
Release: alt2
License: GPLv2
Vendor: http://www.kde-apps.org/content/show.php?content=41784
Summary: Convert MP3 tags into unicode
Group: Sound
Url: http://mp3unicode.sourceforge.net/index.html
Source: https://github.com/downloads/alonbl/mp3unicode/mp3unicode-1.2.1.tar.bz2

# Automatically added by buildreq on Tue Jul 22 2014
# optimized out: gnu-config libcloog-isl4 libstdc++-devel pkg-config
BuildRequires: gcc-c++ libtag-devel man xsltproc

%description
MP3Unicode is a command line utility to convert ID3 tags in mp3 files
between different encodings.

%prep
%setup

%build
%configure --disable-rpath

%make_build

%install
%makeinstall

%files
%exclude %_defaultdocdir/%name
%doc README ChangeLog AUTHORS
%_bindir/*
%_man1dir/*

%changelog
* Sat Jul 11 2015 Fr. Br. George <george@altlinux.ru> 1.2.1-alt2
- Rebuild with new dependencies

* Tue Jul 22 2014 Fr. Br. George <george@altlinux.ru> 1.2.1-alt1
- Initial build from upstream spec

* Sat Apr 14 2007 Aon Bar-Lev <alon.barlev@gmail.com>
- Initial.
