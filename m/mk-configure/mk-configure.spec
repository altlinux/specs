Name: mk-configure
Version: 0.21.2
Release: alt5

Summary: Lightweight replacement for GNU autotools
License: BSD
Group: Development/Tools

Url: http://sourceforge.net/projects/mk-configure/
Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2
Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Automatically added by buildreq on Thu Jun 24 2010
BuildRequires: bmake flex gcc-c++ glib2-devel groff-base zlib-devel
BuildRequires: perl-podlators perl-devel

%description
mk-configure is a lightweight replacement for GNU autotools, written in
bmake (portable version of NetBSD make), POSIX shell and POSIX utilities.

%prep
%setup

%define env \
unset MAKEFLAGS \
export PREFIX=%prefix \
export MANDIR=%_mandir

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
# FIXME: https://bugzilla.altlinux.org/show_bug.cgi?id=26566
# PREFIX=/usr/local	# this one to be fixed upstream
unset MAKEFLAGS
env NOSUBDIR='lua_dirs hello_lua hello_lua2 hello_reqd' bmake test

%files
%doc ChangeLog NEWS README TODO doc/presentation.pdf
%doc doc/examples/
%_bindir/*
%_datadir/mk-configure/
%_datadir/mkc-mk/
%_man1dir/*
%_man7dir/*

%changelog
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
