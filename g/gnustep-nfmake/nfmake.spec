%set_verify_elf_method unresolved=strict

Name: gnustep-nfmake
Version: 0.2
Release: alt1.svn20111010.1
Summary: Tool for building OpenStep projects on GNUstep
License: LGPLv2
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/tools/nfmake/trunk/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
nfmake is a tool for building OpenStep projects on GNUstep by reading
and using the PB.project file created by ProjectBuilder.

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
%doc 00_Docs/*
%_bindir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt1.svn20111010.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20111010
- Snapshot from svn

* Sun Jan 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.cvs20140126
- Initial build for Sisyphus

