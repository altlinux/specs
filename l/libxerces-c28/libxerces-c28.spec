%define oname xerces-c
%define tarname %oname-src_2_8_0

%ifarch alpha ppc64 s390x sparc64 x86_64 ia64
%define rcopts -b 64
%else
%define rcopts -b 32
%endif

# threads
# values: pthreads, none
%define threads pthreads

Name: libxerces-c28
Version: 2.8.0
Release: alt3.qa5

Summary: Xerces-C++ validating XML parser

Url: http://xml.apache.org/xerces-c/
License: Apache
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://apache.rinet.ru/dist/xerces/c/sources/%tarname.tar.bz2
Source1: %name.pc
Patch0: xerces-c-src_2_6_0-lsattr.patch
# fix lib linking
Patch1: %name.patch
Patch2: %name-gcc43.patch

Provides: xerces-c
Obsoletes: xerces-c
Conflicts: %name-utils < %version-%release

# Automatically added by buildreq on Wed Mar 09 2005
BuildRequires: gcc-c++ libstdc++-devel

%description
Xerces-C++ is a validating XML parser written in a portable subset of C++.
Xerces-C++ makes it easy to give your application the ability to read and
write XML data. A shared library is provided for parsing, generating,
manipulating, and validating XML documents.

The parser provides high performance, modularity, and scalability. Source
code, samples and API documentation are provided with the parser. For
portability, care has been taken to make minimal use of templates, no RTTI,
and minimal use of #ifdefs.

%package utils
Summary: Utils for Xerces-C++ validating XML parser
Group: File tools
Requires: %name = %version-%release
Conflicts: libxerces-c-utils

%description utils
Xerces-C++ is a validating XML parser written in a portable subset of C++.
Xerces-C++ makes it easy to give your application the ability to read and
write XML data. A shared library is provided for parsing, generating,
manipulating, and validating XML documents.

The parser provides high performance, modularity, and scalability. Source
code, samples and API documentation are provided with the parser. For
portability, care has been taken to make minimal use of templates, no RTTI,
and minimal use of #ifdefs.

This package contains utils for Xerces-C++ validating XML parser.

%package devel
Group: System/Libraries
Summary: Header files for Xerces-C++ validating XML parser
Requires: %name = %version
Provides: xerces-c-devel
Obsoletes: xerces-c-devel

%description devel
Header files you can use to develop XML applications with Xerces-C++.

Xerces-C++ is a validating XML parser written in a portable subset of C++.
Xerces-C++ makes it easy to give your application the ability to read and
write XML data. A shared library is provided for parsing, generating,
manipulating, and validating XML documents.

%package doc
Group: System/Libraries
Summary: Documentation for Xerces-C++ validating XML parser
BuildArch: noarch

%description doc
Documentation for Xerces-C++.

Xerces-C++ is a validating XML parser written in a portable subset of C++.
Xerces-C++ makes it easy to give your application the ability to read and
write XML data. A shared library is provided for parsing, generating,
manipulating, and validating XML documents.

%prep
%setup -n %tarname
%patch0 -p1
%patch1
%patch2

%build
#_configure_update_config
export XERCESCROOT=$(pwd)
cd $XERCESCROOT/src/xercesc
install -pm755 /usr/share/gnu-config/config.sub /usr/share/gnu-config/config.guess .
# in addition to the now-ineffective patch0
sed -i 's,/usr/sbin/lsattr,lsattr,' config.guess
%autoreconf
./runConfigure %rcopts -plinux -cgcc -xg++ -minmem -nsocket -tnative -r%threads -P%prefix
%make_build

cd $XERCESCROOT/samples
install -pm755 /usr/share/gnu-config/config.sub /usr/share/gnu-config/config.guess .
sed -i 's,/usr/sbin/lsattr,lsattr,' config.guess
%autoreconf
./runConfigure -plinux -cgcc -xg++
%make_build

%install
export XERCESCROOT=$(pwd)
cd $XERCESCROOT/src/xercesc
%make_install PREFIX=%buildroot%prefix install

# x86_64 hack, fix it more correctly
if [ ! -x %buildroot%_libdir ] ; then
    mv %buildroot/usr/lib %buildroot%_libdir
fi

mkdir -p %buildroot%_bindir
#we don't want obj directory
install `find $XERCESCROOT/bin -maxdepth 1 -type f` %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name
cp -a $XERCESCROOT/samples %buildroot%_datadir/%name
install -m644 -D %SOURCE1 %buildroot%_pkgconfigdir/xerces-c.pc

%files
%_libdir/libxerces-c.so.*
%_libdir/libxerces-depdom.so.*

%files devel
%_includedir/xercesc/
%_libdir/libxerces-c.so
%_libdir/libxerces-depdom.so
#dir %_datadir/%name/
#_datadir/%name/samples/
%_pkgconfigdir/xerces-c.pc

%files doc
%doc LICENSE NOTICE STATUS credits.txt Readme.html doc/

%files utils
%_bindir/*

%changelog
* Wed Feb 21 2018 Michael Shigorin <mike@altlinux.org> 2.8.0-alt3.qa5
- autoreconf
- drop useless samples (thx ldv@)

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 2.8.0-alt3.qa4
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libxerces-c28-doc

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt3.qa3
- Avoid conflict with libxerces-c
- Moved utils into utils subpackage

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt3.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.8.0-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libxerces-c28
  * postun_ldconfig for libxerces-c28
  * postclean-05-filetriggers for spec file

* Fri Dec 19 2008 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt3
- add provides/obsoletes: xerces-c(-devel)

* Tue Dec 02 2008 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt2
- fix build with gcc 4.3

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- build separate package, rename package to libxerces-c28
- enable SMP-build, add Source URL, cleanup spec
- add pkgconfig file

* Fri Nov 17 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.7.0-alt1
- new version 2.7.0

* Wed Mar 09 2005 Denis Klykvin <nikon@altlinux.ru> 2.6.0-alt1
- Spec cleanup

* Fri Jun  6 2003 Tuan Hoang <tqhoang@bigfoot.com>
- updated for new Xerces-C filename and directory format
- fixed date format in changelog section

* Fri Mar 14 2003 Tinny Ng <tng@ca.ibm.com>
- changed to 2.3

* Wed Dec 18 2002 Albert Strasheim <albert@stonethree.com>
- added symlink to libxerces-c.so in lib directory

* Fri Dec 13 2002 Albert Strasheim <albert@stonethree.com>
- added seperate doc package
- major cleanups

* Tue Sep 03 2002  <thomas@linux.de>
- fixed missing DESTDIR in Makefile.util.submodule

* Mon Sep 02 2002  <thomas@linux.de>
- Initial build.
