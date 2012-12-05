Name: jal
Version: 0.3
Release: alt1.rc1.1

Summary: Java Application Loader for Motorola phones
License: GPLv2+
Group: Communications
Url: http://softmile.com/download/

Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %name-%version.tar.bz2
Patch0: %name-0.2-alt-translations-path.patch

BuildPreReq: gcc-c++ libqt4-devel

%description
Java Application Loader for Motorola phones (tool similar to Motorola
MidWay).

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure \
	--with-qmake=%_bindir/qmake-qt4
%make_build

pushd qjal
qmake-qt4 \
	QMAKE_CFLAGS+="%optflags" \
	QMAKE_CXXFLAGS+="%optflags" \
	DEFINES+='DATADIR=\\\"%_datadir/qjal\\\"' \
	qjal.pro
%make_build
popd

%install
%makeinstall

install -d %buildroot%_datadir/qjal/images
install -m755 qjal/qjal %buildroot%_bindir
install -p -m644 qjal/*.qm %buildroot%_datadir/qjal
install -p -m644 qjal/images/* %buildroot%_datadir/qjal/images/

%files
%_bindir/*
%_datadir/qjal
%doc AUTHORS ChangeLog README

%changelog
* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.rc1.1
- Fixed build

* Sat Mar 08 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt1.rc1
- 0.3 rc1

* Wed May 02 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt2
- fix Group:
- spec cleanup
- use optflags

* Tue Oct 03 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt1.1
- add Packager:

* Sat Sep 30 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt1
- initial build

