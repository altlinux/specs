Name:		qshare
Summary:	qShare is a FTP server
License:	GPLv3
Group:		Networking/File transfer
Version:	1.3
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
URL:		http://qt-apps.org/content/show.php/qShare?content=116612

Source0:	http://qt-apps.org/CONTENT/content-files/116612-%name-%version-src.tar.gz
Source1:	%name.desktop

# Automatically added by buildreq on Thu Dec 17 2009 (-bi)
BuildRequires: ImageMagick-tools gcc-c++ libqt4-devel

%description
qShare is a FTP server with a service discovery feature
that makes qShare clients aware of other clients running
on the same network.

You can easily add/remove folders from the shared folders
list, enable/disable the built-in FTP server.

%prep
%setup -n %name

%build
export PATH=$PATH:%_qt4dir/bin
lrelease ./i18n/%{name}_ru.ts
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
%__install -Dp -m 0755 %name %buildroot%_bindir/%name
%__install -pD -m 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 icons/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 icons/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 icons/%name.png %buildroot%_miconsdir/%name.png

%files
%doc docs
%_bindir/*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Mon May 24 2010 Motsyo Gennadi <drool@altlinux.ru> 1.3-alt1
- 1.3

* Sat Jan 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt1
- 1.2

* Thu Dec 17 2009 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt1
- initial build for ALT Linux
