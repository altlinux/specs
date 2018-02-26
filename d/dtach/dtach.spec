Name: dtach
Version: 0.8
Release: alt1

Summary: A simple program that emulates the detach feature of screen
Group: System/Base
License: GPL
Url: http://dtach.sourceforge.net/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz

%description
dtach is a program that emulates the detach feature of screen, with
less overhead. It is designed to be transparent and un-intrusive; it
avoids interpreting the input and output between attached terminals
and the program under its control. Consequently, it works best with
full-screen applications such as emacs.

%prep
%setup -q

%build
%configure
%make_build

%install
%__mkdir -p %buildroot%_bindir
%__mkdir -p %buildroot%_man1dir
%__install -m 755 %name %buildroot%_bindir
%__install -m 644 %name.1 %buildroot%_man1dir

%files
%doc COPYING README
%_bindir/%name
%_man1dir/%name.*

%changelog
* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8-alt1
- 0.8

* Wed Oct 26 2005 Andrei Bulava <abulava@altlinux.ru> 0.7-alt1
- initial build for ALT Linux

* Sat Jul 3 2004 Ned T. Crigler <crigler@users.sourceforge.net> 0.7
- New release

* Fri Nov 30 2001 Ned T. Crigler <crigler@hell-city.org> 0.5
- Fix fd leakage.
- Prevent atexit from being called twice on dtach -A.

* Fri Nov 30 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.4-1
- s/Copyright/License/
- Minor description change
- fix use of %%doc
- Add full location of source tarball

* Sat Nov 03 2001 Ned T. Crigler <crigler@hell-city.org> 0.4
- Portability updates thanks to sourceforge's compile farm. dtach should now
  work on: FreeBSD, Debian/alpha, Debian/PPC, Debian/sparc, Debian/PPC, and
  Solaris.

* Thu Sep 27 2001 Ned T. Crigler <crigler@hell-city.org>
- Modified spec file URL: to point to http://dtach.sourceforge.net

* Wed Sep 26 2001 Ned T. Crigler <crigler@hell-city.org> 0.3
- Use getrlimit and dynamically allocate the data structures, if possible.
- Added some more autoconf checks.
- Initial sourceforge release.

* Thu Sep 20 2001 Ned T. Crigler <crigler@hell-city.org>
- Changed the master to send a stream of text to attaching clients instead
  of sending a huge packet all the time.
- Decreased the client <-> master packet size.
- Changed the attach code so that it tells the master when a suspend occurs.

* Tue Sep 18 2001 Ned T. Crigler <crigler@hell-city.org>
- Fixed a typo in dtach.1

* Tue Sep 18 2001 Ned T. Crigler <crigler@hell-city.org> 0.2
- Removed silly thinko regarding terminal settings in attach, we
  always set the terminal to raw mode now.
- Moved redraw code into the master, which tries to be smarter when
  using ^L.
- Moved the code that obtains the current terminal settings into main,
  preventing a race condition between the master and attach processes.
- Rewrote argument parsing code.
- Changed name to dtach.
- Added a man page.

* Mon Sep 17 2001 Ned T. Crigler <crigler@hell-city.org>
- Changed fchmod to chmod in create_socket.

* Mon Sep 17 2001 Isaiah Weiner <iweiner@redhat.com>
- Modified spec file to correct detach binary permissions
- Modified spec file to correct detach documentation path
- Modified spec file URL: to point to http://people.redhat.com/iweiner/detach
- Modified spec file %clean to remove buildroot and builddir.

* Mon Sep 17 2001 Ned T. Crigler <crigler@hell-city.org> 0.1
- Initial rpm release.
