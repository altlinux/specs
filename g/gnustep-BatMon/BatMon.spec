%set_verify_elf_method unresolved=strict

Name: gnustep-BatMon
Version: 0.6
Release: alt1
Summary: Battery monitor for laptops
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel

%description
Battery Monitor is a battery monitor for laptops. It displays the
current status of the battery (charge/discharge and energy level) as
well as some information about the general health of the cell.

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
%_bindir/*
%_libdir/GNUstep

%changelog
* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

