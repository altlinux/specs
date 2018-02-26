Name: xmessage
Version: 1.0.3
Release: alt1
Summary: display a message or query in a window
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libXaw-devel xorg-util-macros

%description
The  xmessage  program  displays a window containing a message from the
command line, a file, or standard input.  Along the lower edge  of  the
message  is  row  of  buttons; clicking the left mouse button on any of
these buttons will cause xmessage to exit.  Which button was pressed is
returned  in  the  exit status and, optionally, by writing the label of
the button to standard output.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_sysconfdir/X11/app-defaults/*
%_bindir/*
%_man1dir/*

%changelog
* Sat Jan 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Nov 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- rebuild with libXaw.so.7

* Fri Aug 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Thu Nov 24 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial release

