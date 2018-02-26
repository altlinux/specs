Name: fbset
Version: 2.1
Release: alt1
Serial: 1

Summary: Framebuffer device maintenance utilities
License: GPL
Group: System/Kernel and hardware
Url: http://users.telenet.be/geertu/Linux/fbdev/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# http://users.telenet.be/geertu/Linux/fbdev/fbset-%version.tar.gz
Source: fbset-%version.tar

Patch: fbset-%version-%release.patch

BuildRequires: flex

%description
fbset is a system utility to show or change the settings of the
frame buffer device.  The frame buffer device provides a simple and
unique interface to access different kinds of graphic displays.

%prep
%setup -q
%patch -p1

%build
make CC=gcc CFLAGS="%optflags"

%install
make install DESTDIR=%buildroot
mkdir -p %buildroot%_sbindir
ln -s ../bin/{fbset,modeline2fb} %buildroot%_sbindir/

%files
%config(noreplace) %_sysconfdir/*
%_bindir/*
%_sbindir/*
%_mandir/man?/*
%doc FAQ etc/*

%changelog
* Wed Jan 24 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.1-alt1
- Imported fixes and enhancements from Debian fbset_2.1-19.diff
- Packaged con2fbmap, moved utils to %_bindir.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 2.1-ipl9mdk
- Rebuilt in new environment.

* Mon Apr 15 2002 Dmitry V. Levin <ldv@altlinux.org> 2.1-ipl8mdk
- Rebuilt.

* Thu Jan 18 2001 Dmitry V. Levin <ldv@fandra.org> 2.1-ipl7mdk
- RE adaptions.

* Wed Feb 23 2000 Dmitry V. Levin <ldv@fandra.org>
- added modeline2fb utility.

* Wed Aug 16 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Sun Jul 18 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 2.1
- handle RPM_OPT_FLAGS

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- include fb devs too (#1515)
- update to 19990118 version.

* Thu Nov  5 1998 Jeff Johnson <jbj@redhat.com>
- import from ultrapenguin 1.1.
- upgrade to 19981104.

* Thu Oct 29 1998 Jakub Jelinek <jj@ultra.linux.cz>
- new package
