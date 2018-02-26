Name: ftpcopy
Version: 0.6.7
Release: alt1

Summary: An ftp mirroring tool
License: Free, no warranties
Group: Networking/File transfer
Url: http://www.ohse.de/uwe/%name.html

Source: http://www.ohse.de/uwe/%name/%name-%version.tar.gz

%description
%name is a simply FTP client written to copy files or directories
(recursively) from a FTP server. It's primary purpose is to mirror
FTP sites which support the EPLF directory listing format, but it
may be used to mirror other sites, too.

%prep
%setup -q -n web

%build
CFLAGS="$RPM_OPT_FLAGS" make -C %name-%version

%install
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_man1dir}
install -p -m755 %name-%version/command/* $RPM_BUILD_ROOT%_bindir
install -p -m644 %name-%version/doc/* $RPM_BUILD_ROOT%_man1dir

%files
%_bindir/*
%_mandir/man?/*
%doc %name-%version/src/{ChangeLog,INSTALL,NEWS,README,THANKS}

%changelog
* Sat Oct 23 2004 Sasha Martsinuk <scampler@altlinux.ru> 0.6.7-alt1
- 0.6.7

* Fri Nov 23 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.4.4-alt1
- 0.4.4
- ALT adaptions.

* Wed Sep 19 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.4.3-1
- 0.4.3
- rewrite specfile to adapt to the ultimately broken new build system used by
  ftpcopy

* Sun Jun 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.3.9-1
- 0.3.9

* Tue Apr 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 0.3.7-1
- 0.3.7

* Fri Jan 19 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.3.4 - fixes date mismatches in a couple of cases

* Tue Dec  5 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- update to 0.3.3 - fixes security bugs. A ftp server being mirrored could
  overwrite any files on the mirroring system by sending filenames containing
  "../"

* Wed Jul 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 0.3.0 to get man pages

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat May 12 2000 Nalin Dahyabhai <nalin@redhat.com>
- initial package
