Name: dwdiff
Version: 2.1.1
Release: alt1

Summary: front-end for the diff program that operates at the word level

License: OSL
Group: Text tools
Url: http://os.ghalkes.nl/dwdiff.html

Source: http://os.ghalkes.nl/dist/%name-%version.tar

# Automatically added by buildreq on Sat Nov 08 2008
BuildRequires: libicu-devel

%description
dwdiff is a front-end for the diff program that operates at the word level
instead of the line level. It is different from wdiff in that it allows the
user to specify what should be considered whitespace, and in that it takes an
optional list of characters that should be considered delimiters. Delimiters
are single characters that are treated as if they are words, even when there
is no whitespace separating them from preceding words or delimiters. dwdiff
is mostly commandline compatible with wdiff.

%prep
%setup

%build
export CC=gcc
export CXX=g++
./configure
%make_build

%install
%make_install install prefix=%buildroot/%prefix
%find_lang %name
rm -rf %buildroot%_mandir/nl*

%files -f %name.lang
%_bindir/dwdiff
%_bindir/dwfilter
%_man1dir/*
%_docdir/%name-%version/

%changelog
* Fri Jan 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt1
- Updated to upstream version 2.1.1.

* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt2
- rebuild with libicu 5.6.1

* Sun Oct 18 2015 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0 (with rpmrb script Kaluga)

* Wed Feb 26 2014 Vitaly Lipatov <lav@altlinux.ru> 2.0.9-alt1
- new version 2.0.9 (with rpmrb script)

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version 2.0.5 (with rpmrb script)

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.1
- Rebuilt with icu 5.1

* Wed Dec 14 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script)

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Tue Mar 16 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- new version (1.7) import in git

* Thu Jan 14 2010 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt1
- new version (1.6.1) 

* Tue Jan 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Sat Nov 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- new version 1.4 (with rpmrb script)
- update buildreq
- add message files

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- new version 1.3 (with rpmrb script)

* Wed Mar 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Wed Jan 25 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt0.1
- initial build for ALT Linux Sisyphus
