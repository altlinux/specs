%set_automake_version 1.4

Name: cfdg-fe
Version: v20061127
Release: alt1.qa1

Summary: Frontend for CFDG
License: GPLv2
Group: Graphics
Url: http://www.contextfreeart.org/mediawiki/index.php/LinuxGUI

Packager: Timur Batyrshin <erthad@altlinux.org>
Source: %name-%version.tar.bz2
Source1: %name.desktop.conf

BuildRequires(pre): ImageMagick-tools

# Automatically added by buildreq on Sat Apr 18 2009
BuildRequires: libgtk+2-devel

Requires: cfdg
BuildRequires: desktop-file-utils

%description
A frontend for CFDG
  
%prep
%setup

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%_liconsdir
convert pixmaps/icon.png -resize 48x48 %buildroot%_liconsdir/%name.png

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=VectorGraphics \
	%buildroot%_desktopdir/cfdg-fe.desktop

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README COPYING TODO 
%_bindir/*
%_datadir/%name/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> v20061127-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for cfdg-fe

* Sat Apr 18 2009 Timur Batyrshin <erthad@altlinux.org> v20061127-alt1
- initial build
