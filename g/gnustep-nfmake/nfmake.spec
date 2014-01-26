%set_verify_elf_method unresolved=strict

Name: gnustep-nfmake
Version: 0.2
Release: alt1.cvs20140126
Summary: Tool for building OpenStep projects on GNUstep
License: LGPLv2
Group: Graphical desktop/GNUstep
Url: http://savannah.gnu.org/projects/gnustep
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d:pserver:anonymous@cvs.sv.gnu.org:/sources/gnustep co gnustep/dev-apps/nfmake
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

%description
nfmake is a tool for building OpenStep projects on GNUstep by reading
and using the PB.project file created by ProjectBuilder.

%prep
%setup

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' $i
done

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP -DGNU_RUNTIME' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc 00_Docs/*
%_bindir/*

%changelog
* Sun Jan 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.cvs20140126
- Initial build for Sisyphus

