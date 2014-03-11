
Name:     epsoneplijs
Version:  0.4.1
Release:  alt1
Summary:  Ghostscript IJS Plugin for the Epson EPL-5700L/5800L/5900L/6100L/6200L printers

Packager: Andrey Cherepanov <cas@altlinux.org>

Group:    Publishing
License:  BSD

URL:      http://sourceforge.net/projects/epsonepl/

Source:	  http://osdn.dl.sourceforge.net/sourceforge/epsonepl/epsoneplijs-%{version}.tgz
Patch:    epsoneplijs-0.4.1-mdk-use_system_libs.patch
Patch1:   epsoneplijs-0.4.0-alt-fortify-source.patch

Requires: ghostscript >= 6.53

BuildRequires: libieee1284-devel libusb-devel

%description
Support for the Epson EPL-5700L/5800L/5900L/6100L/6200L printer family
under linux and other unix-like systems.
It is known to work for at least one user for each of 5700L, 5800L,
5900L, and 6100L. 6100L and 6200L support is new.

%prep

%setup -q
%patch -p2
%patch1 -p1

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;


%build
%autoreconf

%configure \
    --with-kernelusb \
    --with-kernel1284 \
    --with-libusb \
    --with-libieee1284 

%make_build

%install
install -d %buildroot/%_bindir

%makeinstall

install -d %buildroot%_datadir/cups/model/
cp -a cups/*.ppd* %buildroot%_datadir/cups/model/

%files
%doc ChangeLog FAQ LIMITATIONS README* *.pdf epl_docs/epl-protocol.pdf epl_docs/README.1st
%_bindir/*
%_datadir/cups/model/*

%changelog
* Tue Mar 11 2014 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1
- New version (ALT #29458)

* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.1
- Fixed build

* Wed Nov 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.4.0-alt1
- Build as a separate package
