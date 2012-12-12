# based on Fedora's package

Name: gnustep-gui
Version: 0.23.0
Release: alt4.svn20121209
Summary: The GNUstep GUI library
License: GPLv2+ and GPLv3
Group: Development/Tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/gui/trunk/
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel libtiff-devel libjpeg-devel
BuildPreReq: libpng-devel libcups-devel libaspell-devel
BuildPreReq: libungif-devel libaudiofile-devel libportaudio2-devel
BuildPreReq: libX11-devel libicu-devel imake libImageMagick-devel
BuildPreReq: ImageMagick-tools libsndfile-devel libao-devel
BuildPreReq: flite-devel libicns-devel /proc
BuildPreReq: texinfo texi2html texlive-latex-base

Requires: lib%name = %version-%release

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

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

%build
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-imagemagick \
	--with-x \
	--with-installation-domain=SYSTEM

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%make_build -C Documentation \
	messages=yes \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Documentation \
     GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
     GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

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
