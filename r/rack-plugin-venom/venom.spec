Name: rack-plugin-venom
Version: 2.9.1
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

