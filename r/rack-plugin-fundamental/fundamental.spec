Name: rack-plugin-fundamental
Version: 2.6.0
Release: alt1

Summary: VCV Free modules
License: GPLv3
Group: Sound
Url: https://github.com/VCVRack/Fundamental

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel
BuildRequires: pkgconfig(samplerate)

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
* Thu Feb 22 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- initial
