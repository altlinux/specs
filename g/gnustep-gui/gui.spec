%set_verify_elf_method unresolved=strict

# based on Fedora's package

Name: gnustep-gui
Version: 0.24.0
Release: alt6.svn20140223.2
Summary: The GNUstep GUI library
License: GPLv2+ and GPLv3
Group: Development/Tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-gui.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel libtiff-devel libjpeg-devel
BuildPreReq: libpng-devel libcups-devel libaspell-devel aspell
BuildPreReq: libungif-devel libaudiofile-devel libportaudio2-devel
BuildPreReq: libX11-devel libicu-devel imake libImageMagick-devel
BuildPreReq: ImageMagick-tools libsndfile-devel libao-devel
BuildPreReq: flite-devel libicns-devel /proc gnustep-base-doc
BuildPreReq: texinfo texi2html texlive-latex-base
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libdispatch-objc2-devel
BuildPreReq: libkrb5-devel

Requires: lib%name = %version-%release
Requires: aspell flite

%description
The GNUstep GUI library is a library of graphical user interface classes
written completely in the Objective-C language; the classes are based
upon the OpenStep specification as release by NeXT Software, Inc.  These
classes include graphical objects such as buttons, text fields, popup
lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries
License: LGPLv2+ and LGPLv3+

%description -n lib%name
The GNUstep GUI library is a library of graphical user interface classes
written completely in the Objective-C language; the classes are based
upon the OpenStep specification as release by NeXT Software, Inc.  These
classes include graphical objects such as buttons, text fields, popup
lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

This package contains the libraries for %name.

%package devel
Summary: Header files for the gnustep-gui package
Group: Development/Objective-C
Requires: gnustep-base-devel
Requires: lib%name = %version-%release
Requires: %name = %version-%release

%description devel
The GNUstep GUI library is a library of graphical user interface classes
written completely in the Objective-C language; the classes are based
upon the OpenStep specification as release by NeXT Software, Inc.  These
classes include graphical objects such as buttons, text fields, popup
lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

This package contains the header files for gnustep-gui.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
License: GFDL
Requires: gnustep-base-doc
#Requires: %name = %version-%release

%description doc
The GNUstep GUI library is a library of graphical user interface classes
written completely in the Objective-C language; the classes are based
upon the OpenStep specification as release by NeXT Software, Inc.  These
classes include graphical objects such as buttons, text fields, popup
lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

This package contains the documentation for %name.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-imagemagick \
	--with-x \
	--with-installation-domain=SYSTEM

#make_build \
#	messages=yes \
#	debug=yes \
#	strip=no \
#	shared=yes \
#	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
#	||:
#touch Tools/GSspell.service/Resources/Info-gnustep.plist
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-I%_includedir/dispatch'
 
%make_build -C Documentation \
	messages=yes

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Documentation \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

for i in ChangeLog*; do
	gzip $i
done

# broken info
rm -fR %buildroot%_infodir

%files
%doc ANNOUNCE BUGS ChangeLog* COPYING NEWS README
%_bindir/*
%_libdir/GNUstep
%_man1dir/*

%files -n lib%name
%doc COPYING.LIB
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_datadir/GNUstep

%files doc
#_infodir/*
%_docdir/GNUstep

%changelog
* Fri Feb 26 2016 Andrey Cherepanov <cas@altlinux.org> 0.24.0-alt6.svn20140223.2
- Rebuild with new icu

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.24.0-alt6.svn20140223.1
- NMU: Rebuild with libgnutls30.

* Tue Jul 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt6.svn20140223
- Fixed build

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 0.24.0-alt5.svn20140223
- rebuild with new ImageMagick

* Mon Mar 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt4.svn20140223
- New snapshot

* Mon Feb 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt4.svn20140126
- Added documentation

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt3.svn20140126
- Rebuilt with clang

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt2.svn20140126
- New snapshot

* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt2.git20140101
- Set _isVertical is public in %_includedir/AppKit/NSProgressIndicator.h

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt1.git20140101
- Version 0.24.0

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt3.git20130913
- New snapshot

* Sun May 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt3.git20130424
- New snapshot

* Thu Apr 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt3.git20130318
- Rebuilt with new ImageMagick

* Wed Mar 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt2.git20130318
- New snapshot

* Wed Mar 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt2.git20130302
- Rebuilt

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt1.git20130302
- Version 0.23.1

* Wed Jan 30 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt5.git20130129
- New snapshot

* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt5.git20121231
- New snapshot

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt5.git20121226
- New snapshot

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt4.svn20121209
- Added requirement %name-devel on %name

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt3.svn20121209
- Rebuilt with fixed gnustep-make

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt2.svn20121209
- Built with /proc support

* Mon Dec 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt1.svn20121209
- Initial build for Sisyphus

* Fri Nov 30 2012 Jochen Schmitt <Jochen herr-schmitt de> - 0.22.0-3
- Rebuilt for new gnustep-base release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb  8 2012 Jochen Schmitt <Jochen herr-schmitt de> 0.22.0-1
- New upstream release

* Wed Jan  4 2012 Jochen Schmitt <JOchen herr-schmitt de> 0.20.0-5
- Fix depedencies issues on rawhide (libobjc.so.3)

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> 0.20.0-4
- Rebuild for new libpng

* Mon Oct 10 2011 Jochen Schmitt <JOchen herr-schmitt de> 0.20.0-3
- Rebuilt again

* Sun Oct  9 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.20.0-2
- Rebuilt for gnustep-base-1.23.0

* Wed Apr 27 2011 Jochen Schmitt <JOchen herr-schmitt de> 0.20.0-1
- New upstream release which is compatible to gcc-4.6

* Thu Feb 10 2011 Jochen Schmitt <Jochen herr-schmitt de> - 0.20.0-0.20110210
- First building unstable release agains gcc-4.6.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-3
- Rebuild for new libobjc

* Tue Jul  6 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-2
- Use new gnustep parallel build feature

* Fri May 14 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-1
- New upstream release

* Tue Oct 13 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-5
- Fix missing BRs

* Tue Sep 29 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-4
- Fix typo

* Sun Sep 27 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-3
- Create separate libs subpackage
- Fix license tag

* Thu Sep 24 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-2
- Rework for new gnustep-make and gnustep-base releases

* Tue Feb 17 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-1
- New upstream release

* Thu Dec 11 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.14.0-2
- Add some missing BRs

* Wed Dec 10 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.14.0-1
- Initional Package
