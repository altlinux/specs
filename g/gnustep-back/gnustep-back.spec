%set_verify_elf_method unresolved=strict

Name: gnustep-back    
Version: 0.30.0
Release: alt1
Summary: The GNUstep back-end library
License: LGPL-2.1+ and GPL-3.0+
Group: Graphical desktop/GNUstep
URL: http://www.gnustep.org

# https://github.com/gnustep/libs-back
Source: libs-back-%version.tar
Patch1: gnustep-back-DejaVu-compatible-font.patch

BuildRequires: libfreetype-devel libX11-devel libXt-devel libXext-devel
BuildRequires: libXmu-devel libICE-devel libXft-devel libGL-devel
BuildRequires: libart_lgpl-devel libglitz-devel libcairo-devel
BuildRequires: gnustep-make-devel gnustep-base-devel
BuildRequires: gnustep-gui-devel = %version
BuildRequires: libXcursor-devel libXfixes-devel
BuildRequires: fonts-type1-urw gnustep-gui-doc
BuildRequires: texinfo /proc
BuildRequires: libgmp-devel libgnutls-devel libgcrypt-devel
BuildRequires: libxslt-devel libffi-devel libicu-devel

Requires: gnustep-base
Requires: gnustep-gui = %version
Requires: fonts-ttf-core

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
%setup -n libs-back-%version
%patch1 -p1

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%autoreconf
%configure \
	--libexecdir=%_libdir \
	--enable-glitz \
	--enable-server=x11 \
	--enable-graphics=xlib \
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

rm -rf %buildroot%_libdir/GNUstep/Documentation/Developer/Back/ReleaseNotes

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
* Thu Dec 29 2022 Andrey Cherepanov <cas@altlinux.org> 0.30.0-alt1
- New version.

* Tue Jun 15 2021 Andrey Cherepanov <cas@altlinux.org> 0.29.0-alt1
- New version compatible with current gnustep-gui (ALT #40221).

* Wed Oct 21 2020 Andrey Cherepanov <cas@altlinux.org> 0.28.0-alt2
- Use only common TTF font (Sans, Mono) instead of Type1 fonts and hardcoded DejaVu (ALT #39083).

* Tue Oct 13 2020 Andrey Cherepanov <cas@altlinux.org> 0.28.0-alt1
- New version.
- Build from upstream https://github.com/gnustep/libs-back.

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.24.0-alt7
- Build without libgnustep-objc2-devel.

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
