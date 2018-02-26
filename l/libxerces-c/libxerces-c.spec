%define oname xerces-c
%define tarname %oname-3.0.0

%ifarch alpha ppc64 s390x sparc64 x86_64 ia64
%define rcopts -b 64
%else
%define rcopts -b 32
%endif

# threads
# values: pthreads, none
%define threads pthreads

Name: libxerces-c
Version: 3.0.1
Release: alt1.qa4

Summary: Xerces-C++ validating XML parser

Url: http://xml.apache.org/xerces-c/
License: Apache
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://apache.rinet.ru/dist/xerces/c/3/sources/%tarname.tar.bz2
#Source1: %name.pc
#Patch0: xerces-c-src_2_6_0-lsattr.patch
# fix lib linking
#Patch1: %name.patch

# Automatically added by buildreq on Wed Mar 09 2005
BuildRequires: gcc-c++ libstdc++-devel

#Conflicts: xerces-c
#Conflicts: libxerces-c28
Conflicts: %name-utils < %version-%release

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
Conflicts: libxerces-c28-utils

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
Provides: xerces-c-devel = %version
Conflicts: libxerces-c28-devel
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
Provides: xerces-c-doc = %version
Obsoletes: xerces-c-doc
Conflicts: libxerces-c28-doc

%description doc
Documentation for Xerces-C++.

Xerces-C++ is a validating XML parser written in a portable subset of C++.
Xerces-C++ makes it easy to give your application the ability to read and
write XML data. A shared library is provided for parsing, generating,
manipulating, and validating XML documents.

%prep
%setup -q -n %tarname

%build
%configure --disable-static --enable-transcoder-iconv
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

# x86_64 hack, fix it more correctly
#if [ ! -x %buildroot%_libdir ] ; then
#    mv %buildroot/usr/lib %buildroot%_libdir
#fi

#mkdir -p %buildroot%_bindir
#we don't want obj directory
#install `find $XERCESCROOT/bin -maxdepth 1 -type f` %buildroot%_bindir
#mkdir -p %buildroot%_datadir/%name
#cp -a samples %buildroot%_datadir/%name

rm -f %buildroot%_libdir/%name.a

%files
%_libdir/libxerces-c-3.0.so
#%_libdir/libxerces-depdom.so.*

%files devel
%_includedir/xercesc/
%_libdir/libxerces-c.so
#%_libdir/libxerces-depdom.so
#%dir %_datadir/%name/
#%_datadir/%name/samples/
%_pkgconfigdir/xerces-c.pc

%files doc
%doc LICENSE NOTICE CREDITS doc/

%files utils
%_bindir/*

%changelog
* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.qa4
- Avoid conflict with libxerces-c28
- Moved utils into utils subpackage

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.qa3
- Removed bad RPATH

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.qa2
- Rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Sep 23 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- new version 3.0.1 (with rpmrb script) (bug #21587)

* Sat Jan 10 2009 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt2
- fix conflicts/obsoletes (bug #18469)

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version 3.0.0 (with rpmrb script)
- cleanup spec, update buildreq

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
