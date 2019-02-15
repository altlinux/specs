Name: qkismet
Version: 0.3.1
Release: alt2

Summary: Qt4 frontend to kismet
License: %gpl2plus
Group: Security/Networking
Url: http://qkismet.sf.net/

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source0: %name-%version.tar

Patch1: %name-%version-alt-gcc8.patch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: gcc-c++ libqt4-devel

%description
qKismet is graphical Kismet client written in Qt. It aims to be a
full-featured client, which provides features allowing easy overview of
Kismet output. Currently it displays networks, clients, alerts and
status messages and allows to sort and filter them.

%prep
%setup
%patch1 -p2

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
* Thu Feb 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.1-alt2
- NMU: fixed build with gcc-8.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Sep 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Mon Aug 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.1.1-alt1
- initial build
