Name: rack-plugin-bogaudio
Version: 2.6.47
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
* Wed May 28 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.6.47-alt1
- 2.6.47 released

* Tue May 27 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.6.46-alt1
- 2.6.46 released

* Thu Feb 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.45-alt1
- initial

