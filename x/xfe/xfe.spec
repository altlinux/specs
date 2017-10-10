Name: xfe
Version: 1.42
Release: alt1

Summary: MS-Explorer or Commander like file manager for X
License: GPLv2+
Group: File tools

Url: http://roland65.free.fr/xfe/
Source: %name-%version.tar
Packager: Mike Radyuk <torabora@altlinux.org>

# Automatically added by buildreq on Mon Oct 09 2017
# optimized out: fontconfig fontconfig-devel glibc-kernheaders-x86 gnu-config libX11-devel libXrender-devel libfreetype-devel libstdc++-devel perl perl-Encode perl-XML-Parser pkg-config python-base tzdata xorg-kbproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ glibc-kernheaders-generic imake intltool libXft-devel libfox-devel libpng-devel xorg-cf-files

BuildRequires: desktop-file-utils

%description
X File Explorer (Xfe) is a filemanager for X. It is based on the popular
X Win Commander, which is discontinued. Xfe is desktop independent and
is written with the C++ Fox Toolkit. It has Windows Commander or
MS-Explorer look and is very fast and simple. The main features are:
file associations, mount/umount devices, directory tree for quick cd,
change file attributes, auto save registry, compressed archives
view/creation/extraction and much more.

%prep
%setup

%build
%configure --enable-release
%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
        --add-mime-type=inode/directory \
        %buildroot%_desktopdir/xfe.desktop
desktop-file-install --dir %buildroot%_desktopdir \
        --remove-category=Utility \
        --add-category=Graphics \
        --add-category=RasterGraphics \
        --add-category=2DGraphics \
        --add-mime-type=image/jpg \
        %buildroot%_desktopdir/xfi.desktop
desktop-file-install --dir %buildroot%_desktopdir \
        --remove-category=Utility \
        --add-category=Settings \
        %buildroot%_desktopdir/xfp.desktop

%files -f %name.lang
%doc AUTHORS COPYING README TODO BUGS
%_bindir/*
%_datadir/xfe/
%_desktopdir/xf*.desktop
%_pixmapsdir/*
%_man1dir/*


%changelog
* Tue Oct 10 2017 Mike Radyuk <torabora@altlinux.org> 1.42-alt1
- New version (closes: #25570, #27616)

* Sat Jun 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.32.3-alt1.qa2
- Fixed build

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.32.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for xfe

* Tue Apr 12 2011 Mike Radyuk <torabora@altlinux.org> 1.32.3-alt1
- initial build for ALT Linux Sisyphus (closes: #23321)
