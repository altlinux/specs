%define oname libqwt
Name: %{oname}6
Version: 6.0.1
Release: alt3

Summary: 2D plotting widget extension to the Qt GUI

License: LGPL
Group: System/Libraries
Url: http://sourceforge.net/projects/qwt

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://qwt.svn.sourceforge.net/svnroot/qwt/trunk/qwt
Source: qwt-%version.tar.bz2

Patch1: qwt-6.0.1-qwtconfig.pri.patch

#Provides: %oname = %version-%release

# Automatically added by buildreq on Tue Jul 21 2009
BuildRequires: gcc-c++ libqt4-devel libXext-devel doxygen graphviz

%description
Qwt is an extension to the Qt GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

%package qt4-designer-plugin
Summary: Qwt plugin for qt4-designer
Group: Development/KDE and QT
Requires: %name = %version-%release
Conflicts: %name < %version-%release
Conflicts: %oname %{oname}5_3

%description qt4-designer-plugin
Qwt is an extension to the Qt GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

This package contains Qwt plugin for qt4-designer

%package devel
Summary: Development tools for programs which uses Qwt Widget set
Group: Development/C
#Provides: %oname-devel = %version-%release
Requires: %name = %version-%release
Conflicts: %oname-devel %{oname}5_3-devel

%description devel
The libqwt-devel package contains the header files and libraries
necessary for developing programs using the Qwt Widget set

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt package.

%package devel-doc
Summary: Documentation and examples for Qwt Widget set
Group: Development/Documentation
BuildArch: noarch
Conflicts: %oname-devel-doc %oname-devel %{oname}5_3-devel %{oname}5_3-devel-doc

%description devel-doc
This package contains development documentation and examples for Qwt
Widget set.

%prep
%setup

%patch1 -p0

sed -i "s|/lib|/%_lib|g" qwtconfig.pri
find . -type f -name '*.pro' |while read f; do
echo 'QMAKE_CXXFLAGS += %optflags' >> $f
done

%build
export QTDIR=%_qt4dir
export PATH=$QTDIR/bin:$PATH
qmake qwt.pro

# incompatible with SMP build
%make

pushd doc
doxygen
popd

%install
%make_install install INSTALL_ROOT=%buildroot

# man absent in 6.0.1
#install -d %buildroot%_man3dir
#install -m644 doc/man/man3/* %buildroot%_man3dir

# clean up the example tree
(cd examples; make distclean)
(cd examples; rm -f .*.cache */.*.cache */*/.*.cache)
(cd examples; rm -rf Makefile */moc */obj */*/moc */*/obj)

#install -d %buildroot%_qt4dir
#mv %buildroot%prefix/plugins %buildroot%_qt4dir/
#install -d %buildroot%_includedir/qwt
#mv %buildroot%_includedir/*.h %buildroot%_includedir/qwt/
#mv %buildroot%prefix/features/* %buildroot%_includedir/qwt/

%files
%doc CHANGES README COPYING
%_libdir/libqwt.so.*
%_libdir/libqwtmathml.so.*
%exclude %prefix/doc

%files qt4-designer-plugin
%dir %_qt4dir/plugins/designer
%_qt4dir/plugins/designer/*.so

%files devel
%_includedir/qwt
%_libdir/libqwt.so
%_libdir/libqwtmathml.so

%files devel-doc
%doc doc/html
%doc examples
#_man3dir/*

%changelog
* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.0.1-alt3
- rebuild with rpm optflags

* Thu Jan 12 2012 Sergey Y. Afonin <asy@altlinux.ru> 6.0.1-alt2
- fixed paths in qwtconfig.pri (ALT #26800/c#7)

* Wed Jan 11 2012 Sergey Y. Afonin <asy@altlinux.ru> 6.0.1-alt1
- Version 6.0.1

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt1.svn20101008.1
- Rebuilt for debuginfo

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt1.svn20101008
- New snapshot
- Fixed underlinking of libraries

* Wed Jun 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt1.svn20100626
- New snapshot

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt1.svn20100307
- Version 6.0.0

* Tue Oct 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.0-alt2.svn20091002
- New snapshot
- Avoided conflict with Trilinos documentation

* Wed Sep 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.0-alt2.svn20090920
- Renamed devel package
- Moved qt4-designer plugin into separate package

* Fri Sep 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.0-alt1.svn20090920
- Soname changed

* Fri Sep 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3.0-alt1.svn20090920
- Version 5.3.0
- Extracted documentation into separate package

* Thu Jul 23 2009 Vitaly Lipatov <lav@altlinux.ru> 5.2.0-alt2
- build for Sisyphus

* Wed Jul 22 2009 Michael Shigorin <mike@altlinux.org> 5.2.0-alt1
- new version 5.2.0 (with rpmrb script) (closes: #20844)
- updated patch
- buildreq

* Wed Jun 18 2008 Vitaly Lipatov <lav@altlinux.ru> 5.1.1-alt1
- new version 5.1.1 (with rpmrb script) - fix #14854

* Thu May 15 2008 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- new version 5.1.0 (with rpmrb script)

* Thu Aug 02 2007 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt2
- fix build on x86_64

* Tue Jul 31 2007 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt1
- new version 5.0.2 (with rpmrb script)
- build with QT4, fix install process
- disable man for API, use html version

* Sun Jun 18 2006 Vitaly Lipatov <lav@altlinux.ru> 5.0-alt0.1
- new version (snapshot 20060130)

* Sat Jul 30 2005 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt4
- fix bug #7496 (pseudo unexpanded macros)

* Tue Mar 01 2005 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt3
- move include to %_includedir

* Fri Feb 11 2005 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt2
- move libraries to %_libdir, fix .so placement

* Fri Dec 03 2004 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt1
- first build for ALT Linux Sisyphus

* Mon Oct 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-3mdk
- rebuild against new libpng

* Mon Aug 20 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-2mdk
- rebuild

* Tue Jan 26 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-1mdk
- added by Stefano Borini <munehiro@ferrara.linux.it> :
	- First RPM release

