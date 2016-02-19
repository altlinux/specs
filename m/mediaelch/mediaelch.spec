Name:           mediaelch
Summary:        A Media Manager for XBMC
Url:            http://www.kvibes.de/mediaelch
Version:        2.4
Release:        alt1

License:        GPL-3.0+
Group:          Video

Source0:        %name-%version.tar
Patch0:         desktop.patch

Provides:       MediaElch = %version-%release

BuildRequires(pre): qt5-base-devel
BuildRequires:  gcc-c++
BuildRequires:  qt5-multimedia-devel
BuildRequires:  qt5-script-devel
BuildRequires:  qt5-tools
BuildRequires:  qt5-webkit-devel
BuildRequires:  libmediainfo-devel
BuildRequires:  zlib-devel
BuildRequires:  libzen-devel
BuildRequires:  libcurl-devel

Requires:       qt5-translations

%description
MediaElch is your Media Manager for handling Movies, TV Shows and
Concerts/Music Videos in XBMC. It is designed to gather information from
various movie databases on the internet and store these information
directly to XBMCs database or in nfo files. MediaElch is also
downloading movie posters, backdrops, fan arts and pictures of the
actors as well as trailers.

%prep
%setup -q
%patch0 -p1

%build
DESTDIR=%buildroot PREFIX=/usr %qmake_qt5 *.pro
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc COPYING README.md
%_bindir/*
%_desktopdir/*.desktop
%_pixmapsdir/*.png

%changelog
* Fri Feb 19 2016 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1
- Inital build in Sisyphus
