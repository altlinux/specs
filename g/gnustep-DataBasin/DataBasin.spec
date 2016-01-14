%set_verify_elf_method unresolved=strict

Name: gnustep-DataBasin
Version: 0.7
Release: alt1.1
Summary: Data access tool and for SalesForce.com based on the SOAP API interfaces
License: GPL / LGPLv3+
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/databasin/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-webservices-devel

Requires: gnustep-back

%description
DataBasin is a tool to access and work with SalesForce.com. It allows
to perform queries remotely, export and import data.

To connect to SFDC, DataBasin uses the WebServices exposed by the SFDC
API and exposes them as methods of the DBSoap class. Currently not all
methods are implemented yet. To send and receive the SOAP messages, DB
uses the websevices (GSWS) available from GNUstep libraries and which is
a mandatory requisite.

Features

* Reusable core library
* Session and User inspectors
* connect via http or https
* Data Operations
  * Insert
  * Query and QueryAll
  * Quick Delete
  * execute select on records identified by Id or Unique identifier
* Describe Object (and export to CSV)
* Table based object-inspector

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

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog *.txt
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt1.1
- NMU: Rebuild with libgnutls30.

* Thu May 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt4
- Built with clang

* Mon Feb 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Added Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

