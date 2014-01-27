%set_verify_elf_method unresolved=strict

Name: gnustep-Switcher
Version: 20140127
Release: alt1.cvs20140127
Summary: Allow applications to appear when the icon is clicked on from another workspace
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
This is a quick hack to allow applications to appear when the icon is
clicked on from another workspace.

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
%doc README ChangeLog
%_libdir/GNUstep

%changelog
* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140127-alt1.cvs20140127
- Initial build for Sisyphus

