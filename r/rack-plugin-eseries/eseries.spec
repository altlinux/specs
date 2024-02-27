Name: rack-plugin-eseries
Version: 2.0.2
Release: alt1

Summary: E340 Cloud Generator
License: GPLv3
Group: Sound
Url: https://github.com/VCVRack/ESeries

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel

%description
VCV Rack plugin based on Synthesis Technology Eurorack modules

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
* Tue Feb 27 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt1
- 2.0.2 released

