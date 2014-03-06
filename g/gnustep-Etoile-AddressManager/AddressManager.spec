%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-AddressManager
Version: 0.4.6
Release: alt1.svn20121130
Summary: Versatile address book application for managing contact information
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Services/User/AddressManager/
Source: %name-%version.tar
Source1: gnustep-AddressManager.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator
BuildPreReq: gnustep-Etoile-AddressesKit-devel

Requires: gnustep-back gnustep-Etoile-AddressesKit

%description
AddressManager is a versatile address book application for managing
contact information.

It stores addresses, phone numbers, pictures, instant messaging
information, email, homepages and whatever.

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
	documentation=yes \
	PROJECT_NAME=AddressManager

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=AddressManager

install -d %buildroot%_menudir
install -m644 %SOURCE1 %buildroot%_menudir/gnustep-AddressManager

%files
%doc AUTHORS NEWS README THANKS TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.svn20121130
- Initial build for Sisyphus

