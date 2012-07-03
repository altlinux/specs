%add_python_req_skip feedparser

Summary: Canto is an Atom/RSS feed reader for the console
Name: canto
Version: 0.7.10
Release: alt1.1
License: GPLv2
Group: Networking/News
Source0: http://codezen.org/static/%name-%version.tar
Patch: %name-%version-alt.patch
Packager: Evgenii Terechkov <evg@altlinux.ru>
Url: http://www.codezen.org/canto
Obsoletes: nrss

# Automatically added by buildreq on Sat Jan 17 2009 (-bi)
BuildRequires: libncursesw-devel python-devel python-modules-encodings tzdata

%description
Canto is an Atom/RSS feed reader for the console that is meant to be
quick, concise, and colorful. It's meant to allow you to crank through
feeds like you've never cranked before by providing a minimal, yet
information packed interface. No navigating menus. No dense blocks of
unreadable white text. An interface with almost infinite customization
and extensibility using the excellent Python programming language.

%prep
%setup
%patch -p1

%build
python setup.py build

%install
python setup.py install --prefix=%prefix --root=%buildroot

%files
%_bindir/%{name}*
%_man1dir/%{name}*.1*
%python_sitelibdir/Canto-*.egg-info
%python_sitelibdir/%name
%python_sitelibdir/%name/widecurse.so
%python_sitelibdir/%name/*.py[co]
%doc ChangeLog INSTALL README doc/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.10-alt1.1
- Rebuild with Python-2.7

* Thu Jul 29 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.10-alt1
- 0.7.10

* Tue May 25 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.9-alt2
- git-20100525 (Issue #10)

* Tue May 25 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.9-alt1
- 0.7.9

* Sun May 23 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.8-alt2
- Drop useless require (builtin feedparser used by default)

* Thu May 20 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Wed May 19 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.7-alt3
- git-20100519

* Tue May 18 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.7-alt2
- git-20100518

* Thu May 13 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.7-alt1
- 0.7.7
- Cleanup to get pristine tar

* Thu Apr 15 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.5-alt5
- git-20100415

* Tue Feb 16 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.5-alt4
- git-20100216

* Tue Feb  2 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.5-alt3
- git-20100208

* Wed Jan 27 2010 Terechkov Evgenii <evg@altlinux.ru> 0.7.5-alt2
- git-20100127 to fix tracker issue #3

* Sat Dec 12 2009 Terechkov Evgenii <evg@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1.1
- Rebuilt with python 2.6

* Tue Aug 18 2009 Terechkov Evgenii <evg@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Mon Aug  3 2009 Terechkov Evgenii <evg@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Mon Aug  3 2009 Terechkov Evgenii <evg@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Sat Jul 25 2009 Terechkov Evgenii <evg@altlinux.ru> 0.7.0-alt1
- 0.7.0 (Beware, experimental release!)

* Wed May 13 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.13-alt1
- 0.6.13

* Wed May 13 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.12-alt1
- 0.6.12

* Thu May  7 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.11-alt1
- 0.6.11

* Sat Apr 18 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.10-alt1
- 0.6.10

* Fri Apr 17 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.9-alt2
- Cosmetic fix to canto-fetch from upstream

* Thu Apr 16 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.9-alt1
- 0.6.9

* Thu Mar 19 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.8-alt1
- 0.6.8

* Sat Mar  7 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.7-alt1
- 0.6.7

* Mon Mar  2 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Wed Feb 25 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.4-alt2
- Critical fixes from upstream git

* Tue Feb 24 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.4-alt1
- 0.6.4
- Integrate with upstream git
- Packager tag added

* Sat Jan 17 2009 Terechkov Evgenii <evg@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Sun Dec 28 2008 Terechkov Evgenii <evg@altlinux.ru> 0.5.7-alt1
- Initial build for ALT Linux Sisyphus (thanks PLD for initial spec)
