%set_verify_elf_method unresolved=strict

Name: gnustep-pbxbuild
Version: 0.1
Release: alt4
Summary: This tool converts XCode(tm) projects into GNUmakefiles and builds them
License: GPLv2+ and GPLv3
Group: File tools
Url: http://www.gnustep.org/
Packager: Andrey Cherepanov <cas@altlinux.org>

# https://github.com/gnustep/gnustep-pbxbuild.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: /proc
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
This tool converts XCode(tm) projects into GNUmakefiles and builds them.
Those GNUmakefiles may be the basis for further user modifications
in order to make up for the platform differences of GNUstep and OS X.
Currently OSX Version 3.9 and 4.2 project files are supported.

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
%doc ChangeLog ISSUES README
%_bindir/*

%changelog
* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt4
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt3.git20120619.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.git20120619
- Built with clang

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.git20120619
- Fixed build

* Sat Jan 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20120619
- Initial build for Sisyphus

