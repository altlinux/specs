Name: SILLY
Version: 0.1.0
Release: alt4
Summary: Simple and easy to use library for image loading
Group: System/Libraries
License: MIT
Url: http://www.cegui.org.uk
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://downloads.sourceforge.net/crayzedsgui/%name-%version.tar.gz
Source1: http://downloads.sourceforge.net/crayzedsgui/%name-DOCS-%version.tar.gz

BuildRequires: doxygen
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: gcc-c++

%description
The Simple Image Loading LibrarY is a companion library of the CEGUI project.
It provides a simple and easy to use library for image loading.

It currently supports the following formats:
TGA (Targa)
JPEG (Joint Photographic Experts Group)
PNG (Portable Network Graphics)

%package devel
Summary: Development files for SILLY
Group: Development/C++
Requires: %name = %version-%release

%description devel
Development files for SILLY

%prep
%setup -q -a1
# Don't use full path, otherwise it shows buildroot as part of the path
sed -i 's|\(FULL_PATH_NAMES[ \t][ \t]*= \)YES|\1NO|' Doxyfile

# Get rid of some useless noise
sed -i 's|\(WARNINGS[ \t][ \t]*= \)YES|\1NO|' Doxyfile
sed -i 's|\(WARN_IF_UNDOCUMENTED[ \t][ \t]*= \)YES|\1NO|' Doxyfile
sed -i 's|\(WARN_IF_DOC_ERROR[ \t][ \t]*= \)YES|\1NO|' Doxyfile

# Generate developer man pages
sed -i 's|\(GENERATE_MAN[ \t][ \t]*= \)NO|\1YES|' Doxyfile

# Multiarch hack, we are now using prebuilt HTML
sed -i 's|\(GENERATE_HTML[ \t][ \t]*= \)YES|\1NO|' Doxyfile

#Fix encoding on AUTHORS
iconv -f iso8859-1 AUTHORS -t utf8 > AUTHORS.conv && /bin/mv -f AUTHORS.conv AUTHORS

%autoreconf

%build
%configure --disable-static --with-pic
%make

#Build developer documentation
doxygen

%install

%makeinstall_std INSTALL="install -p"

#Install man pages
mkdir -p %buildroot%_man3dir
cp -a doc/man/man3/* %buildroot%_man3dir

#Fix so that RPM's strip works (only strips files marked executable)
chmod 0755 %buildroot%_libdir/*.so.*

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog COPYING

%files devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/%name.pc
%_man3dir/*
%doc %name-%version/doc/html

%changelog
* Wed Mar 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt4
- rebuild for debuginfo

* Tue Dec 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt3
- rebuild for soname set-version

* Tue Jun 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2
- rebuild with new libpng

* Thu Jun 05 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt1
- Initial for ALT

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.0-5
- Autorebuild for GCC 4.3

* Sun Oct 28 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.1.0-4
- Multiarch fixes (BZ 343181)

* Wed Aug 22 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.1.0-3
- Release bump for F8 mass rebuild

* Sun Mar 11 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.1.0-2
- Preserve timestamps on install
- Changed source URL
- Improved sed replacements
- Changed encoding of AUTHORS to UTF-8

* Mon Feb 26 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.1.0-1
- Initial Release
