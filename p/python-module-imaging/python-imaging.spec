Version: 1.1.7
Release: alt7
%setup_python_module imaging
Summary: Python's own image processing library
Name: python-module-imaging
Source0: http://www.pythonware.com/downloads/%modulename-%version.tar.gz
# wget -r -np -nH http://effbot.org/imagingbook/index.html
Source1: imaging-doc.tar
Packager: Fr. Br. George <george@altlinux.ru>
License: Distributable
Group: Development/Python
Url: http://www.pythonware.com/products/pil/
Icon: linux-python-paint-icon.xpm

Patch0: python-imaging-tk.patch
Patch1: python-imaging-1.1.4-ft.patch
Patch2: python-imaging-giftrans.patch
Patch3: python-imaging-1.1.6-sane-types.patch
# buffer overflow patch, bz 703212
Patch5: python-imaging-buffer.patch

Provides: python-imaging = %version-%release
Obsoletes: python-imaging <= 1.1.4-alt6
BuildRequires: python-modules-tkinter zlib-devel
BuildRequires: libfreetype-devel libjpeg-devel liblcms-devel libpng-devel tk-devel

%description
Python Imaging Library version %version

The Python Imaging Library (PIL) adds image processing capabilities
to your Python interpreter.

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

%package qt
Summary: Qt interface for python-imaging
Group: Development/Python
Requires: %name = %version-%release

%description qt
Python Imaging Library version %version

The Python Imaging Library (PIL) adds image processing capabilities
to your Python interpreter.

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

This package contains Qt interface for python-imaging.

%package devel
Summary: Developers files for python-imaging
Group: Development/Python
BuildArch: noarch

%description devel
Python Imaging Library version %version

The Python Imaging Library (PIL) adds image processing capabilities
to your Python interpreter.

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

Developers files for python-imaging

%package doc
Summary: Documentation and examples for python-imaging
Group: Development/Documentation
BuildArch: noarch

%description doc
Python Imaging Library version %version

The Python Imaging Library (PIL) adds image processing capabilities
to your Python interpreter.

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

Documentation and examples for python-imaging

%prep
%setup -n %modulename-%version -a1
# %patch -p0
# %patch1 -p1
%patch2 -p1
%patch3 -p1 -b .sane-types
%patch5 -p1 -b .buffer

find -type f |xargs fgrep -l /usr/local |
	xargs -r perl -pi -e 's|/usr/local|/usr|g'
rm PIL/ImageGL.py

%build
%python_build build_ext -i
python selftest.py

#python setup.py build

%install
%python_build_install --optimize=2 --record=INSTALLED_FILES

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/buildreqs/files/ignore.d \
	$RPM_BUILD_ROOT%_includedir/python%_python_version

install -p  libImaging/Im*.h $RPM_BUILD_ROOT%_includedir/python%_python_version
install -p -m644 PIL.pth $RPM_BUILD_ROOT%_libdir/python%_python_version/site-packages

cat > $RPM_BUILD_ROOT%_sysconfdir/buildreqs/files/ignore.d/%name << EOF
^/usr/lib/python[^/]*/site-packages/PIL$
EOF

%add_python_lib_path  %_libdir/python%_python_version/site-packages/PIL

%files -f INSTALLED_FILES
%exclude %python_sitelibdir/PIL/ImageQt.py*
%doc  CHANGES CONTENTS
%config %_sysconfdir/buildreqs/files/ignore.d/%name

%files qt
%python_sitelibdir/PIL/ImageQt.py*

%files devel
%_includedir/python%_python_version/Im*.h

%files doc
%doc imagingbook Scripts Images Sane Docs

%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt7
- Fixed build

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.7-alt6
- added patches from fedora

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.7-alt5.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt5
- Rebuilt for debuginfo

* Thu Oct 21 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.7-alt4
- Dropped redundant manual package requirements.
- Updated build requirements.

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt3
- Fixed underlinking

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt2
- Set devel and doc packages as noarch

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt1
- Version 1.1.7
- Moved PIL/ImageQt.py into separate package (ALT #23008)

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt3.1
- Rebuilt with python 2.6

* Sat Jun 06 2009 Alexey Morsov <swi@altlinux.ru> 1.1.6-alt3
- remove PIL.pth from -devel package and include 
  in main package

* Wed Sep 03 2008 Alexey Morsov <swi@altlinux.ru> 1.1.6-alt2
- fixed bug #16194

* Sun May 25 2008 Fr. Br. George <george@altlinux.ru> 1.1.6-alt1
- Version up
- Handbook updated

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.1.4-alt11.1
- Rebuilt with python-2.5.

* Sat Mar 12 2005 Andrey Orlov <cray@altlinux.ru> 1.1.4-alt11
- Rebuild with python2.4

* Thu Dec 09 2004 Andrey Orlov <cray@altlinux.ru> 1.1.4-alt10
- Provide python-imaging added

* Tue Nov 16 2004 Andrey Orlov <cray@altlinux.ru> 1.1.4-alt9
- Some problem with new freetype library fixed

* Fri Jun 18 2004 Andrey Orlov <cray@altlinux.ru> 1.1.4-alt8
- Add PIL directory in search path (because of PIL.pth)

* Tue May 18 2004 Andrey Orlov <cray@altlinux.ru> 1.1.4-alt7
- Rebuild with new python policy

* Wed Apr 14 2004 Gennady Kovalev <gik@altlinux.ru> 1.1.4-alt6
- Fix installing _imagingft.so library

* Sun Nov 30 2003 Andrey Orlov <cray@altlinux.ru> 1.1.4-alt5
- Try to build on py23

* Thu Nov 20 2003 Andrey Orlov <cray@altlinux.ru> 1.1.4-alt4
- Fix build requires and test on python223

* Tue Oct 07 2003 Andrey Orlov <cray@altlinux.ru> 1.1.4-alt3
- Fix build requires: add tcl & tk devel

* Mon May 19 2003 Andrey Orlov <cray@altlinux.ru> 1.1.4-alt2
- Add some fixes of spec-file

* Sun May 18 2003 Andrey Orlov <cray@altlinux.ru> 1.1.4-alt1
- Rebuild package for new version

* Tue Feb 12 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.2-alt4
- Added buildreq filter

* Mon Jan 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.2-alt3
- rebuild with new python

* Wed Jun 27 2001 AEN <aen@logic.ru> 1.1.2-alt2
- some header-files added

* Wed Jun 27 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.2-alt1
- 1.1.2. Rebuilt with python-2.1

* Sun Dec 10 2000 Dmitry V. Levin <ldv@fandra.org> 1.1-ipl4mdk
- Fix out /usr/local.
- Fix building for python version != 1.5.
- Fix Requires.
- Automatically added BuildRequires.

* Wed Nov 29 2000 AEN <aen@logic.ru> 1.1-ipl3mdk
- rebuild for RE
- patch to find-req

* Tue Sep 19 2000 David BAUDENS <baudens@mandrakesoft.com> 1.1-2mdk
- Fix FredL's typo

* Wed Sep 13 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.1-1mdk
- 1.1

* Thu Mar 30 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0b1-3mdk
- group fix.

* Mon Jan 10 2000 Lenny Cartier <lenny@mandrakesoft.com>
- build for oxygen
- deactivate provinding of tkinter lib since Chmouel one's works perfectly

* Mon Dec 27 1999 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- bz2 archive

* Mon Jan 11 1999 Oliver Andrich <oli@andrich.net>
- upgraded to Imaging 1.0b1

* Sun Dec 27 1998 Oliver Andrich <oli@andrich.net>
- changed Setup file so that the tkinter module is compiled with Tix and BLT
  support

* Mon Jul 20 1998 Oliver Andrich <oli@andrich.net>
- had to recompile and update the package to support the uptodate graphics
  libs

* Sat Jun 07 1998 Oliver Andrich <oli@andrich.net>
- updated package to version 0.3a4
