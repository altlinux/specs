Summary: 	Documentation and tutorials for kicad
Name: 		kicad-doc
Version:	r647
Release:	alt1
Group: 		Documentation
License: 	Free Documentation Licence
Url:		https://code.launchpad.net/kicad
#Url: 		http://bazaar.launchpad.net/~kicad-developers/kicad/doc
Source:		~kicad-developers-%name-%version.tgz
BuildArch:      noarch
# Automatically added by buildreq on Fri Feb 13 2009
BuildRequires: ccmake gcc-c++ cmake >= 2.8.4 cmake-modules glibc-pthread libstdc++-devel

%description 
KiCad is a open source (GPL) integrated package for schematic circuit capture and PCB layout.
This is the documentation package for kicad. It contains documentation, tutorials and files localization.


%prep
%setup -q -n ~kicad-developers/kicad/doc


%build
cmake -DCMAKE_INSTALL_PREFIX=/usr

%install
%make DESTDIR=%buildroot install

%clean
%__rm -rf %buildroot

%files
%_datadir/doc/*
%_datadir/kicad/*

%changelog
* Sat Nov 29 2014 barssc <barssc@altlinux.ru> r647-alt1
- new version

* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 1.1-alt0.2
- fix Group

* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 1.1-alt0.1
- first build for ALT Linux

