%define video_format pal

Name: dvdauthor
Version: 0.7.2
Release: alt1

Summary: set of tools to author a DVD
Group: Video
License: GPLv2
Url: http://sourceforge.net/projects/dvdauthor/

Source: http://downloads.sourceforge.net/%name/%name-%version.tar.gz
Provides: /etc/%name.conf

BuildRequires: libImageMagick-devel libdvdread-devel libfreetype-devel
BuildRequires: fontconfig-devel libpng-devel libxml2-devel libfribidi-devel

%description
dvdauthor is a program that will generate a DVD movie from a valid
mpeg2 stream that should play when you put it in a DVD player.

%prep
%setup -n %name

%build
%autoreconf
%configure --enable-default-video-format=%video_format
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir
touch %buildroot%_sysconfdir/%name.conf

%files
%_bindir/%name
%_bindir/dvddirdel
%_bindir/dvdunauthor
%_bindir/mpeg2desc
%_bindir/spumux
%_bindir/spuunmux
%_mandir/man?/*
%doc README TODO ChangeLog
%config(noreplace) %_sysconfdir/%name.conf
%_datadir/%name

%changelog
* Tue Feb 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.1
- Rebuilt with libpng15

* Sat Sep 01 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sat Oct 30 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.0-alt1
- 0.7.0

* Tue Oct 05 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.18-alt1
- 0.6.18

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.14-alt1.2
- rebuild with libdvdread.so.4

* Sat Dec 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.14-alt1.1
- Automated rebuild with libImageMagick-6.4.x.

* Tue Jan 22 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.6.14-alt1
- 0.6.14
- Update BuildRequires

* Tue May 23 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.12-alt2.2.1
- Rebuild with libMagick++.so.10.0.2 .

* Thu Sep 15 2005 Anton Farygin <rider@altlinux.ru> 0.6.12-alt2.2
- rebuild with libMagick.so.9

* Mon Sep 12 2005 Anton Farygin <rider@altlinux.ru> 0.6.12-alt2.1
- NMU: rebuild with new libImageMagick

* Wed Mar 09 2005 Alex Yustasov <yust@altlinux.ru> 0.6.12-alt2
- 0.6.12-alpha-2992

* Sun Feb 27 2005 Alex Yustasov <yust@altlinux.ru> 0.6.12-alt1
- 0.6.12-alpha-2979

* Thu Feb 17 2005 Alex Yustasov <yust@altlinux.ru> 0.6.11-alt1
- uptated to 0.6.11

* Sat Jan 15 2005 Alex Yustasov <yust@altlinux.ru> 0.6.10-alt2
- fixed build with gcc3.4

* Mon Dec 13 2004 Alex Yustasov <yust@altlinux.ru> 0.6.10-alt1
- initial release

