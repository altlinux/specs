%define photos_dir %_datadir/wallpapers
%define rname flowers


Name: wallpapers-%rname
Version: 1
Release: alt1.2


Summary: Photo wallpapers flowers.
License: Free Art License
Group: Graphics

Url: http://yakushin.livejournal.com
Source: %name-%version.tar.bz2

Summary(ru_RU.UTF-8): Фоны для рабочего стола - цветы

Buildarch: noarch


%description
Packaged as jpeg 

%description -l ru_RU.UTF-8
сжаты  JPEG 


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

* Mon Jul 07 2003 Anatoly Yakushin <jaa@altlinux.ru> 1-alt1
- build for AltLinux Team



