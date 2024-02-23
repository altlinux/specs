Name: rack-plugin-audible-instruments
Version: 2.0.0
Release: alt1

Summary: VCV Audible Instruments
License: GPLv3
Group: Sound
Url: https://github.com/VCVRack/AudibleInstruments

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel

%description
%summary

%prep
%setup

%build
make RACK_DIR=%_datadir/rack/sdk

%install
make install RACK_DIR=%_datadir/rack/sdk \
     PLUGINS_DIR=%buildroot%_libdir/rack

%files
%doc README*
%_libdir/rack/*

%changelog
* Thu Feb 22 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- initial
