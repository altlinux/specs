%set_verify_elf_method unresolved=strict

Name: gnustep-LaTeXService
Version: 0.1
Release: alt5
Summary: LaTeX service for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.roard.com/latexservice/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
This is a small service which could convert a LaTeX text into an image
-- just select the text, click on the service item menu, choose "Return
the LaTeX rendering" and voila ! your text is replaced by its LaTeX
rendering.

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
%doc AUTHORS README
%_libdir/GNUstep

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt5
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt4
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt3.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added Requires: gnustep-back

* Fri Jan 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

