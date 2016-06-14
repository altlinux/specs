%def_without python
Name: cegui
Version: 0.8.4
Release: alt2.qa4
Summary: Free library providing windowing and widgets for graphics APIs / engines
Group: System/Libraries
License: MIT
Url: http://www.cegui.org.uk
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: https://bitbucket.org/cegui/cegui/get/v0-8-4.tar.gz
Source1: http://downloads.sourceforge.net/crayzedsgui/CEGUI-DOCS-%version.tar.gz

BuildRequires: SILLY-devel gcc-c++ libGLU-devel libSM-devel libexpat-devel libfreetype-devel libpcre-devel libxerces-c-devel libxml2-devel tinyxml-devel tolua++-devel tzdata libogre-devel libdirectfb-devel

BuildRequires: cmake libminizip-devel libfribidi-devel libGLEW-devel
BuildRequires: libglm-devel libirrlicht-devel libGLES-devel
BuildRequires: libdevil-devel libcorona-devel
BuildRequires: python-devel boost-devel doxygen graphviz libgtk+2-devel
BuildRequires: libglfw-devel rapidxml boost-python-devel

%if_with python
Requires: python-module-%name = %version-%release
%endif

%description
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines where such functionality is not natively available, or
severely lacking. The library is object orientated, written in C++, and
targeted at games developers who should be spending their time creating great
games, not building GUI sub-systems!

%package devel
Summary: Development files for cegui
Group: Development/C++
Requires: %name = %version-%release
Requires: libGLU-devel

%description devel
Development files for cegui

%package devel-doc
Summary: API documentation for cegui
Group: Documentation
Requires: cegui-devel = %version-%release
BuildArch: noarch

%description devel-doc
API and Falagard skinning documentation for cegui

%if_with python
%package -n python-module-%name
Group: Development/Python
Summary: python library for %name
Requires: %name = %version-%release

%description -n python-module-%name
%summary
%endif

%prep
%setup -qb1 -qn CEGUI

# Permission fixes for debuginfo RPM
#chmod -x include/falagard/*.h

# Delete zero length file
#rm -f documentation/api_reference/keepme

# Encoding fixes
iconv -f iso8859-1 AUTHORS -t utf8 > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 TODO -t utf8 > TODO.conv && mv -f TODO.conv TODO
iconv -f iso8859-1 README -t utf8 > README.conv && mv -f README.conv README

%build
%add_optflags -I%_includedir/pcre
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCEGUI_BUILD_RENDERER_NULL:BOOL=ON \
	.

%make_build VERBOSE=1

pushd doc/doxygen
doxygen
popd

%install
%makeinstall_std
find %buildroot -name '*.la' -exec rm -f {} ';'

%files
%doc README*
%_bindir/*
%_libdir/*.so.*
%_libdir/cegui-0.8

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/*
%_datadir/cegui-0
%exclude %_datadir/cegui-0/xml_schemas

%files devel-doc
%_datadir/cegui-0/xml_schemas
%doc doc/doxygen/html

%if_with python
%files -n python-module-%name
%{python_sitelibdir}/*
%endif

%changelog
* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt2.qa4
- NMU: rebuild with irrlicht
- TODO: update to a fresh version
- TODO: add python (can't add due to NEW bad_elf_symbols detected:
  /usr/lib64/python2.7/site-packages/cegui-0.8/PyCEGUIOpenGLRenderer.so
  U _ZN5CEGUI18OpenGLRenderTargetINS_12RenderTargetEED2Ev )

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8.4-alt2.qa3
- NMU: rebuilt with libGLEW.so.1.13.

* Tue Jun 09 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.4-alt2.1.1
- Rebuilt for gcc5 C++11 ABI.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.8.4-alt2.1
- rebuild with boost 1.57.0

* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt2
- Built without freeimage

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1
- Version 0.8.4

* Fri Jul 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.6-alt1.3
- Rebuild with new ogre

* Tue Dec 04 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.7.6-alt1.2
- Rebuild with new libxerces-c

* Sun May 27 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.6-alt1.1
- Rebuild with new ogre

* Fri Apr 06 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.5-alt1.2
- Removed bad RPATH

* Sun May 15 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.5-alt1.1
- Rebuild with new ogre

* Tue May 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Wed Mar 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt3
- rebuild for debuginfo

* Tue Dec 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt2
- rebuild for soname set-version

* Fri Dec 19 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1
- 0.6.2b

* Tue Dec 02 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt4
- build repaired

* Tue Nov 04 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt3
- build without libdevil

* Thu Oct 09 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt2
- noarch build for devel-doc

* Wed Oct 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon May 26 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt1
- Initial for ALT

* Sun May 18 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.0-1
- New upstream release 0.6.0
- No ABI stability, use full versioned (libtool -release) sonames
- Use system tolua++, change license tag to match
- Use system tinyxml

* Wed Feb 13 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-7
- Added patch for new xerces-c. Courtesy of Hans de Goede
- Converted some documentation to UTF8
- Minor spec cleanups

* Wed Aug 29 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-6
- Yet another release bump, for building against expat2.

* Tue Aug 21 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-5
- Release bump for F8 mass rebuild
- License change due to new guidelines

* Sat Jun 30 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-4
- Release bump

* Sun Jun 17 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-3
- rpath fixes for x86_64

* Sun Jun 10 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-2
- Added patch to fix undefined-non-weak-symbol warnings

* Wed May 30 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.5.0b-1
- Upgrade to 0.5.0b
- Added patch from Gentoo to compile with lua 5.1
- Updated the patch to use versioned .so for dlopen()
- Dropped several patches as they are no longer needed
- Dropped useless provides. Nothing used them anyway
- Added support for the SILLY image codec
- Added support for xerces-c

* Mon Aug 28 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-11
- Release bump for FC6 mass rebuild

* Sat Aug 05 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-10
- Header fix for g++ v4.1+

* Tue Jul 18 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-9
- Use versioned .so for dlopen()

* Sun Jun 11 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-8
- Updated --rpath fixes again
- Package devel-docs renamed to devel-doc as per 'new' guidelines

* Sat Jun 10 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-7.iss
- Updated --rpath fixes

* Fri Jun 09 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-6.iss
- Added patch courtesy of Hans de Goede fixing TinyXML usage
- Added patch courtest of Hans de Goede fixing 64bit issues
- Updated --rpath fixes
- Trivial correction for pkg-config BR, should be >= really and not >

* Wed Jun 07 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-5.iss
- Removed IrrlichtRender headers as we don't support it (yet - anyway)
- Removed usage of --rpath during build process
- libtool dropped as a BR (no longer needed due to --rpath fix)
- Moved rebuilding of C++ bindings to %%build section

* Mon Jun 05 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-4.iss
- Added a tentative patch for building with the system tolua++/lua
- Added tolua++-devel as a buildrequire
- Rebuild the C++ bindings using the system tolua++

* Sun May 28 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-3.iss
- Added patch courtesy of Hans de Goede to force compilation against the system
  pcre libs instead of the bundled pcre.
- Added pcre-devel to buildrequires
- Replace xorg-x11-devel with libGLU-devel
- Removed PCRE-LICENSE from doc as it's now compiled against system pcre
- Specified version for pkg-config buildrequires
- Replaced source URL with primary sf site, rather than a mirror
- Don't use bootstrap
- Added cegui_mk2 provides
- Removed superfluous documentation from devel package

* Sat May 27 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-2.iss
- Use %%{?dist} for most recent changelog entry - avoids incoherent changelog
  versions if %%{?dist} macro is missing or different.
- Added %%{version}-%%{release} to provides field
- Replaced %%{__sed} with sed

* Sun May 21 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.4.1-1.iss
- Initial Release
