Name: rack-plugin-befaco
Version: 2.11.0
Release: alt1

Summary: Virtual Eurorack Modules for VCV Rack
License: GPLv3
Group: Sound
Url: https://github.com/VCVRack/Befaco

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel

%description
%summary

%prep
%setup

%build
%add_optflags -Wno-suggest-override
%make_build RACK_DIR=%_datadir/rack/sdk

%install
make install RACK_DIR=%_datadir/rack/sdk \
     PLUGINS_DIR=%buildroot%_libdir/rack

%files
%doc README*
%_libdir/rack/*

%changelog
* Wed Jun 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.11.0-alt1
- 2.11.0 released

* Fri Oct 31 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.9.1-alt1
- initial
