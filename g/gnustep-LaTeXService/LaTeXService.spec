%set_verify_elf_method unresolved=strict

Name: gnustep-LaTeXService
Version: 0.1
Release: alt1
Summary: LaTeX service for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.roard.com/latexservice/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
This is a small service which could convert a LaTeX text into an image
-- just select the text, click on the service item menu, choose "Return
the LaTeX rendering" and voila ! your text is replaced by its LaTeX
rendering.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc AUTHORS README
%_libdir/GNUstep

%changelog
* Fri Jan 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

