%set_verify_elf_method unresolved=strict

Name: gnustep-FlexiSheet
Version: 0.1
Release: alt1.cvs20140127
Summary: A Quantrix-like spreadsheet
License: BSD
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/flexisheet/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d:pserver:anonymous@cvs.sv.gnu.org:/sources/gap co gap/user-apps/FlexiSheet
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-ObjcUnit-devel
BuildPreReq: gnustep-simplewebkit-devel

Requires: gnustep-ObjcUnit
Requires: gnustep-simplewebkit

%description
A Quantrix-like spreadsheet.

%package docs
Summary: Documentation for FlexiSheet
Group: Documentation
BuildArch: noarch

%description docs
A Quantrix-like spreadsheet.

This package contains documentation for FlexiSheet.

%prep
%setup

for i in $(find ./ -type f); do
	sed -i 's|objc/|objc2/|g' "$i" ||:
done

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS="-O2 -DGNUSTEP" \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc TODO
%_bindir/*
%_libdir/GNUstep

%files docs
%doc Application/FlexiSheet\ Help
%doc Documentation

%changelog
* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.cvs20140127
- Initial build for Sisyphus

