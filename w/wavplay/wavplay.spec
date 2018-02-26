Name: wavplay
Version: 1.4
Release: alt1
Summary: Utility to play WAV files
Group: Sound
License: GPL2
Url: http://sourceforge.net/projects/wavplay/

Packager: Yuriy Shirokov <yushi@altlinux.org>

Obsoletes: wavplay <= 1.4

Source: wavplay-1.4.tar.bz2

Patch: wavplay-1.4-fix-compile.patch
Patch1: wavplay-1.4-alt-make.patch
Patch2: wavplay-1.4-alt-no486.patch

%description
The Linux wavplay command line utility used for playing "wav" files.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
%make_build

%install
install -pD wavplay %buildroot%_bindir/wavplay
ln -s wavplay %buildroot%_bindir/wavrec

%files
%_bindir/*

%changelog
* Wed Apr 21 2010 Yuriy Shirokov <yushi@altlinux.org> 1.4-alt1
- First separated spec for ALT Linux
