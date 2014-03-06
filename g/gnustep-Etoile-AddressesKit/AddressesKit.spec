%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-AddressesKit
Version: 0.4.7
Release: alt1.svn20140227
Summary: Addresses for GNUstep
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Frameworks/AddressesKit/
Source: %name-%version.tar
Source1: gnustep-adgnumailconverter.menu
Source2: gnustep-adserver.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator gnustep-gworkspace-devel
BuildPreReq: gnustep-gsldap-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
This package constitutes a personal address manager for the GNUstep
software system. It allows archiving complete personal contact
information, organizing contacts in groups, integration with other
software such as mail clients and sharing address information with
other users over the network.

%package -n lib%name
Summary: Shared libraries of AddressesKit
Group: System/Libraries

%description -n lib%name
This package constitutes a personal address manager for the GNUstep
software system. It allows archiving complete personal contact
information, organizing contacts in groups, integration with other
software such as mail clients and sharing address information with
other users over the network.

This package contains shared libraries of AddressesKit.

%package -n lib%name-devel
Summary: Development files of AddressesKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
This package constitutes a personal address manager for the GNUstep
software system. It allows archiving complete personal contact
information, organizing contacts in groups, integration with other
software such as mail clients and sharing address information with
other users over the network.

This package contains development files of AddressesKit.

%package -n gnustep-Etoile-VCFInspector
Summary: A content inspector bundle for GWorkspace
Group: Graphical desktop/GNUstep
Requires: %name = %EVR
Requires: gnustep-gworkspace

%description -n gnustep-Etoile-VCFInspector
A content inspector bundle for GWorkspace. It's horribly useful
nonetheless. You can use it to browse through VCFs and also to drag
single addresses out of VCFs into the address book, terminal, any
text field, ...

%package -n gnustep-Etoile-adgnumailconverter
Summary: Merge your GNUMail address book into the Addresses database
Group: Networking/Mail
Requires: %name = %EVR

%description -n gnustep-Etoile-adgnumailconverter
A tool that will merge your GNUMail address book into the Addresses
database.

%package -n gnustep-Etoile-adserver
Summary: A stand-alone Addresses network server
Group: Networking/Mail
Requires: %name = %EVR

%description -n gnustep-Etoile-adserver
A stand-alone Addresses network server.

%package -n gnustep-Etoile-adtool
Summary: A command-line tool for address database manipulation
Group: Networking/Mail
Requires: %name = %EVR

%description -n gnustep-Etoile-adtool
A command-line tool for address database manipulation

%package -n gnustep-Etoile-LDAPAddressBook
Summary: An address book plugin to handle LDAP connections
Group: Graphical desktop/GNUstep
Requires: %name = %EVR

%description -n gnustep-Etoile-LDAPAddressBook
An address book plugin to handle LDAP connections.

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
	AUXILIARY_CPPFLAGS="-I$PWD/Frameworks" \
	PROJECT_NAME=AddressesKit

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=AddressesKit

rm -f \
	%buildroot%_libdir/GNUstep/Frameworks/*.framework/*.framework

rm -f %buildroot%_includedir/AddressBook
ln -s Addresses %buildroot%_includedir/AddressBook

pushd %buildroot%_libdir
for j in AddressView Addresses; do
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

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

install -d %buildroot%_menudir
install -m644 %SOURCE1 %buildroot%_menudir/gnustep-adgnumailconverter
install -m644 %SOURCE2 %buildroot%_menudir/gnustep-adserver

%files
%doc AUTHORS ChangeLog NEWS README THANKS TODO*
%doc Frameworks/Addresses/Documentation/*
%_libdir/GNUstep/Frameworks
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/AddressView.framework/Versions/0/Headers
%exclude %_libdir/GNUstep/Frameworks/Addresses.framework/Versions/0/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/AddressView.framework/Versions/0/Headers
%_libdir/GNUstep/Frameworks/Addresses.framework/Versions/0/Headers

%files -n gnustep-Etoile-VCFInspector
%_libdir/GNUstep/Bundles/VCFViewer.inspector

%files -n gnustep-Etoile-adgnumailconverter
%_bindir/adgnumailconverter
%_menudir/gnustep-adgnumailconverter

%files -n gnustep-Etoile-adserver
%_bindir/adserver
%_menudir/gnustep-adserver

%files -n gnustep-Etoile-adtool
%_bindir/adtool

%files -n gnustep-Etoile-LDAPAddressBook
%_libdir/GNUstep/Bundles/LDAPAddressBook.abclass

%changelog
* Thu Mar 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.7-alt1.svn20140227
- Initial build for Sisyphus

