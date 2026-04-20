Name: rack-plugin-venom
Version: 2.15.0
Release: alt1

Summary: Venom modules for VCV Rack
License: GPLv3
Group: Sound
Url: https://github.com/DaveBenham/VenomModules

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel

%description
%summary

%prep
%setup

%build
%make_build RACK_DIR=%_datadir/rack/sdk

%install
make install RACK_DIR=%_datadir/rack/sdk \
     PLUGINS_DIR=%buildroot%_libdir/rack

%files
%doc README*
%_libdir/rack/*

%changelog
* Mon Apr 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.15.0-alt1
- 2.15.0 released

* Wed Dec 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14.5-alt1
- 2.14.5 released

* Thu Dec 11 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14.4-alt1
- 2.14.4 released

* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14.3-alt1
- 2.14.3 released

* Mon Dec 08 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14.2-alt1
- 2.14.2 released

* Wed Nov 26 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14.1-alt1
- 2.14.1 released

* Tue Nov 25 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.14.0-alt1
- 2.14.0 released

* Mon Oct 06 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.13.2-alt1
- 2.13.2 released

* Wed Oct 01 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.13.1-alt1
- 2.13.1 released

* Mon Sep 22 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.13.0-alt1
- 2.13.0 released

* Fri Jun 06 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.12.3-alt1
- 2.12.3 released

* Wed Jun 04 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.12.2-alt1
- 2.12.2 released

* Mon May 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.12.1-alt1
- 2.12.1 released

* Thu Jan 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.11.1-alt1
- 2.11.1 released

* Tue Nov 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.11.0-alt1
- 2.11.0 released

* Mon Oct 28 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.10.0-alt1
- 2.10.0 released

* Tue Sep 10 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.9.1-alt1
- 2.9.1 released

* Fri Aug 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.9.0-alt1
- 2.9.0 released

* Thu Jun 27 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.8.0-alt1
- 2.8.0 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.0-alt1
- 2.7.0 released

* Thu Feb 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.1-alt1
- initial

