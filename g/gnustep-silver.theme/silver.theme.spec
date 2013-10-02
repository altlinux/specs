%set_verify_elf_method unresolved=strict

Name: gnustep-silver.theme
Version: 3.0
Release: alt1
Summary: Silver theme for GNUstep
License: GPLv3
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/Themes
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

%description
Silver.theme is a theme with menu in-window, silvered controls,
scrollbars at right side and arrows at opposite sides. Ideal for
people who want use GNUstep apps in desktops like Gnome, KDE, ...

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc README
%_libdir/GNUstep

%changelog
* Wed Oct 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Version 3.0

* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Initial build for Sisyphus

