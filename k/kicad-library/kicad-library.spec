Summary:  Library for kicad (creation of electronic schematic diagrams)
Name:     kicad-library
Version:  1.0
Release:  alt2.20101208
Source0:  %name-%version.tar.bz2
License:  GPL
Group:    Sciences/Computer science
Url: 	  https://code.launchpad.net/~kicad-lib-committers/kicad/library

# Automatically added by buildreq on Fri Feb 13 2009
BuildRequires: ccmake gcc-c++ cmake >= 2.4.6 cmake-modules glibc-pthread libstdc++-devel
BuildArch: noarch

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad-library is a set of library needed by kicad.

%prep
%setup -n %name 

%build
export LC_ALL=C
cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DCMAKE_INSTALL_PREFIX=/usr
%make

%install
%make DESTDIR=%buildroot install

%files
%defattr(-,root,root)
%_datadir/kicad/library
%_datadir/kicad/modules

%changelog
* Tue Jun 07 2011 Denis Klimov <zver@altlinux.org> 1.0-alt2.20101208
- add BuildArch

* Tue Jun 07 2011 Denis Klimov <zver@altlinux.org> 1.0-alt1.20101208
- new version
- remove needless -q option for setup macro

* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 1.0-alt0.1
- first build for ALT Linux

