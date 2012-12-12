Name: gnustep-charsets
Version: r29248
Release: alt3.svn20100109
Summary: Utilities for use with NSCharacterSet bitmap files
License: LGPLv2+
Group: Development/Tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/tools/charsets/trunk/
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel libgnustep-ucsdata-devel
BuildPreReq: /proc

%description
mkcharsets: Creates the standard set of bitmap files for NSCharacterSet
  in the current directory.  Takes no argument ... it expects
  to read UnicodeData.txt in the current directory, and this
  file should be downloaded from mthe web (currently from
  http://www.unicode.org/Public/UNIDATA/)

data2header: Takes the bitmaps produced by mkcharsets and generates a
  header file for use by NSCharacterSet.m ... which should
  be copied into core/base/Source.
  This contains two alternative representations of each
  characterset, one as a bitmap, and one as a list of ranges.

 ckcharset:Takes filename of character set bitmap as argument and
  prints out the Unicode names of all of the characters in
  the character set.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc README
%_bindir/*

%changelog
* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r29248-alt3.svn20100109
- Rebuilt with fixed gnustep-make

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r29248-alt2.svn20100109
- Rebuilt with /proc support

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r29248-alt1.svn20100109
- Initial build for Sisyphus

