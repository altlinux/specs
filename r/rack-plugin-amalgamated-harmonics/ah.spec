Name: rack-plugin-amalgamated-harmonics
Version: 2.0.1
Release: alt1

Summary: Virtual Eurorack Modules for VCV Rack
License: BSD-3-Clause
Group: Sound
Url: https://github.com/jhoar/AmalgamatedHarmonics

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
* Fri Oct 31 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.1-alt1
- initial
