%set_verify_elf_method unresolved=strict

Name: gnustep-AddressManager
Version: 0.4.8
Release: alt9.svn20131019
Summary: Versatile address book application for managing contact information
License: LGPL
Group: Networking/Mail
Url: http://gap.nongnu.org/addresses/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.savannah.nongnu.org/svn/gap/trunk/system-apps/Addresses/
Source: %name-%version.tar
Source1: %name.menu
Source2: gnustep-adgnumailconverter.menu
Source3: gnustep-adserver.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel gnustep-gui-devel
BuildPreReq: gnustep-gworkspace-devel gnustep-gsldap-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
AddressManager is a versatile address book application for managing
contact information.

It stores addresses, phone numbers, pictures, instant messaging
information, email, homepages and whatever.

%package -n lib%name
Summary: Shared libraries of GNUstep AddressManager
Group: System/Libraries

%description -n lib%name
AddressManager is a versatile address book application for managing
contact information.

It stores addresses, phone numbers, pictures, instant messaging
information, email, homepages and whatever.

This package contains shared libraries of GNUstep AddressManager.

%package -n lib%name-devel
Summary: Development files of GNUstep AddressManager
Group: Development/Objective-C
Requires: lib%name = %EVR
Requires: %name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
AddressManager is a versatile address book application for managing
contact information.

It stores addresses, phone numbers, pictures, instant messaging
information, email, homepages and whatever.

This package contains development files of GNUstep AddressManager.

%package -n gnustep-VCFInspector
Summary: A content inspector bundle for GWorkspace
Group: Graphical desktop/GNUstep
Requires: %name = %EVR
Requires: gnustep-gworkspace

%description -n gnustep-VCFInspector
A content inspector bundle for GWorkspace. It's horribly useful
nonetheless. You can use it to browse through VCFs and also to drag
single addresses out of VCFs into the address book, terminal, any
text field, ...

%package -n gnustep-adgnumailconverter
Summary: Merge your GNUMail address book into the Addresses database
Group: Networking/Mail
Requires: %name = %EVR

%description -n gnustep-adgnumailconverter
A tool that will merge your GNUMail address book into the Addresses
database.

%package -n gnustep-adserver
Summary: A stand-alone Addresses network server
Group: Networking/Mail
Requires: %name = %EVR

%description -n gnustep-adserver
A stand-alone Addresses network server.

%package -n gnustep-adtool
Summary: A command-line tool for address database manipulation
Group: Networking/Mail
Requires: %name = %EVR

%description -n gnustep-adtool
A command-line tool for address database manipulation

%package -n gnustep-LDAPAddressBook
Summary: An address book plugin to handle LDAP connections
Group: Graphical desktop/GNUstep
Requires: %name = %EVR

%description -n gnustep-LDAPAddressBook
An address book plugin to handle LDAP connections.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build -C Frameworks/Addresses \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base -lobjc2'

%make_build $1 $2 \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS="-lAddresses -lgnustep-gui -lgnustep-base -lobjc2"

 %make_build -C Goodies \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS="-lAddresses -lgsldap -lgnustep-gui -lgnustep-base -lobjc2"
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for i in Addresses AddressView; do
	lib=$(ls lib$i.so.*.*.*)
	for j in lib$i.so*; do
		rm -f $j
		mv GNUstep/Frameworks/$i.framework/Versions/0/$j ./
		ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$j
	done
	rm -f GNUstep/Frameworks/$i.framework/Versions/0/$i
	ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/0/$i
done
popd

%makeinstall_std -C Goodies GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -d %buildroot%_menudir
install -m644 %SOURCE1 %buildroot%_menudir/%name
install -m644 %SOURCE2 %buildroot%_menudir/gnustep-adgnumailconverter
install -m644 %SOURCE3 %buildroot%_menudir/gnustep-adserver

%files
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%_bindir/AddressManager
%_libdir/GNUstep/Applications
%_libdir/GNUstep/Frameworks
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers
%_menudir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/0/Headers

%files -n gnustep-VCFInspector
%_libdir/GNUstep/Bundles/VCFViewer.inspector

%files -n gnustep-adgnumailconverter
%_bindir/adgnumailconverter
%_menudir/gnustep-adgnumailconverter

%files -n gnustep-adserver
%_bindir/adserver
%_menudir/gnustep-adserver

%files -n gnustep-adtool
%_bindir/adtool

%files -n gnustep-LDAPAddressBook
%_libdir/GNUstep/Bundles/LDAPAddressBook.abclass

%changelog
* Fri Feb 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt9.svn20131019
- Added menu files for adgnumailconverter and adserver (thnx kostyalamer@)

* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt8.svn20131019
- New snapshot

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt8
- Built with clang

* Tue Feb 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt7
- Built goodies

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt6
- Added Requires: gnustep-back

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt5
- Rebuilt with new gnustep-gui

* Thu Feb 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt4
- Added menu file (thnx kostyalamer@)

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt3
- Added requirement on %name for lib%name-devel

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt2
- Moved Headers into devel subpackage

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1
- Initial build for Sisyphus

