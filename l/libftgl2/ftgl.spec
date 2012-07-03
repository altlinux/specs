%define oname libftgl
Name: %{oname}2
Version: 2.2.0
Release: alt8.svn20110521
Summary: OpenGL frontend to Freetype 2

Group: System/Libraries
License: LGPLv2
Url: http://ftgl.wiki.sourceforge.net/
# https://ftgl.svn.sourceforge.net/svnroot/ftgl/trunk/
Source0: %name-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Automatically added by buildreq on Sun Aug 23 2009
BuildRequires: ImageMagick-tools cppunit-devel doxygen gcc-c++
BuildPreReq: libGL-devel libICE-devel libX11-devel libGLUT-devel
#BuildPreReq: libfreetype-devel texlive-extra-utils texlive-fonts-recommended
BuildPreReq: libfreetype-devel zlib-devel

Provides: %{oname}220 = %version-%release
Conflicts: libftgl213

%description
FTGL is a free open source library to enable developers to use arbitrary
fonts in their OpenGL (www.opengl.org)  applications.
Unlike other OpenGL font libraries FTGL uses standard font file formats
so doesn't need a preprocessing step to convert the high quality font data
into a lesser quality, proprietary format.
FTGL uses the Freetype (www.freetype.org) font library to open and 'decode'
the fonts. It then takes that output and stores it in a format most
efficient for OpenGL rendering.

%package -n %oname-devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Requires: pkgconfig
Requires: libfreetype-devel
Provides: ftgl-devel = %version
Provides: libftgl220-devel = %version-%release
Conflicts: libftgl213-devel

%description -n %oname-devel
The %oname-devel package contains libraries and header files for
developing applications that use %oname.

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description docs
This package contains documentation files for %oname.

%prep
%setup

ln -s %_datadir/libtool/libltdl/aclocal.m4 ./

%build
touch msvc/Makefile.in
%autoreconf
#./autogen.sh
%configure \
  --enable-shared \
  --disable-static \
  --with-gl-inc=%_includedir \
  --with-gl-lib=%_libdir \
  --with-glut-inc=%_includedir \
  --with-glut-lib=%_libdir \
  --with-x

sed -i 's/~rc[0-9]*//' ftgl.pc

%make_build all

%install
%makeinstall_std
find %buildroot -name '*.la' -exec rm -f {} ';'

install -p -m644 src/*.h %buildroot%_includedir/FTGL

# Doc fixes
mkdir -p __doc/html
install -pm 0644 %buildroot%_datadir/doc/ftgl/html/* __doc/html
rm -rf %buildroot%_datadir/doc

%files
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%_libdir/*.so.*

%files -n %oname-devel
%_includedir/FTGL/
%_libdir/*.so
%_libdir/pkgconfig/*

%files docs
%doc __doc/*

%changelog
* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt8.svn20110521
- Fixed build

* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt7.svn20110521
- Rebuilt with libtool_2.4

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt6.svn20110521
- New snapshot

* Wed Aug 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt6
- Fixed build

* Sun May 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt5
- Added necessary headers

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt4
- Disabled PDF generation

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt3
- Renamed libftgl220 -> libftgl2

* Thu Mar 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2
- Tuned unnecessary conflicts

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Tue Dec 14 2010 Fr. Br. George <george@altlinux.ru> 2.1.3-alt2
- Rebuild with set-versioned

* Sun Aug 23 2009 Fr. Br. George <george@altlinux.ru> 2.1.3-alt1
- Initial build from FC

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.2.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 kwizart < kwizart at gmail.com > - 2.1.3-0.1.rc5
- Update to 2.1.3-rc5
- Obsoletes -utils sub-package

* Fri Feb 27 2009 kwizart < kwizart at gmail.com > - 2.1.2-10
- Switch from freefont to dejavu-sans-fonts - #480455

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  9 2008 kwizart < kwizart at gmail.com > - 2.1.2-8
- Rebuild for gcc43

* Sat Dec 15 2007 kwizart < kwizart at gmail.com > - 2.1.2-7
- Add -docs to fix multiarch conflicts  #341191
- Fix libGL requirement.
- Project Moved to sourceforge

* Sun Aug 26 2007 kwizart < kwizart at gmail.com > - 2.1.2-6
- rebuild for ppc32
- Update the license field

* Sat Jul 14 2007 kwizart < kwizart at gmail.com > - 2.1.2-5
- Fix version field the whole package

* Fri Jul 13 2007 kwizart < kwizart at gmail.com > - 2.1.2-4
- Modified ftgl-2.1.2-pc_req.patch
- Add Requires freefont to -utils

* Fri Jul 13 2007 kwizart < kwizart at gmail.com > - 2.1.2-3
- Add Requirements for -devel
- Preserve timestramp for install step
- Add ftgl-utils to prevent conflict with multilibs
  Add patch to prevent rpath

* Mon May 28 2007 kwizart < kwizart at gmail.com > - 2.1.2-2
- Add ftgl.pc patch
- Add BR freeglut-devel
- Remove unneeded LDFLAGS
- Cleaned spec file

* Mon May 14 2007 kwizart < kwizart at gmail.com > - 2.1.2-1
- Initial package for Fedora
