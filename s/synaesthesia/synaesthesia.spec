Name: synaesthesia
Version: 2.4
Release: alt1

Summary: This program visualizes audio input
License: GPL
Group: Sound

Url: http://www.logarithmic.net/pfh-files/synaesthesia
Source: %url/%name-%version.tar.gz

# Automatically added by buildreq on Mon Jun 26 2006
BuildRequires: esound-devel gcc-c++ libSDL-devel

%description
This is a program for representing sounds visually.  It goes beyond
the usual oscilliscope style program by combining an FFT and stereo
positioning information to give a two dimensional display.

%prep
%setup -q

%build
%configure --disable-rpath
%make

%install
%makeinstall

%files
%doc README
%_bindir/*

%changelog
* Mon Jun 26 2006 Michael Shigorin <mike@altlinux.org> 2.4-alt1
- 2.4
- built for ALT Linux
- spec based on Mandriva's
- buildreq'ed

* Mon May  9 2005 Götz Waschk <waschk@mandriva.org> 2.3-1mdk
- drop the patch
- New release 2.3

* Wed Jun 30 2004 Michael Scherer <misc@mandrake.org> 2.2-2mdk
- rebuild for new gcc ( patch 0 )
- rpmbuildupdate aware
- update Url
- correct BuildRequires

* Mon Jul 28 2003 Götz Waschk <waschk@linux-mandrake.com> 2.2-1mdk
- new version

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.1-10mdk
- rebuild

* Fri Aug 16 2002 Götz Waschk <waschk@linux-mandrake.com> 2.1-9mdk
- gcc 3.2-0.3mdk build

* Mon Jul 29 2002 Götz Waschk <waschk@linux-mandrake.com> 2.1-8mdk
- gcc 3.2 build

* Fri Jul 12 2002 Götz Waschk <waschk@linux-mandrake.com> 2.1-7mdk
- rebuild to remove svgalib dependancy

* Mon May 06 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.1-6mdk
- rebuild against new alsa

* Tue Sep 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.1-5mdk
- rebuild
- update requires/buildrequires

* Mon Feb 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.1-4mdk
- used srpm from Götz Waschk <waschk@linux-mandrake.com> :
	- fixed library requirements again

* Tue Jan 30 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.1-3mdk
- added url

* Thu Jan 18 2001  Lenny Cartier <lenny@mandrakesoft.com> 2.1-2mdk
- updated by Götz Waschk <waschk@linux-mandrake.com> :
	- fixed library requirements

* Thu Oct 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.1-1mdk
- used srpm from Götz Waschk :
	Tue Oct  3 2000 Götz Waschk <waschk@linux-mandrake.com> 2.1-1mdk
	- initial Mandrake build
