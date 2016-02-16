Name: mk-configure
Version: 0.29.1
Release: alt1

Summary: Lightweight replacement for GNU autotools
License: BSD
Group: Development/Tools

Url: http://sourceforge.net/projects/mk-configure/
# Source: http://prdownloads.sf.net/%name/%name-%version.tar
Source: %name-%version.tar.bz2
Packager: Aleksey Cheusov <cheusov@altlinux.org>

BuildArch: noarch

Requires:      bmake bmkdep
BuildRequires: bmake binutils

# required for tests
BuildRequires: flex bison gcc-c++ glib2-devel groff-base zlib-devel bmkdep
BuildRequires: perl-podlators perl-devel liblua5-devel info-install makeinfo m4

%description
mk-configure is a lightweight replacement for GNU autotools, written in
bmake (portable version of NetBSD make), POSIX shell and POSIX utilities.

%prep
%setup

%define env \
  unset MAKEFLAGS; \
  export PREFIX=%prefix MANDIR=%_mandir SYSCONFDIR=%_sysconfdir

# examples are built and tested either,
# let's keep a pristine copy
cp -al examples doc

%build
%env
bmake all

%install
%env
bmake install DESTDIR=%buildroot
rm -rf %buildroot%_docdir/%name

%check
unset MAKEFLAGS
# lua tests expect correct lua.pc
export NOSUBDIR='lua_dirs hello_lua hello_lua2 hello_lua3 hello_reqd'
# hello_libdeps was already fixed in upstream, for now we skip it too
export NOSUBDIR="$NOSUBDIR examples/hello_libdeps"
# /sbin/install-info
export PATH=/sbin:$PATH
bmake test

%files
%doc doc/FAQ doc/LICENSE doc/NEWS doc/NOTES README presentation/presentation.pdf
%doc doc/examples/
%_bindir/*
%_datadir/mk-configure/
%_datadir/mkc-mk/
%_man1dir/*
%_man7dir/*

%changelog
* Tue Feb 16 2016 Michael Shigorin <mike@altlinux.org> 0.29.1-alt1
- new version 0.29.1

* Sat Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 0.28.0-alt5
- Fix .gear/rules

* Sat Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 0.28.0-alt4
- Remove bad requirement "install"

* Sat Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 0.28.0-alt3
- Make hasher(1) happy

* Thu Nov 27 2014 Aleksey Cheusov <cheusov@altlinux.org> 0.28.0-alt2
- 0.28.0-alt2

* Thu Nov 27 2014 Aleksey Cheusov <vle@gmx.net> 0.28.0-alt1
- 0.28.0

* Mon Mar 11 2013 Michael Shigorin <mike@altlinux.org> 0.24.0-alt1
- 0.24.0

* Sun Mar 10 2013 Michael Shigorin <mike@altlinux.org> 0.23.0-alt2
- fixed build (thx upstream)

* Fri Sep 07 2012 Michael Shigorin <mike@altlinux.org> 0.23.0-alt1
- 0.23.0

* Tue Dec 27 2011 Michael Shigorin <mike@altlinux.org> 0.21.2-alt5
- tweak examples so that they're built as well but packaged pristine

* Mon Dec 26 2011 Michael Shigorin <mike@altlinux.org> 0.21.2-alt4
- don't install just-built examples as docs

* Sat Dec 24 2011 Michael Shigorin <mike@altlinux.org> 0.21.2-alt3
- further spec cleanup
- check fixup (thx upstream)
- extended BR: properly

* Mon Nov 21 2011 Michael Shigorin <mike@altlinux.org> 0.21.2-alt2
- dropped MKCATPAGES (thx upstream)

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.21.2-alt1
- 0.21.2
- minor spec cleanup

* Tue Jun 29 2010 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt4
- add check section

* Fri Jun 25 2010 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt3
- disable examples build

* Thu Jun 24 2010 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt2
- fix install, disable lua test, enable all tests
- update buildreqs

* Fri Jun 18 2010 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt1
- new version 0.16.0 (with rpmrb script)

* Tue Nov 17 2009 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version 0.12.0 (with rpmrb script)

* Wed Jul 29 2009 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt3
- build for Sisyphus

* Thu Jul 23 2009 Aleksey Cheusov <vle@gmx.net> 0.10.0-alt2
- Not it depends on pkgsrc-mk-files, fixes and clean-ups

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- initial build for ALT Linux Sisyphus
