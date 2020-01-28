Name:       getmail
Version:    5.14
Release:    alt1

Summary:    POP3 mail retriever with reliable Maildir delivery
License:    GPL
Group:      Networking/Mail
Url:        http://pyropus.ca/software/getmail

BuildArch:  noarch

Source:     %name-%version.tar.gz
Patch0:     port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

Summary(ru_RU.KOI8-R): Выкачивание почты по POP3 с надежной доставкой в Maildir
Summary(uk_UA.KOI8-U): Витягування пошти за POP3 ╕з над╕йним постачанням до Maildir


%description
getmail is intended as a simple replacement for fetchmail for those people
who do not need its various and sundry configuration options, complexities,
and bugs.  It retrieves mail from one or more POP3 servers for one or more
email accounts, and reliably delivers into a Maildir specified on a
per-account basis.  It can also deliver into mbox files, although this
should not be attempted over NFS.  getmail is written entirely in python.

%description -l ru_RU.KOI8-R
getmail предназначен быть простой заменой fetchmail для тех, кому не нужны
разнообразные опции, сложности и ошибки.  Способен забирать почту с одного или
нескольких POP3-серверов и надежно доставлять в Maildir; возможна доставка в
mbox, но не поверх NFS.  Написан на Python.

%description -l uk_UA.KOI8-U
getmail ма╓ бути простою зам╕ною fetchmail для тих, кому не потр╕бн╕
р╕зноман╕тн╕ опц╕╖, складнощ╕ та помилки.  Здатен забирати пошту з одного чи
к╕лькох POP3-сервер╕в й над╕йно поставляти до Maildir; можливе й використання
mbox, але не по NFS.  Написаний на Python.

%prep -q
%setup
%patch0 -p2

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install --optimize=2

pushd docs
mv CHANGELOG THANKS COPYING BUGS TODO ../
popd

%files
%doc COPYING docs/
%doc %_man1dir/*
%_bindir/*
%python3_sitelibdir/*


%changelog
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
