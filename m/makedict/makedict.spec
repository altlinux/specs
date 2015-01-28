Name: makedict
Version: 0.4.1_beta1
Release: alt2.git.ga70119

Summary: XDXF based converter from any dictionary format to any

Group: System/Libraries
License: GPL2
Url: http://xdxf.sf.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# from git://github.com/soshial/xdxf_makedict.git
Source: %name.tar

# Automatically added by buildreq on Fri May 31 2013
# optimized out: cmake-modules libstdc++-devel pkg-config
BuildRequires: cmake ctest discount gcc-c++ glib2-devel libexpat-devel zlib-devel

%description
XDXF based converter from any dictionary format to any.

%prep
%setup -n %name
%__subst "s|lib/makedict-codecs|share/makedict-codecs|g" CMakeLists.txt

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
