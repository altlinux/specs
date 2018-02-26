Name: qkismet
Version: 0.3.1
Release: alt1

Summary: Qt4 frontend to kismet
License: %gpl2plus
Group: Security/Networking
Url: http://qkismet.sf.net/

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildPreReq: gcc-c++ libqt4-devel

%description
qKismet is graphical Kismet client written in Qt. It aims to be a
full-featured client, which provides features allowing easy overview of
Kismet output. Currently it displays networks, clients, alerts and
status messages and allows to sort and filter them.

%prep
%setup

%build
pushd src
qmake-qt4
sed -i 's,-pipe ,%optflags ,g' Makefile.Release
%make_build

%install
%makeinstall -C src INSTALL_ROOT=%buildroot

%files
%_bindir/*

%changelog
* Tue Sep 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Mon Aug 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.1-alt1
- initial build
