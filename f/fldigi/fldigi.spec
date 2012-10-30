Name: fldigi
Version: 3.21.58
Release: alt1
Summary: Digital modem program
License: GPL
Group: Communications
Source0: %name-%version.tar

# Automatically added by buildreq on Mon Jan 04 2010 (-bi)
BuildRequires: gcc-c++ libX11-devel libXext-devel libXft-devel libfltk-devel libjpeg-devel libpng-devel libsamplerate-devel

BuildPreReq: libpixman-devel libcairo-devel libXinerama-devel

%description
Digital modem program

%prep
%setup

%build
%configure --enable-optimizations=native --with-xmlrpc=no
%make_build

%install
%makeinstall

%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*.desktop
%_pixmapsdir/*.xpm
%_man1dir/*

%changelog
* Tue Oct 30 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 3.21.58-alt1
- Version 3.21.58

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.21.8-alt3
- Rebuilt with libpng15

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.21.8-alt2
- Rebuilt with FLTK 1.3.0.r8575

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.21.8-alt1
- Version 3.21.8

* Tue Jan 05 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 3.12.5-alt1.1
- fix description

* Mon Jan 04 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 3.12.5-alt1
- initial build

