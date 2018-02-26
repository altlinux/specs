Name: spcaview
Version: 20071224
Release: alt1.1

Summary: Sdl video recorder and viewer with sound

License: GPL
Group: System/Libraries

Url: http://mxhaard.free.fr/sview.html
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://mxhaard.free.fr/spca50x/Download/%name-%version.tar.bz2
Patch0: spcaview-20071224-alt-debuginfo.patch
Patch1: spcaview-20071224-alt-v4l.patch

# Automatically added by buildreq on Sun May 06 2007
BuildRequires: esound libSDL-devel
BuildPreReq: libv4l-devel

%description
spcaview - Sdl video recorder and viewer with sound.
spcaserv - Streaming TCP server
spcacat - Picture grabber
This package work with the spca5xx based webcam with the raw jpeg feature.

%prep
%setup -q
%patch0 -p2
%patch1 -p2
# fix buffer overflow
%__subst "s|fourcc\[4\]|fourcc\[5\]|g" *.c

%build
%make_build

%install
mkdir -p %buildroot%_bindir
install -m 755 spcaview %buildroot%_bindir
install -m 755 spcaserv %buildroot%_bindir
install -m 755 spcacat %buildroot%_bindir

%files
%doc README Changelog http-java-applet/ readme.avilib
%_bindir/*

%changelog
* Tue Jun 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20071224-alt1.1
- Fixed build

* Mon Jul 13 2009 Vitaly Lipatov <lav@altlinux.ru> 20071224-alt1
- new version 20071224 (with rpmrb script)
- fix buffer overflow

* Sun May 06 2007 Vitaly Lipatov <lav@altlinux.ru> 20061208-alt1
- initial build for ALT Linux Sisyphus

