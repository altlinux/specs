Name: contractor
Version: 0.3
Release: alt3.r131

Summary: service for sharing data between apps
License: GPLv3+
Group: Graphical desktop/Other
Url: https://launchpad.net/contractor

Source0: %name.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake vala glib2-devel libgee-devel libgio-devel gcc-c++

%description
A sharing service that allows source apps to send their data to
registered destination apps. This way, data source apps don't have to
have the destination apps hard coded into them.

%prep
%setup -q -n %name

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%files
%doc INSTALL
%_bindir/*
%_datadir/contractor
%_datadir/dbus-1/services/org.elementary.contractor.service

%changelog
* Mon Nov 25 2013 Igor Zubkov <icesik@altlinux.org> 0.3-alt3.r131
- r131

* Mon Sep 16 2013 Igor Zubkov <icesik@altlinux.org> 0.3-alt2.revno130
- Add docs
- Make build verbose

* Wed Sep 11 2013 Igor Zubkov <icesik@altlinux.org> 0.3-alt1.revno130
- build for Sisyphus

