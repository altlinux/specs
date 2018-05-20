%define ver_major 0.3

Name: contractor
Version: %ver_major.3
Release: alt1

Summary: service for sharing data between apps
License: GPLv3+
Group: Graphical desktop/Other
Url: https://github.com/elementary/contractor

# VCS: https://github.com/elementary/contractor.git
Source: %name-%version.tar.gz

BuildRequires: cmake gcc-c++ vala-tools libgee0.8-devel libgio-devel

%description
A sharing service that allows source apps to send their data to
registered destination apps. This way, data source apps don't have to
have the destination apps hard coded into them.

%prep
%setup

%build
%cmake
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%files
%_bindir/*
%_datadir/dbus-1/services/org.elementary.contractor.service
%doc README*

%changelog
* Sun May 20 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Fri Jan 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Thu Sep 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Mon Jan 06 2014 Igor Zubkov <icesik@altlinux.org> 0.3-alt4.r132
- r132

* Mon Nov 25 2013 Igor Zubkov <icesik@altlinux.org> 0.3-alt3.r131
- r131

* Mon Sep 16 2013 Igor Zubkov <icesik@altlinux.org> 0.3-alt2.revno130
- Add docs
- Make build verbose

* Wed Sep 11 2013 Igor Zubkov <icesik@altlinux.org> 0.3-alt1.revno130
- build for Sisyphus

