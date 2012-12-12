#based on Fedora's spec

Name: gnustep-back    
Version: 0.23.0
Release: alt3.svn20121126
Summary: The GNUstep back-end library
License: LGPLv3+ and GPLv3+
Group: Development/Objective-C
URL: http://www.gnustep.org
Source: %name-%version.tar

BuildPreReq: libfreetype-devel libX11-devel libXt-devel libXext-devel
BuildPreReq: libXmu-devel libICE-devel libXft-devel libGL-devel
BuildPreReq: libcairo-devel libart_lgpl-devel gcc-objc libglitz-devel
BuildPreReq: gnustep-make-devel gnustep-gui-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel libXcursor-devel libXfixes-devel
BuildRequires: texinfo /proc

%description 
This is a back-end for the GNUstep GUI library which allows you to use
the GNUstep GUI library on an X Windows System (other back-ends will
be added later to allow you to use the GNUstep GUI Library in other
windowing environments). This package includes development headers too.

%prep
%setup

%build
%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-glitz \
	--enable-server=x11 \
	--enable-graphics=cairo \
	--with-tiff-library \
	--with-x \
	--with-installation-domain=SYSTEM

%ifarch x86_64
sed -i 's|i586|x86_64|g' $(find ./ -type f)
%endif
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2'

%make_build -C Documentation \
	messages=yes \
	GNUSTEP_MAKEFILES=/usr/share/GNUstep/Makefiles

%install
%makeinstall_std \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Documentation \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=/usr/share/GNUstep/Makefiles \

rm -rf \
	%buildroot%_libdir/GNUstep/Documentation/Developer/Back/ReleaseNotes

gzip ChangeLog

%files
%doc ANNOUNCE ChangeLog* COPYING* NEWS README
%doc %_docdir/GNUstep
%_bindir/*
%_libdir/GNUstep
%_man1dir/*

%changelog
* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt3.svn20121126
- Rebuilt with fixed gnustep-make

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt2.svn20121126
- Built with /proc support

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt1.svn20121126
- Initial build for Sisyphus

* Fri Nov 30 2012 Jochen Schmitt <sochen herr-schmitt de> - 0.22.0-3
- Rebuilt for new release of gnustep-base and gnustep-gui
- Clean up the SPEC file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb  8 2012 Jochen Schmitt <Jochen herr-schmitt de> 0.22.0-1
- New upstream release

* Wed Jan  4 2012 Jochen Schmitt <JOchen herr-schmitt de> 0.20.0-4
- Fix dependencies issues on rawhide (libobjc.so.3)

* Mon Oct 10 2011 Jochen Schmitt <JOchen herr-schmitt de> 0.20.0-3
- Rebuilt for new gnustep-base

* Thu Apr 28 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.20.0-2
- Rebuild for new gnustep-base release

* Wed Apr 27 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.20.0-1
- New upstream release

* Thu Feb 10 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-7
- Rebuild agains gnustep snapshot

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-5
- Rebuild for new libobjc

* Mon Jul 12 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-4
- Untabify
- Mark %%{_datadir}/GNUstep/Documentation/Developer/Back/ as %%doc

* Tue Jul  6 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-3
- Use of new gnustep parallel build feature

* Mon Jun 21 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-2
- Add versioned BR. agains gnustep-base-devel
- Fix license tag

* Sun May 16 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.18.0-1
- New upstream release

* Sun Apr 25 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-3
- Fix typos
- Remove unnecessaries Documentation files

* Thu Oct 15 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.16.0-2
- Modified package on feedback of other GNUstep package reviews

* Thu Dec 11 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.14.0-1
- Initional Package
