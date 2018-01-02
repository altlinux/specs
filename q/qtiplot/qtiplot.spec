#Determint whether to use system-wide liborigin or builtin
%def_with liborigin
%def_with new_sip

Name: qtiplot
Version: 0.9.8.9
Release: alt6.svn20120124

Summary: WYSIWYG tool to make two- and three-dimensional plots of scientific data
Group: Sciences/Other
License: GPL
Url: http://soft.proindependent.com/%name.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%define pkgdocdir %_docdir/%name-%version

# http://svn.berlios.de/svnroot/repos/qtiplot/trunk
Source: %name-%version.tar.bz2
Source1: %name.xml
Source2: %name.png
Source3: %name.desktop
Source4: faq.html
Source5: help.html
Source6: colormaps.tar.gz
Source7: %{name}_ru.ts
Source8: build.conf

Patch3: %name-0.9.7.8-alt-docbook_stylesheet.patch
Patch5: %name-0.9.7.8-alt-boostincludes.patch
Patch6: %name-0.9.7.8-alt-sip_kludge.patch
# based on Debian sipFTBFS.patch
Patch7: %name-0.9.8.9-alt-sipFTBFS.patch
# based on Debian 11_ftbfs-gcc-6.cpp
Patch8: %name-0.9.8.9-alt-gcc6.patch
Patch9: %name-0.9.8.9-alt-gcc6_indents.patch
Patch10: %name-0.9.8.9-debian-gsl2.patch
# https://bugs.gentoo.org/609280#c1
Patch11: %name-0.9.8.9-gentoo-sip-4.19.patch

BuildPreReq: texlive-latex-extra

# Automatically added by buildreq on Sun Feb 03 2008
BuildRequires: gcc-c++ libgsl-devel libmuparser-devel libqt4-devel
BuildRequires: python-module-PyQt4-devel python-module-sip-devel
BuildRequires: docbook-utils docbook-style-dsssl dblatex boost-devel
BuildRequires: doxygen boost-datetime-devel libpng-devel
BuildRequires: desktop-file-utils shared-mime-info >= 0.15-alt2
BuildRequires: libqtexengine-devel
%if_with liborigin
BuildRequires: liborigin2-devel
%endif
%if_with new_sip
BuildRequires: python-module-sip-devel >= 4.7.9
%endif
BuildRequires: python-modules-multiprocessing libqt4-assistant-devel

Requires: %name-data = %version-%release
Requires: %name-manual-html = %version-%release

Provides: python%_python_version(qti)

%description
qtiplot is a program for scientific data visualizing. It can produce
two- and three-dimensional graphics and diagrams and export them to
various graphics formats. It also can make some kind of data processing.

%package data
Summary: Data files for QtiPlot
Group: Sciences/Other
BuildArch: noarch
Requires: %name = %version-%release

%description data
qtiplot is a program for scientific data visualizing. It can produce
two- and three-dimensional graphics and diagrams and export them to
various graphics formats. It also can make some kind of data processing.

This package contains data files for QtiPlot.

%package -n %name-manual-html

Summary: Manual for QtiPlot program
Group: Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description -n %name-manual-html
This package contains manual for QtiPlot, the program for scientific
data manipulation and visualization. The manual is in HTML format.

Requires: %name
Obsoletes: %name-manual
Conflicts: %name-manual

%package -n %name-manual-pdf

Summary: Manual for QtiPlot program
Group: Documentation
BuildArch: noarch

%description -n %name-manual-pdf
This package contains manual for QtiPlot, the program for scientific
data manipulation and visualization. The manual is in PDF format.

Requires: %name
Obsoletes: %name-manual
Conflicts: %name-manual

%prep
%setup

%patch3 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p0

subst "s/lupdate/lupdate-qt4/;s/lrelease/lrelease-qt4/;\
s/#system(lupdate/system(lupdate/;s/#system(lrelease/system(lrelease/" \
	%name/%name.pro
sed -i "s|/usr/local|%_libdir|" %name/%name.pro
sed -i "s|/lib|/%_lib|g" 3rdparty/qwt/qwtconfig.pri
sed -i 's|@VERSION@|%version|' qtiplot/qtiplot.pro

find . -type f -name '*.pro' | while read FILE; do
    echo "QMAKE_CXXFLAGS_RELEASE = %optflags -fno-strict-aliasing" >> "$FILE"
    echo "QMAKE_CFLAGS_RELEASE = %optflags -fno-strict-aliasing" >> "$FILE"; done
#cp -f %SOURCE7 %name/translations/

install -m644 %SOURCE8 .

%build
mkdir -p tmp/qtiplot
export QTI_ROOT=$PWD
qmake-qt4 %name.pro
%make

pushd qtiplot/translations
%_qt4dir/bin/lrelease *.ts
popd

%install
make install INSTALL_ROOT=%buildroot
install -pD -m644 %SOURCE2 %buildroot%_niconsdir/%name.png
mkdir -p %buildroot%_pixmapsdir
ln -s %_niconsdir/%name.png %buildroot%_pixmapsdir/%name.png

install -pD -m644 %SOURCE3 %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_datadir/%name/translations
cp %name/translations/*.qm %buildroot%_datadir/%name/translations

mkdir -p %buildroot%pkgdocdir/manual
install -pD -m644 {%SOURCE4,%SOURCE5} %buildroot%pkgdocdir
mkdir -p %buildroot%_man1dir
install -pD -m644 %name.1 %buildroot%_man1dir

tar xzvf %SOURCE6 -C $RPM_BUILD_ROOT%_datadir/%name

#mv -f %buildroot%_docdir/%name/manual %buildroot%pkgdocdir/
install -p -m644 manual/%name-manual-en.pdf %buildroot%pkgdocdir/manual

install -pD -m644 %SOURCE1  %buildroot%_datadir/mime/packages/%name.xml

install -d %buildroot%_bindir
install -m755 %name/%name %buildroot%_bindir
install -m644 %name/qti*.py %name/*.txt %buildroot%_libdir/%name
chmod 644 %buildroot%_libdir/%name/*.txt

%ifarch x86_64
install -d %buildroot%_libdir/%name/plugins
mv %buildroot%_libexecdir/%name/plugins/* \
	%buildroot%_libdir/%name/plugins/
%endif

%files
%dir %_datadir/%name
%dir %pkgdocdir
%dir %pkgdocdir/manual
%pkgdocdir/*.html
%_bindir/*
%_niconsdir/*
%dir %_libdir/%name
%_libdir/%name/plugins
%_libdir/%name/*.py
%_libdir/%name/*.pyc
%_libdir/%name/*.txt
%_pixmapsdir/*
%_desktopdir/*
%_man1dir/*
%_datadir/mime/packages/*
%exclude %_includedir
%exclude %_libdir/*.a
%exclude %_libdir/%name/*.pyo
%exclude %_libdir/%name/qtiplot_remote_ctl.py*
%exclude %_docdir/%name
%exclude %prefix/src

%files data
%_datadir/%name/*

%files -n %name-manual-html
%pkgdocdir/manual/html

%files -n %name-manual-pdf
%pkgdocdir/manual/*.pdf

%changelog
* Tue Jan 02 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.8.9-alt6.svn20120124
- Fixed FTBFS.

* Tue Aug 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.8.9-alt5.svn20120124
- Rebuilt with new libgsl.

* Mon Jan 30 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.8.9-alt4.svn20120124
- Fixed build with gcc6

* Mon Aug 01 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.8.9-alt3.svn20120124
- Fix build

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.9-alt2.svn20120124
- Rebuilt with libpng15

* Wed Jan 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.9-alt1.svn20120124
- New snapshot

* Sat Dec 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.9-alt1.svn20111212
- Version 0.9.8.9

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8.5-alt1.svn20110411.1
- Rebuild with Python-2.7

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.5-alt1.svn20110411
- Version 0.9.8.5 (ALT #25428)

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.4-alt1.svn20101119.3
- Rebuilt for debuginfo

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.4-alt1.svn20101119.2
- Rebuilt with Boost 1.46.1

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.4-alt1.svn20101119.1
- Rebuilt for soname set-versions

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.4-alt1.svn20101119
-  Version 0.9.8.4

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.svn20100719.1
- Fixed for gcc 4.5.1

* Fri Jul 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.svn20100719
- Version 0.9.8
- Rebuilt with Qt 4.7

* Mon Mar 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.12-alt1.svn20100301
- Version 0.9.7.12

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.10-alt1.svn20091104.1
- Rebuilt with python 2.6

* Thu Nov 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.10-alt1.svn20091104
- Fixed crash on deleting directory (ALT #22144), thnx mutabor@
- New snapshot

* Fri Oct 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.10-alt1.svn20091021.1
- Added missing translation files (ALT #22013)

* Thu Oct 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.10-alt1.svn20091021
- Version 0.9.7.10 (ALT #22013)

* Wed Sep 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.9-alt3.svn20090923
- New snapshot
- Built with embedded libqwtplot3d & libqwt (external libraries has
  different API)

* Thu Sep 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.9-alt2
- Rebuilt with external liborigin2
- Moved architecture independent data files into separate package
- Clean spec

* Tue Sep 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7.9-alt1
- Version 0.9.7.9 (ALT #20200)
- Temporarily fixed build with embedded libraries libqwt & liborigin
  (awaiting updates in Sisyphus)

* Tue Jul 21 2009 Michael Shigorin <mike@altlinux.org> 0.9.7.8-alt0.1
- NMU: 0.9.7.8 (closes: #20200)
  + updated patches
  + rediffed patch1 (ah, Gentoo has more full version)
  + dropped patch6 (just hurts now)
  + added patch8 (hm, should bundled qwtplot3d get built anyways?)
  + added patch9 (#elif instead of #else, hmmm)
  + merged patch5 into patch7 (were overlapping by now)
  + renamed the rest of patches according to ALT specfile conventions
- dropped deprecated macros

* Wed Dec 31 2008 Yury Aliaev <mutabor@altlinux.org> 0.9.7.4-alt1
- new version
- new sip behaviour fix (now it doesn't perform types substitution)
  (ifdef'ed for sipmler backporting)

* Wed Oct 01 2008 Yury Aliaev <mutabor@altlinux.org> 0.9.7.2-alt1
- new version

* Wed Oct 01 2008 Yury Aliaev <mutabor@altlinux.ru> 0.9.7.2-alt2
- 0.9.7.2
- reverted to use built-in liborigin

* Tue Aug 05 2008 Yury Aliaev <mutabor@altlinux.ru> 0.9.7-alt1
- 0.9.7
- fixes and cleanups by repocop warnings (.desktop, .spec)
- QtiPlot project mime type added
- pdf manual is now built from the main sources

* Tue May 27 2008 Yury Aliaev <mutabor@altlinux.ru> 0.9.6.2-alt1
- 0.9.6.2

* Wed May 21 2008 Yury Aliaev <mutabor@altlinux.ru> 0.9.6-alt2.5
- warning about undefined symbols in fitRational.so.1.0.0 fixed

* Wed May 21 2008 Yury Aliaev <mutabor@altlinux.ru> 0.9.6-alt2
- x86_64 build fixed

* Fri May 16 2008 Yury Aliaev <mutabor@altlinux.ru> 0.9.6-alt1
- 0.9.6
- manuals are now built from the same source package

* Wed Feb 13 2008 Grigory Batalov <bga@altlinux.ru> 0.9.2-alt1.1
- Rebuilt with python-2.5.

* Sun Feb 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- NMU: new version 0.9.2
- cleanup spec, update buildreq

* Tue May 1 2007 Yury Aliaev <mutabor@altlinux.ru> 0.8.9-alt2
- Python scripting enabled

* Sat Apr 7 2007 Yury Aliaev <mutabor@altlinux.ru> 0.8.9-alt1
- 0.8.9
- manual now becomes a separate package (qtiplot-manual)
- adjusted desktop/menu issue

* Thu Nov 23 2006 Yury Aliaev <mutabor@altlinux.ru> 0.8.8-alt1
- 0.8.8
- Python scripting disabled for a while
- Russian translation updated

* Sat Jun 10 2006 Yury Aliaev <mutabor@altlinux.ru> 0.8.5-alt2
- Ooops! Fixed translation installation path
- Russian translation updated (although so far from completeness and quality...)
- Some spec cleanups

* Wed May 29 2006 Yury Aliaev <mutabor@altlinux.ru> 0.8.5-alt1
- 0.8.5
- Russian localization added
- Now works with liborigin installed in the system
- Manual added and packed in the separate package, qtiplot-manual

* Sat Dec 24 2005 Yury Aliaev <mutabor@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Sat Apr 10 2005 Yury Aliaev <mutabor@altlinux.ru> 0.5.8.3-alt1
- initial release, spec created
