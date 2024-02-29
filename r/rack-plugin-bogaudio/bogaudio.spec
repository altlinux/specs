Name: rack-plugin-bogaudio
Version: 2.4.45
Release: alt1

Summary: BogaudioModules for VCV Rack
License: GPLv3
Group: Sound
Url: https://github.com/bogaudio/BogaudioModules

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
* Thu Feb 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.45-alt1
- initial

