%set_verify_elf_method unresolved=strict

Name: gnustep-pbxbuild
Version: 0.1
Release: alt1.git20120619
Summary: This tool converts XCode(tm) projects into GNUmakefiles and builds them
License: GPLv2+ and GPLv3
Group: File tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-pbxbuild.git
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-objc2-devel /proc

%description
This tool converts XCode(tm) projects into GNUmakefiles and builds them.
Those GNUmakefiles may be the basis for further user modifications
in order to make up for the platform differences of GNUstep and OS X.
Currently OSX Version 3.9 and 4.2 project files are supported.

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
%doc ChangeLog ISSUES README
%_bindir/*

%changelog
* Sat Jan 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20120619
- Initial build for Sisyphus

