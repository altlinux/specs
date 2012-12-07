Name:		qshare
Summary:	qShare is a FTP server
License:	GPLv3
Group:		Networking/File transfer
Version:	2.1.5
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
URL:		http://www.zuzuf.net/qshare/

Source0:	http://www.zuzuf.net/qshare/files/%name-%version-src.tar.bz2

Patch0:		%name-2.1.5-desktop.diff

BuildRequires:	/usr/bin/convert cmake gcc-c++ libqt4-devel libavahi-devel

%description
qShare is a FTP server with a service discovery feature
that makes qShare clients aware of other clients running
on the same network.

You can easily add/remove folders from the shared folders
list, enable/disable the built-in FTP server.

%prep
%setup
%patch0 -p1

%build
lrelease-qt4 i18n/*.ts
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"

%make_build

%install
make DESTDIR=%buildroot install

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 icons/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 icons/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 icons/%name.png %buildroot%_miconsdir/%name.png

%files
%dir %_datadir/%name
%dir %_datadir/%name/docs
%dir %_datadir/%name/translations
%doc AUTHORS README
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/kde4/services/ServiceMenus/*.desktop
%_datadir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_pixmapsdir/%name.png

%changelog
* Fri Dec 07 2012 Motsyo Gennadi <drool@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Thu Aug 30 2012 Motsyo Gennadi <drool@altlinux.ru> 2.1.4-alt1.1
- update Russian & Ukrainian translations

* Wed Aug 29 2012 Motsyo Gennadi <drool@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Fri Aug 17 2012 Motsyo Gennadi <drool@altlinux.ru> 2.1.3-alt2
- update BuildRequires

* Thu Aug 16 2012 Motsyo Gennadi <drool@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Mon May 24 2010 Motsyo Gennadi <drool@altlinux.ru> 1.3-alt1
- 1.3

* Sat Jan 02 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt1
- 1.2

* Thu Dec 17 2009 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt1
- initial build for ALT Linux
