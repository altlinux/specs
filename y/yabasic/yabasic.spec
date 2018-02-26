Name: yabasic
Version: 2.763
Release: alt3

Summary: Small basic interpreter with printing and graphics

License: Public Domain
Group: Development/Other
Url: http://www.yabasic.de/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.yabasic.de/download/%name-%version.tar.bz2
Patch: %name-make.patch

# manually removed: xorg-cf-files
# Automatically added by buildreq on Wed Oct 22 2008
BuildRequires: imake libXt-devel libncurses-devel

BuildPreReq: bison flex

%description
Yabasic implements the most common and simple elements of the basic
langugage; It comes with for-loops and goto with while-loops and
procedures. Yabasic does monochrome line grafics, printing comes with
no extra effort. Yabasic runs under Unix and Windows; it is small
(less than 200KB) and free.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure --with-x
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README *.htm
%_bindir/%name
%_man1dir/*

%changelog
* Wed Mar 10 2010 Vitaly Lipatov <lav@altlinux.ru> 2.763-alt3
- add autoreconf, migrate to git

* Wed Oct 22 2008 Vitaly Lipatov <lav@altlinux.ru> 2.763-alt2
- update buildreq

* Tue Jan 22 2008 Vitaly Lipatov <lav@altlinux.ru> 2.763-alt1
- "Yabasic has probably reached its final Version 2.763"
- cleanup spec, update buildreqs

* Sun Oct 16 2005 Vitaly Lipatov <lav@altlinux.ru> 2.763-alt0.1
- new version

* Sun Oct 16 2005 Vitaly Lipatov <lav@altlinux.ru> 2.751-alt0.1
- new version
- spec from PLD Team <feedback@pld-linux.org>
