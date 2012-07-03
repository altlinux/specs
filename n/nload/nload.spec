Name: nload
Version: 0.7.4
Release: alt1

Summary: monitors network traffic and bandwidth usage
URL: http://www.roland-riegel.de/nload/
Source: %name-%version.tar.gz
License: GPL
Group: Monitoring

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Sun Aug 06 2006
BuildRequires: gcc-c++ libncurses-devel

%description
real time monitor for network traffic

%prep
%setup -qn %name-%version

%build
%configure 
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%_man1dir/*
%_bindir/%name

%changelog
* Thu May 03 2012 Ilya Mashkin <oddity@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Mon Dec 15 2008 Ilya Mashkin <oddity@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Sun Aug 06 2006 Anton Gorlov <stalker@altlinux.ru> 0.6.0-alt1
-  First built for Sisyphus 


