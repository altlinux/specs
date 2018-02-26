Name: aewan
Version: 1.0.01
Release: alt1

Summary: Ascii-art Editor Without a Name
License: GPL
Group: Graphics
Url: http://aewan.sourceforge.net/

Packager: Alexandra Panyukova <mex3@altlinux.ru>
Source: http://ovh.dl.sourceforge.net/sourceforge/aewan/%name-%version.tar.gz

# Automatically added by buildreq on Fri Apr 06 2007
BuildRequires: libncurses-devel zlib-devel

%description
Aewan is a multi-layered ascii-art/animation editor that produces both stand-alone cat-able art files and an easy-to-parse format for integration in your terminal applications.
   
%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%_bindir/*
%doc README CHANGELOG COPYING TODO

%changelog
* Fri Apr 06 2007 Alexandra Panyukova <mex3@altlinux.ru> 1.0.01-alt1
Initial build

