Name:           gnustep-examples

Version:        1.3.0
Release:        alt5.1

Summary:        The GNUstep examples 
License:        GPLv2+ and GPLv3+
Group:          Graphical desktop/GNUstep

URL:            http://www.gnustep.org
Source:         %name-%version.tar

BuildRequires:  clang-devel libgnustep-objc2-devel gnustep-make-devel
BuildRequires:  gnustep-base-devel gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back
 
%description 
This package contains sample applications for the GNUstep framework.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	OBJCFLAGS="%optflags -DGNUSTEP" \
	USE_NONFRAGILE_ABI=no

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

cp gui/ExampleTheme/Rhea/COPYING .

%files
%_bindir/*
%_libdir/GNUstep/

%doc README ChangeLog COPYING

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt5.1
- NMU: Rebuild with libgnutls30.

* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt5
- Built with clang

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt4
- Built with gcc

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt3
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2
- Rebuilt with new gnustep-gui

* Wed Mar 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Jochen Schmitt <Jochen herr-schmitt de> - 1.3.0-13
- Rebuilt for new releases of gnustep-base and gnustep-gui
- Clean up SPEC file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb  9 2012 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-11
- Build agains new gnustep core

* Wed Jan  4 2012 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-10
- Fix dependencies issues on rawhide (libobjc.so.3

* Wed Oct 19 2011 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-9
- Rebuilt to fix dependecies issues

* Thu Apr 28 2011 Jochen Schmitt <JOchen inet.herr-schmitt de> 1.3.0-8
- Rebuild for new gnustep-base and gnustep-gui

* Thu Feb 10 2011 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-7
- Rebuild for gnustep snapshot

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-5
- Rebuild for new libobjc

* Wed Sep 29 2010 jkeating - 1.3.0-4
- Rebuilt for gcc bug 634757

* Sun Sep 26 2010 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-3
- Set version of BR of gnustep-gui-devel >= 0.18

* Wed Sep 22 2010 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-2
- Put COPYING file in the %%doc stanza

* Tue Jul  6 2010 Jochen Schmitt <Jochen herr-schmitt de> 1.3.0-1
- Initial package for Fedora

