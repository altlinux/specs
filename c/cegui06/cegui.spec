Name: cegui06
Version: 0.6.2
Release: alt6.1

Summary: Free library providing windowing and widgets for graphics APIs / engines
Group: System/Libraries
License: MIT
Url: http://www.cegui.org.uk
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://downloads.sourceforge.net/crayzedsgui/CEGUI-%version.tar.gz
Source1: http://downloads.sourceforge.net/crayzedsgui/CEGUI-DOCS-%version.tar.gz
Patch0: cegui-0.6.0-userverso.patch
Patch1: cegui-0.6.0-release-as-so-ver.patch
Patch2: cegui-0.6.1-libdl-alt.patch
Patch3: CEGUI-pld-new-tinyxml.patch
Patch4: cegui-0.6.2-alt-gcc4.6.patch

BuildRequires: gcc-c++
BuildRequires: expat-devel
BuildRequires: libfreetype-devel
BuildRequires: libICE-devel libX11-devel libXext-devel
BuildRequires: libGLU-devel
BuildRequires: libSM-devel
BuildRequires: pcre-devel
BuildRequires: libglew-devel

%description
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines. This package contains the older version 0.6 for
apps which cannot be easily ported to 0.7. As such this version has been build
without additional image codecs or xml parsers.

%package devel
Summary: Development files for cegui
Group: Development/C++
Requires: %name = %version-%release
Requires: libGLU-devel

%description devel
Development files for cegui

%prep
%setup -qb1 -qn CEGUI-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p2

# Permission fixes for debuginfo RPM
chmod -x include/falagard/*.h

# Delete zero length file
rm -f documentation/api_reference/keepme

# Encoding fixes
iconv -f iso8859-1 AUTHORS -t utf8 > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 TODO -t utf8 > TODO.conv && mv -f TODO.conv TODO
iconv -f iso8859-1 README -t utf8 > README.conv && mv -f README.conv README

%build
%configure \
	--disable-static --disable-samples --disable-lua-module \
	--disable-corona --disable-devil --disable-silly --disable-freeimage \
	--disable-irrlicht-renderer --disable-directfb-renderer \
	--disable-xerces-c --disable-libxml --disable-tinyxml \
	--with-default-xml-parser=ExpatParser \
	--with-default-image-codec=TGAImageCodec \
	--with-pic
# We do not want to get linked against a system copy of ourselves!
sed -i 's|-L%_libdir||g' RendererModules/OpenGLGUIRenderer/Makefile
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
%make_install install DESTDIR=%buildroot
find %buildroot -name '*.la' -exec rm -f {} ';'

# Move some things around to make cegui06-devel co-exist peacefully with
# cegui-devel
mkdir -p %buildroot/%_libdir/CEGUI-0.6
for i in libCEGUIBase libCEGUIExpatParser libCEGUIFalagardWRBase \
	 libCEGUIOpenGLRenderer libCEGUITGAImageCodec; do
    rm %buildroot/%_libdir/$i.so
    ln -s ../$i-%version.so %buildroot/%_libdir/CEGUI-0.6/$i.so
done
mv %buildroot/%_includedir/CEGUI %buildroot/%_includedir/CEGUI-0.6
mv %buildroot/%_datadir/CEGUI %buildroot/%_datadir/CEGUI-0.6
sed -e 's|/CEGUI|/CEGUI-0.6|g' \
    -e 's|libdir=%_libdir|libdir=%_libdir/CEGUI-0.6|g' \
    -i %buildroot/%_libdir/pkgconfig/*.pc
for i in %buildroot/%_libdir/pkgconfig/*.pc; do
    mv $i `echo $i | sed 's|\.pc\$|-0.6.pc|'`
done

%files
%doc AUTHORS ChangeLog COPYING README TinyXML-License TODO
%_libdir/libCEGUI*-%version.so

%files devel
%_libdir/CEGUI-0.6/*.so
%_pkgconfigdir/CEGUI-OPENGL-0.6.pc
%_pkgconfigdir/CEGUI-0.6.pc
%_includedir/CEGUI-0.6
%_datadir/CEGUI-0.6

%changelog
* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt6.1
- Fixed build

* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt6
- fix load module TGAImageCodec (#26483)

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt5
- revert devel package (need for build spice)
- change build options:
  + --disable-lua-module
  + --disable-devil
  + --disable-silly
  + --disable-freeimage
  + --disable-xerces-c
  + --disable-libxml
  + --disable-tinyxml
  + --with-default-image-codec=TgaImageCodec
- update BR:

* Tue May 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt4
- build as compat package

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
