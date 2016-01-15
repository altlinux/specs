%set_verify_elf_method unresolved=strict

#based on Fedora's spec

Name: gnustep-back    
Version: 0.24.0
Release: alt6.svn20140127.1
Summary: The GNUstep back-end library
License: LGPLv3+ and GPLv3+
Group: Graphical desktop/GNUstep
URL: http://www.gnustep.org
# http://svn.gna.org/svn/gnustep/libs/back/trunk/
Source: %name-%version.tar
Source1: Courier.FontInfo.plist
Source2: Times.FontInfo.plist

BuildPreReq: libfreetype-devel libX11-devel libXt-devel libXext-devel
BuildPreReq: libXmu-devel libICE-devel libXft-devel libGL-devel
BuildPreReq: libart_lgpl-devel clang-devel libglitz-devel libcairo-devel
BuildPreReq: gnustep-make-devel gnustep-gui-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel libXcursor-devel libXfixes-devel
BuildPreReq: fonts-type1-urw gnustep-gui-doc
BuildRequires: texinfo /proc
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel

Requires: fonts-type1-urw gnustep-base gnustep-gui

%description 
This is a back-end for the GNUstep GUI library which allows you to use
the GNUstep GUI library on an X Windows System (other back-ends will
be added later to allow you to use the GNUstep GUI Library in other
windowing environments). This package includes development headers too.

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch
Requires: gnustep-gui-doc

%description doc
This is develompent documentation for %name.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-glitz \
	--enable-server=x11 \
%ifarch x86_64
	--enable-graphics=cairo \
%else
	--enable-graphics=xlib \
%endif
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
	shared=yes

%make_build -C Documentation \
	messages=yes

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%makeinstall_std -C Documentation \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

rm -rf \
	%buildroot%_libdir/GNUstep/Documentation/Developer/Back/ReleaseNotes

pushd %buildroot%_libdir/GNUstep/Fonts/Helvetica.nfont
for i in $(ls *.?f?); do
	rm -f $i
	ln -s %_datadir/fonts/type1/urw/$i ./
done
popd

install -d %buildroot%_libdir/GNUstep/Fonts/Courier.nfont
pushd %buildroot%_libdir/GNUstep/Fonts/Courier.nfont
install -p -m644 %SOURCE1 ./FontInfo.plist
for i in n022003l n022023l n022004l n022024l; do
	ln -s %_datadir/fonts/type1/urw/$i.afm ./
	ln -s %_datadir/fonts/type1/urw/$i.pfb ./
	ln -s %_datadir/fonts/type1/urw/$i.pfm ./
done
popd

install -d %buildroot%_libdir/GNUstep/Fonts/Times.nfont
pushd %buildroot%_libdir/GNUstep/Fonts/Times.nfont
install -p -m644 %SOURCE2 ./FontInfo.plist
for i in n021003l n021023l n021004l n021024l; do

	ln -s %_datadir/fonts/type1/urw/$i.afm ./
	ln -s %_datadir/fonts/type1/urw/$i.pfb ./
	ln -s %_datadir/fonts/type1/urw/$i.pfm ./
done
popd

install -d %buildroot%_sysconfdir/profile.d
echo "export GNUSTEP_STRING_ENCODING=UTF-8" \
	> %buildroot%_sysconfdir/profile.d/%name.sh
chmod +x %buildroot%_sysconfdir/profile.d/%name.sh

gzip ChangeLog

%files
%doc ANNOUNCE ChangeLog* COPYING* NEWS README
%_sysconfdir/profile.d/*
%_bindir/*
%_libdir/GNUstep
%_man1dir/*

%files doc
%_docdir/GNUstep

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.24.0-alt6.svn20140127.1
- NMU: Rebuild with libgnutls30.

* Thu Mar 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt6.svn20140127
- Set default font as Helvetica, and Courier for mono space font

* Mon Mar 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt5.svn20140127
- Rebuilt

* Wed Feb 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt4.svn20140127
- Moved documetation into separate package

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt3.svn20140127
- Built with clang

* Tue Feb 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt2.svn20140127
- Built with xlib for i586

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt1.svn20140127
- New snapshot

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt1.git20140101
- Version 0.24.0

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt4.git20130910
- New snapshot

* Sun May 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt4.git20130425
- New snapshot

* Wed Mar 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt4.git20130301
- Disabled optimization

* Wed Mar 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt3.git20130301
- Rebuilt

* Wed Mar 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt2.git20130301
- Rebuilt

* Tue Mar 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt1.git20130301
- New snapshot

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt6.git20130201
- New snapshot

* Tue Jan 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt6.git20130105
- Set UTF-8 encoding (thnx aen@)
- Added requirements on gnustep-base, gnustep-gui

* Sun Jan 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt5.git20130105
- Use fonts-type1-urw for cyrillic text (thnx aen@)

* Sat Jan 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt4.git20130105
- New snapshot
- Built with xlib instead of cairo

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt4.git20121126
- Rebuilt with libobjc2 instead of libobjc

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
