%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-XMPPKit
Version: 0.2
Release: alt1.git20131126
Summary: Objective-C implementation of XMPP
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/XMPPKit.git
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel
BuildPreReq: gnustep-Etoile-EtoileSerialize-devel
BuildPreReq: gnustep-Etoile-AddressesKit-devel

Requires: lib%name = %EVR
Requires: gnustep-back gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-AddressesKit gnustep-Etoile-EtoileSerialize

%description
XMPPKit is an Objective-C implementation of the Extensible Messaging and
Presence Protocol (XMPP) that can be used to write Jabber-enabled
applications.
For more informations about XMPP itself, see <http://xmpp.org/>.

%package -n lib%name
Summary: Shared libraries of XMPPKit
Group: System/Libraries

%description -n lib%name
XMPPKit is an Objective-C implementation of the Extensible Messaging and
Presence Protocol (XMPP) that can be used to write Jabber-enabled
applications.

This package contains shared libraries of XMPPKit.

%package -n lib%name-devel
Summary: Development files of XMPPKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
XMPPKit is an Objective-C implementation of the Extensible Messaging and
Presence Protocol (XMPP) that can be used to write Jabber-enabled
applications.

This package contains development files of XMPPKit.

%package docs
Summary: Documentation for XMPPKit
Group: Development/Documentation
BuildArch: noarch

%description docs
XMPPKit is an Objective-C implementation of the Extensible Messaging and
Presence Protocol (XMPP) that can be used to write Jabber-enabled
applications.

This package contains documentation for XMPPKit.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/RPM/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	doc=yes \
	PROJECT_NAME=XMPPKit

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	doc=yes \
	PROJECT_NAME=XMPPKit

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

pushd %buildroot%_libdir
for j in XMPPKit; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/Current/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$i
			rm GNUstep/Frameworks/$j.framework/Versions/Current/$j
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$j
		done
	done
done
popd

%files
%doc ChangeLog.rtf NEWS README
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/XMPPKit.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/XMPPKit.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/XMPPKit.framework/Headers
%_libdir/GNUstep/Frameworks/XMPPKit.framework/Versions/0/Headers

%files docs
%_docdir/GNUstep

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20131126
- Initial build for Sisyphus

