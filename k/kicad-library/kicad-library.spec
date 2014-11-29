Summary:  Library for kicad (creation of electronic schematic diagrams)
Name:     kicad-library
Version:  r240
Release:  alt1
Source0:  ~kicad-product-committers-%name-%version.tgz
License:  GPLv2+
Group:    Sciences/Computer science
Url: 	  https://code.launchpad.net/kicad
#Url: 	  http://bazaar.launchpad.net/~kicad-product-committers/kicad/library

# Automatically added by buildreq on Fri Feb 13 2009
BuildRequires: ccmake gcc-c++ cmake >= 2.6.1 cmake-modules glibc-pthread libstdc++-devel
BuildArch: noarch

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-library is a set of library needed by kicad.

%prep
%setup -n ~kicad-product-committers/kicad/library/ 

%build
export LC_ALL=C
cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DCMAKE_INSTALL_PREFIX=/usr
%make

%install
%make DESTDIR=%buildroot install

%files
%_datadir/kicad/library/*
%_datadir/kicad/modules/*
#%_datadir/kicad/template/*

%changelog
* Sat Nov 29 2014 barssc <barssc@altlinux.ru> r240-alt1
- new version

* Tue Jun 07 2011 Denis Klimov <zver@altlinux.org> 1.0-alt2.20101208
- add BuildArch

* Tue Jun 07 2011 Denis Klimov <zver@altlinux.org> 1.0-alt1.20101208
- new version
- remove needless -q option for setup macro

* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 1.0-alt0.1
- first build for ALT Linux

