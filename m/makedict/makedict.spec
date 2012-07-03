Name: makedict
Version: 0.4
Release: alt4svn.1.1

Summary: XDXF based converter from any dictionary format to any

Group: System/Libraries
License: GPL
Url: http://xdxf.sf.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/xdxf/%name-%version.tar.bz2
Patch: %name-0.4.patch

# Automatically added by buildreq on Fri Dec 14 2007
BuildRequires: cmake gcc-c++ glib2-devel libexpat-devel zlib-devel

%description
XDXF based converter from any dictionary format to any.

%prep
%setup -q
%patch
%__subst "s|lib/makedict-codecs|share/makedict-codecs|g" CMakeLists.txt

%build
cmake -DCMAKE_INSTALL_PREFIX:=%prefix
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README TODO ChangeLog
%_bindir/%name
%_datadir/makedict-codecs/
%_man1dir/*

%changelog
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
