Name: lazy
Version: 0.24d
Release: alt2

Summary: Lazy - a console-based CD player with CDDB support to display song titles
License: GPL
Group: Sound
Url: http://www.cscience.org/~lucasvr/Projects/lazy.html
Packager: Andrey Semenov <mitrofan@altlinux.ru>

Source: %name-%version.tar.bz2

%description
Lazy is a console-based CD player with freedb support.
It provides artist, album, and song name display, looking at the main
freedb-server for unrecognized songs. It can also extract audio digitally
if the CD-ROM drive does not have an analog audio cable connected to it.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall
%__mkdir %buildroot%_sysconfdir
%__cp src/lazyrc.sample %buildroot%_sysconfdir/.lazyrc

%files
%doc AUTHORS BUGS CDDB_HOWTO ChangeLog FAQ INSTALL README TODO
%_bindir/*
%_man1dir/*
%_sysconfdir/.lazyrc

%changelog
* Fri Sep 10 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.24d-alt2
- add .lazyrc file

* Mon May 3 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.24d-alt1
- 0.24c
- Fixed a bad malloc on cddb_get.c
- A few cleanups were also made
- A problem with a missing errno.h was fixed as well

* Tue Apr 29 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.24c-alt1
- 0.24c

* Tue Apr 22 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.23d-alt1
- First version of RPM package.

