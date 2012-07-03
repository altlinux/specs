%define photos_dir %_datadir/wallpapers
%define rname landscapes

Name: wallpapers-%rname
Version: 1
Release: alt1.2

Summary: It's photos of various natural landscapes.
Summary(ru_RU.UTF-8): Фоны для рабочего стола. Пейзажи.
License: GPL
Group: Graphics
Url: http://www.openoffice.ru
Packager: Anatoly Yakushin <jaa@altlinux.ru>

Buildarch: noarch

Source: wallpapers-%rname-%version.tar.bz2

%description
Packaged as jpeg 

%description -l ru_RU.UTF-8
упаковано в JPEG 

%prep
%setup -q

%build

%install
%__mkdir_p %buildroot/%photos_dir/%rname
%__install -m 0644 *.jpg %buildroot/%photos_dir/%rname


%files
%photos_dir/*
%doc README COPYING

%changelog
* Mon Sep 29 2008 Anatoly Yakushin <jaa@altlinux.ru> 1-alt1.2
- removed package intersection

* Mon Jan 17 2005 Anatoly Yakushin <jaa@altlinux.ru> 1-alt1
- initial build for Altlinux Team


