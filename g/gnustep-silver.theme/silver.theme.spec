%set_verify_elf_method unresolved=strict

Name: gnustep-silver.theme
Version: 3.1
Release: alt5
Summary: Silver theme for GNUstep
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/Themes
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Silver.theme is a theme with menu in-window, silvered controls,
scrollbars at right side and arrows at opposite sides. Ideal for
people who want use GNUstep apps in desktops like Gnome, KDE, ...

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
%_libdir/GNUstep

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 3.1-alt5
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 3.1-alt4
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 3.1-alt3.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt2
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Rebuilt with new gnustep-gui

* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Version 3.0

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Initial build for Sisyphus

