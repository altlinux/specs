Name: pinfo
Version: 0.6.10
Release: alt2

Summary: Przemek's Info Viewer - a (much) better info
Group: System/Base
License: GPL
#Url: http://dione.ids.pl/~pborys/software/pinfo
#Url: http://pinfo.alioth.debian.org/
Url: https://github.com/baszoetekouw/pinfo
Source: %name-%version.tar.gz
Patch1: pinfo-0.6.10-alt.patch
Patch2: pinfo-0.6.10-xz.patch

Requires: url_handler

# Automatically added by buildreq on Wed Jan 17 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-mips libncurses-devel libtinfo-devel perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl python-base xz
BuildRequires: libncursesw-devel makeinfo

%description
Hypertext info file viewer. User interface similar to lynx.
It is based on ncurses. It can handle now as well info
pages as man pages. Regexp searching included.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure --disable-rpath
%make_build

%install
mkdir -p %buildroot/{%_sysconfdir,%_bindir,%_mandir/man1}
%make_install DESTDIR=%buildroot install
%find_lang %name

ln -s %name %buildroot%_bindir/pman

%files -f %name.lang
%doc ABOUT-NLS AUTHORS ChangeLog* NEWS README*
%config(noreplace) %_sysconfdir/%{name}rc
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*

%changelog
* Wed Jan 17 2018 Fr. Br. George <george@altlinux.ru> 0.6.10-alt2
- Optimizing buildreq

* Fri Oct 13 2017 Fr. Br. George <george@altlinux.ru> 0.6.10-alt1
- Upstream switch to GH
- Freshen (version is 0.6.10 sitll)
- Provide .xz recognition

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.9-alt3.qa1.1
- NMU: added BR: texinfo

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.9-alt3.qa1
- NMU: rebuilt for debuginfo.

* Thu Apr 23 2009 Afanasov Dmitry <ender@altlinux.org> 0.6.9-alt3
- alt changes patch:
  + incorporate debian fix_segfault patch.

* Thu Apr 23 2009 Afanasov Dmitry <ender@altlinux.org> 0.6.9-alt2
- build against ncursesw (fixes: #16407, #19732).
- remove obsolete install info's scripts.
- generate cumulative alt-changes patch
  + fix ncursesw detection in macros/curses.m4.
  + disable autopoint calling in the right way.
  + incorporate alt-url_handler patch.
- minor spec changes:
  + use %buildroot; use %make_install.
  + build with autoreconf.

* Fri May 19 2006 Stanislav Ievlev <inger@altlinux.org> 0.6.9-alt1
- 0.6.9, build from git

* Fri Mar 10 2006 Stanislav Ievlev <inger@altlinux.org> 0.6.8-alt3
- fixed build

* Tue Mar 23 2004 Stanislav Ievlev <inger@altlinux.org> 0.6.8-alt2
- use url_handler to process ftp and http requests (#1032)

* Mon Oct 27 2003 Stanislav Ievlev <inger@altlinux.org> 0.6.8-alt1
- 0.6.8

* Fri May 16 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.7-alt1.1
- fix package group

* Wed Mar 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.7-alt1
- 0.6.7

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 0.6.6p1-alt2
- rebuild with gcc3

* Fri Aug 16 2002 Stanislav Ievlev <inger@altlinux.ru> 0.6.6p1-alt1
- 0.6.6p1, readopt and rename patches

* Tue Jan 08 2002 Stanislav Ievlev <inger@altlinux.ru> 0.6.4-alt3
- fixed tmpdir patch.

* Thu Jan 03 2002 Stanislav Ievlev <inger@altlinux.ru> 0.6.4-alt2
- added normal support for tmpdir using.
- close bug #0000275.

* Fri Dec 07 2001 Stanislav Ievlev <inger@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Fri Nov 16 2001 Stanislav Ievlev <inger@altlinux.ru> 0.6.3-alt2
- fix charsets

* Thu Jul 26 2001 Stanislav Ievlev <inger@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Fri Jul 06 2001 Stanislav Ievlev <inger@altlinux.ru> 0.6.1-alt2
- Small corrections.

* Fri Jun 22 2001 Stanislav Ievlev <inger@altlinux.ru> 0.6.1-alt1
- 0.6.1. Spec corrections

* Sat Feb 3 2001 AEN <aen@logic.ru>
- RE adaptation
* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.6.0-2mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Francis Galiegue <fg@mandrakesoft.com> 0.6.0-1mdk

- 0.6.0
- BMacros

* Thu Mar 16 2000 Francis Galiegue <francis@mandrakesoft.com> 0.5.9-2mdk

- Spec file changes
- Changed group to match 7.1 specs
- now there's pman, too
- Let spec-helper do its job

* Fri Feb 18 2000 Francis Galiegue <francis@mandrakesoft.com> 0.5.9-1mdk
- First Mandrake RPM
