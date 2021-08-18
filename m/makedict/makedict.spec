Name: makedict
Version: 0.4.1_beta1
Release: alt5.git.ga70119

Summary: XDXF based converter from any dictionary format to any

Group: System/Libraries
License: GPLv2
Url: http://xdxf.sf.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/soshial/xdxf_makedict.git
Source: %name-%version.tar

# Automatically added by buildreq on Fri May 31 2013
# optimized out: cmake-modules libstdc++-devel pkg-config
BuildRequires: cmake ctest discount gcc-c++ glib2-devel libexpat-devel zlib-devel

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-tools

%description
XDXF based converter from any dictionary format to any.

%prep
%setup
%__subst "s|lib/makedict-codecs|share/makedict-codecs|g" CMakeLists.txt
find -type f -name '*.py' -exec python3-2to3 -w -n '{}' +
%__subst "s|/usr/bin/env python\$|/usr/bin/env python3|" src/*.py

%build
cmake -DCMAKE_INSTALL_PREFIX:=%prefix \
	-DBUILD_TESTS:=true \

%make_build
markdown -o  format_standard/xdxf_description.html \
			format_standard/xdxf_description.md

%install
%makeinstall_std

%check
make test

%files
%doc AUTHORS CHANGELOG README* TODO format_standard/
%_bindir/%name
%_datadir/makedict-codecs/
%_man1dir/*

%changelog
* Wed Aug 18 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4.1_beta1-alt5.git.ga70119
- switch to python3

* Mon May 17 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4.1_beta1-alt4.git.ga70119
- add BR: rpm-build-python

* Tue Feb 11 2020 Vitaly Lipatov <lav@altlinux.ru> 0.4.1_beta1-alt3.git.ga70119
- use python2

* Thu Jan 29 2015 Ildar Mulyukov <ildar@altlinux.ru> 0.4.1_beta1-alt2.git.ga70119
- new upstream source

* Fri May 31 2013 Ildar Mulyukov <ildar@altlinux.ru> 0.4.1_beta1-alt1.git.146f2f
- new upstream source

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt4svn.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt4svn.1
- Rebuilt with python 2.6

* Sat Nov 22 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt4svn
- move ext. codecs to datadir (fix build on x86_64)

* Sun Nov 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt3svn
- svn revision 93

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2svn
- fix install path for codecs
- add interpreter for mdparser.py

* Fri Dec 14 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1svn
- build SVN release 82 (fix bug #13599)
- use cmake now, update buildreqs, cleanup spec

* Fri Jun 15 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- fix codecs install

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt0.1
- initial build for ALT Linux Sisyphus
