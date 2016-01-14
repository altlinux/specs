%set_verify_elf_method unresolved=strict

Name: gnustep-charsets
Version: r29248
Release: alt7.git20100109.1
Summary: Utilities for use with NSCharacterSet bitmap files
License: LGPLv2+
Group: Development/Tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-charsets.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel libgnustep-ucsdata-devel
BuildPreReq: /proc
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

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
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc README
%_bindir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> r29248-alt7.git20100109.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r29248-alt7.git20100109
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r29248-alt6.git20100109
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r29248-alt5.git20100109
- Rebuilt with new gnustep-gui

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r29248-alt4.git20100109
- Rebuilt with libobjc2 instead of libobjc

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r29248-alt3.svn20100109
- Rebuilt with fixed gnustep-make

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r29248-alt2.svn20100109
- Rebuilt with /proc support

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r29248-alt1.svn20100109
- Initial build for Sisyphus

