Summary: 	Documentation and tutorials for kicad
Name: 		kicad-doc
Version:	1.1
Release:	alt0.2
Group: 		Documentation
License: 	GPL
Url: 		http://kicad.sourceforge.net/
Packager: Alexey Shentzev <ashen@altlinux.ru>
Source:		%name-%version.tar.bz2
BuildArch:      noarch
# Automatically added by buildreq on Fri Feb 13 2009
BuildRequires: ccmake gcc-c++ cmake >= 2.4.6 cmake-modules glibc-pthread libstdc++-devel

%description 
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork up to 16 layers.
This is the documentation package for kicad. It contains documentation
and tutorials.


%prep
%setup -q -n kicad
cmake -DCMAKE_INSTALL_PREFIX=/usr

%build
%make DESTDIR=%buildroot install

%clean
%__rm -rf %buildroot

%files
%defattr(-,root,root,-)
%_datadir/doc/*

%changelog
* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 1.1-alt0.2
- fix Group

* Fri Feb 13 2009 Alexey Shentzev <ashen@altlinux.ru> 1.1-alt0.1
- first build for ALT Linux

