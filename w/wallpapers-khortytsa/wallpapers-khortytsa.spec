%define photos_dir %_datadir/wallpapers
%define rname khortytsa

Name: wallpapers-%rname
Version: 2
Release: alt2

Summary: Photo wallpapers from Khortytsa island
URL:	http://picasaweb.google.com/nick.grechukh/YnAJgD?feat=directlink
License: GPL
Group: Graphics

Buildarch: noarch

Source: wallpapers-%rname-%version.tar.bz2

%description
Packaged as jpeg

%prep
%setup -q

%build

%install
%__mkdir_p %buildroot/%photos_dir/%rname
%__install -m 0644 *.jpg %buildroot/%photos_dir/%rname
%__mkdir_p %buildroot/%photos_dir/%rname/dniprohes
%__install -m 0644 dniprohes/*.jpg %buildroot/%photos_dir/%rname/dniprohes/

%files
%photos_dir/*
%doc COPYING

%changelog
* Thu Mar 03 2011 Mykola Grechukh <gns@altlinux.ru> 2-alt2
- fixed

* Thu Mar 03 2011 Mykola Grechukh <gns@altlinux.ru> 2-alt1
- added photos of The Dnieper Hydroelectric Station (DniproHES)

* Thu Jul 22 2010 Mykola Grechukh <gns@altlinux.ru> 1-alt0.M51.1
- build for 5.1

* Thu Jul 22 2010 Mykola Grechukh <gns@altlinux.ru> 1-alt1
- first build for ALT Linux
