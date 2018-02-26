Name: jal
Version: 0.3
Release: alt1.rc1

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
%configure \
	--with-qmake=%_bindir/qmake-qt4
%make_build

%install
%makeinstall

%files
%_bindir/*
%_datadir/qjal/*.qm
%doc AUTHORS ChangeLog README

%changelog
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

