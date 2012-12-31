%set_verify_elf_method unresolved=strict

Name: gnustep-easydiff
Version: 0.4.1
Release: alt2.git20121210
Summary: GNUstep's implementation of the OPENSTEP FileMerge application
License: GPLv2+ and GPLv3
Group: File tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-easydiff.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel gnustep-gui-devel /proc

%description
EasyDiff is GNUstep's implementation of the OPENSTEP FileMerge
application. EasyDiff allows for easy merging of differences between
files and is a convenient way to explore changes. It also knows about
different SCMSs and is useful in resolving merge conflicts.

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
%doc AUTHORS ChangeLog
%_bindir/*
%_libdir/GNUstep

%changelog
* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2.git20121210
- Rebuilt with libobjc2 instead of libobjc

* Wed Dec 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20121210
- Initial build for Sisyphus

