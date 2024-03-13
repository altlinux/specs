Name: rack-plugin-venom
Version: 2.7.0
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
* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.0-alt1
- 2.7.0 released

* Thu Feb 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.1-alt1
- initial

