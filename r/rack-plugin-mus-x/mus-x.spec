Name: rack-plugin-mus-x
Version: 2.1.0
Release: alt1

Summary: MUS-X Rack plugin
License: GPLv3
Group: Sound
Url: https://github.com/Jojosito/MUS-X

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel

%description
Modules for VCV Rack, with a focus on MIDI-controllable,
analog poly-synths, and per-voice variance.

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
* Fri Aug 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.0-alt1
- 2.1.0 released

* Thu Feb 22 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.1-alt1
- initial
