# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/ccache boost-devel boost-python-devel cmake gcc-c++ glib2-devel libGL-devel libGLES-devel libSDL2-devel libSDL2_image-devel libatk-devel libcairo-devel libgtk+2-devel libminizip-devel libpango-devel pkgconfig(CEGUI-0-IRRLICHT) pkgconfig(tinyxml2) python-devel rpm-build-python
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           cegui
Version:        0.8.7
Release:        alt3_7
Summary:        Free library providing windowing and widgets for graphics APIs / engines
Group:          System/Libraries
License:        MIT
URL:            http://www.cegui.org.uk
Source0:        http://downloads.sourceforge.net/crayzedsgui/cegui-%{version}.tar.bz2
Patch0:         cegui-0.8.4-lua53.patch
Patch1:         cegui-0.8.7-alt-gcc7.patch

BuildRequires:  libdevil-devel
BuildRequires:  libfreeimage-devel
BuildRequires:  libexpat-devel
BuildRequires:  libfreetype-devel > 2.0.0
BuildRequires:  libxml2-devel
BuildRequires:  libICE-devel
BuildRequires:  libglm-devel
BuildRequires:  libGLU-devel
BuildRequires:  libtool-common
BuildRequires:  libSM-devel
BuildRequires:  lua-devel >= 0.5.2
BuildRequires:  libpcre-devel libpcrecpp-devel
BuildRequires:  SILLY-devel
BuildRequires:  libxerces-c-devel
BuildRequires:  tolua++-devel >= 1.0.93
BuildRequires:  tinyxml-devel
BuildRequires:  libGLEW-devel
BuildRequires:  libogre-devel >= 1.7.0
BuildRequires:  libois-devel
BuildRequires:  libirrlicht-devel >= 1.8
BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
# We no longer build a python subpackage as the python bindings are
# broken when building with gcc6 / boost-1.60 and no-one uses them
Obsoletes:      %{name}-python < %{version}-%{release}
Source44: import.info

%description
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines where such functionality is not natively available, or
severely lacking. The library is object orientated, written in C++, and
targeted at games developers who should be spending their time creating great
games, not building GUI sub-systems!


%package devel
Summary:        Development files for cegui
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       cegui = %{version}-%{release}
Requires:       %{name}-freeimage-imagecodec = %{version}-%{release}
Requires:       cegui = %{version}-%{release}
Requires:       cegui = %{version}-%{release}
Requires:       cegui = %{version}-%{release}
Requires:       cegui = %{version}-%{release}
Requires:       cegui = %{version}-%{release}
Requires:       cegui = %{version}-%{release}

%description devel
Development files for cegui


%package devel-doc
Summary:        API documentation for cegui
Group:          Documentation
Requires:       cegui = %{version}-%{release}
BuildArch:      noarch

%description devel-doc
API and Falagard skinning documentation for cegui


%package samples
Group: System/Libraries
Summary:        Executable samples provided with the library
Requires:       cegui = %{version}-%{release}

%description samples
Several interactive sample programs demonstrating functionality of
the CEGUI library.


%package DevIL-imagecodec
Summary:        Alternative imagecodec library for CEGUI using DevIL
Group:          System/Libraries
Requires:       cegui = %{version}-%{release}

%description DevIL-imagecodec
Alternative imagecodec library for CEGUI using DevIL.


%package freeimage-imagecodec
Summary:        Alternative imagecodec library for CEGUI using freeimage
Group:          System/Libraries
Requires:       cegui = %{version}-%{release}

%description freeimage-imagecodec
Alternative imagecodec library for CEGUI using freeimage.


%package irrlicht-renderer
Summary:        Irrlicht renderer for CEGUI
Group:          System/Libraries
Requires:       cegui = %{version}-%{release}

%description irrlicht-renderer
Irrlicht renderer for CEGUI.


%package ogre-renderer
Summary:        OGRE renderer for CEGUI
Group:          System/Libraries
Requires:       cegui = %{version}-%{release}

%description ogre-renderer
OGRE renderer for CEGUI.


%package null-renderer
Summary:        Null renderer for CEGUI
Group:          System/Libraries
Requires:       cegui = %{version}-%{release}

%description null-renderer
Null renderer for CEGUI. Useful for headless deployments or unit testing.


%package libxml-xmlparser
Summary:        Alternative xml parsing library for CEGUI using libxml
Group:          System/Libraries
Requires:       cegui = %{version}-%{release}

%description libxml-xmlparser
Alternative xml parsing library for CEGUI using libxml.


%package tinyxml-xmlparser
Summary:        Alternative xml parsing library for CEGUI using tinyxml
Group:          System/Libraries
Requires:       cegui = %{version}-%{release}

%description tinyxml-xmlparser
Alternative xml parsing library for CEGUI using tinyxml.


%package xerces-xmlparser
Summary:        Alternative xml parsing library for CEGUI using xerces
Group:          System/Libraries
Requires:       cegui = %{version}-%{release}

%description xerces-xmlparser
Alternative xml parsing library for CEGUI using xerces.


%prep
%setup -q
%patch0 -p1
%patch1 -p2
find -name "*.orig" -exec rm -f {} ';'


%build
%{fedora_cmake} \
-D CMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
-D CEGUI_BUILD_RENDERER_DIRECTFB=false \
-D CEGUI_BUILD_IMAGECODEC_STB=false \
-D CEGUI_BUILD_IMAGECODEC_TGA=false \
-D CEGUI_BUILD_PYTHON_MODULES=false \
-D CEGUI_OPTION_DEFAULT_XMLPARSER=ExpatParser \
-D CEGUI_OPTION_DEFAULT_IMAGECODEC=SILLYImageCodec \
-D CEGUI_BUILD_RENDERER_NULL=true \
-D CEGUI_BUILD_TESTS=true \
.

%make_build
make html %{?_smp_mflags}


#%check
# CEGUITests is in $BUILDDIR/bin, datafiles are in $BUILDDIR/datafiles
#CEGUI_SAMPLE_DATAPATH=../datafiles ctest -V


%install
make install DESTDIR=%{buildroot} 
mkdir -p %{buildroot}/%{_docdir}/cegui-0.8.4/
cp -r doc/doxygen/html %{buildroot}/%{_docdir}/cegui-0.8.4/

# CEGUITests is not very useful to install
find $RPM_BUILD_ROOT -name "CEGUITests-0.8" -exec rm -f {} ';'


%files
%doc README.md
%doc COPYING
%{_libdir}/libCEGUIBase-0.so.*
%{_libdir}/libCEGUICommonDialogs-0.so.*
%{_libdir}/libCEGUILuaScriptModule-0.so.*
%{_libdir}/libCEGUIOpenGLRenderer-0.so.*
%{_libdir}/cegui-0.8/libCEGUICoreWindowRendererSet.so
# this is the default parser, that's why it's not split off into a subpackage
%{_libdir}/cegui-0.8/libCEGUIExpatParser.so
# same with silly image codec
%{_libdir}/cegui-0.8/libCEGUISILLYImageCodec.so

%files devel
%{_libdir}/libCEGUI*-0.so

%{_bindir}/toluappcegui-0.8

%{_libdir}/pkgconfig/CEGUI-0.pc
%{_libdir}/pkgconfig/CEGUI-0-OPENGL.pc
%{_libdir}/pkgconfig/CEGUI-0-OPENGL3.pc
%{_libdir}/pkgconfig/CEGUI-0-OGRE.pc
%{_libdir}/pkgconfig/CEGUI-0-NULL.pc
%{_libdir}/pkgconfig/CEGUI-0-LUA.pc
%{_libdir}/pkgconfig/CEGUI-0-IRRLICHT.pc

%{_includedir}/cegui-0

%{_datadir}/cegui-0

#%files devel-doc
#%doc %{_docdir}/cegui-0.8.4/html

%files samples
%{_bindir}/CEGUISampleFramework-0.8
%{_libdir}/cegui-0.8/libCEGUI*Demo.so
%{_libdir}/cegui-0.8/libCEGUIDemo6.so
%{_libdir}/cegui-0.8/libCEGUIMinesweeper.so

%files irrlicht-renderer
%{_libdir}/libCEGUIIrrlichtRenderer-0.so.*

%files ogre-renderer
%{_libdir}/libCEGUIOgreRenderer-0.so.*

%files null-renderer
%{_libdir}/libCEGUINullRenderer-0.so.*

%files DevIL-imagecodec
%{_libdir}/cegui-0.8/libCEGUIDevILImageCodec.so

%files freeimage-imagecodec
%{_libdir}/cegui-0.8/libCEGUIFreeImageImageCodec.so

%files libxml-xmlparser
%{_libdir}/cegui-0.8/libCEGUILibXMLParser.so

%files tinyxml-xmlparser
%{_libdir}/cegui-0.8/libCEGUITinyXMLParser.so

%files xerces-xmlparser
%{_libdir}/cegui-0.8/libCEGUIXercesParser.so


%changelog
* Tue Apr 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.7-alt3_7
- Rebuilt with new libboost.

* Tue Feb 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.7-alt2_7
- Fixed build with new toolchain.

* Fri Sep 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.7-alt1_7
- new version by fcimport
- disabled devel-doc due to arch dependent png

* Tue Sep 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.4-alt4.S1
- Rebuilt with boost 1.65.0.
- Added %%ubt to release.

* Fri Jul 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.4-alt3
- Fixed build with new toolchain

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
