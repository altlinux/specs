Name:       getmail
Version:    6.20.01
Release:    alt1

Summary:    Mail retriever with Maildir/mbox delivery
License:    GPL-2.0 AND Apache-2.0
Group:      Networking/Mail
Url:        https://getmail6.org
Vcs:        https://github.com/getmail6/getmail6.git

BuildArch:  noarch

Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

Provides: getmail6 = %EVR

Summary(ru_RU.UTF-8): Получение почты по POP3/IMAP с доставкой в Maildir

%description
getmail6 is a flexible, extensible mail retrieval system with support
for POP3, IMAP4, SSL variants of both, maildirs, mboxrd files, external
MDAs, arbitrary message filtering, single-user and domain mailboxes.

It is a Python 3 fork of getmail 5.14, intended as a simple replacement
for fetchmail.

%description -l ru_RU.UTF-8
getmail6 — гибкая система получения почты с поддержкой POP3, IMAP4,
их SSL-вариантов, Maildir, mbox, внешних MDA и фильтрации сообщений.

Это форк getmail 5.14 для Python 3, простая замена fetchmail.

%prep
%setup

%build
%python3_build

%install
%python3_install --optimize=2
# setup.py dumps docs under %%_datadir/doc/getmail; ship them via %%doc
rm -rf %buildroot%_datadir/doc

%files
%doc README docs/COPYING docs/CHANGELOG docs/THANKS docs/BUGS docs/HACKING docs/getmailrc-examples
%_bindir/*
%_man1dir/*
%python3_sitelibdir/*

%changelog
* Sun Sep 06 2026 Anton Farygin <rider@altlinux.org> 6.20.01-alt1
- 6.20.01 (switch to getmail6, Python 3 fork of getmail 5.14) (Closes: #48791)

* Tue Jan 28 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.14-alt1
- Version updated to 5.14
- porting on python3.

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.46.0-alt1
- Version 4.46.0

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.43.0-alt1
- Version 4.43.0

* Fri Jun 21 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.41.0-alt1
- Version 4.41.0

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.37.0-alt1
- Version 4.37.0

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.34.0-alt1
- Version 4.34.0

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.24.0-alt1
- Version 4.24.0

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.23.0-alt1
- Version 4.23.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.20.0-alt1.1
- Rebuild with Python-2.7

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.20.0-alt1
- Version 4.20.0

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7.6-alt1.1.1
- Rebuilt with python 2.6

* Sat Feb 02 2008 Grigory Batalov <bga@altlinux.ru> 4.7.6-alt1.1
- Rebuilt with python-2.5.

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 4.7.6-alt1
- 4.7.6 release.

* Tue Jun 12 2007 Pavlov Konstantin <thresh@altlinux.ru> 4.7.5-alt1
- 4.7.5 release.
- Removed macro abuse.

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 4.7.4-alt1
- 4.7.4 release.

* Sat Mar 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 4.7.3-alt1
- 4.7.3 release.

* Sun Mar 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 4.7.2-alt1
- 4.7.2 release.

* Fri Jan 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 4.6.7-alt1
- 4.6.7 release.

* Thu Dec 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 4.6.6-alt1
- 4.6.6 release.

* Thu Oct 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 4.6.4-alt1
- 4.6.4 release.

* Mon Jul 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 4.6.3-alt1
- 4.6.3 release.
- Added packager: field.

* Fri Jun 02 2006 Pavlov Konstantin <thresh@altlinux.ru> 4.6.1-alt1
- 4.6.1 release.

* Tue Mar 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 4.5.4-alt1
- 4.5.4 release.

* Thu Feb 09 2006 Pavlov Konstantin <thresh@altlinux.ru> 4.5.3-alt1
- 4.5.3 release.

* Sat Jan 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 4.4.4-alt1
- 4.4.4 release.

* Mon Dec 05 2005 Pavlov Konstantin <thresh@altlinux.ru> 4.4.3-alt1
- 4.4.3 release.

* Tue Jul 19 2005 Pavlov Konstantin <thresh@altlinux.ru> 4.3.11-alt1
- 4.3.11 release.

* Sat Jun 11 2005 Pavlov Konstantin <thresh@altlinux.ru> 4.3.10-alt1
- 4.3.10 release
- python-modules-compiler buildreq added. (Should it be there?)

* Fri Mar 25 2005 Pavlov Konstantin <thresh@altlinux.ru> 4.3.4-alt1
- 4.3.4 release

* Fri Mar 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 4.3.3-alt1
- 4.3.3 release 

* Thu Jan 20 2005 Pavlov Konstantin <thresh@altlinux.ru> 4.3.1-alt1
- 4.3.1 release

* Sat Sep 25 2004 Michael Shigorin <mike@altlinux.ru> 4.2.0-alt1
- 4.2.0 (security fixes included)

* Tue Mar 23 2004 Michael Shigorin <mike@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Sun Mar 07 2004 Michael Shigorin <mike@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Tue Oct 07 2003 Michael Shigorin <mike@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Fri Aug 22 2003 Michael Shigorin <mike@altlinux.ru> 3.1.8-alt1
- 3.1.8
- spec cleanup

* Thu Oct 03 2002 Michael Shigorin <mike@altlinux.ru> 2.3.9-alt1
- built for ALT Linux
- python22 is used (though code should work with 1.5.2)

* Thu Jul 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.3.9-1mdk
- 2.3.9
