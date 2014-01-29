#set_verify_elf_method unresolved=strict

Name: gnustep-Grouch
Version: 20061120
Release: alt2
Summary: Grouch is an AOL Instant MessengerSM and ICQ client for GNUstep
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://sveikauskas.org/projects/grouch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-renaissance-devel

Requires: lib%name = %EVR
Requires: gnustep-renaissance
Requires: gnustep-back

%description
Grouch is an AOL Instant MessengerSM and ICQ client for GNUstep.

Grouch supports basic messaging and chat. However it is lacking many
ICQ-specific features.

%package -n lib%name
Summary: Shared libraries of Grouch
Group: System/Libraries

%description -n lib%name
Grouch is an AOL Instant MessengerSM and ICQ client for GNUstep.

Grouch supports basic messaging and chat. However it is lacking many
ICQ-specific features.

This package contains shared libraries of Grouch.

%package -n lib%name-devel
Summary: Development files of Grouch
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
Grouch is an AOL Instant MessengerSM and ICQ client for GNUstep.

Grouch supports basic messaging and chat. However it is lacking many
ICQ-specific features.

This package contains development files of Grouch.

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
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc ChangeLog README
%_bindir/*
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20061120-alt2
- Added Requires: gnustep-renaissance and Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20061120-alt1
- Initial build for Sisyphus

